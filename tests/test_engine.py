import numpy as np
import pandas as pd
import pytest

from edge.engine import CostModel, Limits, apply_limits, run
from tests.helpers import frame, panel

NO_LIMITS = Limits(max_positions=None, max_weight=1.0, max_gross=1.0, daily_loss=None, max_drawdown=None)


def ts(i: int) -> pd.Timestamp:
    return pd.Timestamp("2024-01-01", tz="UTC") + pd.Timedelta(days=i)


class Fixed:
    """Targets fixed weights on rebalance days; optional per-day exits."""

    def __init__(self, weights, exits=None):
        self.weights, self._exits, self.seen, self.helds = weights, exits or {}, [], {}

    def target_weights(self, view, d, held):
        self.seen.append(view.close.index.max())
        self.helds[d] = held
        return pd.Series(self.weights, dtype=float)

    def exits(self, view, d, held):
        return set(self._exits.get(d, ()))


def on(*days):
    s = {ts(i) for i in days}
    return lambda d: d in s


def test_strategy_receives_actual_holdings_not_its_own_targets():
    a = frame("2024-01-01", [10, 10, 10])  # delisted after day 2
    b = frame("2024-01-01", [10] * 5)
    s = Fixed({"A-USD": 0.4, "B-USD": 0.4})
    run(panel({"A-USD": a, "B-USD": b}), s, ts(0), ts(4), lambda d: True, CostModel(0, 0), NO_LIMITS)
    assert s.helds[ts(0)] == frozenset()
    assert s.helds[ts(1)] == {"A-USD", "B-USD"}
    assert s.helds[ts(3)] == {"B-USD"}  # A was written off on day 3


def test_costs_and_fill_at_next_open_not_same_close():
    p = panel({"A-USD": frame("2024-01-01", [100, 110, 121], opens=[100, 105, 110])})
    c = CostModel(fee=0.008, slippage=0.002)
    r = run(p, Fixed({"A-USD": 1.0}), ts(0), ts(2), on(0), c, NO_LIMITS)
    bought = 1 / 1.01  # value such that value * (1 + 1%) = 1.0 cash
    eq1 = bought * 110 / 105
    assert r.returns.loc[ts(0)] == 0.0
    assert r.returns.loc[ts(1)] == pytest.approx(eq1 - 1)
    assert r.returns.loc[ts(2)] == pytest.approx(0.1)
    t = r.trades.iloc[0]
    assert t["date"] == ts(1) and t["cost"] == pytest.approx(bought * 0.01)


def test_delay_shifts_fill_by_one_bar():
    p = panel({"A-USD": frame("2024-01-01", [100, 110, 121], opens=[100, 105, 110])})
    r = run(p, Fixed({"A-USD": 1.0}), ts(0), ts(2), on(0), CostModel(0, 0), NO_LIMITS, delay=1)
    assert r.returns.loc[ts(1)] == 0.0
    assert r.returns.loc[ts(2)] == pytest.approx(121 / 110 - 1)


def test_scaled_costs_double():
    c = CostModel(fee=0.006, slippage=0.002).scaled(2)
    assert c.per_side == pytest.approx(0.016)


def test_apply_limits_positions_weight_and_gross():
    w = pd.Series({f"A{i}-USD": 0.3 for i in range(7)})
    out = apply_limits(w, Limits())
    assert len(out) == 5
    assert list(out.index) == [f"A{i}-USD" for i in range(5)]  # ties broken by name
    assert out.max() <= 0.20 + 1e-12
    assert out.sum() == pytest.approx(0.90)
    assert apply_limits(pd.Series({"A-USD": -0.1, "B-USD": np.nan}), Limits()).empty


def test_engine_enforces_limits_whatever_strategy_asks():
    fr = {f"A{i}-USD": frame("2024-01-01", np.full(4, 10.0)) for i in range(8)}
    r = run(panel(fr), Fixed({k: 5.0 for k in fr}), ts(0), ts(3), on(0), CostModel(0, 0), Limits())
    held = r.weights.loc[ts(1)]
    assert (held > 0).sum() == 5 and held.max() <= 0.2 + 1e-9 and held.sum() <= 0.9 + 1e-9


def test_daily_loss_blocks_entries_at_next_execution_only():
    a = frame("2024-01-01", [10, 5, 5, 5, 5], opens=[10, 10, 5, 5, 5])  # -50% during day 1
    b = frame("2024-01-01", [10, 10, 10, 10, 10])
    lim = Limits(max_positions=5, max_weight=0.2, max_gross=0.9, daily_loss=0.05, max_drawdown=None)
    r = run(panel({"A-USD": a, "B-USD": b}), _Seq({0: {"A-USD": 0.2}, 1: {"A-USD": 0.2, "B-USD": 0.2},
                                                   2: {"A-USD": 0.2, "B-USD": 0.2}}),
            ts(0), ts(4), on(0, 1, 2), CostModel(0, 0), lim)
    trades = r.trades.set_index(["date", "asset"])
    assert r.returns.loc[ts(1)] <= -0.05
    assert (ts(2), "B-USD") not in trades.index      # blocked day after the loss
    assert (ts(2), "A-USD") not in trades.index      # no top-up either
    assert (ts(3), "B-USD") in trades.index           # allowed again next day
    assert "daily_loss_halt" in {e["event"] for e in r.events}


class _Seq:
    def __init__(self, by_day):
        self.by_day = {ts(k): v for k, v in by_day.items()}

    def target_weights(self, view, d, held):
        return pd.Series(self.by_day.get(d, {}), dtype=float)

    def exits(self, view, d, held):
        return set()


def test_drawdown_breaker_flattens_and_halts_until_reset():
    a = frame("2024-01-01", [10, 7, 7, 7, 7, 7, 7], opens=[10, 10, 7, 7, 7, 7, 7])  # -30% day 1
    lim = Limits(max_positions=5, max_weight=1.0, max_gross=0.9, daily_loss=None, max_drawdown=0.15)
    r = run(panel({"A-USD": a}), Fixed({"A-USD": 0.9}), ts(0), ts(6), lambda d: True,
            CostModel(0, 0), lim, dd_reset_dates=[ts(4)])
    w = r.weights["A-USD"]
    assert w.loc[ts(1)] > 0.8
    assert (w.loc[ts(2):ts(4)] == 0).all()   # flattened at day-2 open, halted through reset day
    assert w.loc[ts(5)] > 0.8                # decision at close of reset day -> buy day 5
    assert "drawdown_halt" in {e["event"] for e in r.events}


def test_delisted_holding_exits_with_haircut_and_gap_day_holds_price():
    a = frame("2024-01-01", [10, 10, 10])                       # last bar day 2
    g = frame("2024-01-01", [10, 10, 10, 10, 10, 10]).drop(index=3)  # gap on day 3 only
    b = frame("2024-01-01", [10] * 6)
    r = run(panel({"A-USD": a, "G-USD": g, "B-USD": b}), Fixed({"A-USD": 0.5, "G-USD": 0.5}),
            ts(0), ts(5), on(0), CostModel(0, 0), NO_LIMITS)
    assert r.returns.loc[ts(3)] == pytest.approx(-0.05)  # 10% haircut on 50% sleeve
    assert r.weights.loc[ts(3), "A-USD"] == 0
    assert r.returns.loc[ts(4)] == 0 and r.weights.loc[ts(4), "G-USD"] > 0
    assert any(e["event"] == "delisted" and e["asset"] == "A-USD" for e in r.events)


def test_untradeable_and_out_of_universe_targets_are_skipped():
    a = frame("2024-01-01", [10, 10, 10]).drop(index=1)  # no bar on execution day 1
    b = frame("2024-01-01", [10, 10, 10])
    c = frame("2024-01-01", [10, 10, 10])
    uni = pd.DataFrame(True, index=[ts(i) for i in range(3)], columns=["A-USD", "B-USD", "C-USD"])
    uni["C-USD"] = False
    r = run(panel({"A-USD": a, "B-USD": b, "C-USD": c}),
            Fixed({"A-USD": 0.3, "B-USD": 0.3, "C-USD": 0.3}),
            ts(0), ts(2), on(0), CostModel(0, 0), NO_LIMITS, universe=uni)
    assert set(r.trades["asset"]) == {"B-USD"}


def test_no_trade_band_skips_small_rebalances_but_not_entries_or_exits():
    a = frame("2024-01-01", [10, 10, 11, 11, 11, 11])  # A drifts up 10% on day 2
    b = frame("2024-01-01", [10] * 6)
    seq = _Seq({0: {"A-USD": 0.4, "B-USD": 0.4}, 2: {"A-USD": 0.4, "B-USD": 0.4}, 3: {"B-USD": 0.4}})
    r = run(panel({"A-USD": a, "B-USD": b}), seq, ts(0), ts(5), on(0, 2, 3), CostModel(0, 0),
            NO_LIMITS, band=0.20)
    days = r.trades.groupby("date")["asset"].apply(set).to_dict()
    assert days[ts(1)] == {"A-USD", "B-USD"}  # entries always trade
    assert ts(3) not in days                  # drift within 20% of target: no trade
    assert days[ts(4)] == {"A-USD"}           # exit always trades


def test_strategy_only_sees_bars_up_to_decision_date():
    p = panel({"A-USD": frame("2024-01-01", np.arange(1, 11, dtype=float))})
    s = Fixed({"A-USD": 0.5})
    run(p, s, ts(0), ts(9), lambda d: True, CostModel(0, 0), NO_LIMITS)
    # one call per decision day, each seeing exactly bars <= d; no decision on the last bar
    # because nothing could execute after it
    assert s.seen == [ts(i) for i in range(9)]


class Momentum:
    def target_weights(self, view, d, held):
        ret = view.close.iloc[-1] / view.close.iloc[-8] - 1 if len(view.close) >= 8 else view.close.iloc[-1] * 0
        return (ret.nlargest(2) > -1).astype(float) * 0.4

    def exits(self, view, d, held):
        r1 = view.close.iloc[-1] / view.close.iloc[-2] - 1 if len(view.close) >= 2 else None
        return set() if r1 is None else {a for a in held if r1.get(a, 0) < -0.08}


def test_look_ahead_future_perturbation_leaves_past_decisions_unchanged():
    rng = np.random.default_rng(0)
    n, k = 120, 70
    fr = {f"X{i}-USD": frame("2024-01-01", 100 * np.exp(np.cumsum(rng.normal(0, 0.04, n))))
          for i in range(6)}
    base = run(panel(fr), Momentum(), ts(10), ts(n - 1), lambda d: d.dayofweek == 6,
               CostModel(), Limits())
    fr2 = {}
    for key, f in fr.items():
        f = f.copy()
        shock = np.exp(rng.normal(0, 0.3, n - k - 1))
        for col in ("open", "high", "low", "close"):
            f.loc[k + 1:, col] = f.loc[k + 1:, col].to_numpy() * shock
        fr2[key] = f
    pert = run(panel(fr2), Momentum(), ts(10), ts(n - 1), lambda d: d.dayofweek == 6,
               CostModel(), Limits())
    pd.testing.assert_series_equal(base.returns.loc[:ts(k)], pert.returns.loc[:ts(k)])
    early = [d for d in base.decisions if d <= ts(k)]
    assert early and all(base.decisions[d].equals(pert.decisions[d]) for d in early)
    assert not base.returns.loc[ts(k + 2):].equals(pert.returns.loc[ts(k + 2):])
