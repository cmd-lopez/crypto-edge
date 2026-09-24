"""Edge-bar evaluation pieces (SPEC §7.3-7.4, EDGE_REPORT.md §2.0)."""

from __future__ import annotations

import pandas as pd

from edge.folds import Fold
from edge.metrics import sharpe

MIN_FOLDS = 8
FOLD_WIN_BAR = 0.60
ALPHA = 0.05


def fold_sharpes(r: pd.Series, folds: list[Fold]) -> pd.Series:
    return pd.Series([sharpe(r.loc[f.test_start:f.test_end]) for f in folds],
                     index=[f.test_start for f in folds])


def fold_win_rate(strategy: pd.Series, benchmarks: list[pd.Series]) -> float:
    """Share of folds where the strategy's Sharpe strictly beats every benchmark's."""
    wins = pd.Series(True, index=strategy.index)
    for b in benchmarks:
        wins &= strategy.to_numpy() > b.to_numpy()
    return float(wins.mean())


def select_cells(train_sharpe: pd.DataFrame) -> list[str]:
    """Per fold (row), the grid cell (column, grid order) with the highest train Sharpe."""
    return [row.index[row.to_numpy().argmax()] for _, row in train_sharpe.iterrows()]


class Switching:
    """Delegates to the strategy selected for the fold whose test window contains d."""

    def __init__(self, folds: list[Fold], strategies: list):
        self.folds, self.strategies = folds, strategies

    def _at(self, d: pd.Timestamp):
        for f, s in zip(self.folds, self.strategies):
            if f.test_start <= d <= f.test_end:
                return s
        raise KeyError(f"{d} outside all test folds")

    def rebalance(self, d: pd.Timestamp) -> bool:
        return self._at(d).rebalance(d)

    def target_weights(self, view, d, held):
        return self._at(d).target_weights(view, d, held)

    def exits(self, view, d, held):
        return self._at(d).exits(view, d, held)


def verdict(c1: bool, c2: bool, c1_stress: bool, c2_stress: bool, holm_p: float,
            n_folds: int) -> str:
    if n_folds < MIN_FOLDS:
        return "inconclusive"
    if not (c1 and c2):
        return "no edge"
    if c1_stress and c2_stress and holm_p < ALPHA:
        return "edge"
    return "inconclusive"
