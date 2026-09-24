import numpy as np
import pandas as pd
import pytest

from edge.evaluation import Switching, fold_sharpes, fold_win_rate, select_cells, verdict
from edge.folds import Fold


def T(s):
    return pd.Timestamp(s, tz="UTC")


FOLDS = [Fold(T("2021-01-01"), T("2021-12-31"), T("2022-01-01"), T("2022-01-10")),
         Fold(T("2021-01-11"), T("2022-01-10"), T("2022-01-11"), T("2022-01-20"))]


def test_fold_sharpes_slice_each_test_window():
    idx = pd.date_range("2022-01-01", "2022-01-20", tz="UTC")
    r = pd.Series(np.r_[np.tile([0.01, -0.005], 5), np.zeros(10)], index=idx)
    fs = fold_sharpes(r, FOLDS)
    assert fs.iloc[0] > 0 and fs.iloc[1] == 0.0 and len(fs) == 2


def test_fold_win_rate_requires_strictly_beating_every_benchmark():
    s = pd.Series([1.0, 0.5, 0.0, 2.0])
    b1 = pd.Series([0.5, 0.5, -1.0, 1.0])
    b2 = pd.Series([0.9, 0.1, -0.5, 3.0])
    assert fold_win_rate(s, [b1, b2]) == pytest.approx(2 / 4)  # folds 0 and 2


def test_select_cells_picks_best_train_sharpe_ties_to_grid_order():
    train = pd.DataFrame({"a": [1.0, 0.2, 0.5], "b": [0.5, 0.9, 0.5]})
    assert select_cells(train) == ["a", "b", "a"]


def test_switching_routes_decisions_to_the_fold_strategy():
    class S:
        def __init__(self, tag):
            self.tag = tag
            self.rebalance = lambda d: tag == "x"

        def target_weights(self, view, d, held):
            return pd.Series({self.tag: 0.1})

        def exits(self, view, d, held):
            return {self.tag}

    sw = Switching(FOLDS, [S("x"), S("y")])
    assert sw.target_weights(None, T("2022-01-05"), frozenset()).index[0] == "x"
    assert sw.target_weights(None, T("2022-01-15"), frozenset()).index[0] == "y"
    assert sw.rebalance(T("2022-01-05")) and not sw.rebalance(T("2022-01-15"))
    assert sw.exits(None, T("2022-01-15"), frozenset()) == {"y"}
    with pytest.raises(KeyError):
        sw.target_weights(None, T("2023-01-01"), frozenset())


@pytest.mark.parametrize("args, expected", [
    (dict(c1=True, c2=True, c1_stress=True, c2_stress=True, holm_p=0.01, n_folds=20), "edge"),
    (dict(c1=True, c2=True, c1_stress=False, c2_stress=True, holm_p=0.01, n_folds=20), "inconclusive"),
    (dict(c1=True, c2=True, c1_stress=True, c2_stress=True, holm_p=0.20, n_folds=20), "inconclusive"),
    (dict(c1=True, c2=True, c1_stress=True, c2_stress=True, holm_p=0.01, n_folds=7), "inconclusive"),
    (dict(c1=False, c2=True, c1_stress=True, c2_stress=True, holm_p=0.01, n_folds=20), "no edge"),
    (dict(c1=True, c2=False, c1_stress=True, c2_stress=True, holm_p=0.01, n_folds=20), "no edge"),
])
def test_verdict_rules_match_spec_7_4(args, expected):
    assert verdict(**args) == expected
