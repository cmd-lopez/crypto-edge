# EDGE_REPORT — Phase 2

Status: **COMPLETE. Verdict: NO EDGE for H1, H2 and H3.**
- §1–2 (pre-registration) were committed at `c24ad22` before any hypothesis touched real prices.
- §3–6 were added after the runs. The canonical run is git `9446793`.

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

---

## 3. What happened after pre-registration (change control)

| Commit | Event |
|---|---|
| `c24ad22` | Pre-registration (§1–2). |
| `d216e6e` | Implemented H1–H3 exactly per §2, plus the runner. **Run 1**: 215 ledger rows with `git_hash=d216e6e`. Verdicts: no edge ×3. |
| — | Independent code review (read-only reviewer agent). No critical findings. Look-ahead was independently confirmed absent: perturbing future prices and volumes left all earlier decisions identical, including through the walk-forward switching. It found five confirmed minor issues, listed below. |
| `9446793` | All five fixed, each with a failing-first test. **Run 2 is canonical**: 215 ledger rows with `git_hash=9446793`. Verdicts: no edge ×3, unchanged. |

Fixes in `9446793`:
1. **Universe:** a product with no bar on d is excluded from U_d. Before, a delisted name stayed eligible for up to about 29 days on its trailing ADV. SPEC §4.1 requires a tradeable product.
2. **No-trade band:** it can no longer hold a position above the 20% cap. Before, the band could leave a position at 0.216.
3. **Unsellable holdings:** if a held name has no bar on execution day, new entries are trimmed so that ≤ 5 positions and ≤ 90% gross still hold, and the sale is retried on the next bar.
4. **H3 fill:** step 2 now excludes *every* held name, per the §2 text "not held". Before, bottom-half held names could be re-selected when ≤ 8 names were scored. This was a deviation from the pre-registration and is corrected to match it.
5. **Equal-weight benchmark:** it now uses the same 20% no-trade band as the strategies. Without it the benchmark paid more cost, which favored the strategies.

Sensitivity disclosed:
- **H1 is fragile.** The fixes moved H1's primary out-of-sample Sharpe from **+0.197 (run 1) to −0.147 (run 2)**.
- **Cause:** 3 of 20 per-fold walk-forward selections flipped (folds 8, 10, 19) because train Sharpes of near-tied cells changed slightly.
- **Reading:** that a tiny implementation change can swing aggregate Sharpe by 0.34 shows that walk-forward selection among H1's cells is choosing noise [INFERENCE]. This counts *against* a robust edge. Neither run passes the bar.

Interpretation note on multiple testing:
- The pre-registration fixed the Holm family at the **11 base-cost out-of-sample strategy trials**. SPEC §7.3 says "the total number of trials in the ledger" (the ledger holds 430 rows, including train-window, stress, delay, benchmark and diagnostic runs).
- The choice does not matter. **The smallest raw p-value of any trial is 0.263, so nothing passes even with no correction at all.**

Post-report test hardening (packaging, 2026-09-24):
- Mutation testing showed the engine look-ahead unit test did not catch a one-bar leak.
- **Cause:** it rebalanced weekly and the cut day was not a decision day.
- **Fix:** the test now rebalances daily with continuous weights. It fails on an injected one-bar leak and passes on the unmodified engine.
- **Engine code is unchanged,** so all Phase 2 results stand. The reviewer's independent end-to-end perturbation check had already found no leak.

## 4. Results (run 2, `9446793`; out-of-sample 2021-07-01 → 2026-06-30, 20 folds, 1,826 days) [MEASURED]

Reproduce: `uv run python -m edge.fetch && uv run python -m edge.run_phase2`, then `uv run python research/02_phase2_diagnostics.py`.
Outputs are in `research/results/phase2/`:
- `verdicts.json`
- `trials_summary.csv`
- `fold_sharpes.csv`
- `oos_daily_returns.csv`
- `train_selection_H*.csv`
- `diagnostics.json`
- `manifest.json`: sha256 of every cached candle file.

### 4.1 Benchmarks (net of the same costs)
| | Sharpe | Max drawdown | CAGR | Notes |
|---|---|---|---|---|
| BTC buy-and-hold, base | **0.472** | 76.7% | +11.6% | One entry trade. The stronger benchmark in every case |
| Equal-weight PIT universe, monthly, base | −0.186 | 94.5% | −35.1% | 3 delistings written off. Universe size 7–50 (median 32) |

Engine cross-check (zero cost, independent vectorized reimplementation):
- BTC: engine and vectorized both give +74.641%; they agree to within 1e-14.
- Equal-weight: engine −85.766% vs vectorized −85.786%. The 0.02 pp gap comes from positions that could not trade on a rebalance day.

### 4.2 Primary (walk-forward) trials: the edge bar
| | C1 fold wins, base (need ≥ 60%) | C1, 2× cost | C2 max DD vs BTC 76.7% (base / 2×) | Raw p vs BTC | Holm p | DSR | **Verdict** |
|---|---|---|---|---|---|---|---|
| H1 trend gate | 25% ✗ | 20% ✗ | 51.1% ✓ / 57.4% ✓ | 0.880 | 1.0 | 0.040 | **no edge** |
| H2 per-asset trend | 30% ✗ | 20% ✗ | 72.4% ✓ / 66.9% ✓ | 0.947 | 1.0 | 0.013 | **no edge** |
| H3 trend composite | 20% ✗ | 20% ✗ | 74.6% ✓ / 88.5% ✗ | 0.968 | 1.0 | 0.006 | **no edge** |

Out-of-sample Sharpe (base / 2× / one-day delay):
- H1: −0.147 / −0.330 / −0.299
- H2: −0.339 / −0.298 / −0.281
- H3: −0.479 / −0.971 / −0.585

### 4.3 All fixed cells (base cost; each is a Holm-family member)
| Cell | Sharpe | Max DD | Fold wins | Raw p | Turnover/yr | Avg gross exposure | Costs paid (fraction of starting equity) |
|---|---|---|---|---|---|---|---|
| H1 L=50 btc | 0.510 | 9.2% | 20% | 0.458 | 0.9× | 9% | 0.08 |
| H1 L=50 top5 | **0.765** | 46.4% | 35% | **0.263** | 4.9× | 37% | 1.01 |
| H1 L=100 btc | 0.301 | 12.4% | 25% | 0.679 | 0.5× | 9% | 0.04 |
| H1 L=100 top5 | 0.187 | 54.7% | 30% | 0.716 | 3.9× | 30% | 0.36 |
| H2 L=20 | −0.096 | 56.6% | 25% | 0.886 | 8.6× | 28% | 0.41 |
| H2 L=50 | −0.226 | 66.3% | 20% | 0.915 | 7.3× | 32% | 0.31 |
| H3 weekly | −0.335 | 69.0% | 25% | 0.933 | 6.8× | 25% | 0.30 |
| H3 biweekly | −0.153 | 62.5% | 35% | 0.894 | 5.8× | 30% | 0.33 |

The best-looking cell is H1 L=50 top5, with aggregate Sharpe 0.765 vs BTC's 0.472. It still fails:
- Fold wins are 35%, against the 60% bar.
- Raw p is 0.263.
- At 2× cost its Sharpe is 0.287, below BTC's.
- Picking it after the fact would be exactly the selection bias the protocol exists to prevent.

### 4.4 Diagnostics (post-hoc, not pre-registered, not in the Holm family)
- **Gross, zero-cost primaries:**
  - H1 Sharpe −0.034, H2 +0.103, H3 −0.312, against BTC gross 0.475.
  - Gross fold-win rates vs gross benchmarks: 30%, 40%, 20%.
  - **The failure is not a cost story. The signals do not beat buy-and-hold BTC even before costs.** Costs make it worse: H2 and H3 turn over 6–9× a year, which costs 25–40% of starting equity across the window.
- **Split by BTC trend** (BTC above its 200-day SMA at the prior close):
  - Every trend rule does worse than BTC in BTC-uptrend days. For example, H1 primary Sharpe is 0.30 vs BTC 0.80.
  - In downtrend days, H2 and H3 still lose, with Sharpe −0.19 and −0.51.
- **Drawdown breaker:** it fired 13–20 times per alt-basket trial. With the quarterly reset it re-arms each quarter, so drawdown compounds across quarters. This explains aggregate drawdowns of 50–75% despite a 15% breaker.
- **Untouched holdout, 2026-07-01 → 09-22** (descriptive; parameters chosen on the prior 12 months):
  - BTC: Sharpe 4.06, +42.6%.
  - Equal-weight: Sharpe 4.17, +66.7%.
  - H1 L=100 top5: 2.70 (+22.2%).
  - H2 L=20: 2.44 (+30.0%).
  - H3 weekly: 3.36 (+60.1%).
  - All positive, all below both benchmarks. This is consistent with the out-of-sample verdict: one quarter, no inference.

## 5. Verdicts

| Hypothesis | Verdict | Reasons |
|---|---|---|
| **H1** BTC trend gate | **NO EDGE** | Fails C1 (25%, and 20% at 2× cost). Its drawdown pass (51% vs 77%) comes from being out of the market (23% average exposure), not from better risk-adjusted return: Sharpe −0.15 vs BTC 0.47. p = 0.88. Selection is unstable (§3). |
| **H2** per-asset trend | **NO EDGE** | Fails C1 (30% / 20%). Negative net Sharpe. Gross Sharpe of 0.10 means the signal is absent before costs, too. p = 0.95. |
| **H3** trend composite | **NO EDGE** | Fails C1 (20% / 20%), and C2 at 2× cost (88.5%). Negative even gross (−0.31). p = 0.97. |

**Phase 2 conclusion:** no pre-registered hypothesis shows an edge. Per SPEC kill criterion 1 and the core principle "edge before infrastructure", **the trading system should not be built.** Phases 3–6 do not proceed unless a new, separately pre-registered study passes the bar.

### 5.1 Recommended next steps (operator decision)
1. **Stop here and package** (recommended). The deliverable is the research harness plus a negative result. The harness is TDD'd and reviewed, with a PIT survivorship-safe universe, walk-forward, trial ledger and multiple-testing correction. Write README.md for reviewers; archive the branch.
2. **One new pre-registered study, with a fresh Holm family and an explicit trial budget.** Candidates from the research: volume-spike breakout (`03_…md`), and loser-avoidance re-specified within the 5-position limit. Expect low power: 20 folds, and a 60% fold-win bar against BTC.
3. **Revisit the constraints, not the data.** Two constraints shape the result:
   - The 20%-per-asset cap forces an alt-heavy book, and in 2021-07..2026-06 the PIT alt universe lost 86% equal-weighted.
   - The "beat BTC Sharpe in 60% of folds" bar is strict.
   Relaxing either is a SPEC change and must happen *before* any new test, never after seeing results.

Not recommended: tuning H1–H3 further on this data, or promoting the H1 L=50 top5 cell after the fact.

## 6. Final check (SPEC §13)
- **Organic or incentive-driven edge?** None found. The trend rules tested are behavioral/organic in origin, and they did not survive.
- **Catalyst already priced in?** Not applicable to the rule tests. §1.2 notes that most current "disconnects" are momentum episodes, and momentum did not pay here.
- **Does value accrue to the token?** Assessed per asset in §1.2. It was not testable point-in-time (§1.4).
- **Beats both benchmarks after fees, slippage and taxes?** No, not even before fees (gross diagnostic). Taxes would only widen the gap: the strategies realize short-term gains, while BTC buy-and-hold defers.
- **Any hard limit delegated to a model?** No. All limits are enforced in `edge.engine`, tested (`tests/test_engine.py`), and reviewed.
- **Look-ahead, survivorship, overfitting?**
  - Look-ahead: a perturbation test in the unit suite plus the reviewer's end-to-end perturbation.
  - Survivorship: delisted products included; 3 write-offs in the benchmark; universe requires a bar on d.
  - Overfitting: pre-registration, an 11-trial family, and the ledger. The result is negative, so overfitting could not have produced a false positive here.

## WHAT COULD I BE WRONG ABOUT?
- **"No edge" is narrower than it sounds.** It covers three trend rules under these constraints (≤ 5 names, ≤ 20% each, weekly, Coinbase USD). It says nothing about event-driven, cross-venue, or fundamental strategies, which could not be tested honestly with free data (§1.4).
- **The constraints may decide the outcome.** With a 20% cap, beating BTC's Sharpe requires alts to add value, and over 2021–26 the PIT alt universe lost 86% equal-weighted. A BTC-dominant trend overlay was not testable within the SPEC (the H1-btc cells hold only 18%). Its Sharpe of 0.51 at L=50 hints that it might match BTC, with p = 0.46.
- **Fold-level Sharpe over 91 days is noisy,** and "strictly beat both benchmarks in ≥ 60% of folds" is a demanding bar. A true modest edge could fail it. Here, though, aggregate Sharpe and p-values fail too, so the verdict does not hinge on criterion 1.
- **The drawdown-breaker reset assumption** (operator reset every quarter) shapes criterion 2. A never-reset breaker would sit in cash after the first breach. Different policies would change the drawdown numbers, but not the Sharpe-based failures.
- **Fills at the next open with 0.2% slippage** may be optimistic for the smallest names at 00:00 UTC. The strategies already fail gross, so this only strengthens the verdict.
- **The data comes from a single venue** (Coinbase). Prices were not cross-checked against another source.
- **The universe ignores USDC/USDT-quoted volume.** Some delisted products may have been removed from `/products` entirely (SPEC §4.4).
- **Bugs may remain.** Five were found and fixed after run 1. Run 1 → run 2 changed H1's Sharpe by 0.34 without changing any verdict. The engine matches an independent vectorized computation for the benchmarks, but not every strategy path is cross-checked that way.
- **Hindsight.** I (the analyst) broadly know crypto's 2021–24 history. That may have shaped which hypotheses were chosen. Here it favored trend rules, which failed, so it did not produce a false positive. It still means the out-of-sample split is not a truly unseen test.
- **One market era.** Five years, dominated by the 2022 bear market and persistent alt underperformance, gives low power and limited regime diversity. The current regime (§1.1, early uptrend) could favor trend rules going forward. This data cannot show that, and assuming it would be speculation.
