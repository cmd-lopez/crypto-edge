"""Pre-registered hypotheses H1-H3 (EDGE_REPORT.md §2, commit 7c879de).

Each strategy returns at most 5 names at WEIGHT each; the engine applies SPEC limits.
Strategies only receive `view = panel.upto(d)` and read universe row d (causal).
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from edge.data import Panel

WEIGHT = 0.18  # 90% / 5
MAX_NAMES = 5
ANCHOR_SUNDAY = pd.Timestamp("2020-07-05", tz="UTC")


def weekly(d: pd.Timestamp) -> bool:
    return d.dayofweek == 6


def biweekly(d: pd.Timestamp) -> bool:
    return weekly(d) and ((d - ANCHOR_SUNDAY).days // 7) % 2 == 0


def _members(universe: pd.DataFrame, d: pd.Timestamp) -> list[str]:
    row = universe.loc[d]
    return list(row[row].index)


def _top_by(values: pd.Series, k: int) -> list[str]:
    """Highest values first; ties broken by name for determinism."""
    df = pd.DataFrame({"v": values, "name": values.index}).dropna()
    return list(df.sort_values(["v", "name"], ascending=[False, True])["name"].iloc[:k])


def _adv30(view: Panel, names: list[str]) -> pd.Series:
    return view.dollar_volume[names].iloc[-30:].mean()


def _complete(view: Panel, names: list[str], n: int) -> list[str]:
    tail = view.close[names].iloc[-n:]
    return [c for c in names if len(tail) == n and tail[c].notna().all()]


def _equal(names: list[str]) -> pd.Series:
    return pd.Series(WEIGHT, index=names, dtype=float)


class _Base:
    rebalance = staticmethod(weekly)

    def exits(self, view, d, held) -> set[str]:
        return set()


class H1TrendGate(_Base):
    def __init__(self, L: int, portfolio: str, universe: pd.DataFrame):
        assert portfolio in ("btc", "top5")
        self.L, self.portfolio, self.universe = L, portfolio, universe

    def target_weights(self, view: Panel, d: pd.Timestamp, held: frozenset[str]) -> pd.Series:
        btc = view.close["BTC-USD"].iloc[-self.L:]
        if len(btc) < self.L or btc.isna().any() or not btc.iloc[-1] > btc.mean():
            return pd.Series(dtype=float)
        if self.portfolio == "btc":
            return _equal(["BTC-USD"])
        names = _members(self.universe, d)
        return _equal(_top_by(_adv30(view, names), MAX_NAMES))


class H2AssetTrend(_Base):
    def __init__(self, L: int, universe: pd.DataFrame):
        self.L, self.universe = L, universe

    def target_weights(self, view: Panel, d: pd.Timestamp, held: frozenset[str]) -> pd.Series:
        names = _complete(view, _members(self.universe, d), self.L + 28)
        if not names:
            return pd.Series(dtype=float)
        c = view.close[names]
        now, sma, ago = c.iloc[-1], c.iloc[-self.L:].mean(), c.iloc[-29]
        eligible = [n for n in names if now[n] > sma[n] and now[n] > ago[n]]
        return _equal(_top_by(_adv30(view, eligible), MAX_NAMES)) if eligible else pd.Series(dtype=float)


class H3TrendComposite(_Base):
    LOOKBACKS = (5, 10, 20, 50, 100)

    def __init__(self, cadence: str, universe: pd.DataFrame):
        assert cadence in ("weekly", "biweekly")
        self.cadence, self.universe = cadence, universe
        self.rebalance = weekly if cadence == "weekly" else biweekly

    def score(self, view: Panel, d: pd.Timestamp) -> pd.Series:
        names = _complete(view, _members(self.universe, d), max(self.LOOKBACKS))
        if not names:
            return pd.Series(dtype=float)
        c = view.close[names]
        ranks = [np.log(c.iloc[-1] / c.iloc[-L:].mean()).rank(pct=True) for L in self.LOOKBACKS]
        return pd.concat(ranks, axis=1).mean(axis=1)

    def target_weights(self, view: Panel, d: pd.Timestamp, held: frozenset[str]) -> pd.Series:
        score = self.score(view, d)
        if score.empty:
            return score
        order = _top_by(score, len(score))
        top_half = set(order[: math.ceil(len(order) / 2)])
        kept = [n for n in order if n in held and n in top_half][:MAX_NAMES]
        fill = [n for n in order if n not in held][: MAX_NAMES - len(kept)]  # §2: "not held"
        return _equal(kept + fill)
