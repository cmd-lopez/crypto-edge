"""README chart: out-of-sample equity of the best pre-registered trial vs the benchmarks.

"Best" = lowest raw bootstrap p-value among the 11 Holm-family trials (base cost). It is
chosen after the fact for illustration only; it did not pass the edge bar.
Reads committed results only (no network, no data cache).

Usage: uv run --group charts python research/03_equity_chart.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "research" / "results" / "phase2"
OUT = ROOT / "docs" / "equity_curve.png"


def sharpe(r: pd.Series) -> float:
    return float(r.mean() / r.std(ddof=1) * np.sqrt(365))


def main() -> None:
    summary = pd.read_csv(RESULTS / "trials_summary.csv")
    family = summary[(summary.case == "base") & summary.p_vs_stronger.notna()]
    best = family.loc[family.p_vs_stronger.idxmin()]
    stress = summary[(summary.trial == best.trial) & (summary.case == "stress")].iloc[0]
    btc_stress = summary[(summary.trial == "BTC_buy_hold") & (summary.case == "stress")].iloc[0]
    daily = pd.read_csv(RESULTS / "oos_daily_returns.csv", index_col=0, parse_dates=True)

    series = {
        f"Best rule: {best.trial} (raw p = {best.p_vs_stronger:.2f}; picked post hoc)":
            daily[f"{best.trial}|base"],
        "BTC buy-and-hold": daily["BTC_buy_hold|base"],
        "Equal-weight basket (PIT universe, monthly)": daily["EW_monthly|base"],
    }
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=150)
    for (label, r), color in zip(series.items(), ("#1f77b4", "#f2a900", "#7f7f7f")):
        eq = (1 + r).cumprod()
        ax.plot(eq.index, eq, color=color, lw=1.6,
                label=f"{label}  |  Sharpe {sharpe(r):.2f}, end {eq.iloc[-1]:.2f}x")
    ax.set_yscale("log")
    ax.axhline(1.0, color="black", lw=0.6, ls=":")
    ax.set_ylabel("Equity (log scale, start = 1.0)")
    ax.set_title("Out-of-sample 2021-07-01 to 2026-06-30, net of 0.8%/side costs: no edge found")
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    ax.text(0.01, 0.97,
            "Why the blue line is still not an edge:\n"
            f"- beats both benchmarks in {best.fold_win_rate:.0%} of 20 quarterly folds (bar: 60%)\n"
            f"- raw p = {best.p_vs_stronger:.2f} before any multiple-testing correction\n"
            f"- at 2x costs its Sharpe falls to {stress.sharpe:.2f} (BTC {btc_stress.sharpe:.2f})\n"
            "- chosen after seeing results, from 11 trials",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.5,
            bbox=dict(boxstyle="round", fc="white", ec="#999999", alpha=0.9))
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT)
    print(f"wrote {OUT.relative_to(ROOT)}; best trial = {best.trial}, raw p = {best.p_vs_stronger:.3f}")


if __name__ == "__main__":
    main()
