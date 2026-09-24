# 01 — Market regime as of 2026-09-23

Scope: descriptive snapshot to condition Phase-2 hypotheses. No backtests run. All price-derived numbers use the **last complete Coinbase 1D candle, 2026-09-23 (00:00 UTC open, closes 2026-09-24 00:00 UTC)**. Fetch time ≈ 2026-09-24 03:05–03:15 UTC. "Snapshot" = current-only value, not reproducible later.

## 1. Measured facts

### 1.1 BTC / ETH trend, vol, drawdown
Source: `https://api.exchange.coinbase.com/products/{BTC,ETH}-USD/candles?granularity=86400` (paged 300/request, 2018-07-08 → 2026-09-23). Computed locally: SMA on closes; RV = stdev of daily log returns × √365; drawdown vs max daily close/high in fetched history.

| Metric | BTC-USD | ETH-USD |
|---|---|---|
| Close 2026-09-23 | 84,378.31 | 2,683.88 |
| SMA20 / SMA50 / SMA200 | 79,508 / 74,529 / 70,759 | 2,536 / 2,325 / 2,087 |
| Close vs SMA50 / SMA200 | +13.2% / +19.3% | +15.4% / +28.6% |
| SMA50 20-day change | +8.9% | +12.6% |
| SMA200 20-day change | +1.7% | +2.7% |
| Last 50/200 cross | golden, 2026-09-08 | golden, 2026-08-31 |
| Consecutive closes > SMA200 | 36 (since 2026-08-19) | 36 (since 2026-08-19) |
| Return 7d / 30d / 90d / 180d / 365d | +10.8% / +6.8% / +41.3% / +27.2% / −24.7% | +11.1% / +8.1% / +71.5% / +34.8% / −35.6% |
| RV30 / RV90 / RV365 (ann.) | 43.4% / 39.2% / 45.5% | 47.3% / 53.8% / 64.4% |
| RV30 percentile within its trailing-1y distribution | 62nd (1y range 22.1%–84.1%) | 25th (1y range 28.4%–106.2%) |
| 30d efficiency ratio (|Δ30| / Σ|Δ1d|) | 0.149 | 0.141 |
| 90d efficiency ratio | 0.276 | 0.311 |
| ATH (daily high) | 126,296 on 2025-10-06 | 4,955.90 on 2025-08-24 |
| ATH (daily close) | 124,720.09 on 2025-10-06 | 4,831.24 on 2025-08-22 |
| Drawdown from ATH close | −32.3% | −44.5% |
| 90d low / high (daily low/high) | 57,717.55 / 87,397 | 1,510 / 2,807.10 |

Path (BTC closes, 15-day steps): 66.4k (03-27) → 81.7k (05-11) → 61.4k (06-10) → 59.7k (06-25) → 64.8k (08-09) → 79.0k (08-24) → 78.4k (09-08) → 84.4k (09-23). Last 14 days: range-bound 75.6k–78.2k through 09-17, then +10.8% breakout 09-18→09-21 (86.6k close), −2.1% on 09-23.

ETH/BTC (Coinbase closes ratio): 0.03181 on 2026-09-23; +1.2% over 30d, +21.3% over 90d.

### 1.2 BTC dominance
CoinGecko `https://api.coingecko.com/api/v3/global` (free, no key), `updated_at` 2026-09-24 03:03:36 UTC — **snapshot**:

| Field | Value |
|---|---|
| BTC dominance | 58.74% |
| ETH dominance | 11.37% |
| USDT / USDC share | 6.36% / 2.61% |
| Total market cap | $2.882T |
| 24h total volume | $123.9B |
| 24h mcap change | −5.16% |

BTC dominance 30d/90d change: **not found** from a free source. CoinGecko historical global market cap (`/global/market_cap_chart`) is a paid endpoint; the free `/global` has no history. A reconstructable proxy is "BTC mcap / sum of top-N mcaps", but that is not the same series.

### 1.3 Stablecoin supply (DefiLlama)
Source: `https://stablecoins.llama.fi/stablecoincharts/all` (sum of `totalCirculatingUSD.peggedUSD`, daily), accessed 2026-09-24.

| Window ending 2026-09-23 | Start value (peggedUSD) | Change |
|---|---|---|
| Level 2026-09-23 | $311.72B | — |
| 7d (from 2026-09-16) | $309.52B | +0.71% |
| 30d (from 2026-08-24) | $308.39B | +1.08% |
| 90d (from 2026-06-25) | $311.90B | −0.06% |
| 180d (from 2026-03-27) | $312.98B | −0.40% |
| 365d (from 2025-09-23) | $292.28B | +6.65% |
| All-time peak | $320.87B on 2026-05-17 | now −2.9% below peak |
| 90d trough | $305.16B on 2026-08-11 | +2.1% since trough |

Per-asset 30d (DefiLlama `https://stablecoins.llama.fi/stablecoins?includePrices=false`, `circulating` vs `circulatingPrevMonth`): USDT $183.49B (+0.21%), USDC $76.27B (+3.23%), USDS $6.56B (−0.94%), USDe $4.89B (+20.1%), DAI $4.80B (+0.32%), USD1 $4.40B (+8.8%).

Caveat: DefiLlama history is revised (new chains/assets backfilled); treat as not strictly point-in-time.

### 1.4 Perp funding and open interest (US-reachable public APIs)
All fetched ≈ 2026-09-24 03:06–03:08 UTC.

**Reachability**

| Venue / endpoint | HTTP from US | Notes |
|---|---|---|
| Kraken Futures `futures.kraken.com/derivatives/api/v3/tickers` | 200 | Funding history `/api/v4/historicalfundingrates` returns only the last ~1y (8,916 hourly rows, from 2025-09-17); OI analytics `/api/charts/v1/analytics/{sym}/open-interest` returns daily OHLC OI from 2023-03-07 |
| Hyperliquid `api.hyperliquid.xyz/info` (`metaAndAssetCtxs`, `fundingHistory`) | 200 | Funding history paginated (500/call). No free historical OI endpoint found |
| Deribit `www.deribit.com/api/v2/public/*` | 200 | `get_funding_rate_history` returns hourly data back to at least 2020-07-01 (tested 744 rows for 2020-07) → **point-in-time back to 2020-07** |
| Coinbase International `api.international.coinbase.com/api/v1/instruments` | 200 | Current OI, predicted funding, 24h/30d notional; history not tested |
| Binance `fapi.binance.com` | **451** | "Service unavailable from a restricted location" — geo-blocked |
| Bybit `api.bybit.com` | **403** | CloudFront "block access from your country" — geo-blocked |
| OKX `www.okx.com/api/v5/public/funding-rate` | 200 | Responds from US, but OKX excludes US persons in its ToS; **not used** |

**Funding (annualized, simple: hourly rate × 8760; Deribit: period sum × 365/days)**

| Series | 7d | 30d | 90d | 365d | Share of negative hours (30d) |
|---|---|---|---|---|---|
| Kraken PF_XBTUSD | +6.5% | +6.6% | +5.6% | +3.2% | 17% |
| Kraken PF_ETHUSD | +11.4% | +8.9% | +6.7% | +3.2% | 13% |
| Hyperliquid BTC | +11.8% | +9.4% | +8.6% | n/a | 7% |
| Hyperliquid ETH | +12.2% | +9.9% | +8.6% | n/a | 5% |
| Deribit BTC-PERPETUAL | +9.3% | +4.5% | not fetched (API "Too wide time range") | — | — |
| Deribit ETH-PERPETUAL | +7.4% | +5.1% | not fetched | — | — |

Reference: Hyperliquid funding embeds a fixed interest component of 0.00125%/h (≈10.95% simple annualized; docs say "11.6% APR") — `https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding`. HL BTC/ETH 30d at 9.4–9.9% ⇒ average premium slightly **below** zero. Latest hourly prints: Kraken BTC relative −3.08e-6/h (≈ −2.7% ann.), HL BTC −7.2e-6/h, Deribit BTC `funding_8h` 3.36e-5, CB Intl BTC-PERP predicted 0.000008 (interval 1h).

**Open interest (snapshot, USD = contracts × mark)**

| Venue | BTC OI | ETH OI |
|---|---|---|
| Hyperliquid | 37,283 BTC ≈ $3.14B | 1,085,129 ETH ≈ $2.91B |
| Deribit perpetual (USD-denominated field) | $861M | $255M |
| Coinbase International perp | 1,144 BTC ≈ $96.5M | 16,216 ETH ≈ $43.5M |
| Kraken PF | 2,220 BTC ≈ $187M | 27,361 ETH ≈ $73M |

Kraken OI trend (daily close of OI analytics × Coinbase close): BTC $123.5M (06-25) → $142.3M (08-24) → $187.8M (09-23): +32% 30d, +52% 90d in USD; in coin terms 2,068 → 1,802 → 2,225 BTC (+23% 30d, +8% 90d). ETH $44.0M → $63.0M → $77.3M; 28,135 → 25,386 → 28,805 ETH. Single small venue; not representative of global OI.

CB Intl 24h notional: BTC-PERP $4.98B, ETH-PERP $3.29B; `avg_daily_notional` BTC $4.24B, ETH $2.65B.

### 1.5 Macro backdrop

| Item | Value | Source (date) |
|---|---|---|
| FOMC decision | **Hike** +25bp to 3.75–4.00%, 12–0 vote; "Inflation remains elevated"; first hike since 2023 | Fed statement, 2026-09-16 `https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm`; CNBC 2026-09-16 `https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html` |
| SEP median fed funds (end-2026 / 2027 / 2028 / 2029 / LR) | 4.1 / 4.1 / 3.9 / 3.6 / 3.2 (June: 3.8 / 3.6 / 3.4 / — / 3.1) | Fed SEP 2026-09-16 `https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm` |
| SEP median PCE / core PCE 2026 | 3.7 / 3.4 | same |
| Implied path | end-2026 median 4.1 vs 3.875 midpoint now ⇒ roughly one more 25bp hike in 2026 [INFERENCE from medians] | same |
| Market odds of October hike | ~54% (secondary, unverified) | Trading Economics via search, accessed 2026-09-23 `https://tradingeconomics.com/united-states/currency` |
| Chair | Kevin Warsh chaired 2026-09-16 press conference (secondary) | Bondsavvy `https://www.bondsavvy.com/fixed-income-investments-blog/fed-dot-plot` |
| Effective FFR (DFF) | 3.88% (2026-09-22); 3.63% 30d and 90d earlier | FRED `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF` |
| 2y / 10y UST | 4.71% / 4.96% (2026-09-22); 30d ago 4.24% / 4.74%; 90d ago 4.11% / 4.41% | FRED DGS2, DGS10 |
| 10y breakeven | 2.35% (2026-09-23); 2.32% 30d, 2.21% 90d ago | FRED T10YIE |
| DXY (ICE) | 100.745 on 2026-09-23; +1.76% 1m, +2.93% 12m (secondary) | Trading Economics `https://tradingeconomics.com/united-states/currency` |
| Broad trade-weighted USD (primary proxy) | 119.51 (2026-09-18); 118.33 30d ago (+1.0%); 120.40 90d ago (−0.7%) | FRED DTWEXBGS |
| VIX | 14.21 (2026-09-22); 15.13 30d, 18.63 90d ago | FRED VIXCLS |
| S&P 500 | 7,706.03 (2026-09-23); +0.7% 30d, +4.7% 90d | FRED SP500 |

**US spot ETF flows** — Farside Investors, `https://farside.co.uk/bitcoin-etf-flow-all-data/` and `https://farside.co.uk/eth/`, accessed 2026-09-24 (US$m; 2026-09-23 row incomplete and excluded):

| BTC ETFs (total) | US$m |
|---|---|
| Last 7 cal. days (09-16..09-22) | +2,010.3 |
| Last 30 cal. days (08-24..09-22) | +3,168.3 |
| Last 90 cal. days (06-25..09-22) | +4,149.2 |
| June 2026 | −4,509.7 |
| July 2026 | +172.8 |
| August 2026 | +3,539.1 |
| September MTD (to 09-22) | +2,027.1 |
| 09-17..09-22 (4 sessions) | +2,306.2, incl. +999.0 on 09-21 (largest day of 2026 per The Block `https://www.theblock.co/news/markets/2026-09-22-spot-bitcoin-etfs-1-billion-daily-inflow-416005`) and +714.7 on 09-22 |
| Cumulative since launch | +56,976 |

| ETH ETFs (total) | US$m |
|---|---|
| Last 7 cal. days (09-16..09-22) | +312.5 |
| Last 30 cal. days (08-24..09-22) | +1,530.9 |
| Last 90 cal. days (06-25..09-22) | +2,685.5 |
| June 2026 | −530.2 |
| July 2026 | +367.2 |
| August 2026 | +1,851.5 |
| September MTD (to 09-22) | +619.0 |
| 09-17..09-22 (4 sessions) | +536.6 |
| Cumulative since launch | +13,714 |

ETH source: `https://farside.co.uk/ethereum-etf-flow-all-data/` (accessed 2026-09-24). Daily totals summed locally.

### 1.6 Narrative / sector rotation

**(a) Point-in-time universe (Coinbase candles, same endpoint, 28 current-universe USD pairs; returns to 2026-09-23 close).** Caveat: the universe is selected by *current* 30d volume, so it is biased toward recent winners (volume follows price); this is descriptive, not a fair cross-section.

| Stat | 7d | 30d | 90d | 180d |
|---|---|---|---|---|
| Median return (28 assets) | +19.9% | +19.5% | +67.9% | +41.4% |
| Assets beating BTC (of 27) | 23 | 21 | 19 | 16 |

Breadth: 27/28 above SMA200 and SMA50 (only TRUMP below both).

30d leaders: USELESS +350%, ARB +123%, NEAR +122%, UNI +113%, ZEC +80%, VVV +80%, LIGHTER +56%, DASH +39%, AVAX +36%, ENA +35%. Laggards: TRUMP −18%, PUMP −16%, XRP +1%, DOGE +3%, XLM +4%, LINK +6%, BTC +7%.
90d leaders: USELESS +305%, ZEC +260%, PUMP +233%, LIGHTER +229%, UNI +221%, ARB +195%, ENA +151%, NEAR +137%, VVV +122%. Laggards: XLM +13%, TRUMP +20%, HBAR +23%, DOGE +24%, ONDO +32%, TAO +35%.

Grouped [INTERPRETATION of the above]: leaders = DeFi/DEX & perp-DEX tokens (UNI, LIGHTER, ENA, AERO), privacy/"old PoW" (ZEC, DASH, BCH, LTC), L2/alt-L1 (ARB, NEAR, AVAX, SUI), Solana memes (USELESS). Laggards = large-cap payments coins (XRP, XLM, HBAR), politically-linked memes (TRUMP), and BTC itself.

**(b) CoinGecko categories** — `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=<id>&order=market_cap_desc&per_page=25&price_change_percentage=7d,30d,200d,1y`, fetched 2026-09-24 03:11–03:17 UTC (`last_updated` per row). Per category: top 15 constituents by mcap after removing stablecoins/wrapped/LST tickers; "med" = median constituent % change, "mcw" = mcap-weighted mean. CoinGecko has **no 90d field** on this endpoint; 200d is the nearest longer window. 24h category mcap change from `https://api.coingecko.com/api/v3/coins/categories` (fetched ≈03:10 UTC 2026-09-24, during a −5.2% total-mcap day).

| Category (id) | Top constituents | 7d med | 30d med | 30d mcw | 200d med | 24h mcap chg |
|---|---|---|---|---|---|---|
| privacy-coins | ZEC, XMR, DCR, ZANO, NOCK | +8.5% | **+38.8%** | +65.0% | +10.4% | −4.86% |
| decentralized-exchange | HYPE, UNI, ASTER, PUMP, LIT | +12.9% | **+32.1%** | +34.3% | +56.2% | −5.34% |
| layer-2 | OKB, MNT, ARB, POL, STX | +18.6% | **+28.2%** | +41.3% | +8.5% | −5.56% |
| artificial-intelligence | NEAR, TAO, SN0, ICP, VVV | **+28.6%** | +22.0% | +76.2% | +45.6% | −5.09% |
| depin | TAO, RENDER, FIL, BDX, BTT | +20.4% | +20.3% | +21.4% | +9.9% | −5.01% |
| layer-1 | BTC, ETH, BNB, XRP, SOL | +15.7% | +14.7% | +7.4% | +25.4% | −2.70% |
| decentralized-perpetuals | HYPE, ASTER, LIT, JUP, CAKE | +14.3% | +10.1% | +24.1% | +26.8% | n/a |
| oracle | LINK, PYTH, RED, TRB, XYO | +12.9% | +6.7% | +6.4% | +1.3% | −5.21% |
| decentralized-finance-defi | HYPE, LINK, RAIN, UNI, BTW | +16.2% | +5.0% | +22.1% | +54.6% | −4.36% |
| exchange-based-tokens | BNB, HYPE, WBT, LEO, UNI | +7.6% | +3.9% | +12.5% | +15.9% | −3.30% |
| gaming | FLOKI, AXS, MANA, GOMINING, APE | +16.6% | +6.4% | +9.3% | **−23.5%** | −4.15% |
| meme-token | DOGE, SHIB, M, PUMP, PEPE | +15.7% | **+2.8%** | +5.7% | +7.0% | **−7.93%** |
| real-world-assets-rwa | FIGR_HELOC, LINK, XLM, USDY, ONDO | +0.9% | **+0.4%** | +2.3% | +2.3% | −2.10% |

Caveats: RWA's top-15 is dominated by tokenized credit/T-bill products (FIGR_HELOC, USDY, EUTBL, USTB, JAAA, YLDS) that are near-stable by design, so its low return is partly compositional. mcw figures for AI/privacy/DeFi are skewed by single small-cap outliers (e.g., AKE +393% 30d, BTW +132%) — use medians. `pump-fun` category was not fetched (run stopped; the CoinGecko free tier had already returned HTTP 429 on several calls in this run).

Leaders/laggards [INTERPRETATION]: 30d leaders = privacy, DEX, L2, AI/DePIN; laggards = memes, RWA, exchange tokens, gaming, oracles, and the large-cap L1 basket (mcw +7.4%, i.e., BTC-like). Consistent with the Coinbase-universe view in (a). Over 200d, DEX and DeFi medians (+55–56%) lead; L2 and memes (+7–9%) lag and gaming is negative (−23.5%) — i.e., L2 is a *recent* (30d) rotation, not a persistent leader.

## 2. Regime classification

### Rules (stated ex ante; thresholds are round numbers, not fitted)
Applied to BTC (market) with ETH as confirmation.

1. **Trend state**
   - UPTREND: close > SMA200 AND SMA50 > SMA200 AND SMA200 20-day slope > 0.
   - DOWNTREND: close < SMA200 AND SMA50 < SMA200.
   - else TRANSITION.
2. **Vol state**: RV30 percentile within its trailing-365d distribution: >80th = HIGH-VOL, <20th = LOW-VOL, else NORMAL.
3. **Trend quality**: 90d efficiency ratio ≥0.30 = TRENDING; ≤0.15 = CHOPPY/MEAN-REVERTING; between = MIXED.
4. **Crisis flag** (any): BTC drawdown from ATH close >50% with HIGH-VOL; total stablecoin supply 30d change < −2%; BTC 7d return < −20%.
5. **Cycle context**: drawdown from ATH close >20% = "below prior cycle high".
6. **Breadth/rotation**: share of universe above SMA200 >70% and median 30d alt return > BTC 30d = ALT-BROAD; <30% = NARROW.
7. **Leverage**: 30d avg funding (Kraken/HL) > 20% ann. = CROWDED LONG; < 0% = SHORT-SKEWED; else NEUTRAL.
8. **Liquidity/macro**: stablecoin 90d change > +3% = EXPANDING; < −3% = CONTRACTING; else FLAT. Fed stance from latest FOMC action.

### Result

| Rule | Input | State |
|---|---|---|
| Trend | BTC 84.4k > SMA200 70.8k; SMA50 74.5k > SMA200; SMA200 slope +1.7%/20d (ETH same) | **UPTREND** (young: golden cross 2026-09-08; 36 days > SMA200) |
| Vol | BTC RV30 43.4% = 62nd pct; ETH 47.3% = 25th pct | **NORMAL** |
| Trend quality | ER90 BTC 0.276 / ETH 0.311; ER30 ≈ 0.14–0.15 | **MIXED** (90d trend, choppy last 30d until 09-18 breakout) |
| Crisis flag | DD −32%; stablecoin 30d +1.1%; 7d +10.8% | **not triggered** |
| Cycle | −32.3% BTC / −44.5% ETH from ATH close; 365d −25% / −36% | **below prior cycle high** |
| Breadth | 27/28 > SMA200; median 30d +19.5% vs BTC +6.8% | **ALT-BROAD** (survivor-biased universe) |
| Leverage | 30d funding 4.5–9.9% ann.; HL below its 10.95% baseline | **NEUTRAL** |
| Liquidity | stablecoins 90d −0.06%, 30d +1.08%, −2.9% from May peak | **FLAT** (turning up in last 30d) |
| Macro | FOMC hiked 09-16; SEP median implies another hike; 2y +47bp in 30d; DXY up 1.8% 1m | **TIGHTENING** headwind |

**Summary label:** *Early-stage uptrend / recovery rally inside a cyclical drawdown; normal vol; broad alt participation; neutral leverage; flat stablecoin liquidity; tightening Fed.*

### Interpretation (not measured) [SPECULATION where flagged]
- Price and ETF flows turned together: BTC ETF flows −$4.5B in June (price trough ~$58–61k), then +$3.5B Aug and +$2.0B Sep MTD; ETH ETFs −$0.53B June, +$1.85B Aug. The 09-18→09-21 breakout coincided with the +$999M BTC-ETF day. [INFERENCE] ETF flow is contemporaneous with price; causality direction is not established.
- The rally occurred **despite** a Fed hike and rising 2y yields/DXY. [SPECULATION] Either crypto is front-running a different driver (flows/rotation), or it is vulnerable if the October hike (~54% priced, secondary source) lands. This is a regime risk, not a signal.
- Hyperliquid 30d funding sits below HL's fixed interest baseline, Kraken/Deribit 30d funding is +4.5–8.9% ann., and the latest Kraken/HL BTC hourly prints (2026-09-24 03:00 UTC) are negative ⇒ [INFERENCE] the rally was not leverage-led. Press framing of a "short squeeze" (TechTimes 2026-09-23, `https://www.techtimes.com/articles/327946/20260923/record-bitcoin-etf-inflows-short-squeeze-drive-btc-eight-month-high.htm`) is consistent with that but unverified here (no free liquidation data used).
- Stablecoin supply has *not* expanded over 90d; the rally is not supported by new on-chain dollar liquidity on that window. [INFERENCE] USDC (+3.2% 30d) and USDe (+20% 30d) are the growing components; USDT flat.
- Alt outperformance is broad but concentrated in high-beta small caps and specific themes (DeFi revenue tokens, privacy, perp-DEX). [SPECULATION] This looks like a late-summer "risk-on rotation" more typical of the first months after a trend change than of a mature bull.
- Regime is fragile by construction: trend signals are 2–5 weeks old; a close back below ~70.8k (SMA200) would flip rule 1 to TRANSITION.

## 3. Data-source ledger

| Source | Free / key | Reachable from US | Point-in-time back to 2020-07? | Used for |
|---|---|---|---|---|
| Coinbase Exchange candles | free, no key | yes | **yes** (listed pairs; delisted pairs per project data) | trend, vol, DD, returns, breadth |
| CoinGecko `/global` | free, no key | yes | **no** (current snapshot only; history is paid) | dominance |
| CoinGecko `/coins/categories`, `/coins/markets?category=` | free, rate-limited (~429 after a few calls/min) | yes | **no** (category membership & returns are current; categories added over time; survivor-biased) | sector rotation |
| DefiLlama stablecoins | free | yes | history to 2017, **revision-prone** | stablecoin supply |
| Kraken Futures | free | yes | funding: only ~1y via v4 endpoint; OI: from 2023-03 | funding, OI |
| Hyperliquid info API | free | yes | funding history from HL launch (2023); no free OI history found; HL not live in 2020 | funding, OI |
| Deribit public API | free | yes (data); trading restricted for US persons | **funding hourly back to 2020-07** | funding |
| Coinbase International | free | yes | history not tested | OI, predicted funding |
| Binance / Bybit futures | — | **no** (451 / 403) | — | not used |
| OKX public | free | responds, but US excluded by ToS | — | not used |
| FRED (DFF, DGS2, DGS10, T10YIE, DTWEXBGS, VIXCLS, SP500) | free CSV | yes | yes (FRED data are revised rarely; ALFRED gives vintages) | macro |
| Fed statements / SEP | free | yes | yes (dated releases) | policy stance |
| Farside ETF flows | free web page (httpx got 403; browser-style fetch worked) | yes | BTC from 2024-01-11, ETH from 2024-07-23 only; **not back to 2020-07** | ETF flows |
| Trading Economics DXY, news articles | free web | yes | no (secondary, current) | DXY level, market odds |

## Implications for backtestable hypotheses

**Backtestable honestly (free, point-in-time back to 2020-07):**
- **Trend-regime filter on BTC** (close vs SMA200, SMA50 vs SMA200, SMA200 slope) from Coinbase daily candles — a gate for any long-only alt strategy (e.g., hold alts only when BTC is in UPTREND). Current state: UPTREND, so a gated strategy would be *invested* now.
- **Vol-regime scaling** (RV30 percentile vs trailing 1y) — position sizing or on/off switch; fully computable from Coinbase candles.
- **Cross-sectional momentum / rotation within the point-in-time Coinbase USD universe** (30d/90d returns, % above SMA200, alt-median vs BTC) — expressible as a weekly-Monday rank rule. Universe must be rebuilt each date from trailing volume incl. delisted pairs, otherwise the survivor bias visible in §1.6a (27/28 above SMA200) contaminates results.
- **ETH/BTC ratio trend** — from Coinbase candles.
- **Funding-based leverage filter** using **Deribit** BTC/ETH perpetual funding history (hourly, back to 2020-07) — e.g., skip/de-risk when 30d funding > X% ann. Kraken (1y) and Hyperliquid (2023+) histories are too short for the 2020-07 start.
- **Macro gates from FRED** (DFF change, 2y yield 30d change, DTWEXBGS 30d change) and FOMC decision dates — point-in-time with ALFRED vintages; low sample count (few regime changes in 2020–2026) ⇒ high overfitting risk; treat as at most one pre-registered binary gate.
- **Stablecoin supply growth** (DefiLlama) — backtestable only with a lag/haircut and explicit caveat that history is revised; prefer a coarse rule (e.g., 90d change sign) to reduce sensitivity to backfills.

**Not honestly backtestable / discretionary / current-only:**
- **BTC dominance** time series (CoinGecko history is paid; free source gives only today's 58.74%).
- **CoinGecko category/sector returns** — category membership is today's; categories (e.g., perp-DEX, AI agents) did not exist in 2020; composition changes. Sector rotation must instead be proxied by a hand-built, dated tagging of Coinbase tickers, which itself embeds hindsight [SPECULATION on how much].
- **ETF flows** — only exist from 2024-01 (BTC) / 2024-07 (ETH); cannot cover the 2020-07 start; any flow rule would have ~2.5 years of data and a single regime.
- **Open interest** — no free venue with OI history back to 2020 found (Kraken from 2023-03; HL none).
- **Fed dot-plot/market-implied odds, DXY (ICE) level, narratives** ("short squeeze", "risk-on rotation") — discretionary context only.
- **The current regime label itself** — descriptive; any rule using it must be re-derived mechanically from the rules in §2 at each historical date.
