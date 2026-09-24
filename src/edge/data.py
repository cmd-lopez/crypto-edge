"""Daily candle panel. Index = UTC bar-open date; a bar is complete when open + 1 day <= now."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

FIELDS = ("open", "high", "low", "close", "volume")
DAY = pd.Timedelta(days=1)


@dataclass(frozen=True)
class Panel:
    open: pd.DataFrame
    high: pd.DataFrame
    low: pd.DataFrame
    close: pd.DataFrame
    volume: pd.DataFrame
    dollar_volume: pd.DataFrame  # volume * close; 0 on days without a bar

    @property
    def dates(self) -> pd.DatetimeIndex:
        return self.close.index

    def upto(self, d: pd.Timestamp) -> Panel:
        """Only bars whose open date is <= d (i.e. closed by d + 1 day)."""
        return Panel(*(getattr(self, f).loc[:d] for f in (*FIELDS, "dollar_volume")))

    def window(self, start: pd.Timestamp, end: pd.Timestamp) -> Panel:
        return Panel(*(getattr(self, f).loc[start:end] for f in (*FIELDS, "dollar_volume")))


def panel_from_frames(frames: dict[str, pd.DataFrame], now: pd.Timestamp) -> Panel:
    """frames: product id -> DataFrame[time, open, high, low, close, volume]."""
    cutoff = now - DAY  # bars with open <= cutoff have closed
    cols: dict[str, dict[str, pd.Series]] = {f: {} for f in FIELDS}
    for pid, df in frames.items():
        df = df.assign(time=pd.to_datetime(df["time"], utc=True))
        df = df[df["time"] <= cutoff].drop_duplicates("time").set_index("time").sort_index()
        if df.empty:
            continue
        for f in FIELDS:
            cols[f][pid] = df[f].astype(float)
    wide = {f: pd.DataFrame(cols[f]) for f in FIELDS}
    idx = wide["close"].index
    full = pd.date_range(idx.min(), idx.max(), freq="D", tz="UTC", name="time")
    columns = sorted(wide["close"].columns)
    wide = {f: w.reindex(index=full, columns=columns) for f, w in wide.items()}
    dollar = (wide["volume"] * wide["close"]).fillna(0.0)
    return Panel(**wide, dollar_volume=dollar)


def load_panel(cache_dir: Path, now: pd.Timestamp) -> Panel:
    frames = {p.stem: pd.read_csv(p) for p in sorted(Path(cache_dir).glob("*.csv"))}
    return panel_from_frames({k: v for k, v in frames.items() if not v.empty}, now)


def manifest(cache_dir: Path) -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(Path(cache_dir).glob("*.csv"))}
