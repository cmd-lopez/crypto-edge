"""Download Coinbase USD daily candles (listed and delisted) into the local cache.

Free, unauthenticated Coinbase Exchange public API. Incomplete bars may be cached; the
data layer (`edge.data`) drops them using an explicit `now`.

Usage: uv run python -m edge.fetch [--refresh]
"""

from __future__ import annotations

import argparse
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
import pandas as pd

from edge.universe import EXCLUDED, base_of

BASE = "https://api.exchange.coinbase.com"
CACHE = Path(os.environ.get("CRYPTO_EDGE_DATA", Path.home() / ".cache" / "crypto-edge")) / "candles_1d"
START = datetime(2016, 1, 1, tzinfo=timezone.utc)
WINDOW = timedelta(days=299)  # endpoint returns max 300 candles
MIN_INTERVAL_S = 0.12  # stay under the ~10 req/s public limit


class _Client:
    def __init__(self) -> None:
        self.http = httpx.Client(timeout=30, headers={"User-Agent": "crypto-edge-research"})
        self.last = 0.0

    def get(self, path: str, **params) -> list:
        for attempt in range(6):
            wait = MIN_INTERVAL_S - (time.monotonic() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.monotonic()
            r = self.http.get(BASE + path, params=params)
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(2**attempt)
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError(f"gave up on {path} {params}")


def usd_products(client: _Client) -> list[dict]:
    return [p for p in client.get("/products")
            if p["quote_currency"] == "USD" and base_of(p["id"]) not in EXCLUDED]


def fetch_candles(client: _Client, pid: str, now: datetime, cache: Path = CACHE,
                  refresh: bool = False) -> pd.DataFrame:
    path = cache / f"{pid}.csv"
    if path.exists() and not refresh:
        return pd.read_csv(path, parse_dates=["time"])
    rows: list = []
    t = START
    while t < now:
        end = min(t + WINDOW, now)
        rows += client.get(f"/products/{pid}/candles", granularity=86400,
                           start=t.isoformat(), end=end.isoformat())
        t = end
    df = pd.DataFrame(rows, columns=["time", "low", "high", "open", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.drop_duplicates("time").sort_values("time")
    cache.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df


def fetch_all(cache: Path = CACHE, refresh: bool = False) -> dict[str, pd.DataFrame]:
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    client = _Client()
    products = usd_products(client)
    out = {}
    for i, p in enumerate(sorted(products, key=lambda p: p["id"]), 1):
        out[p["id"]] = fetch_candles(client, p["id"], now, cache, refresh)
        if i % 50 == 0:
            print(f"  fetched {i}/{len(products)}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="re-download cached products")
    fetch_all(refresh=ap.parse_args().refresh)
