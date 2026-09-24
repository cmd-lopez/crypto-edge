# 03 — Candidate setups: L1s and payment coins

Track: Phase 2 edge research. Subset: ZEC, SOL, NEAR, SUI, ADA, XLM, AVAX, ARB, HBAR, LTC, BCH, DASH, XRP, DOGE, with ETH for comparison.
Data vintage: all API pulls ran 2026-09-24 03:00–03:25 UTC (≈ 2026-09-23 23:00 ET). Web sources are dated inline. Source IDs `[Sx]` are listed in the Source index.
Tags: **[M]** = measured by my own API pull. **[D]** = derived arithmetic from cited numbers. **[2nd]** = secondary source (news or aggregator), not verified against a primary. [ESTIMATE] and [SPECULATION] are used as the task defines them.
Scope: research only. I did not backtest or evaluate any strategy. The price paths below are descriptive context.

## 0. Bottom line

| Asset | Setup | One-line reason |
|---|---|---|
| **ZEC** | **AVOID on fundamentals.** Any exposure should come only from a price/volume rule. | MC $25.75B against chain fees of $0.67M/yr (38,000×). Issuance of ≈$1.0B/yr is ~1,500× fees. The price is carried by ETF creations, a derivatives squeeze and protocol news. The same asset fell 75% and 64% in its last two drawdowns. |
| **SOL** | **Relative-value LONG candidate (weak).** | Highest fees and REV in the subset. MC/REV is ≈190–220×, against ETH's MC/fees of 1,600×. Fees bottomed in Jun-2026 and have since risen ~90%. ETFs have 12 straight weeks of inflows. But REV is still −70–87% YoY, issuance is ≈7.6× REV, and the Alpenglow mainnet date slipped. |
| **NEAR** | **Catalyst/momentum LONG candidate, overextended.** | It has the only real new token sink in the subset: Intents fees fund NEAR buybacks, live since 2026-02-23. But the buyback covers only ≈13% of issuance. On-chain activity is −78% YoY. The price is +122% in 30d and 5.2× off its Feb low. The ETF is pending with no decision date. |
| **ARB** | **AVOID / fade the narrative.** | The Robinhood Chain revenue share (AEP 8%) is real but spiky. Its fees peaked at $8.36M/day on Sep 4 and now run ≈$0.2–0.36M/day. DAO income is ≈$16M/yr against $20M/month of unlocks until Mar-2027. No mechanism passes value to token holders (CoinDesk). |
| **SUI** | **AVOID (supply overhang).** | FDV/MC is 2.44. 52% of supply has a TBD release schedule. Circulating supply is +14.8% YoY. Fees are −81% YoY and TVL is −73% YoY. Spot ETFs launched Feb-2026 and the price still fell 71% over 1y. |

Cross-cutting finding: in this subset, the biggest price moves of the last 30–365 days (ZEC, NEAR, ARB, BCH, DASH) happened where fee fundamentals are weakest relative to price. A fundamentals filter would have excluded all of them. Each move is visible in Coinbase price and volume data first, as a volume shock plus a breakout. See Implications.

## 1. Screen — all 15 names

Sources: CoinGecko markets [S1] (prices at 2026-09-24 03:03 UTC). DefiLlama chain fees [S4] (1y and 30d windows through 2026-09-23). DefiLlama TVL [S3]. Coinbase 30d ADV from the task universe (I re-derived it independently from [S7]; it matches).
Definitions: "Chain fees" = L1/L2 gas fees only (for SOL this excludes Jito tips). "MC/fees" = market cap ÷ trailing-1y chain fees. ADV/MC is the daily Coinbase turnover in basis points.

| Asset | Price | MC $B | FDV/MC | Circ % of max/total | 30d % | 1y % | Chain fees 1y $M | Fees 30d ann. $M | MC / fees 1y | TVL $M | TVL 1y % | CB ADV $M | ADV/MC bp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH (ref) | 2,689 | 328.17 | 1.00 | 100% | +8 | −36 | 204.06 | 142.66 | 1,608× | 53,570 | −40 | 257 | 7.8 |
| XRP | 1.51 | 94.83 | 1.59 | 63% | −0 | −47 | 0.30 | 0.22 | 316,123× | 44.6 | −54 | 154 | 16.2 |
| SOL | 115.6 | 67.85 | 1.08 | 93% | +15 | −47 | 238.52 | 292.73 | 284× | 6,397 | −44 | 109 | 16.1 |
| ZEC | 1,519 | 25.75 | 1.00* | 81% | +82 | +2,663 | 0.67 | 1.56 | 38,482× | 4.1 | n/m | 144 | 55.9 |
| DOGE | 0.0941 | 14.67 | 1.10 | 100% | +3 | −61 | 0.45 | 0.29 | 32,630× | 1.9 | n/a | 22 | 15.0 |
| ADA | 0.2408 | 9.03 | 1.20 | 83% | +7 | −71 | 1.09 | 0.54 | 8,249× | 64.1 | −81 | 16 | 17.7 |
| XLM | 0.2028 | 7.08 | 1.43 | 70% | +3 | −45 | 0.60 | 0.54 | 11,801× | 245.1 | +88 | 12 | 16.9 |
| BCH | 342.9 | 6.89 | 1.00 | 96% | +24 | −39 | 0.06 | 0.02 | 120,103× | 8.5 | n/a | 7 | 10.2 |
| NEAR | 4.39 | 5.74 | 1.00 | 100% (∞ supply) | +123 | +46 | 1.28 | 0.91 | 4,495× | 201.7 | +9 | 29 | 50.5 |
| LTC | 66.39 | 5.15 | 1.00 | 92% | +25 | −39 | 0.16 | 0.15 | 32,828× | 1.0 | n/a | 9 | 17.5 |
| AVAX | 10.33 | 4.58 | 1.06 | 62% | +35 | −70 | 4.30 | 2.16 | 1,063× | 602.2 | −73 | 11 | 24.0 |
| HBAR | 0.0911 | 3.99 | 1.14 | 88% | +12 | −59 | 0.26† | n/a† | 15,376× | 37.2 | −68 | 7 | 17.6 |
| SUI | 0.9727 | 3.98 | 2.44 | 41% | +19 | −71 | 3.58 | 1.66 | 1,111× | 527.5 | −73 | 21 | 52.8 |
| ARB | 0.2192 | 1.49 | 1.47 | 68% | +122 | −50 | 10.55 | 5.94 | 141× | 1,439 | −57 | 8 | 53.9 |
| DASH | 58.72 | 0.75 | 1.00 | 68% | +37 | +175 | 0.01 | 0.01 | 71,177× | 0.1 | n/a | 5 | 66.3 |

\* CoinGecko computes ZEC FDV on circulating supply. On the 21M cap, FDV is ≈$31.9B [D].
† DefiLlama's Hedera fee adapter returned no data for the last 30d. The 1y figure is stale [M].
Fee-linked revenue outside the "chain" line, 1y [M, S5]: Jito MEV tips (SOL) $68.1M; NEAR Intents fees $48.3M (revenue $6.6M); Robinhood Chain (Arbitrum Orbit) fees $45.3M since its 2026-05 start. These are covered in the candidate sections.
YoY collapse of chain fees, trailing 365d vs prior 365d [M, S5]: ETH −80% ($204M vs $1,027M), SOL −76%, SUI −81%, AVAX −55%, ARB One −37%, NEAR chain −76%. ZEC is +460%, but from a tiny base ($0.12M → $0.67M).

---

## 2. ZEC — AVOID on fundamentals; momentum-only exposure

### 2.1 Data

| Metric | Value | Date | Src |
|---|---|---|---|
| Price / MC / circ | $1,519.03 / $25.75B / 16.95M of 21M (80.7%) | 2026-09-24 | [S1] |
| Price change | 30d +82%, 1y +2,663%. Coinbase close: $74.13 (2025-09-30) → $847 (2026-08-31) → $1,513 | 2026-09-24 | [S1][S7] |
| Last two drawdowns | 2025-11-07 high $744 → 2026-02-06 low $185 (**−75%**). 2026-05-20 high $688 → 2026-06-05 low $250 (**−64%**, Orchard soundness bug) | Coinbase daily | [S7] [M] |
| 30d realized vol | 146% annualized (BTC: 43%) | 2026-09-24 | [S7] [D] |
| Issuance | 1.5625 ZEC/block. Split: 80% miners, 8% ZCG, 12% coinholder-controlled lockbox (NU6/NU6.1) | current | [S51] |
| Issuance rate | 1,148 blocks/24h → ≈1,794 ZEC/day → ≈3.86%/yr of circ → ≈$2.72M/day, **≈$994M/yr** at spot [D]. CoinGecko-implied circ growth over 1y: +3.97% | 2026-09-24 | [S12][S2] |
| Unlocks | None scheduled. All new supply comes from block issuance (Tokenomist: schedule "extends into 2044") | accessed 2026-09-24 | [S14] |
| Next halving | ~Nov-2028 at 75 s blocks [ESTIMATE]. The NU7 vote kept halvings (98.9% of participating ZEC). The date mapping under 25 s blocks was not verified | — | [S22] |
| Chain fees | 30d $128k. 1y $0.669M. Revenue $0: no burn, fees go to miners | through 2026-09-23 | [S4][S5] |
| REV | ≈ chain fees (no MEV data). Pine: fees are "well under 1% of miner revenue" | Aug-2026 | [S18] |
| TVL | $4.1M (DefiLlama tracks from 2025-12-04). Immaterial | 2026-09-24 | [S3] |
| Activity | 36,002 tx/24h. 849,105 transparent addresses with a balance | 2026-09-24 | [S12] |
| Shielded supply | 4.92M ZEC (29.0%). Peak ~31% in Apr-2026. 26.3% on Jun-30 after the bug-driven deshield | ~2026-09-19 | [S24][S18] |
| Holder concentration | ZCSH ETF 596,269 ZEC (3.52% circ, Sep 18). Cypherpunk Technologies 323,394 ZEC (1.91%, avg cost $341.83, Aug 11). Combined **5.43%** [D] | as dated | [S19][S25] |
| Hashrate concentration | Cypherpunk ≈18% of network hashrate. Fortitude (DCG) bought 9,000 Z15 Pros for Oct–Nov delivery | Aug-2026 | [S18] |
| Derivatives | Open interest ≈2.3M ZEC (≈13.6% of circ [D]), ≈$2.3B | 2026-09-04 | [S17] |
| Coinbase liquidity | 30d ADV $144M (56 bp of MC/day). 7d ADV $175M | 2026-09-24 | [S7] [M] |
| Value accrual | None to holders. PoW; fees go to miners. The NU7 vote set NSM reissuance to start Feb-2031. A "≥60% fee burn" is reported [2nd] but I did not verify it ships in NU7. At $0.67M/yr of fees it is immaterial either way | 2026-09-18 | [S21] |

### 2.2 Why ZEC volume surged (Coinbase 30d ADV, $M [M, S7])
2025-09-30: 2 → 2025-11-30: 214 → 2025-12-31: 74 → 2026-03-31: 20 → 2026-06-30: 107 (the bug crash) → 2026-07-31: 37 → 2026-08-31: 51 → **2026-09-24: 144** (7d: 175).
The largest Coinbase dollar-volume days in the last 60 days were Sep 17 ($358M), Sep 18 ($305M) and Sep 16 ($300M) [M].
Drivers, all sourced:
1. **ETF conversion.** Grayscale's Zcash Trust listed as spot ETF **ZCSH on NYSE Arca on 2026-08-25**, with Coinbase as custodian and a 2.5% fee [S20]. By ~Sep 17 it had >$233M of cumulative inflows, including $112M on Sep 8 and $46.6M on Wed Sep 16. Net assets were ≈$890M, and cumulative ETF volume was $11B [S16].
   - Holdings reached 596,269 ZEC on Sep 18. That includes an **in-kind 85,705 ZEC from DCG International on Sep 8** [S19]. DCG is Grayscale's parent, so this is internal reshuffling, not new market demand.
   - Pre-listing holdings: 388,674 ZEC at Jun-30 per the fund's 10-Q [S18]. That makes net growth ≈+208k ZEC in ~3.5 weeks [D], or ≈+122k excluding DCG. That is ≈5k ZEC/day of ETF absorption against ≈1,435 ZEC/day of miner issuance [D]. Sources disagree on the % increase (Crypto Briefing says +28.4%).
2. **Leverage squeeze.** On Sep 4 ZEC rose +20% through $1,000. $36.6M was liquidated in 24h, $34.5M of it shorts. OI was ≈2.3M ZEC [S17]. The rumor of a $47M whale short with liquidation near $2,292 is [2nd, unverified] [S50].
3. **Protocol news flow.**
   - An Orchard soundness bug was disclosed May 29. The Ironwood pool activated 2026-07-28, and 87% of Orchard's balance had migrated by Aug 31 [S18].
   - The NU7 coinholder vote closed Sep 14: 99.9% for 25-second blocks, halvings kept [S22].
   - NU7 targets: testnet Oct 6, mainnet Nov 5 [S21]. The Sep 16–18 volume peak coincides with the vote result, the NU7 date announcement and the $46.6M ETF day.
4. **Corporate miners and treasuries.** Difficulty is at an all-time high. Cypherpunk bought ~18% of hashrate. Fortitude has 9,000 machines arriving Oct–Nov [S18].
5. **Background de-risking.** The SEC closed its Zcash Foundation investigation with no action on 2026-01-14 [S23]. That is not the September driver.
6. **Sector rotation.** CoinDesk's Sep-23 live-updates headline: "money rotates into BCH and ZEC" [S48].

### 2.3 Catalysts

| Date | Event | Status | Src |
|---|---|---|---|
| 2026-09-28 close → 09-30 | ZCSH 3-for-1 split; split-adjusted trading starts Sep 30 | CONFIRMED (SEC 8-K). Cosmetic | [S16] |
| 2026-10-06 | NU7 on testnet | CONFIRMED target, tentative | [S21] |
| 2026-10-27..29 | Zcon7 (network's 10th birthday Oct 28) | CONFIRMED event | [S18] |
| Oct–Nov 2026 | Fortitude's 9,000 Z15 Pro arrive. Hashrate up; potential miner selling | CONFIRMED purchase; timing per company | [S18] |
| 2026-11-05 | NU7 mainnet (25 s blocks) | CONFIRMED target, tentative. NU7 already missed a "late July" target | [S21][S18] |
| 2027-07-10 | EU AMLR applies. CASPs may not handle "anonymity-enhancing coins" (Reg. 2024/1624 Art. 79). One source says Jul 1 | CONFIRMED law; ZEC's inclusion is interpretive | [S26] |
| — | More ZEC ETFs, further DCG in-kind contributions, Cypherpunk resuming buys toward its 5% target (it paused Jun 30–Aug 11) | SPECULATION | [S25] |
| — | Whale short-squeeze to $2,292 | SPECULATION / rumor | [S50] |

### 2.4 Bear case (strongest form)
- **No fundamental floor.**
  - Fees are $0.67M/yr. Holders get no yield and no burn.
  - At spot, the ≈$994M/yr of new issuance (about $2.2M/day to miners [D]) must be absorbed by net buyers forever.
  - The price is set purely by flows: ETF creations, treasury firms, leverage.
- **Flow quality is weaker than the headline.** Roughly 85.7k of the ~208k ZEC of ETF growth was DCG's own in-kind transfer [S19][D]. OI of ≈13.6% of circulating supply means forced selling can outrun spot demand [S17].
- **History repeats quickly.** The last two drawdowns were −75% and −64% within months. The second came from protocol risk (a soundness bug) that the market had not priced [S7][S18].
- **Regulatory cliff dated.** EU CASPs must stop handling privacy coins from Jul-2027 [S26].
- **Hashrate and ETF concentration.** Two corporate miners could control ~⅓ of hashrate by year-end (Pine's plausible case) [S18]. One ETF plus one treasury firm hold 5.4% of supply [D].
- **Execution risk.** The NU7 target has already slipped once.

### 2.5 Invalidation of the AVOID stance
The stance is wrong if all three of these hold for **8 consecutive weeks**:
1. ZCSH net creations *excluding DCG-affiliated in-kind deposits* stay above miner issuance (≈1,435 ZEC/day).
2. The shielded share makes a new high above 31% during strength [S18 benchmark].
3. ZEC holds above its 2026-08-31 close of $847 through NU7 mainnet.

The stance is also wrong if chain fees rise more than 10× (>$6M/yr run-rate), which would show demand for block space rather than for the ticker.

---

## 3. SOL — relative-value LONG candidate (weak)

### 3.1 Data

| Metric | Value | Date | Src |
|---|---|---|---|
| Price / MC / FDV | $115.62 / $67.85B / $73.29B. 30d +15%, 1y −47%. 2026 low $60.11 (Jun-06) | 2026-09-24 | [S1][S7] |
| Supply | Total 634.61M, circ 587.58M (RPC, slot 449,902,590) | 2026-09-24 | [S8] [M] |
| Inflation | **3.634%** (epoch 1041). Governor: 8% initial, −15%/yr taper, 1.5% terminal. ≈23.06M SOL/yr ≈ **$2.67B/yr** [D]. CoinGecko-implied circ growth: 1y +8.1%, last 6m annualized +5.4% | 2026-09-24 | [S8][S2] |
| Staking | 439.96M SOL active stake = **69.3% of total**. Nominal yield ≈ inflation ÷ staked share ≈ **5.2%** + MEV [D]. Real yield vs dilution ≈ +1.6% for stakers and −3.6% for non-stakers [ESTIMATE] | 2026-09-24 | [S8] |
| Unlocks | None material found. New supply is inflation | — | [S14] |
| Chain fees | 30d $24.06M, 1y $238.5M (prev 1y $976.6M, **−76%**). Monthly: Jun-26 $11.5M (trough) → Aug-26 $22.2M → Sep-26 MTD (23d) $17.7M | through 2026-09-23 | [S5] [M] |
| Burn | Base-fee burn $28.0M over 1y ≈ 1% of issuance value [D] | 1y | [S5] |
| REV (fees + Jito tips) | 30d $28.9M → **$352M annualized**. 1y $306.6M. Blockworks REV: Q2-26 $51.0M (−43% QoQ). 21Shares: H1-26 network revenue $141M (**−87.1% YoY**) | as dated | [S5][S30] |
| MC/REV | ≈193× (30d ann.), ≈221× (1y) [D]. ETH MC/fees 1,608× | — | [D] |
| Issuance vs REV | Issuance ≈ **7.6× REV** in dollars [D] | — | [D] |
| TVL | $6.40B (−44% 1y; peak $13.24B on 2025-09-14) | 2026-09-24 | [S3] |
| Stablecoins on chain | $16.9B | 2026-09-24 | [S6] |
| Active addresses | Not measured; no free primary source found. [2nd]: DAA "hit 5M" (Aug-2026); stablecoin DAA 888K (Sep-2026) | — | [S47] |
| Holder concentration | 23 public treasury firms hold 19.35M SOL (**3.06%** of total). Largest is Forward Industries at 8.16M SOL (1.39% of circ, Sep 21). US spot ETFs AUM $1.62B (≈2.4% of MC) | Sep-2026 | [S29][S28] |
| ETF flows | Cumulative net inflows **$1.472B**. 12 consecutive weekly inflows. Weekly pace fell from $153.9M (wk to Aug 28) to $6.2M (wk to Sep 4) | 2026-09-23 | [S28] |
| Coinbase liquidity | 30d ADV $109M. 7d ADV $129M (was $177M 30d earlier). 30d vol 70% | 2026-09-24 | [S7] |
| Value accrual | 50% base-fee burn (small). Priority fees and MEV go to validators and stakers. Staking yield is ~95% inflation-funded [D] | — | [S5][S8] |

### 3.2 Catalysts

| Date | Event | Status | Src |
|---|---|---|---|
| Week of 2026-09-22 | Alpenglow (SIMD-0326) activates on **testnet**. Devnet next, then mainnet "after an observation period" | CONFIRMED (Anza). **No mainnet date.** The earlier Sep-28 mainnet target was superseded | [S27] |
| 2026-11-09 | Agave v4.4 mainnet feature activation resumes | CONFIRMED schedule, tentative | [S27] |
| ongoing | Spot SOL ETF creations; Forward Industries $25M raise (Sep 23) | CONFIRMED, not dated | [S28][S27] |
| — | Alpenglow on mainnet in 2026 | SPECULATION | [S27] |
| — | SIMD-0411 (double the disinflation rate; −22.3M SOL of cumulative emissions). Status "active – proposed May 2026, awaiting Alpenglow" | SPECULATION | [S31] |

### 3.3 Bear case
- REV collapsed 70–87% YoY, and memecoin share of spot volume fell 40% → 16% [S30]. The Aug–Sep fee rebound (+90% from the June trough) is still less than half of Sep-2025's $37.8M/month [M].
- Issuance is ≈7.6× REV. At a 69% staking ratio, "yield" is mostly redistribution from non-stakers [D].
- ETF flow momentum is fading: the weekly pace fell 96% from late Aug to early Sep [S28].
- Upgrade timing is unreliable: Alpenglow slipped from a named date to "no date" [S27].
- MC/REV of ~200× is "cheap" only next to ETH. It is a relative argument, not an absolute one.

### 3.4 Invalidation of the LONG case
Any one of these invalidates it:
- Monthly chain fees fall back below the Jun-2026 trough of $11.5M.
- US SOL ETFs post 4 consecutive weeks of net outflows.
- Alpenglow has no mainnet activation by 2026-12-31.
- SOL/ETH makes a new 12-month low. The thesis is relative, so relative price must confirm.

---

## 4. NEAR — catalyst/momentum LONG candidate, overextended

### 4.1 Data

| Metric | Value | Date | Src |
|---|---|---|---|
| Price / MC | $4.39 / $5.74B. 7d +66%, 30d +123%, 1y +46%. Coinbase low $0.844 (2026-02-06) → $4.41 (**5.2×**). 30d vol 127% | 2026-09-24 | [S1][S7] |
| Supply | Total 1,307.14M, circ 1,249.84M | 2026-09-23 | [S10] [M] |
| Inflation | Protocol `max_inflation_rate` = 1/40 = **2.5%** (cut from 5% on 2025-10-30). Measured total-supply growth: last 6m annualized **2.52%**, 1y 2.72% [M]. ≈32.7M NEAR/yr ≈ **$143M/yr** [D] | 2026-09-24 | [S9][S10][S36] |
| Staking | 550.41M NEAR staked (**42.1%**; 413 validators). Nominal ≈5.9% gross of commission [D] | 2026-09-24 | [S9] |
| Unlocks | None scheduled found. Tokenomist marks supply infinite (inflation) | accessed 2026-09-24 | [S14] |
| Chain fees | 1y $1.28M (−76% YoY). 30d $75k. DefiLlama "revenue" (the burned share) 30d $53k = 70% of fees | through 2026-09-23 | [S5] |
| **Intents fees** | 30d **$6.24M** (ann. ≈$76M). 1y $48.3M. Monthly: Nov-25 $7.76M (peak) → Apr-26 $3.21M → Sep-26 MTD (23d) $5.17M | through 2026-09-23 | [S5] [M] |
| Intents net revenue → buyback | 30d $1.53M (ann. ≈$18.7M). Buyback live **since 2026-02-23**: revenue buys NEAR on the open market; tokens are not burned. The buyback wallet has received **1,261,792 NEAR** all-time (0.097% of supply) | 2026-09-24 | [S5][S15][S32] |
| Buyback vs issuance | ≈**13%** of annual issuance at the 30d run-rate [D]. Net supply growth is still ≈+2.2%/yr [ESTIMATE] | — | [D] |
| MC multiples | MC/Intents fees ≈76×. MC/Intents net revenue ≈308× [D] | — | [D] |
| TVL | $201.7M (30d ago $115.1M; 1y ago $185.5M). Intents "confidential TVL" $131.0M (+356% over 90d) | 2026-09-24 | [S3][S15] |
| Active accounts | 30d avg **67.6k/day**, against 305.7k one year ago (**−78%**) and a 2.26M/day peak on 2024-04-22. Txns 30d avg 743k vs 4.75M (−84%) | through 2026-09-23 | [S10] [M] |
| Stablecoins on chain | $80.6M | 2026-09-24 | [S6] |
| Holder concentration | Only the staking share (42%) was found. Top-holder breakdown: not found | — | — |
| Coinbase liquidity | 30d ADV $29M. **7d ADV $74M vs $16M 30 days earlier** | 2026-09-24 | [S7] [M] |

### 4.2 Catalysts

| Date | Event | Status | Src |
|---|---|---|---|
| 2026-02-23 → | Intents fee → NEAR buyback | CONFIRMED, live | [S32][S15] |
| 2026-09-17 | "Confidential perps" via Hyperliquid launched | CONFIRMED [2nd] | [S35] |
| mid-Sep 2026 | Confidential TVL passes $70M, triggering a NEAR@3.33 incentive snapshot | [2nd] | [S35] |
| 2026-07-31 / 08-28 / **09-16** | Bitwise NEAR ETF S-1/A amendments. Grayscale NEAR-trust conversion also filed | CONFIRMED filings; **no decision or launch date found** | [S34] |
| 2026-08-03 | Polosukhin proposes a ~30M NEAR "Sovereign Fund" as a path to fixed supply | Proposal only; **no on-chain vote scheduled** | [S33] |
| — | ETF approval or listing; fixed-supply governance passing | SPECULATION | — |

### 4.3 Bear case
- **The price has decoupled from usage.** On-chain accounts are −78% YoY and chain fees −76% YoY, while price is +46% YoY and +5.2× from the Feb low [S10][S1].
- **The cash flow is real but small.** At the 30d run-rate, the buyback covers ≈13% of issuance. The rest of Intents fees go to front-ends and partners (DefiLlama's capture share is ~25% [D]).
- **The catalyst stack is soft.** It rests on unverified secondary stories (perps, the airdrop program), a pending ETF with no date, and a governance proposal with no vote.
- **The ZEC read-through cuts both ways.** NEAR Intents lists ZEC as a supported chain and front-end [S15], and privacy-swap flow is part of the fee base. If ZEC activity reverses, Intents fees likely fall with it [SPECULATION].
- **The setup is extended.** 30d vol is 127%. The 7d ADV quadrupled into a +66% week, which is a classic blow-off profile [SPECULATION].

### 4.4 Invalidation of the LONG case
Any one of these invalidates it:
- Intents 30d net revenue falls below $0.5M (the Apr-2026 level was $0.26M).
- The NEAR ETF S-1s are withdrawn, or the SEC declines.
- Price closes below $2.83, the Sep-17 level where the perps-launch leg began per [S35]. That would mean giving back the whole catalyst leg.
- Governance raises inflation back above 2.5%.

---

## 5. ARB — AVOID / fade the narrative

### 5.1 Data

| Metric | Value | Date | Src |
|---|---|---|---|
| Price / MC / FDV | $0.2192 / $1.49B / $2.19B. 30d +122%, 1y −50%. Coinbase low $0.0704 (2026-06-25) → $0.2173 (3.1×). 30d vol **191%** | 2026-09-24 | [S1][S7] |
| Supply | 10B max. Circ 6.786B (CoinGecko). Tokenomist: 59.42% released, **34.04% TBD-locked** (treasury-type), 6.54% scheduled-locked | 2026-09-24 | [S1][S14] |
| Unlocks | **2026-10-16: 92,645,833 ARB** = 1.37% of circ ≈ $20.3M [D]. The team/investor schedule continues monthly to full vesting in **Mar-2027**: ~6 more events ≈ 556M ARB ≈ 8.2% of circ ≈ $122M at spot [D]. CoinGecko-implied circ growth: **+25.6% over 1y** | as dated | [S14][S41][S2] |
| Arbitrum One fees | 1y $10.55M (prev $16.81M). 30d $0.49M. DefiLlama revenue ≈ fees (sequencer) | through 2026-09-23 | [S5] |
| Robinhood Chain (Orbit L2) | Mainnet 2026-07-01 [S40]. Fees since start $45.3M; 30d $39.6M. Daily fees peaked at **$8.36M on Sep 4**; now ≈$0.2–0.36M/day (Sep 23: $0.227M) | through 2026-09-23 | [S5][S13][S40] [M] |
| AEP revenue share | 10% of chain *net* revenue: 8% to the ArbitrumDAO treasury, 2% to the developer guild | docs | [S37] |
| DAO income from AEP | Derived from DefiLlama supply-side revenue: 7d ≈$0.165M (**≈$8.6M/yr run-rate**), 30d ≈$3.18M [D]. CoinDesk (Sep 1): $531,641 over 30d. H1-2026 total DAO income was $6.19M; July AEP was $360k (35% of DAO income) | as dated | [S5][S38][S39] |
| DAO income run-rate | ≈$15.7M/yr (AEP 7d ann. + Arb One sequencer 7d ann. $7.1M) [ESTIMATE] → MC ≈95×, FDV ≈140× [D] | — | [D] |
| Value to token holders | **None.** Income goes to the DAO treasury. CoinDesk: turning it into ARB value "would require a governance vote, and none has been proposed" | 2026-09-01 | [S38] |
| TVL | Arbitrum One $1.44B (−57% 1y; peak $4.20B on 2025-10-07). Robinhood Chain $996M | 2026-09-24 | [S3] |
| Active addresses | Arbitrum One DAA 30d avg 111.6k. Robinhood Chain 411.9k | through 2026-09-22 | [S13] [M] |
| Stablecoins | Arbitrum $3.49B | 2026-09-24 | [S6] |
| Coinbase liquidity | 30d ADV $8M. 7d ADV $12M vs $2M 30 days earlier. Thin: the Aug-31 30d ADV was $1M | 2026-09-24 | [S7] |

### 5.2 Catalysts

| Date | Event | Status | Src |
|---|---|---|---|
| 2026-10-16, then monthly to Mar-2027 | 92.65M ARB unlock (1.37% circ each) | CONFIRMED schedule | [S14][S41] |
| Mar-2027 | Team/investor vesting completes, removing the overhang | CONFIRMED end date (tokenomics.com: Mar 23, 2027) | [S41] |
| ongoing | AEP inflows from Robinhood Chain and other Orbit chains | CONFIRMED mechanism; amount varies | [S37] |
| — | DAO vote routing AEP income to ARB buybacks or distributions | SPECULATION (none proposed as of Sep 1) | [S38] |
| — | Robinhood Chain fees re-accelerating on tokenized equities, as opposed to meme trading | SPECULATION | [S38] |

### 5.3 Bear case
- **The fee spike was meme-driven and has already reverted.** CoinDesk found that the top fee payers were a trading bot and a launchpad, not tokenized equities [S38]. Daily fees are now ~3–4% of the Sep-4 peak [M].
- **Unlocks dwarf DAO income.** ≈$20M/month of unlocks compares with ≈$1.3M/month of DAO income [D].
- **Holders get no claim on the income** unless governance acts [S38].
- **Circulating supply grew 25.6% in a year** [S2].
- **Liquidity is thin and volatile.** Coinbase ADV is $8M and 30d vol is 191%. A 1.6% round-trip cost plus 191% vol makes a narrative long a coin flip on timing.

### 5.4 Invalidation of the AVOID stance
Any one of these invalidates it:
- The DAO passes a proposal that passes AEP/sequencer income to ARB holders (buyback or distribution).
- Robinhood Chain fees stay above $1M/day for 30 days, putting the AEP-to-DAO share at ≈$29M/yr [D].
- ARB holds its post-unlock price through two consecutive monthly unlocks (Oct 16 and Nov 16).
- The unlock schedule completes (Mar-2027).

---

## 6. SUI — AVOID (supply overhang)

### 6.1 Data

| Metric | Value | Date | Src |
|---|---|---|---|
| Price / MC / FDV | $0.9727 / $3.98B / $9.71B (**FDV/MC 2.44**). 30d +19%, 1y −71%. Coinbase low $0.634 (2026-08-18) | 2026-09-24 | [S1][S7] |
| Supply | 10B max. Circ 4.097B (41%). Tokenomist: 40.99% released, **52.17% "TBD locked"**, 6.83% scheduled-locked (dataset v. 2025-04-11, so possibly stale) | accessed 2026-09-24 | [S1][S14] |
| Next unlock | **2026-10-01: 13,260,415 SUI** (Early Contributors) = 0.32% of circ, ≈$12.7M | Tokenomist | [S14] |
| Stake subsidies | 282,429.5 SUI/epoch (1 epoch/day) = **103.1M SUI/yr = 2.52% of circ**, ≈$100M/yr [D]. Subsidy fund balance 234.7M SUI. Amount steps down 10% every 90 distributions; counter is at 1,239, so the next step (to ≈254.2k/day) is ≈2026-10-14 [D from on-chain params] | epoch 1259 (2026-09-23) | [S11][S49] |
| Circ growth | CoinGecko-implied **+14.8% over 1y**; last 6m annualized +10.3% | 2026-09-24 | [S2] |
| Staking | Total stake **7.016B SUI**, which is 70% of total supply and more than the 4.10B circulating. Locked allocations therefore stake and earn subsidies [D]. Staker APY ≈1.49% [D] | epoch 1259 | [S11] |
| Fees | DefiLlama: 1y $3.58M (prev $19.11M, **−81%**); 30d $0.136M; storage-fee burn 1y $0.77M. On-chain: gas 4,745 SUI/epoch ≈ $4.6k/day [D] | as dated | [S5][S11] |
| Usage | Tx/epoch **11.10M** (epoch 1259) vs 4.16M (epoch 895, 2025-09-23). The reference gas price was cut from 495 to 100 MIST, so usage rose while fees fell | [M] | [S11] |
| TVL | $527.5M (−72.8% 1y; peak $2.64B on 2025-10-09) | 2026-09-24 | [S3] |
| Stablecoins | $478.8M | 2026-09-24 | [S6] |
| Active addresses | Numeric: not found (free). Artemis-sourced trend "lower over the past several months" [2nd] | 2026-06-02 | [S43] |
| ETFs | Canary SUIS (2026-02-18), Grayscale Sui Staking, 21Shares TSUI (2026-02-24), 2× TXXS (Jul-2026). CME SUI futures listed | as dated | [S42][S44] |
| Coinbase liquidity | 30d ADV $21M. 7d $40M. 30d vol 89% | 2026-09-24 | [S7] |
| Value accrual | Gas goes to stakers and validators; the storage fund keeps the non-refundable part (small burn). Staker yield is ~98% subsidy-funded (287.2k reward vs 4.7k gas per epoch) [D] | epoch 1259 | [S11] |

### 6.2 Catalysts

| Date | Event | Status | Src |
|---|---|---|---|
| 2026-10-01 | 13.26M SUI unlock (0.32% circ) | CONFIRMED (Tokenomist) | [S14] |
| ≈2026-10-14 | Stake subsidy steps down −10% | CONFIRMED by on-chain parameters [D] | [S11] |
| — | Release of the 52% TBD-locked supply | Timing unknown. SPECULATION either way | [S14] |
| — | ETF inflows reviving demand | SPECULATION. The Feb-2026 launches did not stop a −71% year | [S42] |

### 6.3 Bear case
- **More than half of total supply sits with insiders on a discretionary release schedule.** Locked stake earns subsidies that compound the insiders' share [S14][S11][D].
- **Circulating supply grows ~10–15%/yr.** New supply is ≈60× annual fees in dollar terms [D].
- **Fees are structurally lower** after the gas-price cut, so usage growth doesn't reach token holders [S11].
- **TVL fell 73%** and ETF access came and went without re-rating the token [S3][S42].

### 6.4 Invalidation of the AVOID stance
Any one of these invalidates it:
- The Sui Foundation/Mysten publish a binding lock-up covering the TBD tranche.
- Trailing-30d fees return above $0.5M/month (the Jul-2025 level was $1.1M).
- TVL recovers above $1B.
- CoinGecko-implied circulating supply growth falls below 5%/yr.

---

## 7. Skipped names — why

| Asset | Reason for skip (evidence from §1 unless noted) |
|---|---|
| XRP | Largest valuation disconnect in the subset: MC/fees 316,000×. Only 63% circulating (≈37B non-circulating per [S1]). But there is no fee or REV thesis to test and no dated catalyst was found in this pass. Price is flow-driven like ZEC, without ZEC's current volume shock. |
| DOGE, LTC | Pure monetary-premium PoW coins. Fees of $0.45M and $0.16M a year. No TVL. No dated catalyst found. Nothing fundamental to be "disconnected" from. |
| BCH | +54% in 7d on a **Grayscale BCH trust→ETF filing (S-3/A, Sep 18)** [S45] and **CME BCH futures planned for 2026-10-19, pending regulatory review** [S44]. This is an event-driven analog of ZEC's ETF path at an earlier stage, but Coinbase ADV is only $7M. The ETF decision date is unknown. N=1 event. Covered by the volume-shock rule in Implications, not as a separate thesis. |
| DASH | +175% over 1y as privacy beta to ZEC. Fees $10.6k/yr. ADV $5M is at the universe floor. Same EU AMLR exposure as ZEC [S26]. |
| ADA | TVL −81% YoY. Fees $1.09M/yr (MC/fees 8,249×). CME futures already listed [S44]. No dated catalyst found. |
| XLM | One of the few improving fundamentals: TVL +88% YoY to $245M, stablecoins $915M [S6]. But fees are only $0.6M/yr, FDV/MC is 1.43, and no dated catalyst was found. Worth a later look as a stablecoin-rails story; not a setup today. |
| AVAX | +37% in 7d with no catalyst identified (not researched further). Fees −55% YoY and TVL −73%. 62% circulating. |
| HBAR | DefiLlama fee adapter stale (no data in the last 30d). TVL −68%. Nothing measurable to anchor a thesis. |
| ETH | Comparison only. Fees −80% YoY. MC/fees 1,608× makes SOL look cheap only relative to ETH. |

## 8. Data gaps (explicit)
- **Solana and Sui daily active addresses:** no free primary source. Token Terminal and Artemis need accounts or a paid plan. I used secondary figures only, and labeled them.
- **Top-holder concentration** for NEAR and SOL (beyond staking, ETFs and treasuries): not found.
- **Arbitrum Foundation primary sources:** blog.arbitrum.foundation and forum.arbitrum.foundation failed TLS from this host (SSL WRONG_VERSION_NUMBER). DAO income figures therefore come via CoinDesk and CoinEdition [S38][S39].
- **DefiLlama unlocks pages and api.llama.fi/emissions:** HTTP 403 (Cloudflare) and HTTP 402 (paid plan) respectively. I used Tokenomist public pages instead [S14]. SPEC §5 already marks Tokenomist as research-only because revisions are not archived.
- **CoinGecko public API:** history is limited to the last 365 days (error 10012 observed) [S46].
- **ZEC ETF holdings growth:** Pine/10-Q gives 388,674 ZEC at Jun-30 [S18], 24/7 Wall St gives ~387k ZEC at listing [S52], and Crypto Briefing says "+28.4%" to 596,269 [S19]. The first two are consistent; Crypto Briefing's percentage is not.

## Source index
All pulls ran 2026-09-24 03:00–03:25 UTC unless dated otherwise.
- [S1] CoinGecko markets API: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zcash,solana,near,sui,cardano,stellar,avalanche-2,arbitrum,hedera-hashgraph,litecoin,bitcoin-cash,dash,ripple,dogecoin,ethereum&price_change_percentage=7d,30d,1y
- [S2] CoinGecko market_chart, 365d daily. Circulating supply implied as mcap ÷ price: https://api.coingecko.com/api/v3/coins/{zcash|solana|near|sui|arbitrum}/market_chart?vs_currency=usd&days=365
- [S3] DefiLlama TVL: https://api.llama.fi/v2/chains ; https://api.llama.fi/v2/historicalChainTvl/{Chain}
- [S4] DefiLlama fees overview: https://api.llama.fi/overview/fees?dataType=dailyFees (and dailyRevenue, dailyHoldersRevenue)
- [S5] DefiLlama fee histories and methodology: https://api.llama.fi/summary/fees/{solana|jito-mev-tips|near-intents|near|robinhood-chain|arbitrum|zcash|sui|avalanche|ethereum}?dataType=dailyFees|dailyRevenue
- [S6] DefiLlama stablecoins by chain: https://stablecoins.llama.fi/stablecoinchains
- [S7] Coinbase Exchange daily candles: https://api.exchange.coinbase.com/products/{ZEC|SOL|NEAR|SUI|ARB|BCH|ETH|BTC}-USD/candles?granularity=86400 . Data to 2026-09-24; last day is partial.
- [S8] Solana RPC (getInflationRate, getInflationGovernor, getSupply, getVoteAccounts): https://api.mainnet-beta.solana.com , epoch 1041
- [S9] NEAR RPC (EXPERIMENTAL_protocol_config, validators): https://rpc.mainnet.near.org
- [S10] Nearblocks API: https://api.nearblocks.io/v1/stats ; https://api.nearblocks.io/v1/charts (daily to 2026-09-23)
- [S11] Sui GraphQL, epochs 1259 and 895, including systemState: https://graphql.mainnet.sui.io/graphql
- [S12] Blockchair Zcash stats: https://api.blockchair.com/zcash/stats (2026-09-24 03:08 UTC)
- [S13] growthepie fundamentals: https://api.growthepie.xyz/v1/fundamentals.json (to 2026-09-22)
- [S14] Tokenomist public pages: https://tokenomist.ai/sui , https://tokenomist.ai/arbitrum , https://tokenomist.ai/near , https://tokenomist.ai/zcash , https://tokenomist.ai/solana (accessed 2026-09-24)
- [S15] NEAR revenue dashboard: https://revenue.near.org/ (updated 2026-09-24)
- [S16] The Block, ZCSH split and inflows (2026-09-18): https://www.theblock.co/news/markets/2026-09-18-grayscales-zcash-etf-plans-3-for-1-split-233-million-inflow-surge-415520
- [S17] CoinDesk, ZEC hits $1,000 and liquidations (2026-09-04): https://www.coindesk.com/markets/2026/09/04/zcash-jumps-20-to-landmark-usd1-000-level-as-short-sellers-lose-usd34-million
- [S18] Pine Analytics, Zcash Q3 2026 report (2026-09-10; Blockworks data to Aug 31): https://pineanalytics.substack.com/p/zcash-quarterly-report-q3-2026
- [S19] Crypto Briefing, ZCSH holds 596,269 ZEC (2026-09-20): https://cryptobriefing.com/grayscale-zcsh-etf-zcash-holdings-increase/
- [S20] GlobeNewswire, ZCSH begins trading (2026-08-25): https://www.globenewswire.com/news-release/2026/8/25/3350404/0/en/the-zcash-etf-ticker-zcsh-built-by-grayscale-begins-trading-on-nyse-arca-expanding-investor-access-to-the-leading-privacy-focused-digital-currency.html
- [S21] crypto.news, NU7 mainnet target Nov 5 (2026-09-18): https://crypto.news/zcash-targets-nov-5-for-nu7-mainnet-upgrade/
- [S22] NU7 vote results (2026-09-17): https://cryptonews.com.au/news/zcash-holders-vote-for-faster-blocks-and-existing-halving-schedule-134904/ ; https://unchainedcrypto.com/zcash-holders-back-25-second-blocks-and-keep-bitcoin-style-halvings-in-nu7-vote/
- [S23] Decrypt, SEC ends Zcash Foundation probe (2026-01-14): https://decrypt.co/354587/zcash-foundation-sec-ends-investigation-no-enforcement-action
- [S24] ZecStats shielded pools (search snippet ~2026-09-19): https://zecstats.org/shielded
- [S25] Cypherpunk holdings, 323,394.38 ZEC at Aug 11–18, 2026 [2nd]: https://www.quiverquant.com/news/Cypherpunk+Reports+$39.4+Million+Q2+Net+Income+as+ZEC+Holdings+Rise ; https://phemex.com/academy/cypherpunk-technologies-cyph-zcash-holdings
- [S26] EU AMLR (Reg. 2024/1624) privacy-coin rule from 10 Jul 2027 [2nd] (2026-07-09): https://cryptoimpacthub.com/eu-privacy-coin-ban-2027-amlr-monero-zcash/ ; July-1 variant: https://fincrimecentral.com/eu-privacy-coins-anonymous-crypto-ban-2027/
- [S27] Solana Compass, Alpenglow testnet and Agave v4.4 schedule (2026-09-22): https://solanacompass.com/news/alpenglow-activates-on-solana-testnet-as-frankendancer-era-ends-agave-v44-schedule-targets-november-9-mainnet-activation
- [S28] SOL ETF flows [2nd, SoSoValue-derived]: https://phemex.com/news/article/us-sol-spot-etfs-record-2887-million-in-singleday-net-inflows-97511 (2026-09-23) ; https://cryptoticker.io/en/solana-three-month-high-etf-inflows-check/ (AUM $1.62B, ~2026-09-21)
- [S29] SOL treasuries: https://www.globenewswire.com/news-release/2026/09/21/3365847/0/en/forward-industries-sol-holdings-rise-to-approximately-8-16-million-sol.html ; https://www.coingecko.com/en/treasuries/solana/companies (via search snippet, 2026-09-23)
- [S30] Solana revenue: https://www.21shares.com/en-eu/insights/solana-h1-2026-earnings-analysis (Sep-2026) ; Blockworks Q2 report: https://x.com/Blockworks/article/2079204785425670413 (2026-07-20)
- [S31] Chainflow, SIMD-0411 status (2026-07-02): https://chainflow.io/solanas-inflation-debate-isnt-over-the-simd-proposals-you-need-to-know/
- [S32] DefiLlama near-intents methodology text: buyback since 2026-02-23 (via [S5])
- [S33] The Block, NEAR Sovereign Fund proposal (2026-08-04): https://www.theblock.co/news/ecosystems/2026-08-04-near-protocol-sovereign-fund-410528
- [S34] SEC, Bitwise NEAR ETF S-1/A (2026-09-16): https://www.sec.gov/Archives/edgar/data/0002067111/000119312526393240/ck0002067111-20260916.htm
- [S35] NEAR confidential perps and NEAR@3.33 [2nd]: https://coinpedia.org/price-analysis/near-protocol-price-rally-gains-momentum-as-hyperliquid-perps-launch-adds-fresh-catalyst/ ; https://coinmarketcap.com/cmc-ai/near-protocol/price-analysis/
- [S36] The Defiant, NEAR inflation cut to 2.5% (2025-10-30): https://thedefiant.io/news/blockchains/near-protocol-halving-upgrade-community-vote
- [S37] Arbitrum AEP terms: https://docs.arbitrum.io/launch-arbitrum-chain/aep-license ; https://docs.arbitrum.foundation/new-arb-chains
- [S38] CoinDesk, ARB and Robinhood Chain revenue (2026-09-01): https://www.coindesk.com/markets/2026/09/01/robinhood-s-new-crypto-network-is-printing-cash-and-it-s-sending-arbitrum-s-token-soaring
- [S39] CoinEdition via CryptoRank, Arbitrum DAO H1-2026 $6.19M (2026-09-02) [2nd]: https://cryptorank.io/news/feed/55730-arbitrum-dao-posts-6-19-million-income-as-expansion-revenue-accelerates
- [S40] Robinhood newsroom, Robinhood Chain mainnet (2026-07-01): https://robinhood.com/us/en/newsroom/robinhood-accelerates-global-expansion-robinhood-chain-mainnet-stock-tokens-agentic-trading/
- [S41] tokenomics.com, ARB fully vested by 2027-03-23 [2nd]: https://app.tokenomics.com/tokenomics/arbitrum/unlocks
- [S42] SUI ETFs: https://blog.sui.io/canary-capital-staking-spot-sui-etf-nasdaq-suis/ (2026-02-18) ; https://www.etf.com/sections/news/21shares-spot-sui-etf-nasdaq-tsui-begin-trading-tuesday-feb-24th-expanding-us-access
- [S43] Coinpedia, Sui DAA trend (Artemis) (2026-06-02) [2nd]: https://coinpedia.org/price-analysis/sui-enters-a-pivotal-support-zone-below-1-will-it-trigger-a-rebound-back-within-the-range/
- [S44] CME press release, BCH/UNI futures on Oct 19 (2026-09-22): https://www.cmegroup.com/media-room/press-releases/2026/9/22/cme_group_to_expandcryptoderivativessuitewithbitcoincashandunisw.html ; list of existing CME crypto futures: https://decrypt.co/379004/cme-crypto-bitcoin-cash-uniswap-futures
- [S45] Grayscale Bitcoin Cash Trust S-3/A (2026): https://www.sec.gov/Archives/edgar/data/0001732409/000119312526389253/bch_s-3_amendment_1.htm ; rally coverage: https://invezz.com/news/2026/09/23/bitcoin-cash-surges-26-as-cme-futures-plan-sparks-short-squeeze/
- [S46] CoinGecko public API error 10012, "limited to … past 365 days", observed 2026-09-24 on /coins/near/market_chart?days=1500
- [S47] Solana DAA [2nd]: https://cryptorank.io/news/feed/608cb-solana-price-prediction-points-to-110-as-daily-active-addresses-hit-5-million ; https://www.kucoin.com/news/insight/SOL/6aacaf867d10fa0007ce4baa
- [S48] CoinDesk live-updates headline (2026-09-23): https://www.coindesk.com/business/2026/09/23/live-updates-bitcoin-slips-under-usd86-000-as-money-rotates-into-bch-and-zec
- [S49] Sui stake subsidy schedule: https://www.sui.io/networkinfo
- [S50] TechFlow via KuCoin, whale-short rumor (2026-09-18) [rumor]: https://www.kucoin.com/news/flash/zcash-surges-2-496-in-2026-is-the-rally-ending
- [S51] Zcash dev-fund split: https://z.cash/upgrade/nu6-1/ ; https://electriccoin.co/blog/zcash-halvening-nu6-embracing-the-new-dev-fund/ ; Messari overview (2025-12-22): https://messari.io/report/understanding-zcash-a-comprehensive-overview
- [S52] 24/7 Wall St, ZCSH launched with ~387,000 ZEC (2026-09-08): https://247wallst.com/investing/cryptocurrency/2026/09/08/zcash-crossed-1000-two-weeks-after-grayscales-etf-launched-is-privacy-the-new-institutional-trade/

## Implications for backtestable hypotheses

Honest point-in-time inputs (per SPEC §4/§5):
- **Available:** Coinbase daily OHLCV for listed and delisted USD pairs.
- **Revision-prone:** DefiLlama history.
- **Not free point-in-time:** CoinGecko market cap and circulating supply before 2025-09 [S46]; unlock schedules (not archived).

**Backtestable with Coinbase OHLCV only (recommended channel):**
1. **Volume-shock breakout, long-only.** Every large 2026 move in this subset started as a Coinbase volume shock plus a price breakout:
   - ZEC: 7d ADV $175M vs 30d $51M on Aug-31.
   - NEAR: 7d ADV $74M vs $16M.
   - ARB: 7d ADV $12M vs $2M.
   - BCH: 7d ADV $17M vs $9M. [M, S7]

   Rule sketch, evaluated weekly on Monday using t−1 data:
   - Condition 1: 7d ADV ÷ trailing-90d ADV ≥ k, with k ∈ {2, 3}.
   - Condition 2: close ≥ the 30-day high close.
   - Condition 3: 7d return > 0.
   - Hold h ∈ {1, 2, 4} weeks, equal-weight, universe-eligible names only.

   Caveats:
   - Direction must be pre-registered. ZEC's Nov-2025 and Jun-2026 volume spikes preceded or accompanied −75% and −64% drawdowns [M]. Without the breakout condition, the signal is ambiguous.
   - Events cluster (sector rotation into privacy and L2s in Sep-2026), so the number of independent events is small.
   - Realized vol of 127–191% means the 1.6% round trip (3.2% stress) is small per trade. Drawdown criterion #2 of the edge bar is the binding constraint.
2. **Cross-sectional momentum at 4–12 weeks** is the generic version of the same observation. It is fully point-in-time and survivorship-safe. It should be treated as the same hypothesis family as #1 for the trial count, not as an extra free trial.

**Conditionally backtestable (not recommended as a gating hypothesis):**

3. **Fee momentum.** Chain fees over 30d ÷ trailing-90d, from DefiLlama. It needs no market cap, but:
   - Coverage is about 10–15 universe names, i.e. chains only.
   - History starts late for many series: NEAR 2020-10, SOL 2021-01, ARB 2021-08, AVAX 2022-11, SUI 2024-07, NEAR Intents 2025-05, Robinhood Chain 2026-05.
   - Adapters are revised retroactively (the Hedera adapter is currently stale).
   - It needs a lag of ≥7 days, and a vintage-bias warning on every result.

**Not honestly backtestable (discretionary or current-only):**

4. **Valuation disconnect (MC/fees, MC/REV, FDV/MC, dilution).** This needs point-in-time circulating supply. CoinGecko's free history covers 365 days only [S46] and Tokenomist is not archived. Deterministic on-chain emission parameters (SOL taper, SUI subsidy steps, ZEC/LTC/BCH halvings) can be reconstructed, but they barely vary week to week, so there is no weekly signal.
5. **Unlock avoidance** (ARB monthly 16th, SUI Oct-1). Contractual schedules exist for a handful of tokens only, the event count is small, and revisions are not archived. Keep it as a research-only risk overlay. Do not use it as a tested rule.
6. **ETF, CME and upgrade catalysts.** Examples: ZCSH 2026-08-25; the SUI ETFs, which did not help (−71%/1y); the BCH filing and CME futures on Oct-19; Alpenglow, which slipped from "Sep 28" to "no date"; NU7 on Nov-5. N is tiny, the events are heterogeneous, and dates slip. These are discretionary context only.
7. **Protocol cash-flow narratives** (NEAR Intents buyback, Arbitrum AEP income, ZEC shielded share, corporate treasuries and miners). The data series began in 2025–2026, so they cannot cover the 2020-07 → 2026-09 walk-forward. Record them for monitoring only.
8. **Leverage and short-squeeze signals** (ZEC OI of ≈13.6% of circ). These are not observable from Coinbase spot OHLCV. US-accessible derivatives history was not assessed in this note.

Design warning for pre-registration: in this subset, fundamentals and price were anti-aligned over the last year. The +2,663% (ZEC) and +122% (NEAR, ARB) movers have the worst fee-to-value ratios, while the best fee generator (SOL) is −47%. Any rule that mixes a fundamentals screen with momentum will be dominated by that 2025–26 regime. This is another reason to keep Phase-2 hypotheses to price and volume only.
