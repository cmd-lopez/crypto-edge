"""Phase 2 edge test: one command reproduces every pre-registered trial.

    uv run python -m edge.run_phase2

Protocol: EDGE_REPORT.md §2.0 (pre-registration commit c24ad22). Outputs go to
research/results/phase2/ and every run is appended to research/trials.csv.
"""

from __future__ import annotations

import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew

from edge.benchmarks import BuyHoldBTC, EqualWeightMonthly
from edge.data import load_panel, manifest
from edge.engine import CostModel, Limits, Result, run
from edge.evaluation import FOLD_WIN_BAR, Switching, fold_sharpes, fold_win_rate, select_cells, verdict
from edge.fetch import CACHE
from edge.folds import walk_forward
from edge.hypotheses import H1TrendGate, H2AssetTrend, H3TrendComposite
from edge.ledger import append_trial
from edge.metrics import deflated_sharpe, holm, max_drawdown, sharpe, stationary_bootstrap_pvalue
from edge.universe import eligibility

PREREG_COMMIT = "c24ad22"
AS_OF = pd.Timestamp("2026-09-23", tz="UTC")
DATA_START, DATA_END = pd.Timestamp("2020-07-01", tz="UTC"), pd.Timestamp("2026-09-22", tz="UTC")
HOLDOUT = (pd.Timestamp("2026-07-01", tz="UTC"), DATA_END)
BAND = 0.20
BASE = CostModel(0.006, 0.002)
CASES = {"base": (BASE, 0), "stress": (BASE.scaled(2), 0), "delay": (BASE, 1)}
NO_LIMITS = Limits(max_positions=None, max_weight=1.0, max_gross=1.0, daily_loss=None, max_drawdown=None)

GRID: dict[str, list[dict]] = {
    "H1": [dict(L=50, portfolio="btc"), dict(L=50, portfolio="top5"),
           dict(L=100, portfolio="btc"), dict(L=100, portfolio="top5")],
    "H2": [dict(L=20), dict(L=50)],
    "H3": [dict(cadence="weekly"), dict(cadence="biweekly")],
}
FACTORY = {"H1": H1TrendGate, "H2": H2AssetTrend, "H3": H3TrendComposite}

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "results" / "phase2"
LEDGER = ROOT / "research" / "trials.csv"


def cell_name(h: str, params: dict) -> str:
    return h + "[" + ",".join(f"{k}={v}" for k, v in params.items()) + "]"


GRID_PARAMS = {cell_name(h, p): p for h, g in GRID.items() for p in g}


def git_hash() -> str:
    h = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                       text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "src"], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    return h + ("-dirty" if dirty else "")


class Phase2:
    def __init__(self) -> None:
        self.panel = load_panel(CACHE, AS_OF)
        assert self.panel.dates[-1] == DATA_END, self.panel.dates[-1]
        self.universe = eligibility(self.panel)
        self.folds = walk_forward(DATA_START, DATA_END)
        self.oos = (self.folds[0].test_start, self.folds[-1].test_end)
        self.resets = list(pd.date_range(DATA_START, DATA_END, freq="QS", tz="UTC"))
        self.git = git_hash()
        self.n_runs = 0

    # ---- running -------------------------------------------------------------------
    def strategy(self, h: str, params: dict):
        return FACTORY[h](**params, universe=self.universe)

    def run_strategy(self, s, start, end, case: str) -> Result:
        costs, delay = CASES[case]
        self.n_runs += 1
        return run(self.panel, s, start, end, s.rebalance, costs, Limits(), delay=delay,
                   dd_reset_dates=self.resets, universe=self.universe, band=BAND)

    def run_benchmarks(self, start, end, case: str) -> dict[str, Result]:
        costs, delay = CASES[case]
        btc, ew = BuyHoldBTC(), EqualWeightMonthly(self.universe)
        self.n_runs += 2
        return {
            "BTC_buy_hold": run(self.panel, btc, start, end, btc.rebalance_at(start), costs,
                                NO_LIMITS, delay=delay),
            "EW_monthly": run(self.panel, ew, start, end, ew.rebalance_from(start), costs,
                              NO_LIMITS, delay=delay, universe=self.universe, band=BAND),
        }

    def log(self, hypothesis: str, params, case: str, r: Result, start, end, win=np.nan,
            p=np.nan, note: str = "") -> None:
        append_trial(LEDGER, {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "git_hash": self.git, "hypothesis": hypothesis, "params": json.dumps(params),
            "cost_case": case, "delay": CASES[case][1], "oos_start": start.date(),
            "oos_end": end.date(), "n_days": len(r.returns),
            "sharpe": round(sharpe(r.returns), 6), "max_drawdown": round(max_drawdown(r.returns), 6),
            "fold_win_rate": win, "pvalue_vs_stronger": p, "turnover": round(r.turnover, 4),
            "note": note,
        })

    # ---- reporting helpers -----------------------------------------------------------
    def describe(self, r: Result) -> dict:
        ret = r.returns
        btc = self.panel.close["BTC-USD"].pct_change().reindex(ret.index)
        beta = float(ret.cov(btc) / btc.var()) if btc.var() > 0 else np.nan
        sma200 = self.panel.close["BTC-USD"].rolling(200).mean()
        up = (self.panel.close["BTC-USD"] > sma200).shift(1, fill_value=False).reindex(ret.index)
        up = up.fillna(False).astype(bool)
        years = len(ret) / 365
        return {
            "sharpe": sharpe(ret), "max_drawdown": max_drawdown(ret),
            "cagr": float((1 + ret).prod() ** (1 / years) - 1) if years > 0 else np.nan,
            "total_return": float((1 + ret).prod() - 1), "ann_vol": float(ret.std() * np.sqrt(365)),
            "turnover_annual": r.turnover, "avg_gross_exposure": float(r.weights.sum(axis=1).mean()),
            "btc_beta": beta, "n_trades": len(r.trades),
            "cost_paid": float(r.trades["cost"].sum()) if len(r.trades) else 0.0,
            "delistings": sum(e["event"] == "delisted" for e in r.events),
            "drawdown_halts": sum(e["event"] == "drawdown_halt" for e in r.events),
            "daily_loss_halts": sum(e["event"] == "daily_loss_halt" for e in r.events),
            "sharpe_btc_uptrend_days": sharpe(ret[up]), "sharpe_btc_downtrend_days": sharpe(ret[~up]),
        }

    # ---- main ------------------------------------------------------------------------
    def execute(self) -> dict:
        t0 = time.time()
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "manifest.json").write_text(json.dumps({
            "as_of": str(AS_OF), "git": self.git, "prereg_commit": PREREG_COMMIT,
            "panel_last_bar": str(self.panel.dates[-1]), "n_products": self.panel.close.shape[1],
            "data_sha256": manifest(CACHE)}, indent=1))

        s0, s1 = self.oos
        bench = {case: self.run_benchmarks(s0, s1, case) for case in CASES}
        for case, bs in bench.items():
            for name, r in bs.items():
                self.log(name, {}, case, r, s0, s1, note="benchmark")
        bench_fs = {case: {n: fold_sharpes(r.returns, self.folds) for n, r in bs.items()}
                    for case, bs in bench.items()}
        stronger = max(bench["base"], key=lambda n: sharpe(bench["base"][n].returns))
        btc_mdd = {case: max_drawdown(bench[case]["BTC_buy_hold"].returns) for case in CASES}
        print(f"benchmarks done ({time.time() - t0:.0f}s); stronger={stronger}")

        oos: dict[str, dict[str, Result]] = {}   # trial -> case -> Result
        selection: dict[str, list[str]] = {}
        for h, grid in GRID.items():
            cells = {cell_name(h, p): p for p in grid}
            train = pd.DataFrame(index=range(len(self.folds)), columns=list(cells), dtype=float)
            for k, f in enumerate(self.folds):
                for name, p in cells.items():
                    r = self.run_strategy(self.strategy(h, p), f.train_start, f.train_end, "base")
                    train.loc[k, name] = sharpe(r.returns)
                    self.log(h, p, "base", r, f.train_start, f.train_end, note=f"train fold {k}")
            chosen = select_cells(train)
            selection[h] = chosen
            train.assign(chosen=chosen, test_start=[f.test_start.date() for f in self.folds]).to_csv(
                OUT / f"train_selection_{h}.csv", index=False)
            for name, p in cells.items():
                oos[name] = {c: self.run_strategy(self.strategy(h, p), s0, s1, c) for c in CASES}
            oos[f"{h}[walk-forward]"] = {c: self.run_strategy(
                Switching(self.folds, [self.strategy(h, cells[n]) for n in chosen]), s0, s1, c)
                for c in CASES}
            print(f"{h} done ({time.time() - t0:.0f}s)")

        # ---- statistics on the Holm family (all base-case OOS strategy trials) ----
        family = list(oos)
        stronger_r = bench["base"][stronger].returns
        pvals = {t: stationary_bootstrap_pvalue(oos[t]["base"].returns, stronger_r,
                                                mean_block=7, n_boot=10_000, seed=0) for t in family}
        holm_p = dict(zip(family, holm([pvals[t] for t in family])))
        per_period = {t: sharpe(oos[t]["base"].returns) / np.sqrt(365) for t in family}
        sr_var = float(np.var(list(per_period.values()), ddof=1))
        print(f"bootstrap done ({time.time() - t0:.0f}s)")

        rows, fold_tables, verdicts = [], {}, {}
        for t in family:
            h = t.split("[")[0]
            is_primary = t.endswith("[walk-forward]")
            for case in CASES:
                r = oos[t][case]
                fs = fold_sharpes(r.returns, self.folds)
                fold_tables[f"{t}|{case}"] = fs
                win = fold_win_rate(fs, list(bench_fs[case].values()))
                d = self.describe(r)
                p = pvals[t] if case == "base" else np.nan
                rows.append({"trial": t, "case": case, "fold_win_rate": win,
                             "c1_fold_wins": win >= FOLD_WIN_BAR,
                             "c2_mdd_le_btc": d["max_drawdown"] <= btc_mdd[case],
                             "btc_mdd": btc_mdd[case], "p_vs_stronger": p,
                             "holm_p": holm_p[t] if case == "base" else np.nan, **d})
                params = {"selection": selection[h]} if is_primary else GRID_PARAMS[t]
                self.log(h, params, case, r, s0, s1, win, p,
                         note="primary" if is_primary else "fixed cell")
        for case, bs in bench.items():
            for bn, r in bs.items():
                fold_tables[f"{bn}|{case}"] = bench_fs[case][bn]
                rows.append({"trial": bn, "case": case, **self.describe(r)})
        summary = pd.DataFrame(rows)
        summary.to_csv(OUT / "trials_summary.csv", index=False)
        pd.DataFrame(fold_tables).to_csv(OUT / "fold_sharpes.csv")
        daily = {f"{t}|{c}": oos[t][c].returns for t in oos for c in CASES}
        daily |= {f"{bn}|{c}": bench[c][bn].returns for c in CASES for bn in bench[c]}
        pd.DataFrame(daily).to_csv(OUT / "oos_daily_returns.csv")

        for h in GRID:
            t = f"{h}[walk-forward]"
            base = summary[(summary.trial == t) & (summary.case == "base")].iloc[0]
            stress = summary[(summary.trial == t) & (summary.case == "stress")].iloc[0]
            ret = oos[t]["base"].returns
            verdicts[h] = {
                "trial": t, "selection_per_fold": selection[h],
                "c1_fold_win_rate_base": base.fold_win_rate, "c1_base": bool(base.c1_fold_wins),
                "c2_mdd_base": base.max_drawdown, "btc_mdd_base": btc_mdd["base"],
                "c2_base": bool(base.c2_mdd_le_btc),
                "c1_fold_win_rate_stress": stress.fold_win_rate, "c1_stress": bool(stress.c1_fold_wins),
                "c2_stress": bool(stress.c2_mdd_le_btc),
                "p_vs_stronger": pvals[t], "holm_p": holm_p[t], "stronger_benchmark": stronger,
                "deflated_sharpe": deflated_sharpe(per_period[t], sr_var, len(family), len(ret),
                                                   float(skew(ret)), float(kurtosis(ret, fisher=False))),
                "verdict": verdict(bool(base.c1_fold_wins), bool(base.c2_mdd_le_btc),
                                   bool(stress.c1_fold_wins), bool(stress.c2_mdd_le_btc),
                                   holm_p[t], len(self.folds)),
            }

        holdout = self.holdout()
        result = {"as_of": str(AS_OF), "git": self.git, "prereg_commit": PREREG_COMMIT,
                  "oos": [str(s0.date()), str(s1.date())], "n_folds": len(self.folds),
                  "holm_family_size": len(family), "holm_family": family,
                  "total_backtest_runs": self.n_runs, "stronger_benchmark": stronger,
                  "verdicts": verdicts, "holdout_descriptive": holdout,
                  "runtime_s": round(time.time() - t0, 1)}
        (OUT / "verdicts.json").write_text(json.dumps(result, indent=1, default=str))
        return result

    def holdout(self) -> dict:
        """Descriptive only: params chosen on the 12 months that precede the holdout."""
        h0, h1 = HOLDOUT
        bench = self.run_benchmarks(h0, h1, "base")
        out = {n: self.describe(r) for n, r in bench.items()}
        for bn, r in bench.items():
            self.log(bn, {}, "base", r, h0, h1, note="holdout benchmark")
        tr0, tr1 = h0 - pd.DateOffset(months=12), h0 - pd.Timedelta(days=1)
        for h, grid in GRID.items():
            cells = {cell_name(h, p): p for p in grid}
            train = {}
            for n, p in cells.items():
                r = self.run_strategy(self.strategy(h, p), tr0, tr1, "base")
                train[n] = sharpe(r.returns)
                self.log(h, p, "base", r, tr0, tr1, note="holdout train selection")
            best = select_cells(pd.DataFrame([train]))[0]
            r = self.run_strategy(self.strategy(h, cells[best]), h0, h1, "base")
            self.log(h, cells[best], "base", r, h0, h1, note="holdout (descriptive)")
            out[best] = self.describe(r)
        return out


def main() -> None:
    res = Phase2().execute()
    print(json.dumps({h: {k: v for k, v in d.items() if k != "selection_per_fold"}
                      for h, d in res["verdicts"].items()}, indent=1, default=str))
    print(f"family={res['holm_family_size']} runs={res['total_backtest_runs']} "
          f"stronger={res['stronger_benchmark']} runtime={res['runtime_s']}s")


if __name__ == "__main__":
    main()
