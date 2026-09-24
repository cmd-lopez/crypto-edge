import csv

import numpy as np
import pandas as pd
import pytest

from edge.folds import walk_forward
from edge.ledger import FIELDS, append_trial
from edge.metrics import deflated_sharpe, holm, max_drawdown, sharpe, stationary_bootstrap_pvalue


def T(s):
    return pd.Timestamp(s, tz="UTC")


def test_walk_forward_boundaries_count_and_no_overlap():
    folds = walk_forward(T("2020-07-01"), T("2026-09-22"))
    assert len(folds) == 20
    f0, fl = folds[0], folds[-1]
    assert (f0.train_start, f0.train_end) == (T("2020-07-01"), T("2021-06-30"))
    assert (f0.test_start, f0.test_end) == (T("2021-07-01"), T("2021-09-30"))
    assert (fl.test_start, fl.test_end) == (T("2026-04-01"), T("2026-06-30"))
    for f in folds:
        assert f.train_end < f.test_start
    for a, b in zip(folds, folds[1:]):
        assert b.test_start == a.test_end + pd.Timedelta(days=1)  # contiguous OOS


def test_sharpe_and_drawdown_known_values():
    r = pd.Series([0.01, -0.01, 0.02, 0.0])
    assert sharpe(r) == pytest.approx(r.mean() / r.std(ddof=1) * np.sqrt(365))
    assert sharpe(pd.Series([0.0, 0.0, 0.0])) == 0.0
    assert max_drawdown(pd.Series([0.1, -0.5, 0.2])) == pytest.approx(0.5)
    assert max_drawdown(pd.Series([0.01, 0.02])) == 0.0


def test_bootstrap_pvalue_detects_dominance_and_not_noise():
    rng = np.random.default_rng(1)
    b = pd.Series(rng.normal(0, 0.03, 1500))
    a = b + 0.004 + pd.Series(rng.normal(0, 0.005, 1500))
    assert stationary_bootstrap_pvalue(a, b, n_boot=2000, seed=0) < 0.01
    assert stationary_bootstrap_pvalue(b, a, n_boot=2000, seed=0) > 0.99
    c = pd.Series(rng.normal(0, 0.03, 1500))
    p = stationary_bootstrap_pvalue(c, pd.Series(rng.normal(0, 0.03, 1500)), n_boot=2000, seed=0)
    assert 0.02 < p < 0.98


def test_holm_textbook_example():
    adj = holm([0.01, 0.04, 0.03, 0.005])
    assert adj == pytest.approx([0.03, 0.06, 0.06, 0.02])
    assert holm([0.5, 0.9]) == pytest.approx([1.0, 1.0])  # step-down monotonicity


def test_deflated_sharpe_penalizes_more_trials_and_reduces_to_psr_for_one_trial():
    kw = dict(sr=0.08, sr_var=0.0025, T=1000, skew=0.0, kurt=3.0)
    d1, d10, d1000 = (deflated_sharpe(n_trials=n, **kw) for n in (1, 10, 1000))
    assert d1 > d10 > d1000
    from scipy.stats import norm
    assert d1 == pytest.approx(norm.cdf(0.08 * np.sqrt(999) / np.sqrt(1 + 0.5 * 0.08**2)))


def test_ledger_appends_and_never_rewrites(tmp_path):
    path = tmp_path / "trials.csv"
    rec = {f: "x" for f in FIELDS}
    append_trial(path, rec)
    append_trial(path, {**rec, "hypothesis": "second"})
    rows = list(csv.DictReader(path.open()))
    assert [r["hypothesis"] for r in rows] == ["x", "second"]
    with pytest.raises(ValueError):
        append_trial(path, {"hypothesis": "incomplete"})
    with pytest.raises(ValueError):
        append_trial(path, {**rec, "unexpected": 1})
