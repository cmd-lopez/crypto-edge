"""Rules must match EDGE_REPORT.md §2 exactly (pre-registration commit c24ad22)."""

import numpy as np
import pandas as pd
import pytest

from edge.hypotheses import H1TrendGate, H2AssetTrend, H3TrendComposite, biweekly, weekly
from tests.helpers import frame, panel

N = 160


def last(p):
    return p.dates[-1]


def uni_all(p):
    return pd.DataFrame(True, index=p.dates, columns=p.close.columns)


def test_h1_gate_on_btc_sma_and_portfolios():
    up = np.linspace(100, 200, N)
    fr = {"BTC-USD": frame("2024-01-01", up, volume=1)}
    for i, v in enumerate([9, 8, 7, 6, 5, 4]):  # ADV ranking: A0 highest
        fr[f"A{i}-USD"] = frame("2024-01-01", np.ones(N), volume=v * 1e6)
    p = panel(fr)
    u = uni_all(p)
    w = H1TrendGate(L=50, portfolio="btc", universe=u).target_weights(p, last(p), frozenset())
    assert w.to_dict() == {"BTC-USD": 0.18}
    w5 = H1TrendGate(L=50, portfolio="top5", universe=u).target_weights(p, last(p), frozenset())
    # BTC dollar volume ~ 200/day is lowest; top5 by ADV are A0..A4
    assert sorted(w5.index) == [f"A{i}-USD" for i in range(5)] and (w5 == 0.18).all()
    fr["BTC-USD"] = frame("2024-01-01", up[::-1], volume=1)  # downtrend
    p2 = panel(fr)
    assert H1TrendGate(L=50, portfolio="top5", universe=uni_all(p2)).target_weights(
        p2, last(p2), frozenset()).empty


def test_h1_sma_uses_exactly_last_L_closes():
    closes = np.full(N, 100.0)
    closes[-1] = 100.5          # close_d just above mean of last 50 closes
    closes[-60:-50] = 1000.0    # outside a 50-bar window, inside a 60-bar one
    p = panel({"BTC-USD": frame("2024-01-01", closes)})
    u = uni_all(p)
    assert not H1TrendGate(50, "btc", u).target_weights(p, last(p), frozenset()).empty
    assert H1TrendGate(60, "btc", u).target_weights(p, last(p), frozenset()).empty


def test_h2_requires_both_trend_conditions_and_ranks_by_adv():
    t = np.arange(N, dtype=float)
    fr = {
        "UP1-USD": frame("2024-01-01", 100 + t, volume=1e6),
        "UP2-USD": frame("2024-01-01", 100 + t, volume=3e6),
        "DOWN-USD": frame("2024-01-01", 300 - t, volume=9e6),
        # above SMA20 but below its level 28 days ago -> not eligible
        "BOUNCE-USD": frame("2024-01-01", np.r_[np.full(N - 20, 200.0), np.linspace(150, 190, 20)],
                            volume=9e6),
    }
    p = panel(fr)
    w = H2AssetTrend(L=20, universe=uni_all(p)).target_weights(p, last(p), frozenset())
    assert set(w.index) == {"UP1-USD", "UP2-USD"}
    assert (w == 0.18).all()


def test_h2_caps_at_five_by_adv_and_needs_history():
    t = np.arange(N, dtype=float)
    fr = {f"U{i}-USD": frame("2024-01-01", 100 + t, volume=(i + 1) * 1e6) for i in range(7)}
    fr["YOUNG-USD"] = frame(str((pd.Timestamp("2024-01-01") + pd.Timedelta(days=N - 40)).date()),
                            100 + np.arange(40.0), volume=1e9)
    p = panel(fr)
    w = H2AssetTrend(L=20, universe=uni_all(p)).target_weights(p, last(p), frozenset())
    assert set(w.index) == {f"U{i}-USD" for i in range(2, 7)}  # 40 bars < 20+28


def test_h3_score_selection_buffer_and_fill():
    rng = np.random.default_rng(3)
    fr = {}
    for i in range(20):
        drift = 0.001 * (i - 10)  # higher i -> stronger trend
        fr[f"S{i:02d}-USD"] = frame("2024-01-01",
                                    100 * np.exp(np.cumsum(drift + rng.normal(0, 0.0001, N))))
    p = panel(fr)
    s = H3TrendComposite(cadence="weekly", universe=uni_all(p))
    fresh = s.target_weights(p, last(p), frozenset())
    assert set(fresh.index) == {f"S{i}-USD" for i in range(15, 20)} and (fresh == 0.18).all()
    # S12 ranks 8/20 (top 50%): kept by the buffer; S03 is bottom half: dropped
    kept = s.target_weights(p, last(p), frozenset({"S12-USD", "S03-USD"}))
    assert set(kept.index) == {"S12-USD", "S19-USD", "S18-USD", "S17-USD", "S16-USD"}


def test_h3_requires_100_closes():
    t = np.arange(N, dtype=float)
    fr = {"OLD-USD": frame("2024-01-01", 100 + t),
          "NEW-USD": frame(str((pd.Timestamp("2024-01-01") + pd.Timedelta(days=N - 99)).date()),
                           100 + 5 * np.arange(99.0))}
    p = panel(fr)
    w = H3TrendComposite(cadence="weekly", universe=uni_all(p)).target_weights(p, last(p), frozenset())
    assert "NEW-USD" not in w.index


def test_cadences():
    sundays = pd.date_range("2020-07-05", periods=6, freq="7D", tz="UTC")
    assert all(weekly(d) for d in sundays) and not weekly(sundays[0] + pd.Timedelta(days=1))
    assert [biweekly(d) for d in sundays] == [True, False, True, False, True, False]
