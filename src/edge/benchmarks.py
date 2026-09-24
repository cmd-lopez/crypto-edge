"""SPEC §2 benchmarks, run through the same engine and cost model as strategies."""

from __future__ import annotations

from typing import Callable

import pandas as pd

from edge.data import Panel


def month_end(d: pd.Timestamp) -> bool:
    return (d + pd.Timedelta(days=1)).month != d.month


class BuyHoldBTC:
    def target_weights(self, view: Panel | None, d: pd.Timestamp) -> pd.Series:
        return pd.Series({"BTC-USD": 1.0})

    def exits(self, view, d, held) -> set[str]:
        return set()

    @staticmethod
    def rebalance_at(start: pd.Timestamp) -> Callable[[pd.Timestamp], bool]:
        return lambda d: d == start


class EqualWeightMonthly:
    """Equal weight across the point-in-time universe, rebalanced at each month-end close."""

    def __init__(self, universe: pd.DataFrame):
        self.universe = universe

    def target_weights(self, view: Panel | None, d: pd.Timestamp) -> pd.Series:
        row = self.universe.loc[d]
        names = row[row].index
        return pd.Series(1.0 / len(names), index=names) if len(names) else pd.Series(dtype=float)

    def exits(self, view, d, held) -> set[str]:
        return set()

    @staticmethod
    def rebalance_from(start: pd.Timestamp) -> Callable[[pd.Timestamp], bool]:
        return lambda d: d == start or month_end(d)
