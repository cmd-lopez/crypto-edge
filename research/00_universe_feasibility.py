"""Phase 1 feasibility probe: how many Coinbase USD spot assets clear the $5M 30-day
average daily volume bar at each month-end, point-in-time? Includes delisted products.

Usage: uv run python research/00_universe_feasibility.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from edge.fetch import fetch_all


def main() -> None:
    frames = fetch_all()
    dv = pd.DataFrame({pid: df.set_index("time")["volume"] * df.set_index("time")["close"]
                       for pid, df in frames.items() if not df.empty}).sort_index()
    print(f"USD products after exclusions: {len(frames)}")
    adv30 = dv.fillna(0.0).rolling(30, min_periods=30).mean()
    eligible = (adv30.resample("ME").last() >= 5_000_000).sum(axis=1)
    listed = dv.notna().resample("ME").max().sum(axis=1)
    out = pd.DataFrame({"listed_usd_products": listed, "adv30_ge_5M": eligible})
    out = out[out.index >= "2017-01-01"]
    results = Path(__file__).parent / "results"
    results.mkdir(exist_ok=True)
    out.to_csv(results / "00_universe_feasibility.csv")
    print(out.to_string())
    recent = out[out.index >= "2021-01-01"]["adv30_ge_5M"]
    print(f"\nSince 2021-01: months={len(recent)} min={recent.min()} median={recent.median():.0f} "
          f"max={recent.max()} months_with_>50_eligible={(recent > 50).sum()}")
    run = out["adv30_ge_5M"].ge(10).rolling(3).sum().eq(3)
    print(f"first month-end ending 3 consecutive months with >=10 eligible: {run.idxmax().date()}")


if __name__ == "__main__":
    main()
