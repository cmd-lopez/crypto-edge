import numpy as np
import pandas as pd

from edge.data import load_panel, manifest
from tests.helpers import frame, panel


def test_incomplete_last_bar_is_dropped():
    f = frame("2024-01-01", [1, 2, 3])
    # now = 2024-01-03 12:00 -> bar 2024-01-03 still open
    p = panel({"A-USD": f}, now="2024-01-03T12:00:00Z")
    assert p.close.index.max() == pd.Timestamp("2024-01-02", tz="UTC")
    p2 = panel({"A-USD": f}, now="2024-01-04T00:00:00Z")
    assert p2.close.index.max() == pd.Timestamp("2024-01-03", tz="UTC")


def test_missing_day_is_nan_price_and_zero_dollar_volume():
    f = frame("2024-01-01", [1, 2, 3, 4], volume=10.0).drop(index=2)
    p = panel({"A-USD": f, "B-USD": frame("2024-01-01", [5, 5, 5, 5])})
    gap = pd.Timestamp("2024-01-03", tz="UTC")
    assert np.isnan(p.close.loc[gap, "A-USD"])
    assert np.isnan(p.open.loc[gap, "A-USD"])
    assert p.dollar_volume.loc[gap, "A-USD"] == 0.0


def test_dollar_volume_is_volume_times_close():
    p = panel({"A-USD": frame("2024-01-01", [2.0, 3.0], volume=[10.0, 4.0])})
    assert p.dollar_volume["A-USD"].tolist() == [20.0, 12.0]


def test_upto_hides_future_bars():
    p = panel({"A-USD": frame("2024-01-01", [1, 2, 3, 4])})
    v = p.upto(pd.Timestamp("2024-01-02", tz="UTC"))
    assert v.close.index.max() == pd.Timestamp("2024-01-02", tz="UTC")
    assert len(v.open) == len(v.dollar_volume) == 2


def test_load_panel_and_manifest_roundtrip(tmp_path):
    f = frame("2024-01-01", [1, 2, 3])
    f.to_csv(tmp_path / "A-USD.csv", index=False)
    p = load_panel(tmp_path, pd.Timestamp("2024-01-10", tz="UTC"))
    assert p.close["A-USD"].tolist() == [1.0, 2.0, 3.0]
    m1, m2 = manifest(tmp_path), manifest(tmp_path)
    assert m1 == m2 and set(m1) == {"A-USD.csv"} and len(m1["A-USD.csv"]) == 64
