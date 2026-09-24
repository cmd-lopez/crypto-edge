"""Append-only trial ledger (SPEC §7.2). Every backtest run is one row; nothing is rewritten."""

from __future__ import annotations

import csv
from pathlib import Path

FIELDS = (
    "timestamp", "git_hash", "hypothesis", "params", "cost_case", "delay",
    "oos_start", "oos_end", "n_days", "sharpe", "max_drawdown", "fold_win_rate",
    "pvalue_vs_stronger", "turnover", "note",
)


def append_trial(path: Path, record: dict) -> None:
    keys = set(record)
    if keys != set(FIELDS):
        raise ValueError(f"ledger record fields mismatch: missing={set(FIELDS) - keys} "
                         f"extra={keys - set(FIELDS)}")
    path = Path(path)
    new = not path.exists()
    with path.open("a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(record)
