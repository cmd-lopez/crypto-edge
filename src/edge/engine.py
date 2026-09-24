"""Daily event-driven backtest engine (docs/plans/phase-2.md "Conventions").

Causality: the strategy is only ever called with `panel.upto(d)`; orders decided at the
close of bar d execute at the open of bar d + 1 + delay. The full panel is used only for
accounting (marking prices, detecting that a held asset has no further bars).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, Protocol

import numpy as np
import pandas as pd

from edge.data import Panel

DELIST_HAIRCUT = 0.10  # SPEC §4.4


@dataclass(frozen=True)
class CostModel:
    fee: float = 0.006
    slippage: float = 0.002

    @property
    def per_side(self) -> float:
        return self.fee + self.slippage

    def scaled(self, k: float) -> CostModel:
        return CostModel(self.fee * k, self.slippage * k)


@dataclass(frozen=True)
class Limits:
    """SPEC §2 risk limits. None disables a limit (benchmarks only)."""
    max_positions: int | None = 5
    max_weight: float = 0.20
    max_gross: float = 0.90
    daily_loss: float | None = 0.05
    max_drawdown: float | None = 0.15


class Strategy(Protocol):
    def target_weights(self, view: Panel, d: pd.Timestamp, held: frozenset[str]) -> pd.Series: ...
    def exits(self, view: Panel, d: pd.Timestamp, held: frozenset[str]) -> set[str]: ...


@dataclass
class Result:
    returns: pd.Series
    equity: pd.Series
    weights: pd.DataFrame
    trades: pd.DataFrame
    decisions: dict[pd.Timestamp, pd.Series]
    events: list[dict] = field(default_factory=list)

    @property
    def turnover(self) -> float:
        """Annualized one-sided traded notional / equity."""
        if self.trades.empty:
            return 0.0
        eq = self.equity.reindex(self.trades["date"]).to_numpy()
        years = len(self.returns) / 365
        return float((self.trades["value"].abs().to_numpy() / eq).sum() / 2 / years)


def apply_limits(w: pd.Series, limits: Limits) -> pd.Series:
    """Deterministic caps applied to any model/strategy output: count, per-asset, gross."""
    w = w[(w > 0) & np.isfinite(w)].astype(float)
    if w.empty:
        return w
    w = w.sort_index().sort_values(ascending=False, kind="stable")
    if limits.max_positions is not None:
        w = w.iloc[: limits.max_positions]
    w = w.clip(upper=limits.max_weight)
    if w.sum() > limits.max_gross:
        w = w * (limits.max_gross / w.sum())
    return w.sort_index()


@dataclass
class _Order:
    weights: pd.Series      # target weights for `assets`
    assets: frozenset[str]  # assets this order touches (full rebalance: all held + targets)
    no_increase: frozenset[str] = frozenset()


def _order_deltas(order: _Order, pos: dict, o_row: pd.Series, eq: float, blocked: bool,
                  band: float, limits: Limits) -> tuple[dict[str, float], list[str]]:
    """Target minus current value per asset; assets without a bar today are skipped and,
    if they needed selling, returned in `unsold` for a retry on the next bar."""
    deltas, unsold = {}, []
    for a in order.assets:
        cur = pos.get(a, 0.0)
        tgt = float(order.weights.get(a, 0.0)) * eq
        if blocked or a in order.no_increase:
            tgt = min(tgt, cur)
        if not np.isfinite(o_row.get(a, np.nan)):
            if tgt < cur - 1e-12:
                unsold.append(a)
            continue
        within_band = tgt > 0 and cur > 0 and abs(tgt - cur) <= band * tgt
        if within_band and cur <= limits.max_weight * eq:
            continue
        if abs(tgt - cur) > 1e-12:
            deltas[a] = tgt - cur
    return deltas, unsold


def _projected_gross(pos: dict, deltas: dict) -> float:
    return sum(pos.values()) + sum(deltas.values())


def _cap_new_entries(deltas: dict, pos: dict, limits: Limits) -> dict:
    """Drop the smallest new entries if positions that could not be sold would otherwise
    push the book above max_positions."""
    if limits.max_positions is None:
        return deltas
    after = {a for a in set(pos) | set(deltas) if pos.get(a, 0.0) + deltas.get(a, 0.0) > 1e-12}
    excess = len(after) - limits.max_positions
    if excess <= 0:
        return deltas
    new = sorted((a for a, d in deltas.items() if d > 0 and pos.get(a, 0.0) == 0.0),
                 key=lambda a: (-deltas[a], a))
    drop = set(new[len(new) - excess:]) if excess <= len(new) else set(new)
    return {a: d for a, d in deltas.items() if a not in drop}


def run(panel: Panel, strategy: Strategy, start: pd.Timestamp, end: pd.Timestamp,
        rebalance: Callable[[pd.Timestamp], bool], costs: CostModel, limits: Limits,
        delay: int = 0, dd_reset_dates: Iterable[pd.Timestamp] = (),
        universe: pd.DataFrame | None = None, band: float = 0.0) -> Result:
    """band: skip resizing a held position whose target is non-zero when
    |target - current| <= band * target (entries and exits always trade)."""
    dates = panel.dates[(panel.dates >= start) & (panel.dates <= end)]
    opens, closes = panel.open, panel.close
    last_bar = closes.apply(lambda s: s.last_valid_index())
    resets = set(pd.DatetimeIndex(list(dd_reset_dates)))
    c = costs.per_side

    cash, pos, px = 1.0, {}, {}  # pos: asset -> value; px: last marked price
    peak, prev_eq = 1.0, 1.0
    dd_halted, block_entries_on = False, None
    pending: dict[pd.Timestamp, _Order] = {}
    rets, eqs, wts, trades, events, decisions = [], [], [], [], [], {}

    def mark(prices: pd.Series) -> None:
        for a in list(pos):
            p = prices.get(a, np.nan)
            if np.isfinite(p):
                pos[a] *= p / px[a]
                px[a] = p

    for i, s in enumerate(dates):
        if s in resets and dd_halted:
            dd_halted, peak = False, prev_eq
            events.append({"date": s, "event": "drawdown_reset", "asset": None})
        o_row, c_row = opens.loc[s], closes.loc[s]
        mark(o_row)

        for a in [a for a in pos if last_bar[a] < s]:  # delisted: no bars after last_bar
            cash += pos.pop(a) * (1 - DELIST_HAIRCUT)
            px.pop(a)
            events.append({"date": s, "event": "delisted", "asset": a})

        order = pending.pop(s, None)
        if order is not None:
            eq = cash + sum(pos.values())
            blocked = block_entries_on == s or dd_halted
            deltas, unsold = _order_deltas(order, pos, o_row, eq, blocked, band, limits)
            if _projected_gross(pos, deltas) > limits.max_gross * eq + 1e-12:
                deltas, unsold = _order_deltas(order, pos, o_row, eq, blocked, 0.0, limits)
            deltas = _cap_new_entries(deltas, pos, limits)
            for a, d in sorted(deltas.items()):  # sells first
                if d < 0:
                    pos[a] += d
                    cash += -d * (1 - c)
                    trades.append({"date": s, "asset": a, "value": d, "cost": -d * c})
            buys = {a: d for a, d in deltas.items() if d > 0}
            headroom = max(0.0, limits.max_gross * eq - sum(pos.values()))
            need = sum(buys.values())
            scale = min(1.0, headroom / need, cash / (need * (1 + c))) if need > 0 else 1.0
            for a, d in sorted(buys.items()):
                d *= scale
                pos[a] = pos.get(a, 0.0) + d
                px[a] = o_row[a]
                cash -= d * (1 + c)
                trades.append({"date": s, "asset": a, "value": d, "cost": d * c})
            for a in [a for a, v in pos.items() if v <= 1e-12]:
                pos.pop(a), px.pop(a)
            if unsold and i + 1 < len(dates):  # retry sales that had no bar today
                nxt = dates[i + 1]
                prev = pending.get(nxt)
                retry = pd.Series({a: 0.0 for a in unsold})
                if prev is None:
                    pending[nxt] = _Order(retry, frozenset(unsold))
                else:
                    keep = prev.weights.drop(list(unsold), errors="ignore")
                    pending[nxt] = _Order(keep, prev.assets | frozenset(unsold), prev.no_increase)

        mark(c_row)
        eq = cash + sum(pos.values())
        ret = eq / prev_eq - 1
        rets.append(ret)
        eqs.append(eq)
        wts.append({a: v / eq for a, v in pos.items()})
        prev_eq = eq
        peak = max(peak, eq)

        if i + 1 + delay >= len(dates):
            continue
        exec_day = dates[i + 1 + delay]
        if limits.daily_loss is not None and ret <= -limits.daily_loss:
            block_entries_on = dates[i + 1]
            events.append({"date": s, "event": "daily_loss_halt", "asset": None})
        if limits.max_drawdown is not None and not dd_halted and eq / peak - 1 <= -limits.max_drawdown:
            dd_halted = True
            events.append({"date": s, "event": "drawdown_halt", "asset": None})
            pending[exec_day] = _Order(pd.Series(dtype=float), frozenset(pos))
            continue
        if dd_halted:
            continue

        view = panel.upto(s)
        held = frozenset(pos)
        exits = set(strategy.exits(view, s, held)) & held
        if rebalance(s):
            raw = strategy.target_weights(view, s, held)
            if universe is not None:
                in_uni = universe.loc[s].reindex(raw.index, fill_value=False)
                raw = raw[in_uni | raw.index.isin(held)]
            w = apply_limits(raw, limits).drop(list(exits), errors="ignore")
            no_inc = frozenset() if universe is None else frozenset(
                a for a in w.index if not bool(universe.loc[s].get(a, False)))
            decisions[s] = w
            pending[exec_day] = _Order(w, frozenset(w.index) | held, no_inc)
        elif exits:
            pending[exec_day] = _Order(pd.Series(dtype=float), frozenset(exits))

    idx = pd.DatetimeIndex(dates)
    trade_df = pd.DataFrame(trades, columns=["date", "asset", "value", "cost"])
    return Result(
        returns=pd.Series(rets, index=idx, name="ret"),
        equity=pd.Series(eqs, index=idx, name="equity"),
        weights=pd.DataFrame(wts, index=idx).reindex(columns=panel.close.columns).fillna(0.0),
        trades=trade_df, decisions=decisions, events=events,
    )
