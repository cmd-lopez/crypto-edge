import numpy as np
import pandas as pd
import pytest

from edge.benchmarks import BuyHoldBTC, EqualWeightMonthly, month_end
from edge.engine import CostModel, Limits, run
from tests.helpers import frame, panel

NO_LIMITS = Limits(max_positions=None, max_weight=1.0, max_gross=1.0, daily_loss=None, max_drawdown=None)


def test_buy_hold_btc_pays_one_entry_cost_then_tracks_btc():
    closes = [100, 100, 120, 90]
    p = panel({"BTC-USD": frame("2024-01-01", closes), "ETH-USD": frame("2024-01-01", [1] * 4)})
    s = BuyHoldBTC()
    start = p.dates[0]
    r = run(p, s, start, p.dates[-1], s.rebalance_at(start), CostModel(0.006, 0.002), NO_LIMITS)
    eq = r.equity
    assert eq.iloc[1] == pytest.approx(1 / 1.008)
    assert eq.iloc[3] / eq.iloc[1] == pytest.approx(0.9)
    assert len(r.trades) == 1


def test_equal_weight_over_point_in_time_universe_monthly():
    idx = pd.date_range("2024-01-30", periods=4, freq="D", tz="UTC")  # Jan 30,31, Feb 1,2
    uni = pd.DataFrame({"A-USD": [True] * 4, "B-USD": [True] * 4, "C-USD": [False] * 4}, index=idx)
    s = EqualWeightMonthly(uni)
    w = s.target_weights(None, idx[1], frozenset())
    assert w.to_dict() == {"A-USD": 0.5, "B-USD": 0.5}
    assert [month_end(d) for d in idx] == [False, True, False, False]
