"""Rolling walk-forward splits (SPEC §7.2). Dates are inclusive daily bar dates."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

DAY = pd.Timedelta(days=1)


@dataclass(frozen=True)
class Fold:
    train_start: pd.Timestamp
    train_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp


def walk_forward(start: pd.Timestamp, end: pd.Timestamp, train_months: int = 12,
                 test_months: int = 3) -> list[Fold]:
    """Full test folds only (test_end <= end); consecutive test windows are contiguous."""
    folds, k = [], 0
    while True:
        tr0 = start + pd.DateOffset(months=test_months * k)
        te0 = tr0 + pd.DateOffset(months=train_months)
        te1 = te0 + pd.DateOffset(months=test_months) - DAY
        if te1 > end:
            return folds
        folds.append(Fold(tr0, te0 - DAY, te0, te1))
        k += 1
