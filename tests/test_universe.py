import numpy as np
import pandas as pd

from edge.universe import EXCLUDED, eligibility
from tests.helpers import frame, panel

N = 60


def ts(i: int) -> pd.Timestamp:
    return pd.Timestamp("2024-01-01", tz="UTC") + pd.Timedelta(days=i)


def base_frames():
    return {
        "BIG-USD": frame("2024-01-01", np.ones(N), volume=10e6),     # $10M/day
        "SMALL-USD": frame("2024-01-01", np.ones(N), volume=1e6),    # $1M/day
        "USDC-USD": frame("2024-01-01", np.ones(N), volume=100e6),   # stablecoin
    }


def test_exclusions_and_adv_threshold():
    assert "USDC" in EXCLUDED and "WBTC" in EXCLUDED
    e = eligibility(panel(base_frames()))
    assert e.loc[ts(N - 1), "BIG-USD"]
    assert not e.loc[ts(N - 1), "SMALL-USD"]
    assert not e["USDC-USD"].any()


def test_min_history_and_full_window_required():
    fr = base_frames()
    fr["NEW-USD"] = frame(str(ts(40).date()), np.ones(N - 40), volume=50e6)
    e = eligibility(panel(fr))
    # BIG needs 30 bars: first eligible at index 29
    assert not e.loc[ts(28), "BIG-USD"] and e.loc[ts(29), "BIG-USD"]
    # NEW listed day 40 with only 20 bars by day 59 -> never eligible
    assert not e["NEW-USD"].any()


def test_no_look_ahead_future_perturbation_does_not_change_past_mask():
    fr = base_frames()
    e1 = eligibility(panel(fr))
    fr2 = {k: v.copy() for k, v in fr.items()}
    fr2["SMALL-USD"].loc[45:, "volume"] = 1e12  # huge future volume
    e2 = eligibility(panel(fr2))
    pd.testing.assert_frame_equal(e1.loc[: ts(44)], e2.loc[: ts(44)])
    assert e2.loc[ts(N - 1), "SMALL-USD"]  # and it does matter later


def test_top_n_by_adv():
    fr = {f"A{i}-USD": frame("2024-01-01", np.ones(N), volume=(i + 6) * 1e6) for i in range(5)}
    e = eligibility(panel(fr), top_n=2)
    assert e.loc[ts(N - 1)].sum() == 2
    assert e.loc[ts(N - 1), ["A4-USD", "A3-USD"]].all()


def test_asset_without_a_bar_on_d_is_not_in_universe():
    fr = base_frames()
    fr["DEAD-USD"] = frame("2024-01-01", np.ones(40), volume=10e6)  # last bar day 39
    e = eligibility(panel(fr))
    assert e.loc[ts(39), "DEAD-USD"]
    # trailing ADV is still >= $5M on day 40, but there is no bar: not tradeable
    assert not e.loc[ts(40):, "DEAD-USD"].any()
