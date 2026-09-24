"""Phase 1 feasibility probe: how many Coinbase USD spot assets clear the
$5M 30-day average daily volume bar at each month-end, point-in-time?

Research script (not production code). Uses only the free, unauthenticated
Coinbase Exchange public API. Includes delisted products to avoid
survivorship bias. Raw candles are cached as Parquet-free CSV under
$CRYPTO_EDGE_DATA (default ~/.cache/crypto-edge/candles_1d).

Usage: uv run --with httpx --with pandas research/00_universe_feasibility.py
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
import pandas as pd

BASE = "https://api.exchange.coinbase.com"
CACHE = Path(os.environ.get("CRYPTO_EDGE_DATA", Path.home() / ".cache" / "crypto-edge")) / "candles_1d"
START = datetime(2016, 1, 1, tzinfo=timezone.utc)
WINDOW = timedelta(days=299)  # endpoint returns max 300 candles
MIN_INTERVAL_S = 0.12  # stay under the 10 req/s public limit

# Excluded by SPEC: stablecoins and wrapped / pegged-derivative assets.
STABLE_OR_WRAPPED = {
    "USDC", "USDT", "DAI", "PYUSD", "GUSD", "PAX", "USDP", "BUSD", "UST", "TUSD",
    "EURC", "USDS", "FDUSD", "RLUSD", "USD1", "GYEN", "MUSD", "LUSD", "FRAX", "SUSD",
    "WBTC", "WETH", "CBBTC", "CBETH", "WSTETH", "STETH", "RETH", "MSOL", "JITOSOL",
    "LSETH", "PAXG", "XAUT", "CBDOGE", "CBXRP", "CBADA", "CBLTC",
}

_last = 0.0


def get(client: httpx.Client, path: str, **params) -> list:
    global _last
    for attempt in range(6):
        wait = MIN_INTERVAL_S - (time.monotonic() - _last)
        if wait > 0:
            time.sleep(wait)
        _last = time.monotonic()
        r = client.get(BASE + path, params=params)
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(2**attempt)
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"gave up on {path} {params}")


def fetch_candles(client: httpx.Client, pid: str, now: datetime) -> pd.DataFrame:
    path = CACHE / f"{pid}.csv"
    if path.exists():
        return pd.read_csv(path, parse_dates=["time"])
    rows: list = []
    t = START
    while t < now:
        end = min(t + WINDOW, now)
        rows += get(client, f"/products/{pid}/candles", granularity=86400,
                    start=t.isoformat(), end=end.isoformat())
        t = end
    df = pd.DataFrame(rows, columns=["time", "low", "high", "open", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.drop_duplicates("time").sort_values("time")
    CACHE.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df


def main() -> None:
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    with httpx.Client(timeout=30, headers={"User-Agent": "crypto-edge-research"}) as client:
        products = get(client, "/products")
        usd = sorted(p["id"] for p in products
                     if p["quote_currency"] == "USD" and p["base_currency"] not in STABLE_OR_WRAPPED)
        print(f"USD products after exclusions: {len(usd)} "
              f"(delisted: {sum(p['status'] == 'delisted' for p in products if p['id'] in usd)})")
        dollar_vol = {}
        for i, pid in enumerate(usd, 1):
            df = fetch_candles(client, pid, now)
            if not df.empty:
                dollar_vol[pid] = (df.set_index("time")["volume"] * df.set_index("time")["close"])
            if i % 50 == 0:
                print(f"  fetched {i}/{len(usd)}")

    dv = pd.DataFrame(dollar_vol).sort_index()
    # Missing day = no trading = 0 volume; ADV computed with a trailing, closed window.
    adv30 = dv.fillna(0.0).rolling(30, min_periods=30).mean()
    month_ends = adv30.resample("ME").last()
    eligible = (month_ends >= 5_000_000).sum(axis=1)
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
    ge10 = out["adv30_ge_5M"].ge(10)
    run = ge10.rolling(3).sum().eq(3)
    print(f"first month-end ending 3 consecutive months with >=10 eligible: {run.idxmax().date()}")


if __name__ == "__main__":
    main()
