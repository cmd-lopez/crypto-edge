# 04 — Anomaly literature: crypto return predictability at 1–4 week horizons

Scope: long-only spot, weekly Monday rebalance, 10–50 liquid Coinbase USD pairs, 0.8%/side (1.6% round trip; stress 3.2%).
All sources accessed 2026-09-23. "Data date" = the paper's sample period. Reference keys `[Rn]` → list in §4.

**Read-level legend (applies to every number):**
- **FT** = full text read (version named).
- **WP** = working-paper full text read; the published version was not read.
- **AB** = abstract only; nothing beyond the abstract is verified.
- **SN** = search snippet or secondary summary only; weakest, not verified from the paper.

Evidence-strength scale *for our setting* (long-only, liquid, net of 1.6% RT):
- **Strong** = replicated in peer review, liquid coins, long leg isolated, net of costs ≥ ours. **No effect meets this.**
- **Moderate** = peer-reviewed, consistent sign in large/liquid coins, but gross or tested at low costs.
- **Weak** = mixed results, WP-only, small-cap-driven, or long leg not significant.
- **None** = null, contradictory, or the wrong sign for our universe.

## 0. Bottom line

1. **Only continuation holds in liquid coins.** Trend/momentum is the only family with a consistent sign in liquid coins at 1–4 weeks. Short-term reversal lives in small/illiquid coins [R6][R14][R15][R16][R19].
2. **The long leg is weak.** Most cross-sectional (CS) evidence is long–short, gross, built on CoinMarketCap (CMC) prices, and sorts 1,000–4,000 coins including micro-caps. Where the long leg is isolated against BTC in liquid coins, it is mostly insignificant:
   - LTW WP: winners−BTC is not significant for 1-, 2- and 4-week momentum; only 3-week reaches t=2.25 [R1].
   - Fičura: the BTC-alpha of large-and-liquid winners is −0.17%/wk (t −0.18) [R15].
   - Fieberg et al.: momentum "extracts alphas largely from short positions" [R20].
3. **Our costs are several times the published assumptions.** Published tests assume 10–60 bps/side; ours is 80 bps.
   - Top-30 momentum breaks even at 67 bps (untrimmed) [R12].
   - CTREND is the only large-coin long leg that survives high costs: 2.83%/side break-even in the top 100 [R9]. But it is an ML composite on CMC data ending 2022-05.
4. **Effects decay.**
   - Plain momentum in large, liquid coins "stopped in the early months of 2021" [R15].
   - Crypto anomalies are bull-market-concentrated and "fade over time" [R20].
   - BTC moving-average (MA) alpha roughly halves in the second half of the Detzel sample [R11].
   - There is no out-of-sample BTC predictability in [R24].
   - Equity benchmark: −26% out-of-sample, −58% post-publication [R33].
5. **Results are fragile to data construction.**
   - Survivorship bias is 62%/yr for equal-weighted portfolios [R26].
   - Non-standard errors exceed standard errors [R27].
   - Cong et al. cannot reproduce the LTW size effect in the same >$1M universe (decile 10−1 = −1.0%/wk, t −0.87) [R6].
   - Momentum payoffs are extremely fat-tailed (kurtosis 80.7) [R12], possibly with undefined variance [R13b].
6. **Best-supported long-only mechanism: time-series (TS) trend on BTC/majors** at our cost level, through low turnover and drawdown avoidance. But supporting samples end ≤2025 (most ≤2018), and BTC failed out of sample in [R24].
7. **Token unlocks: no peer-reviewed study found.** The evidence is industry-only (Keyrock: 16k events, ETH-normalised, no statistical tests) [R36], and there is no free point-in-time (PIT) unlock history. Not honestly backtestable.

## 1. Effects table

Abbreviations: L/S = long–short, VW/EW = value/equal-weighted, Qk = k-th quantile portfolio (Q1 = lowest signal), α = alpha, mcap = market capitalization, BE = break-even per-side cost, TO = weekly turnover, NW t = Newey–West t-stat, n.s. = not significant.

### 1.1 Cross-sectional momentum (1–4 week lookback)

| Source (read) | Sample / universe | Construction | Reported effect (gross unless noted) | Costs | Long-leg evidence | Critique / replication |
|---|---|---|---|---|---|---|
| Liu, Tsyvinski, Wu, NBER WP 25882 (2019) [R1] (WP) | CMC, 1,707 coins mcap>$1M, 2014-01..2018-12 | Weekly VW quintiles, 1-wk hold | L/S r1,0 2.7%, r2,0 3.3%, r3,0 4.1% (t 2.74), r4,0 2.5%/wk | None | Q5−BTC: r1 0.9% (t 0.69), r2 1.8% (1.50), **r3 3.0% (2.25)**, r4 1.4% (1.20)/wk. r1,0: Q4 4.2% > Q5 2.1% | Momentum 4.2%/wk above median size vs 0.6% n.s. below. Fama-MacBeth n.s. for >$1M, significant only >$10M |
| LTW, *J. Finance* 77(2):1133–77 (2022), doi:10.1111/jofi.13119 [R2] (FT intro only, via vLex; Wiley 403) | CMC, 1,827 coins >$1M, 2014-01..2020-07 | Same | L/S 1w 2.5%, 2w 3.1%, 3w 3.1%, 4w 2.2%, 1–4w 1.7%/wk | Not checked (JF body unread) | Not checked | Momentum attributed to investor overreaction |
| Cong, Karolyi, Tang, Zhao, WP Apr-2022 [R6] (WP intro+data) | CMC, 4,007 assets, 2014-01-01..2021-01-04 | Weekly VW deciles | Full sample 1–4w L/S **−4.1, −2.4, −2.5, −1.2%/wk** (reversal). By size quintile: −19.5% (small) → **+4.1%/wk (big)** | None | n/a | Momentum only in the largest caps; reversal in the other 80% |
| Dobrynskaya, WP (HSE); publ. *J. Alt. Inv.* 26(1):65–76 (2023), doi:10.3905/jai.2023.1.189 [R7] (WP) | CMC, ~2,000 coins >$1M, 2014–2020 | Cap-weighted 30/40/30 terciles, J/K 1–12 wk | 1/1 +40% p.a. (NW t 0.76); **2/2 +70% p.a. (NW t 1.98)**; 1/4 +42% (1.62). Rebalanced every 4 wks, J=2: +51% p.a. (NW t 1.44) | None | At short horizons winners ≈ losers (1/1: winners 228% p.a., losers 189% p.a., Table 3). Reversal comes from past losers | Author: momentum "less significant in recent years"; reversal beyond ~1 month |
| Fičura, FFA WP 5:003 (2023) [R15] (WP) | CMC, 2017-06..2022-12. "Large & liquid" = mcap ≥$50M **and** prior-week volume ≥$5M | Weekly EW quintiles, 1-wk hold | 1W L/S 1.36% (t 2.33); 2W 1.44% (2.69); 4W 0.84% (1.57); 12W −0.88% (−1.86); 26W −0.71% (−1.91)/wk | None | **1W: Q1 −0.20%, Q3 1.44%, Q5 1.15%/wk. Q5 BTC-α −0.17% (t −0.18); Q1 BTC-α −1.48% (t −1.98)** | "Standard momentum seems to have stopped in the early months of 2021." Not peer-reviewed |
| Grobys, Sandretto, Äijö, *FRL* 92:109602 (2026), doi:10.1016/j.frl.2026.109602 [R12] (FT) | CMC, top-30 mcap (re-set each Dec), 2017-01..2024-08, 398 wks | 30-day formation, skip 1 day, EW quintiles, weekly | **0.56%/wk (t 0.65)**. MDD 211.7% (L/S), kurtosis 80.7. After ex-post 5% trim: 0.93% (t 2.62) | 50 bps → trimmed 0.51% (t 1.42) n.s. BE 67 bps untrimmed, ~111 bps trimmed | n/a (L/S) | 9 "survivor" coins: 0.36%/wk (t 0.75). Trimmed payoff significant only in 2020-10..2024-08 → sample-dependent |
| Grobys, Kolari, Sandretto, Shahzad, Äijö, *FMPM* 39(4):443–76 (2025), doi:10.1007/s11408-025-00474-9 [R13a] (AB) | Large-cap coins (per [R12]: top-30, 2016–2023) | EW momentum | Severe crashes. "Even a single cryptocurrency can cause insignificant" returns. Volatility management mitigates | — | — | Momentum is a large-cap phenomenon |
| Grobys & Shahzad, *IJFE* 31(2):2180–93 (2026), doi:10.1002/ijfe.70036 [R13b] (AB) | 6 momentum strategies | — | Realised variances follow power laws. Infinite variance cannot be rejected → "t-statistics or Sharpe ratios do not exist" | — | — | Undermines every t-stat in this table |
| Ammann, Burdorf, Liebi, Stöckl, SSRN 4287573 (2022) [R26] (WP abstract+intro) | 3,904 coins incl. delisted, 2014–2021 | Weekly sorts, survivorship- and delisting-bias-free | "No evidence of a positive relationship between average returns [and] one-week momentum" | — | — | 39.5% of coins delist; 76% of those are total losses |
| Han, Kang, Ryu, SSRN 4675565 (2023) [R10] (SN; SSRN and PDF 403) | Binance-futures coins, 2014-01-26..2023-08-28 | TS and CS momentum under "realistic assumptions" | "Evidence of time-series momentum is strong, whereas evidence of cross-sectional momentum is weak." Concentrated among large winners | 15 bps/trade | — | Journal publication (JFM?) not verified |
| Fieberg, Liedtke, Zaremba, *IRFA* 94:103218 (2024), doi:10.1016/j.irfa.2024.103218 [R20] (AB) | — | Anomaly zoo under economic restrictions | Momentum "prevails in larger cryptocurrencies but incurs substantial trading costs and extracts alphas largely from short positions" | Yes | **Short-side driven** | "Most abnormal returns occur primarily in bull markets and fade over time" |
| Grobys & Sapkota, *Econ. Letters* 180:6–10 (2019), doi:10.1016/j.econlet.2019.03.028 [R17] (AB) | 143 coins, 2014–2018, monthly | — | No significant momentum | — | — | Monthly horizon misses 1–2 wk momentum per [R7] |
| Tzouvanas, Kizys, Tsend-Ayush, *Econ. Letters* 191:108728 (2020) [R18] (AB) | 12 coins, ~3 yrs daily | J/K | Short-term momentum highly significant; disappears at longer horizons | — | — | Tiny universe |

**Strength for us: Weak.** Continuation is real in large coins gross, but the long leg vs BTC is mostly insignificant, the effect decayed after 2021 [R15], and costs are not survived at ≥50 bps [R12][R20].

### 1.2 Cross-sectional trend composite (technical-indicator aggregate)

| Source (read) | Sample / universe | Construction | Effect | Costs | Long leg | Critique |
|---|---|---|---|---|---|---|
| Fieberg, Liedtke, Poddig, Walker, Zaremba, "A Trend Factor for the Cross Section of Cryptocurrency Returns", *JFQA* 60(7):3116–53 (2025), doi:10.1017/S0022109024000747 [R9] (FT, open access) | CMC, 3,245 coins mcap>$1M, 2015-04..2022-05 (423 wks) | 28 indicators (price/SMA 3–200d, RSI/stochastic/CCI, MACD, volume SMAs, Bollinger) combined by a cross-sectional elastic net. Weekly VW quintiles | L/S **3.87%/wk (t 5.19)**. Top-100 coins: H 3.78% (t 4.41), Q3 1.59%, L 0.38%. 10% largest: H 2.44%, Q3 1.55%, L/S 2.51% (t 3.01). Individual price/SMA signals mostly significant L/S. Most plain momentum n.s. at 2–3 wk holds | Long 30–50 bps / short 40–60 bps: L/S net 2.90→2.35%/wk. **H TO 62.8% (all) / 66.7% (top-100) per week.** BE for H: 3.17% / 2.83% per side (absolute return). 2-wk rebalance L/S 2.34%/wk; significant up to 4-wk holding | **Yes: H quintile carries it in big coins** | ML-aggregated, single sample, CMC VW prices, pre-publication. H excess over market not reported. Our fixed-weight simplification is only a partial transfer |

**Strength: Moderate (gross).** This is the only peer-reviewed large-coin long leg. The margin shrinks sharply in the largest coins (10% largest: H−Q3 = 0.89%/wk gross, see §2).

### 1.3 Short-term reversal (≤1 week) and long-horizon reversal

| Source (read) | Sample | Effect | Where it lives |
|---|---|---|---|
| Zaremba, Bilgin, Long, Mercik, Szczygielski, *IRFA* 78:101908 (2021), doi:10.1016/j.irfa.2021.101908 [R14] (AB) | >3,600 coins, 2015–2021, daily | Low last-day return beats high | Illiquid majority; "the handful of largest and most tradeable coins exhibit daily momentum" |
| Bianchi, Babiak, Dickerson, *JBF* 142:106547 (2022), doi:10.1016/j.jbankfin.2022.106547 [R16] (AB) | USD pairs on CEXs, 2017-03-01..2022-03-01 | Reversal = liquidity-provision return | Concentrated in low-activity, smaller, more volatile pairs |
| Kozlowski, Puleo, Zhou, *Appl. Econ. Lett.* 28(11):887–93 (2021), doi:10.1080/13504851.2020.1784831 [R19] (AB) | 200 coins, 2015–2019 | Reversal at daily, weekly and monthly rebalancing | Most pronounced in small, less liquid coins |
| Shen, Urquhart, Wang, *FRL* 34 (2020), doi:10.1016/j.frl.2019.07.021 [R21] (AB) and Jia, Goodell, Shen, *FRL* 45:102139 (2022) [R22] (AB) | >1,700 coins, 2013-04..2019-03 / later sample | [R21] uses a reversal factor; [R22] shows momentum, not reversal, in the recent sample | Sign flips with the sample |
| Fičura [R15] (WP) | 2017-06..2022-12 | 1W reversal t −7.31 in small/illiquid; momentum t 2.33 in large & liquid | Liquid coins → continuation |
| Long-horizon: Cong et al. [R6] value = −(52-wk return); Dobrynskaya [R7]; Fičura [R15] | See above | Value L/S 5.7%/wk (t 2.7), falling from 15.1% (small) to 0.8% (big). Reversal from K ≥ 8 wks, driven by losers. 12W/26W L/S −0.88% / −0.71% (n.s.) in large & liquid | Small-cap concentrated; hold > our 28-day cap |

**Strength: None for our universe** (wrong sign in liquid coins).

### 1.4 Time-series momentum / trend following

| Source (read) | Sample | Rule | Effect | Costs | Critique |
|---|---|---|---|---|---|
| Liu & Tsyvinski, NBER WP 24877 (2018) [R3] (WP); *RFS* 34(6):2689–2727 (2021), doi:10.1093/rfs/hhaa113 [R4] (AB) | BTC 2011-01-01..2018-05-31 (CoinDesk); XRP, ETH shorter | Regress future on current return; quintiles of weekly return | Weekly: +1 SD this week → +3.16 / 3.66 / 3.49 / 1.50% at 1–4 wks ahead. **Bootstrap t 2.17 / 2.73 / 2.47 / 1.40.** Daily 1-day-ahead bootstrap t 1.22 (n.s.). Next-week return by this-week quintile: top 11.22% vs bottom 2.60%/wk; no-lookahead cutoffs 7.88% vs 3.35% | None | ETH momentum weaker. Regular t-stats overstate significance relative to bootstrap |
| Detzel, Liu, Strauss, Zhou, Zhu, WP Apr-2018; *Fin. Mgmt* 50(1):107–37 (2021), doi:10.1111/fima.12310 [R11] (WP) | BTC 2010-10-27..2018-01-31 | Long BTC if P > MA(L), else T-bill; L = 5–100 days | Daily α 0.24% (MA5) … 0.11% (MA100). Weekly out-of-sample R² 1.17–3.66%. **Second-half α 0.15 … 0.04%/day (MA100 ≈ 0)** | **BE one-way 1.12% (MA5) … 3.96% (MA100)**; daily TO 21.8% … 2.7% | Decay inside the sample; ends before our window |
| Hudson & Urquhart, *Ann. Oper. Res.* 297:191–220 (2021), doi:10.1007/s10479-019-03357-1 [R24] (AB) | 2 BTC markets + 3 cryptos | ~15,000 rules in 5 classes, with data-snooping controls | Significant predictability and profitability; BE costs above typical | BE > typical | **"No predictability for Bitcoin in the out-of-sample period"**; persists in other coins |
| Corbet, Eraslan, Lucey, Sensoy, *FRL* 31:32–37 (2019) [R25] (AB) | High-frequency BTC | MA-oscillator, trading-range breakout | Variable-length MA best | — | Intraday |
| Zarattini, Pagani, Barbon, SSRN 5209907 (Apr-2025) [R23] (WP; not peer-reviewed) | CMC, 2015-01..2025-03-19 | **Long-only** Donchian ensemble (5–360d), 25% vol target, 20% rebalance threshold | BTC: CAGR 30%, vol 17%, Sharpe 1.56, MDD 19%. **Top-20 liquid rotation** (listed ≥365d, median daily vol ≥$2M, monthly): CAGR 18%, vol 9%, Sharpe 1.57, MDD 11%, α 10.8%/yr vs BTC, **β 0.08** | 10 bps base. At 50 bps the 5-day model's CAGR falls 34% → 18% | β 0.08 and vol 9% ⇒ much of the Sharpe comes from low exposure and vol targeting. Costs are 1/8 of ours |
| Grobys, Ahmed, Sapkota, *FRL* 32:101396 (2020) [R29] (SN, as quoted in [R28]) | 11 liquid coins, 2016–2018 | (1,20) MA, long-only | Ex-BTC: +8.76% p.a. over average market return | None | Secondhand |
| Ahmed, Grobys, Sapkota, *FRL* 35:101495 (2020), doi:10.1016/j.frl.2020.101495 [R28] (FT) | 10 privacy coins, 2016–2018 | (1,n) MA, n = 20–200 | Profitable only for DASH. Portfolio (1,20): 2.92% p.a. vs buy-and-hold 45.63% p.a. | None | Negative replication |
| Borgards, *NAJEF* 57:101428 (2021) [R30] (AB) | 20 cryptos | Dynamic momentum periods | Beats buy-and-hold; higher risk-adjusted return, lower downside | — | — |
| Han, Kang, Ryu [R10] (SN) | 2014–2023 | TS vs CS | "Evidence of time-series momentum is strong" | 15 bps | Snippet only |
| Kumar & Jenefer, Zenodo 10.5281/zenodo.19671502 (2026) [R31] (AB; unrefereed, low quality) | BTC, ETH, 2018-01..2026-03 | Monthly, vol-scaled TSMOM | Sharpe 0.82 pre-ETF → 1.22 post-ETF; difference n.s. (p 0.58); lagged buy-and-hold in the pre-ETF bull | — | Only post-2024 item found; weight ≈ 0 |

**Strength: Moderate.** Long-only native and low turnover. Samples are old, and BTC failed out of sample in [R24].

### 1.5 Size, volume, liquidity

| Source (read) | Effect | Critique |
|---|---|---|
| LTW JF [R2]: mcap L/S 5.8%/wk. Dollar volume (low−high) 3.3%/wk; std of dollar volume 3.2%/wk; all subsumed by CSMB. LTW WP [R1]: smallest quintile − BTC 3.4%/wk (t 2.42) | Long leg = smallest coins | Micro-cap |
| Li, Zhang, Xiong, Wang, *Appl. Econ. Lett.* 27(14) (2020) [R32] (AB): >1,800 coins, 2014-01..2019-05, "stable" size effect | — | — |
| Ammann et al. [R26] (WP): survivorship-free VW size premium 1.89%/wk vs 2.84% survivors-only (+50%) | — | Bias inflates the premium |
| Cong et al. [R6] (WP): >$1M sample, 10−1 decile −1.0%/wk (t −0.87) **n.s.** | Fails to reproduce LTW in the same universe | — |
| Fieberg et al. [R20] (AB): "size and volume anomalies originate from micro-cap coins of negligible economic importance" | — | — |
| Mercik, Zaremba, Demir, "Crypto factor zoo", *IRFA* 113:105137 (2026) [R34] (AB): 2–3 of 36 factors kill all alphas; turnover volatility, bid–ask spreads, new-address-to-price most influential; liquidity dominates | Liquidity premia = long illiquid coins | — |
| Leirvik, *FRL* 44:102031 (2022) [R35] (AB): 5 largest coins; liquidity-volatility premium, "highly time-varying" | — | — |

**Strength: None for us.** Our universe excludes the long leg, and true mcap history is not free (§Implications).

### 1.6 Volatility, IVOL, MAX, downside risk

| Source (read) | Effect |
|---|---|
| LTW WP [R1]: beta, beta², IVOL, return vol, skew, kurtosis, MAX return, Amihud all **n.s.** L/S | Null |
| Burggraf & Rudolf, *FRL* 40:101683 (2021) [R37] (AB): 1,000 coins, 2013-04-28..2019-11-01 | "No evidence of a significant low volatility premium" |
| Zhang & Li, *RIBAF* 54:101252 (2020) [R38] (AB) | IVOL **positively** priced (opposite of equities) |
| Zhang, Li, Xiong, Wang, *JBF* 133:106246 (2021) [R39] (AB) | Downside risk positively priced |
| Ammann et al. [R26] (WP) | After survivorship correction: no β or downside-risk relation |
| Li, Urquhart, Wang, Zhang, *IRFA* 77:101829 (2021) [R40] (AB) vs Grobys & Junttila, *JIFMIM* 71:101289 (2021) [R41] (AB) | "MAX momentum" (high MAX → higher returns) vs lottery effect (low−high MAX > 1.50%/wk): **opposite signs** |

**Strength: None/contradictory.** Volatility management is useful only as a crash overlay [R13a].

### 1.7 Network / on-chain value, investor attention

| Source (read) | Effect | Data needed |
|---|---|---|
| LT RFS [R4] (AB): "exposed to cryptocurrency network factors but not … production factors". LT WP [R3]: BTC price-to-wallet-users ratio has **no** predictive power | Contemporaneous exposure, not a signal | On-chain users |
| Liebi, *Econ. Modelling* 109:105777 (2022) [R42] (AB): 652 assets; high active-addresses-to-network-value (AA/NV) +3.7 pp/wk vs low, at comparable size | L/S gross | Active addresses |
| Cong et al. [R6] (WP): addresses-with-balance growth L/S 4.0%/wk (t 2.8); 616-asset core sample (IntoTheBlock) | L/S gross | Paid-vendor on-chain data |
| Mercik et al. [R34] (AB): new-address-to-price among the top factors | — | On-chain |
| LT WP [R3]: Google-search deviation +1 SD → BTC +1.84% / +2.30% at 1–2 wks; Twitter +2.50%; "Bitcoin hack" ratio −2.75% | Attention | Google Trends / Twitter |

**Strength: Moderate academically, but untestable with our data.**

### 1.8 Token unlocks (supply events)

| Source (read) | Sample | Effect | Quality |
|---|---|---|---|
| Keyrock, "From Locked to Liquidity: What 16,000+ Token Unlocks Teach Us" (Dec-2024, upd. Jul-2025) [R36] (FT blog) | 16,000+ unlock events, ±30 days, ETH-normalised | "90% of unlocks create negative price pressure." Decline starts ~30d before and accelerates in the final week; stabilises ~14d after. Team unlocks worst ("-25%"); ecosystem-development unlocks +1.18% | Industry; no statistical tests; data not public. Conflict of interest: market maker selling hedging services |
| Kim, SSRN 6632838 (Apr-2026) [R43] (SN) | 52 hand-collected unlocks on Binance-listed assets, 2023-01..2025-12 | 46/52 negative within 72h (binomial p = 2.2e-9) | Preliminary, n = 52 |
| Animoca Brands Research (SN; source 403) | — | "1% unlock → −0.3% the week before and −0.3% the week after" | **Not verified** |

No peer-reviewed unlock event study was found (search 2026-09-23). **Strength: Weak, and not backtestable.**

### 1.9 Exchange listings

- Ante & Meyer, *Decis. Econ. Finance* 44(2) (2021), doi:10.1007/s10203-021-00323-0 [R44] (AB): 250 cross-listings of 135 ICO tokens on 22 exchanges. Abnormal return +6.51% on listing day and +9.97% over a 7-day window. Effect larger for lower prior volume/mcap.
- Industry claims of post-listing decline were found but are not peer-reviewed; not used.
- **Strength: Weak.** Relevant only as a minimum-history filter.

### 1.10 Meta-evidence: decay, costs, data fragility

| Source (read) | Finding |
|---|---|
| McLean & Pontiff, *JF* 71:5–32 (2016), doi:10.1111/jofi.12365 [R33] (AB/SN) | 97 equity anomalies: returns 26% lower out of sample, 58% lower post-publication |
| Novy-Marx & Velikov, *RFS* 29:104–47 (2016) [R45] (AB) | Anomalies with turnover >50%/month rarely survive costs. A buy/hold spread (stricter to enter than to stay) is the most effective mitigation |
| Fieberg, Günther, Poddig, Zaremba, *IRFA* 92:103106 (2024), doi:10.1016/j.irfa.2024.103106 [R27] (AB) | 20,736 designs × 43 variables: non-standard errors exceed standard errors. Size and momentum remain robust across specifications. Down-weighting the smallest coins reduces the non-standard errors |
| Cakici, Shahzad, Będowska-Sójka, Zaremba, *IRFA* 94:103244 (2024), doi:10.1016/j.irfa.2024.103244 [R46] (AB) | Counterpoint: abnormal returns "originate from the long leg … and persist over time", and most ML strategies stay profitable after costs. **But** "alphas are concentrated in hard-to-trade assets" (small, illiquid, volatile) |
| Fičura [R15]; Fieberg et al. [R20]; Detzel [R11]; Hudson & Urquhart [R24]; Grobys et al. [R12] | Crypto-specific decay and sample dependence (see §1.1, §1.4) |
| Ammann et al. [R26] | Survivorship + delisting bias: 0.93% p.a. VW, **62.19% p.a. EW** |

## 2. Cost arithmetic `[ESTIMATE]`, straight from the SPEC cost model

Annual drag ≈ 52 × τ × 2 × c, where τ = weekly one-way turnover (fraction of the book replaced) and c = per-side cost. This matches CTREND's BE definition: 3.98 / (2 × 0.6284) = 3.17 [R9].

| Weekly τ | 2.5% | 5% | 10% | 20% | 40% | 65% |
|---|---|---|---|---|---|---|
| Drag @0.8%/side | 2.1%/yr | 4.2% | 8.3% | 16.6% | 33.3% | 54.1% |
| Drag @1.6%/side (stress) | 4.2% | 8.3% | 16.6% | 33.3% | 66.6% | 108% |

- **CTREND-style, weekly, top-100 coins** [R9]:
  - Cost: H quintile TO 66.7% → ≈1.07%/wk.
  - Top-100 H−Q3 gross spread 2.19%/wk → ≈ +1.1%/wk net, pre-decay.
  - Applying the equity −58% post-publication haircut [R33] leaves 0.92%/wk gross, below the cost. `[SPECULATION]`: transfers the equity decay rate to crypto.
  - In the **10% largest coins**, H−Q3 is only 0.89%/wk gross, below the ≈1.0%/wk cost even before decay `[ESTIMATE]`.
  - ⇒ Weekly full rebalancing fails; a buy/hold buffer or 2–4-week holds are required.
- **BTC trend gate:** each full in→out→in cycle on 90% notional costs ≈ 0.9 × 1.6% = 1.44% of equity. 6 cycles/yr ≈ 8.6%/yr; 12 cycles/yr ≈ 17.3%/yr `[ESTIMATE]`. The cycle count is unknown until measured.
  - Detzel's BE one-way costs (1.12–3.96%) exceed our 0.8%, but only in 2010–2018 with daily switching [R11].
- **Loser avoidance (Fičura, plain 1W)** [R15]:
  - Gross uplift vs EW-of-all-quintiles ≈ 1.25% − 0.96% = **+0.29%/wk** (EW, large & liquid, 2017-06..2022-12) `[ESTIMATE]`.
  - Drag ≈ 0.16–0.32%/wk at τ 10–20% `[SPECULATION]` on τ ⇒ roughly break-even.

## 3. What survives long-only + 1.6% round trip

| Effect | Verdict | Reason |
|---|---|---|
| Market-level TS trend (BTC-gated exposure) | **Plausible** | Low turnover, long-only native, targets the drawdown criterion. Risks: old samples, BTC out-of-sample failure [R24], lagging re-entry in bull folds (SPEC §7.3 criterion 1) `[INFERENCE]` |
| Per-asset TS trend (breadth-scaled) | **Plausible, weaker evidence** | Only WP evidence, at 10 bps [R23]. Part of the Sharpe comes from low β / vol targeting |
| CS trend composite (CTREND-lite) | **Uncertain** | The only published big-coin long leg [R9]. Weekly TO ~65% eats it at our costs (§2); needs a buffer or longer holds; simplified signal ≠ CTREND |
| Plain CS momentum (long winners) | **Unlikely** | Long leg ≈ BTC [R1][R15]; dead since early 2021 [R15]; ≥50 bps kills it [R12]; alphas from shorts [R20]; survivorship [R26] |
| Loser avoidance (drop bottom quintile) | **Uncertain, near break-even** | The effect lives in Q1 [R15][R20], but the uplift ≈ cost (§2) and tracking error vs the EW benchmark is low |
| Short-term reversal | **No** | Wrong sign in liquid coins [R14][R15][R16] |
| Size / volume / liquidity | **No** | Micro-cap origin [R20][R6]; our universe excludes the long leg |
| Low-vol / IVOL / MAX / downside | **No** | Null or contradictory [R1][R37][R38][R40][R41][R26] |
| Network value / attention | **Unknown** | Cannot be tested honestly with free PIT data |
| Token unlocks | **Unknown** | No peer-reviewed study; no PIT data |

**Not verified / not found:**
- Full texts of the JF [R2] and RFS [R4] papers (paywalled; the NBER WPs were read instead).
- Zaremba et al. [R14] full text.
- Han, Kang, Ryu [R10] full text (SSRN and AUT PDF returned 403) and its journal venue.
- The Animoca unlock numbers (403).
- Published versions of Detzel [R11] and Dobrynskaya [R7].
- The CTREND H-quintile excess over the market.
- Post-2022 out-of-sample evidence for any CS effect in liquid coins beyond [R12] (to 2024-08).

## 4. References (all accessed 2026-09-23)

- [R1] Liu, Tsyvinski, Wu (2019) NBER WP 25882 — https://www.nber.org/system/files/working_papers/w25882/w25882.pdf
- [R2] Liu, Tsyvinski, Wu (2022) JF 77(2) doi:10.1111/jofi.13119 — https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13119 ; intro text https://law-journals-books.vlex.com/vid/common-risk-factors-in-1049437298
- [R3] Liu, Tsyvinski (2018) NBER WP 24877 — https://www.nber.org/system/files/working_papers/w24877/w24877.pdf
- [R4] Liu, Tsyvinski (2021) RFS 34(6) doi:10.1093/rfs/hhaa113 — https://academic.oup.com/rfs/article-abstract/34/6/2689/5912024
- [R6] Cong, Karolyi, Tang, Zhao (2022 draft) — https://abfer.org/media/abfer-events-2022/annual-conference/papers-investfin/AC22P3048_Value-Premium-Network-Adoption-and-Factor-Pricing-of-Crypto-Assets.pdf (SSRN 3985631)
- [R7] Dobrynskaya — WP https://conference.hse.ru/files/download_file_ex?hash=FAE0AB2DC7A67656E89A0B1CB27D8C7D&id=3B5EE9A5-0B18-458A-9458-B4ED0F6C6664 ; JAI doi:10.3905/jai.2023.1.189
- [R9] Fieberg et al. (2025) JFQA doi:10.1017/S0022109024000747 — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4C1509ACBA33D5DCAF0AC24379148178/S0022109024000747a.pdf/trend_factor_for_the_cross_section_of_cryptocurrency_returns.pdf
- [R10] Han, Kang, Ryu (2023) SSRN 4675565 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565
- [R11] Detzel et al. — WP https://community.portfolio123.com/uploads/short-url/jS0qs8gndLATbD3WlYQ79thDnzD.pdf ; FM doi:10.1111/fima.12310 https://ideas.repec.org/a/bla/finmgt/v50y2021i1p107-137.html
- [R12] Grobys, Sandretto, Äijö (2026) FRL 92 — https://osuva.uwasa.fi/server/api/core/bitstreams/2a766d58-9fd3-44b8-b1a3-14a048a0b653/content
- [R13a] Grobys et al. (2025) FMPM — https://ideas.repec.org/a/kap/fmktpm/v39y2025i4d10.1007_s11408-025-00474-9.html
- [R13b] Grobys, Shahzad (2026) IJFE — https://ideas.repec.org/a/wly/ijfiec/v31y2026i2p2180-2193.html
- [R14] Zaremba et al. (2021) — https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html
- [R15] Fičura (2023) FFA WP — https://wp.ffu.vse.cz/pdfs/wps/2023/01/03.pdf
- [R16] Bianchi, Babiak, Dickerson (2022) — https://ideas.repec.org/a/eee/jbfina/v142y2022ics0378426622001418.html
- [R17] Grobys, Sapkota (2019) — https://ideas.repec.org/a/eee/ecolet/v180y2019icp6-10.html
- [R18] Tzouvanas et al. (2020) — https://ideas.repec.org/a/eee/ecolet/v191y2020ics0165176519303647.html
- [R19] Kozlowski et al. (2021) — https://ideas.repec.org/a/taf/apeclt/v28y2021i11p887-893.html
- [R20] Fieberg, Liedtke, Zaremba (2024) — https://ideas.repec.org/a/eee/finana/v94y2024ics1057521924001509.html
- [R21] Shen, Urquhart, Wang (2020) — https://ideas.repec.org/a/eee/finlet/v34y2020ics1544612319304519.html
- [R22] Jia, Goodell, Shen (2022) — https://ideas.repec.org/a/eee/finlet/v45y2022ics1544612321002208.html
- [R23] Zarattini, Pagani, Barbon (2025) — https://concretumgroup.com/wp-content/uploads/2026/02/Catching-Crypto-Trends.pdf (SSRN 5209907)
- [R24] Hudson, Urquhart (2021) — https://ideas.repec.org/a/spr/annopr/v297y2021i1d10.1007_s10479-019-03357-1.html
- [R25] Corbet et al. (2019) — https://ideas.repec.org/a/eee/finlet/v31y2019icp32-37.html
- [R26] Ammann, Burdorf, Liebi, Stöckl (2022) — https://www.alexandria.unisg.ch/bitstreams/2bc8397d-47dd-4f66-8467-9004b2c9d212/download
- [R27] Fieberg, Günther, Poddig, Zaremba (2024) — https://ideas.repec.org/a/eee/finana/v92y2024ics1057521924000383.html
- [R28] Ahmed, Grobys, Sapkota (2020) — https://osuva.uwasa.fi/server/api/core/bitstreams/1655ff2c-b83f-4d98-b737-2dbf539e2c4a/content
- [R29] Grobys, Ahmed, Sapkota (2020) FRL 32:101396 — as quoted in [R28]
- [R30] Borgards (2021) — https://ideas.repec.org/a/eee/ecofin/v57y2021ics1062940821000590.html
- [R31] Kumar, Jenefer (2026) — https://zenodo.org/records/19671502
- [R32] Li, Zhang, Xiong, Wang (2020) — https://ideas.repec.org/a/taf/apeclt/v27y2020i14p1141-1149.html
- [R33] McLean, Pontiff (2016) — https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365
- [R34] Mercik, Zaremba, Demir (2026) — https://ideas.repec.org/a/eee/finana/v113y2026ics1057521926000645.html
- [R35] Leirvik (2022) — https://ideas.repec.org/a/eee/finlet/v44y2022ics1544612321001124.html
- [R36] Keyrock (2024/25) — https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/
- [R37] Burggraf, Rudolf (2021) — https://ideas.repec.org/a/eee/finlet/v40y2021ics154461232030667x.html
- [R38] Zhang, Li (2020) — https://ideas.repec.org/a/eee/riibaf/v54y2020ics0275531920301926.html
- [R39] Zhang, Li, Xiong, Wang (2021) — https://ideas.repec.org/a/eee/jbfina/v133y2021ics0378426621002053.html
- [R40] Li, Urquhart, Wang, Zhang (2021) — https://ideas.repec.org/a/eee/finana/v77y2021ics1057521921001630.html
- [R41] Grobys, Junttila (2021) — https://ideas.repec.org/a/eee/intfin/v71y2021ics1042443121000081.html
- [R42] Liebi (2022) — https://ideas.repec.org/a/eee/ecmode/v109y2022ics0264999322000232.html
- [R43] Kim (2026) SSRN 6632838 — https://papers.ssrn.com/sol3/Delivery.cfm/6632838.pdf?abstractid=6632838&mirid=1 (snippet only)
- [R44] Ante, Meyer (2021) — https://ideas.repec.org/a/spr/decfin/v44y2021i2d10.1007_s10203-021-00323-0.html
- [R45] Novy-Marx, Velikov (2016) — https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html
- [R46] Cakici et al. (2024) — https://ideas.repec.org/a/eee/finana/v94y2024ics1057521924001765.html

## Implications for backtestable hypotheses

### A. Honestly backtestable from Coinbase daily OHLCV (listed + delisted) and the PIT universe
- **Price signals:** TS trend (price/SMA, N-day return, Donchian highs/lows), CS momentum and trend composites, distance to k-day high (uses `high`), short- and long-horizon reversal.
- **Risk signals:** realised volatility, IVOL/β vs BTC or the EW basket, MAX, downside β.
- **Liquidity signals:** dollar volume (close × base volume) and its volatility, Amihud |r|/$vol, the Corwin–Schultz spread from high/low.
- **Listing age:** first Coinbase candle.
- **Caveats:**
  - Coinbase-venue volume ≠ aggregate market volume.
  - There is no supply data, so no true mcap/size.
  - Delistings must be modelled explicitly, because EW results are hypersensitive: 62% p.a. EW survivorship bias [R26] `[INFERENCE: a Coinbase delisting ≠ project death, but the last close may not be executable]`.

### B. Not honestly backtestable (discretionary or current-only)
- **Token unlocks:** no free PIT schedule archive (SPEC §5: revisions not archived); evidence is industry-only [R36][R43]. Forward PIT snapshots at most.
- **On-chain value/network (AA/NV, address growth)** [R42][R6][R34]: needs on-chain histories. Free sources' coverage and revision behaviour were not verified here; they are survivor-skewed `[INFERENCE]`. Research only.
- **True size (mcap):** needs circulating-supply history. Free CoinGecko history covers only the trailing ~365 days (SPEC §4.2), not 2020-07..2026-09.
- **Investor attention (Google Trends)** [R3]: the index is re-normalised and sampled per request, so not PIT-reproducible `[INFERENCE]`.
- **Listing-announcement drift** [R44]: happens before the Coinbase candle history exists; needs announcement timestamps.
- **LTW factor returns** (public file cited in [R9] fn 5): cover our out-of-sample window. **Do not inspect**, to avoid contaminating the walk-forward test.

### C. Candidate rule-based hypotheses (≤5)

**Conventions common to all:**
- **Decision time:** t = Monday 00:00 UTC. Signals use only daily candles with close ≤ t. Fill at t per SPEC §6.1 plus slippage; report the one-day-delay sensitivity.
- **Universe:** U_t = SPEC PIT universe at t (ADV ≥ $5M; stablecoins/wrapped excluded), and ≥ (max lookback + 1) Coinbase daily candles. This doubles as a new-listing filter; prior evidence for that is weak [R44].
- **Sizing:** gross ≤ 90%, rest USD. Weight per selected name = 90% / max(k, 5), so fewer than 5 names leaves cash. This is fixed, not a grid parameter.
- **No-trade band:** trade a held name only if |target − current| > 20% of target, or on entry/exit ([R23] threshold; [R45] mitigation).
- **Exits:** between Mondays only via SPEC risk rules. Weekly re-qualification satisfies the 28-day max-hold rule.
- **Grids:** ≤4 cells per hypothesis. The Holm family = all trials (SPEC §7.3). With ~12 total trials the best p must be < 0.05/12 ≈ 0.0042 `[INFERENCE]`.

**H1 — BTC trend gate (market TSMOM)**
- **Signal:** g_t = 1 if BTC-USD close_t > SMA_L(BTC-USD close, last L daily closes including t); else 0.
- **Book:** g=1 → 90% in P; g=0 → 100% USD. Weekly.
- **Grid:** L ∈ {50, 100} × P ∈ {BTC, EW(U_t)} (4 cells).
- **Evidence for:**
  - BTC weekly TSMOM at 1–3 wks (bootstrap t 2.17–2.73; 2011–2018) [R3].
  - P/MA(5–100) predicts BTC; BE one-way cost 1.12–3.96% (2010–2018) [R11].
  - Long-only BTC Donchian ensemble: Sharpe 1.56 net of 10 bps (2015–2025; WP) [R23].
  - "TSMOM strong" [R10] (SN).
- **Evidence against:**
  - No BTC out-of-sample predictability [R24].
  - α ≈ halves in the second half of the sample [R11].
- **Turnover:** low; ≈1.44% of equity per full cycle `[ESTIMATE]`.
- **Likely failure mode:** loses the fold-level Sharpe race to BTC buy-and-hold in bull quarters, even if the MDD criterion passes `[INFERENCE]`.

**H2 — Per-asset trend, breadth-scaled**
- **Eligibility:** name i eligible at t if close_i,t > SMA_L,i,t AND close_i,t > close_i,t−28d.
- **Book:** hold all eligible names at 90%/max(k,5); rest USD. Weekly.
- **Grid:** L ∈ {20, 50}.
- **Evidence for:**
  - Long-only per-asset trend on the top-20 liquid coins: Sharpe 1.57, MDD 11%, α 10.8%/yr vs BTC (10 bps, WP) [R23].
  - 20-day MA ex-BTC +8.76% p.a. (no costs; SN) [R29].
  - Alt-coin predictability persists out of sample [R24].
  - [R30] (AB).
- **Evidence against:**
  - Privacy-coin replication fails [R28].
  - [R23]'s β 0.08 implies its Sharpe partly reflects low exposure.
- **Turnover:** τ ≈ 10–25%/wk → 8–21%/yr drag `[SPECULATION]`; measure it.

**H3 — Cross-sectional trend composite (CTREND-lite, fixed weights, no ML)**
- **Score:** score_i,t = mean over L ∈ {5, 10, 20, 50, 100} of the cross-sectional percentile rank of ln(close_i,t / SMA_L,i,t).
- **Selection:** top tercile of U_t (k = ⌈N/3⌉), weight 90%/max(k,5).
- **Buffer:** a held name stays while its score is in the top 50%.
- **Grid:** rebalance cadence ∈ {every Monday, every 2nd Monday}.
- **Evidence for:**
  - [R9] (JFQA, peer-reviewed): top-100 H quintile 3.78%/wk vs Q3 1.59% (gross, 2015-04..2022-05). Significant up to 4-week holding. Price/SMA signals significant individually.
  - [R11]: P/MA predicts BTC.
- **Evidence against:**
  - This is not the ML CTREND (no volume or oscillator inputs), so the prior transfers only partially.
  - Weekly TO 63–67% [R9] ≈ 1.0%/wk cost at our rates; the 10%-largest H−Q3 is only 0.89%/wk gross (§2).
  - The plain-momentum long leg ≈ BTC [R15].

**H4 — Loser avoidance (Fičura high-momentum exclusion)**
- **Signal:** hm_i,t = ln(close_i,t) − ln(max of `high` over the W daily candles ending t).
- **Book:** hold U_t EW at 90%/max(k,5), excluding the bottom quintile by hm (≥1 name excluded when N ≥ 5).
- **Hysteresis:** an excluded name re-enters only when its hm rank ≥ 40th percentile.
- **Grid:** W ∈ {7, 14}.
- **Evidence for:**
  - [R15] (WP, 2017-06..2022-12, mcap ≥ $50M & weekly vol ≥ $5M, EW): 1-wk high-momentum L/S t 4.93, "stable over the entire time-period". Only Q1 alphas are significant (Q5 BTC-α 0.69%/wk, t 0.83).
  - Plain 1W mom: Q1 −0.20%/wk vs Q2–Q5 1.09–1.44% [R15].
  - Momentum alpha comes from shorts [R20].
  - LTW WP: r1,0 Q1 −0.6%/wk [R1].
- **Evidence against:**
  - Single unrefereed WP for the high-momentum signal.
  - Gross uplift ≈ 0.29%/wk ≈ cost (§2).
  - Low tracking error vs the EW benchmark → low power.

**H5 — Plain CS momentum, long winners (replication control; low prior)**
- **Signal:** r_i = close_t / close_{t−21d} − 1.
- **Book:** top tercile at 90%/max(k,5); buffer top 50%; weekly.
- **Grid:** single cell.
- **Evidence for:**
  - r3,0 Q5−BTC +3.0%/wk (t 2.25; 2014–2018) [R1].
  - Momentum strongest in big coins [R1][R6].
  - 2/2 +70% p.a. (NW t 1.98) [R7].
- **Evidence against:**
  - Q5 ≈ Q3, dead after early 2021 [R15].
  - Not significant, and killed by 50 bps [R12].
  - Vanishes after survivorship correction [R26].
  - CS momentum weak [R10]; alpha from shorts [R20].
  - 4-weekly rebalanced version not significant [R7].

### D. Recommendation for the 1–3 pre-registrations
1. **H1:** best evidence-to-cost ratio, long-only native, directly targets the MDD criterion.
2. **One of H3/H2:** H3 has the only peer-reviewed large-coin long leg [R9] but high turnover; H2 has lower turnover but WP-only evidence.
3. **H4:** a cheap, sharp test of the "effect lives in losers" finding. Expected result: inconclusive.

**Drop:** reversal, size, volume/liquidity, low-vol/IVOL/MAX, network value, unlocks (wrong sign or untestable). Run H5 only if a canonical-replication control is wanted; it spends Holm budget.
