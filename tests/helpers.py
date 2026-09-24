"""Synthetic market data for harness tests. Never used for research results."""

from __future__ import annotations

import numpy as np
import pandas as pd

from edge.data import Panel, panel_from_frames

DAY = pd.Timedelta(days=1)


def frame(start: str, closes, volume=1.0, opens=None) -> pd.DataFrame:
    """Daily candle frame starting at `start` (bar-open dates)."""
    closes = np.asarray(closes, dtype=float)
    times = pd.date_range(start, periods=len(closes), freq="D", tz="UTC")
    opens = closes if opens is None else np.asarray(opens, dtype=float)
    vol = np.broadcast_to(np.asarray(volume, dtype=float), closes.shape)
    return pd.DataFrame({
        "time": times, "open": opens, "high": np.maximum(opens, closes),
        "low": np.minimum(opens, closes), "close": closes, "volume": vol,
    })


def panel(frames: dict[str, pd.DataFrame], now: str | pd.Timestamp | None = None) -> Panel:
    if now is None:
        last = max(f["time"].max() for f in frames.values())
        now = last + DAY  # every bar complete
    return panel_from_frames(frames, pd.Timestamp(now))
