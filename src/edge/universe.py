"""Point-in-time universe (SPEC §4.1). Row d uses only bars with open date <= d."""

from __future__ import annotations

import pandas as pd

from edge.data import Panel

# base currency -> reason (added 2026-09-23 unless noted)
EXCLUDED: dict[str, str] = {
    **{s: "USD stablecoin" for s in (
        "USDC", "USDT", "DAI", "PYUSD", "GUSD", "PAX", "USDP", "BUSD", "UST", "TUSD",
        "USDS", "FDUSD", "RLUSD", "USD1", "MUSD", "LUSD", "FRAX", "SUSD", "USDE", "USDG")},
    **{s: "non-USD fiat stablecoin" for s in ("EURC", "GYEN")},
    **{s: "wrapped / bridged representation" for s in (
        "WBTC", "WETH", "CBBTC", "CBDOGE", "CBXRP", "CBADA", "CBLTC")},
    **{s: "liquid staking derivative" for s in (
        "CBETH", "WSTETH", "STETH", "RETH", "MSOL", "JITOSOL", "LSETH")},
    **{s: "commodity-pegged token" for s in ("PAXG", "XAUT")},
}


def base_of(product_id: str) -> str:
    return product_id.split("-")[0]


def eligibility(panel: Panel, min_adv: float = 5e6, window: int = 30,
                min_history: int = 30, top_n: int = 50) -> pd.DataFrame:
    """Boolean mask [date x product]: tradeable universe as known at the close of each date."""
    adv = panel.dollar_volume.rolling(window, min_periods=window).mean()
    history = panel.close.notna().cumsum()
    allowed = pd.Series([base_of(c) not in EXCLUDED for c in panel.close.columns],
                        index=panel.close.columns)
    tradeable = panel.close.notna()  # a bar on d: listed and trading at d
    passing = (adv >= min_adv) & (history >= min_history) & allowed & tradeable
    ranked = adv.where(passing).rank(axis=1, ascending=False, method="first")
    return passing & (ranked <= top_n)
