# 02 — DeFi / app-token candidates: fundamentals vs valuation

Subset: HYPE, UNI, AERO, ENA, PUMP, LIGHTER (LIT), ONDO, LINK, VVV, TAO.
**Picked:** PUMP and UNI as possible longs; HYPE, LIGHTER and AERO as avoids. **Skipped:** ENA, ONDO, LINK, VVV, TAO.

## Conventions and data provenance

- **When the data was pulled:** all live pulls ran 2026-09-24 03:00–03:30 UTC, which is the evening of 2026-09-23 in US time. Wherever this note says "access date", it means 2026-09-23.
- **Price, market cap (MC), fully diluted value (FDV), supply:** CoinGecko keyless API, `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=…&price_change_percentage=30d,1y` (last_updated 2026-09-24T03:22Z). MC means CoinGecko's circulating market cap.
- **Fees, revenue and holder revenue (HR):** DefiLlama `https://api.llama.fi/summary/fees/{slug}?dataType={dailyFees|dailyRevenue|dailyHoldersRevenue}`. The last data point is 2026-09-23.
  - HR is DefiLlama `dailyHoldersRevenue`: buybacks, burns, or fees paid to token holders/lockers.
  - Annualized HR = trailing N-day sum × 365/N.
  - All DefiLlama history is **as re-computed today**. It is not a point-in-time record (see Implications).
- **TVL:** `https://api.llama.fi/protocols`.
- **Unlocks:**
  - DefiLlama unlock pages (`https://defillama.com/unlocks/{slug}`, parsed from `__NEXT_DATA__`). The DefiLlama emissions API `https://api.llama.fi/emissions` returned **HTTP 402 Payment Required**.
  - Tokenomist public pages (JSON-LD on `https://tokenomist.ai/{slug}`) and Tokenomist research articles.
- **Coinbase:** ADV comes from the brief. Book spreads come from `https://api.exchange.coinbase.com/products/{id}/book?level=1`. All 10 products report `status=online`.
- **Volume elsewhere:** CoinGecko `/coins/{id}?tickers=true` (24h). Some venues on that list are probably wash venues [INFERENCE].
- **Holders:** Blockscout v2 (eth/base), the Hyperliquid info API, Hypurrscan and Solana RPC. URLs are given per section.
- **Active users:** **not found for any asset from a free source.** Hyperliquid `stats-data.hyperliquid.xyz` returned AccessDenied, and DefiLlama `userData/activeUsers` returned an empty body.

## Screen: all 10 names (2026-09-23)

| Asset | Price | MC | FDV | MC/FDV | HR 30d | HR ann. (30d) | MC / HR | Price 30d / 1y | CB ADV | Call |
|---|---|---|---|---|---|---|---|---|---|---|
| HYPE | $92.16 | $20.50B | $88.03B | 23% | $59.33M | $721.9M | **28.4x** | +16% / +104% (ATH 9/23) | $44M | **Avoid** (rich vs falling HR) |
| UNI | $9.33 | $5.79B | $8.29B | 70% | $16.09M | $195.7M | **29.6x** (7d: 35.3x; 90d: 52.1x) | +114% / +15% | $19M | **Long candidate** (conditional) |
| PUMP | $0.003995 | $1.87B | $3.33B | 56% | $24.09M | $293.0M | **6.4x** | −17% / −33% | $11M | **Long candidate** (value) |
| LIT (LIGHTER) | $5.34 | $1.33B | $5.34B | 25% | $3.13M | $38.1M | **35.0x** (FDV 140x) | +60% / n/a (TGE 12/2025) | $6M | **Avoid** (strongest) |
| AERO | $0.680 | $0.68B | $1.35B | 50% | $6.41M* | $80.6M* | **8.4x** gross; **negative net of emissions** | +27% / −40% | $6M | **Avoid** (value trap) |
| ENA | $0.207 | $2.09B | $3.11B | 67% | $0 (not tracked; HTTP 400) | 0 | n/m | +34% / −66% | $7M | skip |
| ONDO | $0.419 | $2.04B | $4.19B | 49% | $0 | 0 | n/m | +8% / −55% | $7M | skip |
| LINK | $12.34 | $9.23B | $12.34B | 75% | $4.40M | $53.5M | 172x | +5% / −43% | $20M | skip |
| VVV | $30.41 | $1.46B | $2.47B | 59% | $0.81M (on-chain burns only) | $9.9M | 148x (on-chain only) | +81% / +1,356% | $12M | skip (avoid-by-default) |
| TAO | $287.69 | $3.27B | $6.05B | 54% | no DefiLlama HR | — | n/m | +20% / −8% | $12M | skip |

\* AERO excludes a single $7.92M HR print on 2026-09-09, which I flag as a suspected artifact. Including it, HR 30d = $14.33M, annualized $174.3M, MC/HR 3.9x.

Column sources:
- MC, FDV, price: CoinGecko markets API.
- HR: DefiLlama summary/fees.
- CB ADV: the brief's universe list.

---

## 1. PUMP (pump.fun) — LONG candidate (value; conditional)

**Setup:** PUMP is the cheapest name in the subset on holder revenue, at 6.4x MC/HR.
- HR yield on MC is 15.7%. HR is a real, visible daily on-chain buy-and-burn.
- Price is −33% over 1y and −17% over 30d, even though HR recovered from $12.2M (Jun) to $27.1M (Aug).
- The disconnect is priced mainly through the unlock overhang, the lawsuit and memecoin cyclicality.

| Metric | Value | Source / note |
|---|---|---|
| Circulating / total / max | 466.78B / 832.27B / 1,000B | CoinGecko. On-chain `getTokenSupply` = 832,269,188,075 (Solana RPC `api.mainnet-beta.solana.com`) |
| Burned to date | 167.46B PUMP; $461.70M cumulative buyback | Official `https://pump.fun/pump-token`. Consistent with 1T − 832.27B |
| Next unlock | **2026-10-12: 6.875B** (Team 4.167B + Investors 2.708B) = **1.47% of circ**, ≈$27.5M | DefiLlama `defillama.com/unlocks/pump`. Modeled as an 89.4B cliff on 2026-07-12, then monthly through 2029-06 |
| Unlock caveats | Tokenomist records only an 82.5B cliff on 2026-07-12 and calls the rest of the 247.5B insider schedule "undocumented". 240B community bucket has **TBD** timing | Tokenomist research, 2026-07-11 |
| Forward unlocks | 30d 6.875B; 90d 20.6B; 365d 82.5B (17.7% of circ) | DefiLlama chart (modeled) |
| Fees / revenue / HR, 30d | $160.74M / $54.14M / $24.09M | DefiLlama `pump` |
| HR annualized | 7d $295.0M; 30d $293.0M; 90d $248.6M; 1y $281.3M | DefiLlama |
| HR monthly ($M) | Aug-25 40.6 · Sep 42.8 · Oct 28.5 · Nov 24.6 · Dec 23.5 · Jan-26 31.8 · Feb 25.6 · Mar 25.7 · Apr 27.6 · May 16.2 · Jun 12.2 · Jul 15.7 · Aug 27.1 · Sep 1–23: 16.0 | DefiLlama |
| Value accrual | Buyback-and-burn of **~50% of revenue** since 2026-04-29 (100% before). Latest day 2026-09-23: $850.9K bought and burned = 52.25% of revenue. Official 90d annualized revenue $496.64M | `pump.fun/pump-token`; CoinDesk 2026-04-29 (`coindesk.com/markets/2026/04/29/pump-fun-burns-36-of-pump-supply-…`). The official page itself warns the fee dashboard "does not correctly reflect the revenue and buyback amount" since custom pairs launched |
| HR share of fees | 15% of gross fees (gross includes LP and creator fees); 44% of protocol revenue | DefiLlama, derived |
| TVL | PumpSwap $374.2M | DefiLlama `/protocols` |
| Holders / concentration | **not found**. Solana public RPC `getTokenLargestAccounts` returned HTTP 429 on 3 endpoints (mainnet-beta, onfinality); publicnode returned 403 | — |
| Liquidity | Coinbase ADV $11M; spread 7.5 bps. CoinGecko 24h tickers $180M (Binance $30.0M, MEXC $23.7M, Coinbase $8.1M, PumpSwap $6.4M). Coinbase ≈ 4.5% of listed volume | Coinbase API; CoinGecko |
| **MC / HR** | **6.4x** (FDV 11.4x; on the 1T max ≈ 13.7x [derived]). MC / revenue 2.8x | derived |

**Supply-flow check [ESTIMATE, at the current price]**
- Buybacks remove about 5.8–6.0B PUMP per month. That comes from the official ~$0.85M/day, or DefiLlama $24.1M/30d ÷ $0.004.
- The modeled unlock adds 6.875B per month.
- Net float therefore grows about +0.9–1.1B per month (≈ +0.2% of circ). Net supply is roughly flat, not deflationary.

**Catalysts**
- CONFIRMED (dated):
  - Monthly insider unlocks on 2026-10-12, 11-11 and 12-11 (DefiLlama model).
  - Daily/weekly buyback contract running (official page, 437 daily rows). Per Tokenomist, the post-April buybacks run from a locked contract "over 12 months", so it may lapse around 2027-04 [INFERENCE].
- SPECULATION:
  - A memecoin/Solana activity upswing lifts fees (Aug HR doubled month on month).
  - Buyback share raised back above 50%.
  - Additional burns.
  - Negative: the 240B community airdrop gets dated and released.
  - Negative: an adverse development in the securities/RICO class action against Baton Corp (Wolf Popper, `wolfpopper.com/news/pumpfun-class-action-lawsuit-expands-…`).

**Bear case (strongest form)**
- HR depends on memecoin speculation. It fell 71% from Sep-25 to Jun-26 and could do so again.
- Management already cut the holder share from 100% to 50% once. Governance is company-controlled, so a further cut is one tweet away.
- Unscheduled supply adds up to about 105% of today's float:
  - 247.5B insider tokens still to vest;
  - 240B community tokens with TBD timing.
- Buybacks only offset the dated unlocks, not the TBD bucket.
- Revenue data is company-reported and flagged as inaccurate by the company itself.
- The 6.4x multiple may simply be the market's fair discount for a declining, single-product, legally exposed business.

**Invalidation (don't enter / exit)**
- Official daily buyback averages < $0.5M over 14 consecutive days (≈ < $180M/yr).
- OR the buyback share is announced below 50%.
- OR a 240B community distribution is announced with a date in the next 90 days.
- OR MC/HR(30d) > 15x, meaning the value gap has closed.
- OR a court ruling or regulatory action that restricts pump.fun operations in the US.

## 2. UNI (Uniswap) — LONG candidate (fee-switch growth; conditional, already re-rated)

**Setup:** The fee switch (UNIfication) is live on v2, v3 and v4, and fees have surged. The v4 switch and the Robinhood Chain deployment started 2026-07-27.
- HR run-rate went from ~$4.5M/mo (H1-26) to $16.1M over the last 30d.
- UNI has **no insider unlocks**.
- **But price already did +114% in 30d.** The long case is "HR keeps compounding", not "cheap".

| Metric | Value | Source / note |
|---|---|---|
| Circulating / total / max | 620.66M / 887.91M / 1,000M | CoinGecko. 112.09M UNI sits at `0x…dEaD` (11.2%; includes the 100M treasury burn) — Blockscout `eth.blockscout.com/api/v2/tokens/0x1f98…f984/holders` |
| Unlocks | None scheduled; team/investor vesting complete (DefiLlama unlocks: 0 forward). Growth budget of **20M UNI/yr, paid quarterly from 2026-01-01** | `blog.uniswap.org/unification`. Next tranche ≈ 5M UNI ≈ 0.8% of circ around 2026-10-01 [INFERENCE from quarterly cadence] |
| Fees / HR, 30d | $209.13M / $16.09M | DefiLlama `uniswap` |
| HR annualized | 7d $163.9M; 30d $195.7M; 90d $111.2M; 1y n/m (switch live only since 2025-12-28; $51.1M total) | DefiLlama |
| HR monthly ($M) | Jan-26 2.86 · Feb 3.21 · Mar 4.59 · Apr 4.50 · May 3.85 · Jun 5.13 · Jul 4.41 · Aug 9.33 · Sep 1–23: 13.05 | DefiLlama |
| Fee-switch rollout | Ethereum 2025-12-28; OP/Arb/Base/etc. 2026-03-08; Polygon/BSC/Celo 2026-06-02; v4 + Robinhood Chain 2026-07-27. v2 cut = 17% (1/6) of swap fees | DefiLlama methodology, `github.com/DefiLlama/dimension-adapters` (uniswap-v2/v3/v4) |
| **Concentration of the surge** | Robinhood Chain = **69.7% of 30d fees** (v4 $108.4M + v3 $37.4M) and **59.6% of 30d HR** ($9.59M). It was $0 90–120d ago | DefiLlama `totalDataChartBreakdown` |
| Daily fee trend | $17.86M peak on 2026-09-04 → $5.30M on 2026-09-23 (−70%) | DefiLlama |
| Value accrual | Protocol fees collected in TokenJar are used to buy and burn UNI. HR = 7.7% of gross fees (30d) | DefiLlama; UNIfication vote passed Dec 2025 (CoinDesk 2025-12-26) |
| TVL | v2 $1.03B + v3 $1.66B + v4 $1.23B = $3.92B | DefiLlama |
| Holders | 407,981 holders. Top-10 = 52.1% of the 1B total: Timelock/treasury 26.7%, burn 11.2%, Binance hot wallets 3.45% / 1.87% / 1.05%, OKX 1.32%, MerkleDistributor 1.25% | Blockscout |
| Liquidity | Coinbase ADV $19M; spread 0.6 bps. CoinGecko 24h $1.59B (Websea $311M [likely wash], Binance $162M, Coinbase $38.5M) | Coinbase; CoinGecko |
| **MC / HR** | **29.6x** (30d); 35.3x (7d); 52.1x (90d). FDV/HR 42.3x | derived |

**Supply-flow check [ESTIMATE, at the current price]**
- 30d burns ≈ 1.72M UNI.
- The growth budget releases ≈ 1.67M UNI per month.
- Net circulating supply is roughly flat at the current run-rate.

**Catalysts**
- CONFIRMED:
  - The fee switch is live across versions (dated above).
  - Robinhood Chain mainnet launched 2026-07-01 (Robinhood newsroom, cited via Tokenomist research 2026-07-18).
  - Quarterly growth-budget vesting.
- Secondary reports: Robinhood Chain DEX volume > $3B/day on 2026-09-04 with Uniswap at ~98% of it (news.bitcoin.com, `…/robinhood-chain-3b-dex-volume-uniswap-uni-burn-1m/`).
- SPECULATION:
  - Fee-tier or protocol-fee increases.
  - More chains switched on.
  - Robinhood distributing Uniswap to US retail.
  - Negative: Robinhood routing to its own or another DEX.

**Bear case**
- About 60% of HR comes from one 12-week-old chain whose daily fees are already −70% from peak.
- The 30d multiple flatters UNI. On the 90d run-rate it is 52x.
- HR is only ~8% of gross fees, and LPs keep the rest. That limits operating leverage unless governance raises the cut, which risks LP flight to competitors.
- The 20M UNI/yr growth budget roughly cancels the burn.
- Price +114% in 30d means the catalyst is likely priced.
- The treasury holds 26.7% of supply and can be deployed by governance.

**Invalidation**
- HR 7d-annualized < $100M for 2 consecutive weeks. That is MC/HR > 58x at today's MC.
- OR Robinhood Chain share of Uniswap fees drops below 25%.
- OR governance lowers protocol-fee fractions or expands UNI issuance/grants beyond 20M/yr.
- OR MC/HR(7d) > 60x.

## 3. HYPE (Hyperliquid) — AVOID as a value long (rich multiple, falling fundamentals)

**Setup:** Price is at an all-time high: $97.96 on 2026-09-23 per CoinGecko, and +104% over 1y. Over the same period, holder revenue fell by about half.
- Aug-25 HR was $113.9M; Aug-26 was $51.5M, a −55% drop.
- The rally is narrative- and flow-driven: spot ETFs from May 2026, the treasury company "Hyperliquid Strategies", and new products.
- It is not an HR-driven rally.

| Metric | Value | Source / note |
|---|---|---|
| Circulating (official) / total / max | **298.73M** / 998.91M / 1,000M. `futureEmissions` 411.3M | Hyperliquid `POST api.hyperliquid.xyz/info {"type":"tokenDetails","tokenId":"0x0d01dc56dcaaca66ad901c959b4011ec"}` |
| Circulating (CoinGecko) | 222.45M, which gives MC $20.50B. The official circulating supply gives MC **$27.53B** | CoinGecko vs official — **supply definitions disagree by 34%** |
| Non-circulating balances | `0x43e9…f251` 241.4M; Assistance Fund `0xfefe…` 47.45M (= accumulated buybacks) | tokenDetails `nonCirculatingUserBalances` |
| Next unlock (scheduled) | **2026-10-06: 9,916,666 HYPE** (Core Contributors) ≈ $914M = 2.09% of released supply (Tokenomist basis); 3.3% of official circ; 4.5% of CoinGecko circ | Tokenomist JSON-LD `tokenomist.ai/hyperliquid`. **Dataset last updated 2025-12-29** |
| Unlocks actually distributed | DefiLlama tracks transfers from HyperLabs to contributors at only **0.14–1.4M HYPE/month**: 0.433M on 2026-09-06; 5.47M cumulative since 2025-11-29 | `defillama.com/unlocks/hyperliquid` |
| Fees / revenue (= HR), 30d | $76.13M / $59.33M | DefiLlama `hyperliquid` |
| HR annualized | 7d $856.6M; 30d $721.9M; 90d $570.2M; 1y $693.7M | DefiLlama |
| HR monthly ($M) | Aug-25 113.9 · Sep 85.2 · Oct 97.2 · Nov 77.7 · Dec 51.2 · Jan-26 59.8 · Feb 54.0 · Mar 51.5 · Apr 42.4 · May 46.3 · Jun 60.0 · Jul 38.4 · Aug 51.5 · Sep 1–23: 44.0 | DefiLlama |
| Value accrual | 99% of perps fees (excluding builder fees) go to the Assistance Fund, which buys HYPE; spot fees are included. HR = 78% of gross fees (30d) | DefiLlama methodology (`dexs/hyperliquid-perp`) |
| TVL | Bridge $7.43B; HLP $184M | DefiLlama |
| Staking / concentration | 441.8M HYPE staked across 35 validators. The 4 "Hyper Foundation" validators hold **44.5%** of stake. Spot holders: 259,039. Largest spot balances: `0x2222…` 51.8M (HyperEVM system address [INFERENCE]); AF 47.45M; next largest 1.07M | `validatorSummaries`; `api.hypurrscan.io/holdersWithLimit/HYPE/20` |
| ETFs | US spot ETFs (Bitwise BHYP, 21Shares THYP, Grayscale HYPG) live since May 2026. Reported cumulative net inflow ≈ $330M and −$26.4M in the week of Sep 7–11 | CNBC 2026-06-06 (`cnbc.com/2026/06/06/…hyperliquid-etfs.html`); KuCoin/CryptoBriefing flow reports (secondary) |
| Liquidity | Coinbase ADV $44M; spread 2.2 bps. CoinGecko 24h $1.11B (Tapbit $573M [likely wash], Hyperliquid $109M, Coinbase Exchange $46.9M + Coinbase Intl $47.4M ≈ 8.5%) | Coinbase; CoinGecko |
| **MC / HR** | **28.4x** (CoinGecko MC, 30d); **38.1x** on official circ; 35.9x on 90d; FDV/HR 121.9x | derived |

**Supply-flow check [ESTIMATE]**
- AF buys ≈ 0.64M HYPE per month at the current price.
- The scheduled contributor unlock is 9.92M per month, about 15x the buyback.
- Realized distributions are ~0.43M per month, below the buyback.
- Which one is the true supply pressure is the key unknown.

**Catalysts**
- CONFIRMED:
  - 2026-10-06 scheduled unlock (Tokenomist). Monthly recurrence on the ~6th is [INFERENCE] from DefiLlama's tracked transfer dates.
  - ETFs trading.
  - Manual lending (HYPE/BTC collateral) launched 2026-09-18 (Yahoo Finance, `finance.yahoo.com/…/why-hyperliquid-today-130207418.html`).
- SPECULATION:
  - Kraken launching regulated perps on Hyperliquid (CoinMarketCap AI summary only; unverified).
  - HIP-3 market growth.
  - ETF inflows resuming.
  - Treasury-company (DAT) buying.
  - Negative: DAT/ETF selling, contributors selling at the ATH, a volume share loss to Lighter/others.

**Bear case**
- HR is down 55% YoY while price doubled, so the multiple expanded about 4x.
- 70% of max supply sits outside the float (official 298.7M circ vs 1B max), and 411M are "future emissions".
- If contributors start taking the scheduled ~9.9M/month (≈ $0.9B/month) instead of ~0.4M, supply pressure exceeds the AF bid by an order of magnitude.
- The ETF bid has been fading, with weekly outflows in Sep.
- Validator and stake concentration is high: Foundation validators hold 44.5% of stake.

**Invalidation of the AVOID** (what would make HYPE a long)
- HR 30d-annualized > $1.4B, meaning MC/HR < 15x at today's MC.
- OR price falls enough that MC/HR(30d) < 15x.
- OR an official statement or on-chain evidence that contributor vesting is extended or re-locked, confirmed by 3 more months of realized transfers under 1M per month.

## 4. LIT (Lighter) — AVOID (strongest disconnect in the subset)

**Setup:** Price is +133% since 2026-07-17 ($2.29 per Tokenomist → $5.34), +60% over 30d and +162% over 60d. Meanwhile fees are −71% vs the Nov-25 peak and HR is flat at ~$2–3M/mo.
- MC/HR is 35x and FDV/HR is 140x.
- A 3-year insider vest (50% of supply) starts in about 95 days.

| Metric | Value | Source / note |
|---|---|---|
| Circulating / total / max | 250M (≈234M net of burn) / 1,000M / 1,000M | CoinGecko; Tokenomist research 2026-07-18 (`tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2`) |
| Burned | 15.64M LIT (burn address holds 15.639M) | Blockscout `eth.blockscout.com/api/v2/tokens/0x232c…4ee2/holders` |
| **Next unlock** | **Insider cliff ends 2026-12-27** (Tokenomist; DefiLlama shows 12-29). Then linear vesting of Team 26% + Investor 24% over 3 years: **≈3.19M LIT/week** (Team 1.661M + Investors 1.533M) ≈ 166M/yr = **66% of today's circ per year**. ≈$17.1M/week at the current price | Tokenomist; DefiLlama `defillama.com/unlocks/lighter`; Lighter X post 2025-12-30 (`x.com/Lighter_xyz/status/2005862687331303804`) |
| Forward unlocks | 90d 0; 180d 38.3M (15% of circ); 365d 122.8M (49%) | DefiLlama chart |
| Other overhang | 25% Ecosystem/Reserve with no schedule; $11M LIT committed to Robinhood incentives | Tokenomist |
| Fees / revenue / HR, 30d | $5.45M / $4.65M / $3.13M | DefiLlama `lighter` |
| HR annualized | 7d $36.7M; 30d $38.1M; 90d $29.1M; since Jan-26 $28.5M | DefiLlama |
| Fees monthly ($M) | Oct-25 9.6 · Nov 18.1 · Dec 12.0 · Jan-26 9.0 · Feb 6.8 · Mar 3.8 · Apr 2.8 · May 2.9 · Jun 3.9 · Jul 2.8 · Aug 4.3 · Sep 1–23: 4.1 | DefiLlama |
| Value accrual | Treasury buybacks since 2026-01-05; burned since the 2026-06-30 policy change. Staking at ~6% APR is paid from the ecosystem reserve (inflationary to float). Robinhood-perps and spot fees have HR = 0 | DefiLlama methodology (`fees/lighterv2`); Tokenomist |
| TVL | Lighter bridge $644.3M; Robinhood perps $100.3M | DefiLlama |
| Holders (Ethereum L1) | 9,257 holders. Top-10 = 65.2% of max: unlabeled `0xe554…9D62` 23.4%, ZkLighter bridge 16.0%, 6 more unlabeled wallets of 1.8–5.9% each, burn address 1.56%. Most user LIT sits on the L2 | Blockscout |
| Liquidity | Coinbase ADV $6M; spread 9.3 bps. CoinGecko 24h $184M (OKX $23.2M, MEXC $19.9M, Bybit $19.3M, Lighter spot $13.6M, Coinbase $10.7M ≈ 5.8%) | Coinbase; CoinGecko |
| **MC / HR** | **35.0x** (30d); 45.8x (90d); **FDV/HR 140x** | derived |

**Supply-flow check [ESTIMATE]**
- Buybacks remove ≈ 0.59M LIT per month at today's price.
- The post-cliff vest adds ≈ 13.8M per month, about 24x the buyback.

**Catalysts**
- CONFIRMED:
  - 2026-12-27/29 vest start.
  - Robinhood Wallet perps integration live since 2026-07-01, but **not available to US residents**.
  - Burn policy from 2026-06-30; first burn 2026-07-10.
- SPECULATION:
  - Robinhood distribution reverses the fee decline.
  - Binary options / prediction markets (Sep 2026, per CoinMarketCap AI summary only).
  - A US launch.
  - Negative: pre-cliff hedging/shorting by insiders or market makers into the December date.

**Bear case**
- The market is pricing Robinhood optionality at 140x fully-diluted holder revenue, while realized revenue keeps shrinking.
- The float is the smallest in the perp-DEX peer set (25%).
- Series-B investors entered near an implied $1.50/token FDV (Tokenomist, citing Fortune 2025-11-11). Today's price is 3.6x that basis, so they have a strong incentive to sell once unlocked.
- Coinbase ADV of $6M is thin relative to $17M/week of new supply.

**Invalidation of the AVOID**
- HR 30d-annualized > $130M, meaning MC/HR < 10x at today's MC.
- OR an official extension/re-lock of insider vesting.
- OR insider wallets show no net outflow for 8 weeks after the cliff AND price is below $3 (MC/HR < 20x at current HR).

## 5. AERO (Aerodrome) — AVOID (cheap headline, value trap net of emissions)

**Setup:** On headline HR, AERO trades at 8.4x MC/HR (3.9x including the 09-09 print), which a naive screen would rank as "cheap".
- Emissions paid to LPs and the team exceed fees paid to voters by about 2.3x. Owner earnings net of dilution are negative.
- The 2026-09-09 HR print ($7.92M in one day vs a ~$0.2M/day norm) would single-handedly double the 30d metric. That is exactly the kind of revision-prone datum that breaks a fee-yield factor.

| Metric | Value | Source / note |
|---|---|---|
| Circulating / total / max | 996.57M / 1,988.03M / **none** (inflationary) | CoinGecko; Blockscout total supply 1,988.03M |
| Locked as veAERO | 990.64M = 49.8% of total supply (VotingEscrow `0xeBf4…E6B4`) | Blockscout `base.blockscout.com/api/v2/tokens/0x9401…8631/holders` |
| Emissions (tracked on-chain) | **24.22M AERO/30d** (gauge 20.72M, rebase 2.39M, team 1.10M) = **2.43% of circ/month** ≈ $16.5M/month. 365d: 240.7M | DefiLlama unlocks chart `defillama.com/unlocks/aerodrome`. Rate is set by "Aero Fed" voter votes; there is no fixed schedule |
| Fees / HR, 30d | $17.74M / $14.33M (incl. $7.92M on 2026-09-09) → **$6.41M excluding that day** | DefiLlama `aerodrome` |
| HR annualized (excl. spike) | 7d $100.3M; 30d $80.6M; 90d $61.4M; 1y $86.5M | DefiLlama |
| HR monthly ($M) | Aug-25 16.1 · Sep 30.6 · Oct 16.5 · Nov 11.7 · Dec 6.3 · Jan-26 7.9 · Feb 5.7 · Mar 4.7 · Apr 4.6 · May 6.8 · Jun 4.7 · Jul 4.5 · Aug 4.7 · Sep 1–23: 13.1 including the spike, 5.1 excluding it | DefiLlama |
| Value accrual | 100% of gauge swap fees go to veAERO voters ("zero-leak"). Bribes are not in HR [INFERENCE from methodology text] | DefiLlama methodology (`dexs/aerodrome-slipstream`) |
| **Net of emissions [derived]** | LP + team emissions ≈ $14.8M/30d vs HR ≈ $6.4M/29d → **net ≈ −$8.4M/month**. Annualized emissions ≈ $200M vs HR $80.6M | derived |
| TVL | Slipstream $216.5M + V1 $139.1M + Ignition $20.7M ≈ $376M | DefiLlama |
| Holders | 833,544 holders. Top-10 = 66.0% (VotingEscrow 49.8%; 5 unlabeled wallets of exactly 37.668M each ≈ 1.89% each; Aerodrome TGE Safe 1.47%; Bybit 1.38%) | Blockscout |
| Liquidity | Coinbase ADV $6M; spread 6.5 bps. CoinGecko 24h $75M (Aerodrome pools ≈ $21.6M, Coinbase $10.0M ≈ 13.4%, Bybit $6.1M, Binance $5.5M) | Coinbase; CoinGecko |
| **MC / HR** | **8.4x** gross (30d excl. spike); 16.8x FDV. **Negative** net of emissions | derived |

**Catalysts**
- CONFIRMED: the Aerodrome + Velodrome merger into "Aero" was announced 2025-11-12, with a Q2-2026 target and a 94.5% AERO / 5.5% VELO split (ForkLog 2025-11-13, `forklog.com/en/aerodrome-and-velodrome-to-merge-into-aero/`). **Completion status as of 2026-09-23 not verified.** CoinGecko still lists `aerodrome-finance` with a 1.988B total supply.
- SPECULATION:
  - An emissions cut by Aero Fed.
  - Ethereum/Arc expansion.
  - A "Protocol 28 upgrade vote", 2026-09-16 (Messari summary; unverified).

**Bear case**
- Structural inflation of 24% of circulating supply per year.
- HR has been flat at $4.5–7M/mo for 9 months.
- The headline multiple depends on a suspicious print.
- The merger adds VELO supply (5.5%).

**Invalidation of the AVOID**
- 8 consecutive weekly epochs in which the $ value of emissions < HR, i.e. an emissions cut or fee growth.
- AND HR (excl. outliers) 90d-annualized > $120M.

---

## Skipped names (why)

| Asset | Reason (numbers as of 2026-09-23) |
|---|---|
| ENA | **Nothing accrues to holders today.** DefiLlama has no HR series (HTTP 400); revenue over 30d was $14.6K.<br><br>The fee switch vote closed 2026-09-02 and passed, but it only pays out once USDe supply reaches **$7.5B**. USDe TVL is **$4.89B** (DefiLlama). Sources: Tokenomist digest `tokenomist.ai/research/weekly-unlock-digest-aug-31-sep-6-2026-ethenas-fee-switch-2`; gov post `gov.ethenafoundation.com/t/ena-fee-switch-activation/830`.<br><br>Unlocks are heavy: 263M ENA in the next 30d (2.6% of circ) and 3.20B in the next 365d (31.7%) (DefiLlama).<br><br>Upside needs +53% USDe growth [SPECULATION]. The Block (2026-08-27) reports the Foundation bought back locked seed-investor tokens. Worth a revisit if USDe reaches $6.5B+. |
| ONDO | **No holder revenue.** Yield is passed through to token holders and the OUSG fee is waived until 2027 (DefiLlama methodology). HR has been 0 since Oct-25.<br><br>**2027-01-18 unlock of 1.94B ONDO = 36.4% of circ** (Tokenomist JSON-LD; DefiLlama shows 1.71B on 2027-01-17). A clear avoid, but there is no valuation "gap" to measure — only an unlock event. |
| LINK | HR = LINK Reserve buybacks: $4.40M/30d → 172x MC/HR. Of 1B supply, 252M is non-circulating and Labs-controlled (DefiLlama). No dated catalyst found. The disconnect is persistent and not new (−43% 1y), so there is no edge in flagging it. |
| VVV | +1,356% 1y and +81% 30d (ATH 2026-09-21). On-chain buy-and-burn is only $0.81M/30d → 148x.<br><br>DefiLlama methodology states that subscription/API revenue settles **off-chain** and is not measured. The true multiple is therefore unverifiable from free data, and the DefiLlama unlock page and CoinGecko also disagree on circulating supply (113.6M vs 48.1M). Treat as avoid-by-default; it cannot be analyzed to this note's evidence standard. |
| TAO | No protocol fee accrual in DefiLlama (dTAO TVL $506M). Emission ≈ 0.11M TAO/30d ≈ 0.97%/month of circ (~11.6%/yr) (DefiLlama emissions chart). An emission-driven L1-like asset, not a fee-yield candidate. |

---

## Implications for backtestable hypotheses

**1. A cross-sectional fee/revenue-yield value factor, point-in-time back to 2020-07: NO, not honestly.**

The **cross-section is too thin.**
- I measured Coinbase USD pairs clearing $5M 30d ADV at month-ends 2020-07..2026-08 from the cached Coinbase daily candles (stablecoins excluded). 217 distinct assets qualified at least once.
- Mapping by ticker to DefiLlama (`/protocols` symbol field) is noisy [ESTIMATE]. It gives 82 assets with any fee series and 48 with a holder-revenue series.
- I then counted eligible names whose HR series had started ≥30 days before each month-end:

  | Period | Median names with HR | Min / max |
  |---|---|---|
  | 2020-07..2022-12 | **2** | 0 / 5 |
  | 2023..2024 | **3** | — |
  | 2025-01..2026-08 | **7** | max 11 |

- That count uses today's backfilled series, so the true point-in-time count is lower.
- A gross-fees/MC variant has a median of ~15 names. However, gross fees include LP/creator/supply-side flows that holders never receive: UNI HR is 8% of fees and PUMP 15%.

The **fee data is revision-prone.** DefiLlama serves one recomputed history, with no vintages. Examples seen in this pull:
- Pump.fun HR/protocol split is era-based (100% → 0% → 50%) and applied retroactively.
- Uniswap v2 holder revenue is "tracked combined in the v3 adapter".
- Hyperliquid's supply-side share changed on 2025-08-30.
- A one-day $7.92M Aerodrome HR print on 2026-09-09.
- pump.fun's own dashboard says its revenue figures have been wrong since custom pairs launched.
- Any backtest would silently use corrected, later-known numbers — look-ahead.

**2. Market-cap history needed and its free availability.**

A circulating-MC factor needs **daily (or at least weekly) circulating market cap, or circulating supply, per asset, as known on each rebalance date**. That covers every listed and delisted Coinbase USD asset from 2020-07. Free options tested 2026-09-24:

| Source | What it gives | Problem |
|---|---|---|
| **CoinGecko API, keyless** | Only 365 days of history. `market_chart?days=max` returned **HTTP 401, error 10012**: "Public API users are limited to querying historical data within the past 365 days". | **Insufficient.** |
| **CoinGecko website CSV export** (`https://www.coingecko.com/price_charts/export/{id}/usd.csv`) | Full daily `close_price_usd, market_cap_usd, volume_usd`. UNI starts 2020-09-17, with a market-cap value of 0 on that first day. | Free, but it is a website download, so **ToS review required**. Market caps reflect CoinGecko's supply records and later corrections, so they are **not point-in-time** [INFERENCE]. |
| **Coin Metrics Community API** (`community-api.coinmetrics.io/v4`, no key) | `CapMrktEstUSD` daily for **839 assets**. Starts: UNI 2020-09-18, LINK 2019-06-22, HYPE 2024-12-13, LIT 2025-12-30. TAO missing. | Its supply is "self-reported … collected by CoinGecko", and coverage was backfilled when it expanded in 2022 (`coinmetrics.io/coin-metrics-expands-estimated-market-cap-coverage-to-309-assets/`). **Not point-in-time**; check the community licence (non-commercial terms) [INFERENCE]. |
| **Coin Metrics `CapMrktCurUSD`** | Price × on-chain supply. | For ERC-20s this is effectively FDV (LINK SplyCur = 1B). Only available for older assets, not HYPE/PUMP/AERO. |
| **Point-in-time-safe fallback** | FDV = Coinbase close × fixed max supply. | Wrong denominator for low-float tokens: LIT MC/FDV = 25%, HYPE 23%. |

- **Verdict:** a fee-yield factor could run as a descriptive or exploratory screen for 2025–26 only, on ~7–11 names.
- It is not a pre-registrable, walk-forward hypothesis over 2020-07..2026-09.
- If the team insists on something, the most defensible version is a **time-series rule on a single well-measured asset** with a ≥30-day data lag and the stress cost of 3.2% applied. It would still carry DefiLlama revision risk.

**3. Unlock-avoidance filter** ("exclude assets with a scheduled unlock of more than X% of circ in the next N days"): **not backtestable from free data.**
- Only current schedules are free: DefiLlama HTML and Tokenomist JSON-LD. The DefiLlama emissions API is 402.
- Schedules are revised and disagree today, for example:
  - PUMP: 82.5B cliff (Tokenomist) vs 89.4B cliff + monthly (DefiLlama).
  - HYPE: 9.92M/month scheduled vs ~0.43M/month realized.
  - LIT: cliff dated 12-27 vs 12-29.
- The Tokenomist HYPE and ENA datasets are stale (last updated 2025-12-29 and 2025-06-11).
- A hand-built event study of a few announced-ex-ante cliffs (e.g., LIT 2026-12-27, ONDO 2027-01-18) is possible but has tiny N and is forward-only.
- **Use as a discretionary risk overlay, not a tested rule.**

**4. Buyback-flow ideas** (buyback $ / ADV, buyback vs unlock): **current-only.**
- Exact on-chain histories exist for a handful of assets. Examples: the pump.fun burn table (437 daily rows), Hyperliquid AF balance history via RPC, and LIT burns.
- That is 2–4 assets, so no cross-section is possible.

**5. What *is* backtestable with only Coinbase OHLCV (free, point-in-time, includes delisted pairs):**
- Price/volume rules: momentum/trend, breakouts to highs, volatility and volume filters.
- Relevant observation, not a result: 4 of the 5 picks, plus VVV, posted large 60d moves (HYPE +58%, UNI +155%, LIT +162%, PUMP +122%, AERO +60%; VVV +81% over 30d). The "disconnects" here are largely **momentum episodes**.
- A pre-registered momentum/trend hypothesis on the ADV-filtered Coinbase universe is the honest way to test whether such episodes pay after 1.6% round-trip costs.

**6. Discretionary / not backtestable:**
- All five theses above: PUMP value long, UNI fee-switch long, and the HYPE/LIT/AERO avoids.
- Catalysts: Robinhood Chain, ETF flows, fee-switch activations, Aero merger, lawsuit.
- The invalidation thresholds are monitoring rules for live paper-trading. They are **not** evidence of edge.
