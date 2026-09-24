# EDGE_REPORT — Phase 2

Status: **PRE-REGISTRATION.** Sections 1–2 are written and committed before any hypothesis is backtested on real prices. Results (§3–5) are appended after the run and cite the pre-registration commit hash.

Tags: **[MEASURED]** reproduced by repository code · **[SOURCE]** cited in a research note · **[ESTIMATE]** · **[SPECULATION]** · **[INFERENCE]**.

Research notes (sources and data dates are inside each): `research/notes/01_regime.md`, `02_candidates_defi_apps.md`, `03_candidates_l1_payments.md`, `04_anomaly_literature.md`. All were produced 2026-09-23/24 by four parallel research tracks. No note ran a backtest.

---

## 1. Research synthesis

### 1.1 Regime (as of the 2026-09-23 daily close; `01_regime.md`)
- **Trend:** early-stage uptrend inside a cyclical drawdown. BTC closed at $84,378, 19.3% above its 200-day SMA. The 50-day SMA crossed above the 200-day on 2026-09-08 (for ETH, 2026-08-31). BTC is still 32.3% below its 2025-10-06 closing high; ETH is 44.5% below its high.
- **Volatility:** normal. BTC 30-day realized vol is 43%, the 62nd percentile of the past year.
- **Leverage:** neutral. 30-day funding on US-reachable venues is +4.5–9.9% annualized. Binance returns HTTP 451 and Bybit 403 (geo-blocked); neither was used.
- **Flows vs macro:** a hawkish Fed hiked to 3.75–4.00% on 2026-09-16. Against that, US spot BTC ETFs took in +$3.17B over 30 days. Stablecoin supply is flat (+1.1% over 30 days, −0.06% over 90).
- **Sector rotation:** privacy, DEX, L2 and AI/DePIN led over 30 days; memes, RWA and gaming lagged.
- **Interpretation [SPECULATION]:** this looks like a risk-on rotation soon after a trend change. The trend signals are only 2–5 weeks old, so the regime is fragile.

### 1.2 Candidate setups (point-in-time universe on 2026-09-23: 28 names)
These are **discretionary and current-only**. None can be backtested honestly (§1.4). They are recorded as research-layer theses, not tradeable hypotheses.

| Asset | Stance | Core observation | Confirmed catalyst (dated) | Strongest bear case | Invalidation (summary) |
|---|---|---|---|---|---|
| PUMP | possible long | Market cap / annualized holder revenue ≈ 6.4× (buyback-and-burn, 50% of revenue) | Next modeled insider unlock 2026-10-12, 1.47% of circulating | Unlocks (≈6.875B/month) exceed buybacks (≈6B/month). ≈487B tokens (≈105% of float) have no schedule. Class action pending | Buybacks < $0.5M/day for 14 days; buyback share < 50%; a dated 240B distribution |
| UNI | conditional long | Fee switch live since 2026-07-27. Holder revenue annualizing ≈$196M (29.6×; 52× on 90 days). No unlocks | Fee switch (live) | ≈60% of that revenue comes from Robinhood Chain, whose fees are already −70% from the 09-04 peak. Price +114% in 30 days | 7-day annualized holder revenue < $100M for 2 weeks; Robinhood Chain share < 25% |
| SOL | weak long | Most fee revenue in its group. Market cap ≈ 200× annual fees + MEV tips (ETH ≈ 1,600×) | none dated (Alpenglow mainnet: "no date") | Fees −76% year on year. Issuance ≈ 7.6× fees | Monthly fees < $11.5M; 4 straight weeks of ETF outflows; no Alpenglow by 2026-12-31 |
| NEAR | stretched long | Intents fees fund buybacks, but these cover ≈13% of issuance | Bitwise ETF filed (no decision date) | Active accounts −78% year on year while price is +122% in 30 days | Intents 30-day revenue < $0.5M; ETF withdrawn or denied; close < $2.83 |
| ZEC | avoid | Market cap $25.75B vs $0.67M/year chain fees. Issuance ≈ $1.0B/year | Grayscale ZCSH ETF trading since 08-25; NU7 mainnet target 11-05 | (the long case) ETF demand plus a supply narrative | 8 weeks of ETF net creations, excluding affiliate in-kind deposits, above issuance, plus other conditions |
| HYPE | avoid (as a value long) | Price at an all-time high (+104% year on year) while holder revenue is −55% year on year; 28–38× | 9.92M HYPE scheduled to contributors 2026-10-06 | — | 30-day holder revenue > $1.4B annualized (< 15×) |
| LIGHTER | avoid | 35× market cap and 140× FDV to holder revenue; fees −71% from peak | Insider vesting from 2026-12-27 | — | Holder revenue > $130M annualized; re-lock |
| AERO | avoid (value trap) | Emissions of 2.43% of circulating a month exceed fees paid to voters, so net holder revenue is negative | — | — | 8 epochs with emissions below holder revenue AND 90-day holder revenue > $120M |
| ARB | avoid | DAO income ≈ $16M/year against ≈ $20M/month of unlocks; nothing accrues to holders | Monthly unlocks through 2027-03 | — | DAO passes income to holders; Robinhood Chain fees > $1M/day for 30 days |
| SUI | avoid | FDV 2.44× market cap; 52% of supply has no release schedule; fees −81%, TVL −73% year on year | — | — | Binding lock-up; fees > $0.5M/month; TVL > $1B |

Source for every row: `02_candidates_defi_apps.md` and `03_candidates_l1_payments.md` (per-row URLs and dates).

Cross-cutting observation [INFERENCE]: most of today's "valuation disconnects" are momentum episodes, where price ran far ahead of fees, users or TVL. That is why the testable hypotheses below are trend rules. Any fundamental overlay stays discretionary.

### 1.3 Prior evidence (`04_anomaly_literature.md`)
- **Only continuation has a consistent sign.** Trend/momentum is the only effect with a consistent sign in liquid coins at 1–4 weeks. Short-term reversal lives in small, illiquid coins.
- **The long leg of cross-sectional momentum is weak.** Among liquid coins it ≈ BTC (Fičura 2023 WP: top-quintile BTC-alpha −0.17%/week, t −0.18). It is reported dead after early 2021, and most of the alpha comes from the short side.
- **Time-series trend is the best-supported long-only mechanism,** because turnover is low. The supporting samples mostly end by 2018, and the BTC out-of-sample evidence is negative (Hudson & Urquhart).
- **CTREND trend composite:** the only peer-reviewed large-coin long leg (Fieberg et al., JFQA). Weekly turnover of ≈65% implies ≈1.0%/week in costs at our rates [ESTIMATE], above its 0.89%/week gross spread in the largest 10% of coins.

### 1.4 What cannot be tested honestly
- **Fee/revenue-yield value:** point-in-time market-cap history isn't free before the trailing 365 days. DefiLlama history is revised without snapshots. The cross-section is 2–7 names over 2020–26.
- **Token unlocks:** no archived point-in-time schedules; no peer-reviewed evidence.
- **Others:** BTC dominance history, sector labels, ETF flows (which start 2024), open-interest history.

---

## 2. Pre-registered hypotheses

### 2.0 Common protocol (applies to every trial; SPEC §6, §7)

**Data and dates**
- **Data:** Coinbase Exchange daily candles, all USD products listed and delisted, cached by `edge.fetch`. `AS_OF = 2026-09-23T00:00Z`, so the last bar used is 2026-09-22. The sha256 manifest is written to `research/results/phase2/manifest.json`.
- **Universe U_d:** `edge.universe.eligibility`: 30-day ADV ≥ $5M, ≥ 30 bars of history, stablecoins/wrapped excluded, top 50 by ADV.
- **Walk-forward folds:** `edge.folds.walk_forward(2020-07-01, 2026-09-22)`, which gives **20 folds**. Train is 12 months and test is 3 months. The contiguous out-of-sample (OOS) span is **2021-07-01 → 2026-06-30**.
- **Untouched holdout:** 2026-07-01 → 2026-09-22 is reported **descriptively only** and does not gate.

**Execution** (via `edge.engine.run`)
- **Decisions:** at the close of every Sunday bar (d.dayofweek == 6), executed at the open of Monday's bar (00:00 UTC). No daily signal exits.
- **Limits:** SPEC defaults (≤ 5 positions, ≤ 20% each, ≤ 90% gross, 5% daily-loss entry halt, 15% drawdown flatten-and-halt).
- **Drawdown halt reset:** the operator reset is modeled as happening at the start of each calendar quarter, which is every fold start.
- **No-trade band:** 20%.
- **New entries:** only for names in U_d. A held name that leaves U_d may be kept or sold, but not increased.
- **Weights:** every selected name gets **0.18** (= 90% / 5). Fewer than 5 names leaves the rest in cash. Every hypothesis names at most 5 assets itself; the engine never has to truncate.

**Cost cases**
- base: 0.60% fee + 0.20% slippage per side
- stress: 2× base
- delay: base costs with execution one bar later. This is a sensitivity only.

**Benchmarks** (`edge.benchmarks`, same engine and cost case, SPEC limits not applied)
- BTC buy-and-hold, bought at the first OOS bar.
- Equal-weight U_d, rebalanced at each month-end close.

**Parameter selection (walk-forward)**
- For each fold, every grid cell is run over that fold's 12-month train window at base cost. The cell with the highest train Sharpe (ties go to the first in grid order) trades that fold's test window.
- The concatenated OOS series of those selections is the hypothesis's **primary trial**.
- Every grid cell is also run as a fixed-parameter OOS trial and reported.

**Edge bar** (SPEC §7.3), evaluated on the primary trial
1. **Fold wins:** fold Sharpe > both benchmarks' fold Sharpe (strictly) in ≥ 12 of 20 folds. Sharpe is annualized √365 with rf = 0; a zero-variance series counts as Sharpe 0.
2. **Drawdown:** aggregate OOS max drawdown ≤ BTC buy-and-hold's max drawdown over 2021-07-01 → 2026-06-30.
3. **Cost stress:** criteria 1 and 2 still hold under 2× costs, with benchmarks also at 2×.
4. **Multiple testing:**
   - p-value: one-sided paired stationary bootstrap (mean block 7 days, 10,000 resamples, seed 0) on the daily base-cost OOS returns, against the benchmark with the higher aggregate OOS Sharpe.
   - Correction: Holm across the **family of all 11 base-cost trials** (8 fixed grid cells + 3 primary trials). Holm-adjusted p must be < 0.05.
   - Also reported, non-gating: the Deflated Sharpe Ratio, using N = 11 and the variance of the trial Sharpes.

**Verdicts** (SPEC §7.4)
- **Edge:** criteria 1–4 all pass.
- **Inconclusive:** criteria 1 and 2 pass at base cost but criterion 3 or 4 fails.
- **No edge:** otherwise.

**Trial accounting**
- Every run (grid cells × {base, stress, delay}, the primary trials, benchmarks, train-window selection runs) is appended to `research/trials.csv`.
- Only base-cost OOS strategy trials form the Holm family: 11 members.

**Change control**
- Any code fix after this commit that changes how a rule is implemented is logged in §3 with its reason.
- A rule may not be changed after seeing results. A new rule would be a new hypothesis, and it would increase the family size.

### H1 — BTC trend gate (market time-series momentum)
- **Signal at d:** g = 1 if BTC-USD close_d > mean(BTC-USD close over the L bars ending d); otherwise g = 0.
- **Book:**
  - g = 1 → hold portfolio P at 0.18 per name.
  - g = 0 → hold nothing.
- **Grid (4 cells):** L ∈ {50, 100} × P ∈ {`btc` = {BTC-USD}; `top5` = the 5 names with the highest 30-day ADV in U_d}.
- **Prediction:** at least one variant passes the drawdown criterion. It likely loses fold Sharpe to BTC in bull quarters [INFERENCE].
- **Note:** Sharpe is scale-invariant, but drawdown is not. The `btc` cell holds ≤ 18% of equity, so its drawdown pass would be mechanical. This is disclosed and does not by itself make an edge.

### H2 — Per-asset trend on liquid names
- **Eligibility at d:** name i in U_d is eligible if all hold:
  - close_i,d > SMA_L,i,d
  - close_i,d > close_i,d−28
  - the name has all L + 28 closes needed
- **Selection:** the (up to) 5 eligible names with the highest 30-day ADV, at 0.18 each.
- **Grid (2 cells):** L ∈ {20, 50}.
- **Prediction:** its turnover sits between H1's and H3's. The main risk is whipsaw costs [INFERENCE].

### H3 — Cross-sectional trend composite (CTREND-lite, fixed weights, no ML)
- **Score at d:** for every name in U_d that has 100 valid closes ending d, score_i = mean over L ∈ {5, 10, 20, 50, 100} of the cross-sectional percentile rank of ln(close_i,d / SMA_L,i,d).
- **Selection:**
  1. Keep currently held names whose score is in the top 50% of scored names.
  2. Fill the remaining slots, up to 5, with the highest-scored names not held.
  3. Weight 0.18 each.
- **Grid (2 cells):** cadence ∈ {`weekly` = every Sunday decision, `biweekly` = Sundays where ((d − 2020-07-05) in days / 7) is even}. On non-rebalance Sundays there are no trades.
- **Prediction:** highest turnover of the three. The long leg may just be a high-beta tracker, and it is the most cost-sensitive [INFERENCE].

### Not pre-registered (and why)
- **Loser-avoidance (literature H4):** it needs an equal-weight book of the whole universe, which breaks the 5-position limit.
- **Plain cross-sectional momentum (literature H5):** low prior. It would spend multiple-testing budget.
- **Volume-spike breakout (from `03_candidates_l1_payments.md`):** no published prior. It is kept as a candidate for a future, separately pre-registered study.
