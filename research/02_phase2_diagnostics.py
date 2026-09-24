"""Phase 2 post-hoc diagnostics (NOT part of the pre-registered test, NOT in the Holm family).

1. Engine cross-check on real data: BTC buy-and-hold and equal-weight monthly at zero cost,
   engine vs an independent vectorized computation.
2. Gross (zero-cost) versions of the three primary walk-forward trials, to separate
   "no signal" from "signal eaten by costs". Logged to research/trials.csv with a note.

Usage: uv run python research/02_phase2_diagnostics.py
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from edge import run_phase2 as p2
from edge.benchmarks import BuyHoldBTC, EqualWeightMonthly, month_end
from edge.engine import DELIST_HAIRCUT, CostModel, run
from edge.evaluation import Switching, fold_sharpes, fold_win_rate
from edge.metrics import max_drawdown, sharpe

ZERO = CostModel(0.0, 0.0)


def vectorized_btc(panel, s0, s1) -> float:
    c = panel.close["BTC-USD"]
    entry = panel.open["BTC-USD"].loc[s0 + pd.Timedelta(days=1)]
    return float(c.loc[s1] / entry - 1)


def vectorized_ew(panel, universe, s0, s1) -> float:
    """Equal weight at each month-end decision, filled at next open, zero cost; assets whose
    bars end inside a holding period are written off at last close x (1 - haircut)."""
    dates = panel.dates[(panel.dates >= s0) & (panel.dates <= s1)]
    decisions = [d for d in dates if (d == s0 or month_end(d)) and d < s1]
    last_bar = panel.close.apply(lambda s: s.last_valid_index())
    equity = 1.0
    for d, nxt in zip(decisions, decisions[1:] + [s1]):
        row = universe.loc[d]
        names = list(row[row].index)
        if not names:
            continue
        rets = []
        for n in names:  # engine targets 1/N of all names; untradeable ones stay in cash
            entry = panel.open[n].loc[d + pd.Timedelta(days=1)]
            if not np.isfinite(entry):
                rets.append(0.0)
            elif last_bar[n] < nxt:
                rets.append(panel.close[n].loc[last_bar[n]] * (1 - DELIST_HAIRCUT) / entry - 1)
            else:
                end_px = panel.close[n].loc[:nxt].dropna().iloc[-1]
                rets.append(end_px / entry - 1)
        equity *= 1 + float(np.mean(rets))
    return equity - 1


def main() -> None:
    ph = p2.Phase2()
    s0, s1 = ph.oos
    out: dict = {"note": "post-hoc diagnostics; not pre-registered; not in Holm family"}

    btc, ew = BuyHoldBTC(), EqualWeightMonthly(ph.universe)
    r_btc = run(ph.panel, btc, s0, s1, btc.rebalance_at(s0), ZERO, p2.NO_LIMITS)
    r_ew = run(ph.panel, ew, s0, s1, ew.rebalance_from(s0), ZERO, p2.NO_LIMITS, universe=ph.universe)
    out["crosscheck"] = {
        "btc_engine": float(r_btc.equity.iloc[-1] - 1), "btc_vectorized": vectorized_btc(ph.panel, s0, s1),
        "ew_engine": float(r_ew.equity.iloc[-1] - 1),
        "ew_vectorized": vectorized_ew(ph.panel, ph.universe, s0, s1),
    }
    out["ew_universe_size"] = {
        "min": int(ph.universe.loc[s0:s1].sum(axis=1).min()),
        "median": float(ph.universe.loc[s0:s1].sum(axis=1).median()),
        "max": int(ph.universe.loc[s0:s1].sum(axis=1).max()),
    }

    selection = json.loads((p2.OUT / "verdicts.json").read_text())["verdicts"]
    bench_fs = [fold_sharpes(r_btc.returns, ph.folds), fold_sharpes(r_ew.returns, ph.folds)]
    gross = {}
    for h, grid in p2.GRID.items():
        cells = {p2.cell_name(h, p): p for p in grid}
        chosen = selection[h]["selection_per_fold"]
        s = Switching(ph.folds, [ph.strategy(h, cells[n]) for n in chosen])
        r = run(ph.panel, s, s0, s1, s.rebalance, ZERO, p2.Limits(), dd_reset_dates=ph.resets,
                universe=ph.universe, band=p2.BAND)
        fs = fold_sharpes(r.returns, ph.folds)
        gross[h] = {"sharpe_gross": sharpe(r.returns), "mdd_gross": max_drawdown(r.returns),
                    "fold_win_rate_gross_vs_gross_benchmarks": fold_win_rate(fs, bench_fs),
                    "total_return_gross": float(r.equity.iloc[-1] - 1)}
        p2.CASES["gross-diagnostic"] = (ZERO, 0)
        ph.log(h, {"selection": chosen}, "gross-diagnostic", r, s0, s1,
               fold_win_rate(fs, bench_fs), note="post-hoc diagnostic (not in Holm family)")
    out["gross_primary"] = gross
    out["gross_benchmarks"] = {"BTC_buy_hold": {"sharpe": sharpe(r_btc.returns)},
                               "EW_monthly": {"sharpe": sharpe(r_ew.returns),
                                              "mdd": max_drawdown(r_ew.returns)}}
    (p2.OUT / "diagnostics.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
