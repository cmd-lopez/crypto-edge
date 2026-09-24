"""Performance metrics and multiple-testing statistics (SPEC §7.3)."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import norm

ANNUAL = 365
EULER_GAMMA = 0.5772156649015329


def sharpe(r: pd.Series) -> float:
    """Annualized Sharpe of daily returns, risk-free = 0. Zero-variance series -> 0."""
    sd = r.std(ddof=1)
    return 0.0 if not np.isfinite(sd) or sd == 0 else float(r.mean() / sd * np.sqrt(ANNUAL))


def max_drawdown(r: pd.Series) -> float:
    """Peak-to-trough decline of the compounded equity curve, as a positive fraction."""
    eq = np.cumprod(1 + np.asarray(r, dtype=float))
    peak = np.maximum.accumulate(np.concatenate([[1.0], eq]))[1:]
    return float(max(0.0, (1 - eq / peak).max())) if len(eq) else 0.0


def _per_period_sharpe(x: np.ndarray) -> np.ndarray:
    sd = x.std(axis=-1, ddof=1)
    return np.divide(x.mean(axis=-1), sd, out=np.zeros_like(sd), where=sd > 0)


def stationary_bootstrap_pvalue(a: pd.Series, b: pd.Series, mean_block: float = 7,
                                n_boot: int = 10_000, seed: int = 0, batch: int = 500) -> float:
    """One-sided p-value for H0: SR(a) <= SR(b), paired stationary bootstrap
    (Politis & Romano 1994), centered at the observed statistic."""
    x = np.column_stack([np.asarray(a, float), np.asarray(b, float)])
    n = len(x)
    stat = float(_per_period_sharpe(x[:, 0]) - _per_period_sharpe(x[:, 1]))
    rng = np.random.default_rng(seed)
    p_new = 1.0 / mean_block
    exceed = 0
    for lo in range(0, n_boot, batch):
        m = min(batch, n_boot - lo)
        new = rng.random((m, n)) < p_new
        starts = rng.integers(0, n, (m, n))
        idx = np.empty((m, n), dtype=np.int64)
        idx[:, 0] = starts[:, 0]
        for t in range(1, n):
            idx[:, t] = np.where(new[:, t], starts[:, t], (idx[:, t - 1] + 1) % n)
        sa, sb = x[idx, 0], x[idx, 1]
        diff = _per_period_sharpe(sa) - _per_period_sharpe(sb)
        exceed += int(((diff - stat) >= stat).sum())
    return (exceed + 1) / (n_boot + 1)


def holm(pvalues) -> list[float]:
    """Holm-Bonferroni adjusted p-values, returned in input order."""
    p = np.asarray(pvalues, float)
    m = len(p)
    order = np.argsort(p, kind="stable")
    adj = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (m - rank) * p[i]))
        adj[i] = running
    return adj.tolist()


def deflated_sharpe(sr: float, sr_var: float, n_trials: int, T: int, skew: float,
                    kurt: float) -> float:
    """Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014). sr is per-period (not
    annualized); sr_var is the variance of per-period Sharpe across trials; kurt is raw
    (normal = 3)."""
    if n_trials <= 1:
        sr0 = 0.0
    else:
        sr0 = np.sqrt(sr_var) * ((1 - EULER_GAMMA) * norm.ppf(1 - 1 / n_trials)
                                 + EULER_GAMMA * norm.ppf(1 - 1 / (n_trials * np.e)))
    denom = np.sqrt(1 - skew * sr + (kurt - 1) / 4 * sr**2)
    return float(norm.cdf((sr - sr0) * np.sqrt(T - 1) / denom))
