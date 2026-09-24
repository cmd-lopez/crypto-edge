# SPEC — crypto-edge

Status: **APPROVED by operator 2026-09-23 (Phase 1 gate); all [DECISION] items accepted as written**
Date: 2026-09-23 · Branch: `phase-1-spec`

Tags used below: **[MEASURED]** = reproduced by a command in this repo; **[SOURCE]** = primary/secondary source, access date 2026-09-23; **[INFERENCE]** = reasoning, not verified; **[DECISION]** = choice proposed here, needs operator approval.

---

## 1. Goal

1. First, find out whether a real, testable edge exists in long-only spot crypto on a 1–4 week horizon, after realistic retail costs.
2. Only if one exists, build the smallest reliable system that trades it: paper first, then a capped live stage.
3. This is a portfolio and learning project first. A well-supported "no edge found" verdict counts as success.

Out of scope, permanently: leverage, margin, perpetuals, futures, options, lending, staking, shorting, intraday or microstructure trading, and any model output that controls a threshold, size, limit, or side effect.

## 2. Confirmed parameters

| Parameter | Value | Notes |
|---|---|---|
| Venue | Coinbase Advanced Trade (primary), Kraken Pro (fallback) | §3 |
| Jurisdiction | Maryland, US | Every disposal is taxable (§9) |
| Instruments | Spot, long-only, no leverage | |
| Universe | Up to 50 assets, point-in-time, stablecoins/wrapped excluded, 30-day venue ADV ≥ $5M | §4: the ADV filter is the binding constraint |
| Capital | Paper through Phase 5. Live $250–$500 | No increase without explicit operator approval |
| Max drawdown | 15% of bot equity, peak-to-trough | Halt entries and flatten (§6.2) |
| Max position | 20% of bot equity per asset | |
| Max daily loss | 5% of bot equity | Halt entries until next UTC day |
| Max open positions | 5 | |
| Min cash buffer | 10% of bot equity in USD/USDC | So gross exposure ≤ 90% |
| Horizon | 1–4 weeks. Daily evaluation at the 00:00 UTC close. Weekly rebalance Monday 00:00 UTC | Risk exits on any daily evaluation (§6.1) |
| Benchmarks | BTC buy-and-hold; equal-weight, monthly-rebalanced basket of the point-in-time universe | Both charged the same cost model |
| Paper period | ≥ 60 days, extended until it contains a ≥ 50% change in BTC 30-day realized volatility | Defined precisely in §8 |
| Data budget | ≤ $50/month; free sources preferred; paid sources need approval | Planned spend: $0 (§5) |

## 3. Venue constraints

### 3.1 Availability for a Maryland account
- **Coinbase Advanced Trade: available for spot trading [SOURCE].** The only Maryland-specific restriction found is on staking: a state cease-and-desist has blocked staking since 2023-06 (Coinbase public-policy page, https://www.coinbase.com/public-policy/advocacy/staking-action-dismissals; CryptoSlate 2023-11-02). Staking is out of scope, so this does not matter here.
- **Kraken: available in Maryland [SOURCE].** Kraken excludes New York and Maine (https://support.kraken.com/articles/quick-start-for-clients-in-the-united-states).
- **Still unconfirmed: the operator's actual account.** Needed before Phase 6, not before. Operator action: create a **View-only** CDP key, then call `GET /api/v3/brokerage/key_permissions` (documented response fields: `can_view`, `can_trade`, `can_transfer`, `portfolio_uuid`) and `GET /api/v3/brokerage/transaction_summary` to read the account's real fee tier.

### 3.2 Fees (primary sources)
| Venue | Tier | Maker | Taker | Source |
|---|---|---|---|---|
| Coinbase Advanced (US) | entry tier (< $10K 30-day volume) | 0.50% | 0.90% | New schedule effective 2026-09-16 (Investing.com, 2026-09-16). Coinbase's help page defers to the logged-in fee page |
| Kraken Pro | Tier 1 ($0+) | 0.40% | 0.80% | https://www.kraken.com/features/fee-schedule (cross-platform tiers since 2026-07-09) |
| Kraken Pro | Tier 2 ($2.5K+ 30-day volume) | 0.30% | 0.60% | same |

**Cost model [DECISION]:**
- Base case: 0.60% fee plus 0.20% slippage per side, so 1.60% per round trip.
- Stress case: both doubled, so 1.20% + 0.40% per side, or 3.20% per round trip.
- On Coinbase's current schedule, 0.60% is conservative only if at least 75% of filled notional pays the maker rate (0.5m + 0.9(1−m) ≤ 0.6 ⇒ m ≥ 0.75).
- If every fill paid the 0.90% taker rate, total cost would be 1.10% per side. The 2× stress case (1.60% per side) is higher than that, so it covers an all-taker world.
- Phase 5 measures the maker share. If it falls below 75%, base costs are revised upward and the edge re-tested.

Note: Kraken is 0.10% per side cheaper at both entry-tier rates. That is small compared with the modeled costs, and Coinbase's public API has a data advantage for survivorship-safe history (§4). Coinbase stays primary.

### 3.3 API and key security
- Market data comes from the unauthenticated public endpoints: Coinbase Exchange `/products` and `/products/{id}/candles`, 300 candles per request, about 10 requests/second per IP [SOURCE, and exercised in §4].
- Live trading keys:
  - Permissions: View + Trade only. **Transfer disabled.**
  - IP allowlist required.
  - Stored in environment variables or the OS keychain, never in git or logs.
  - At startup the bot calls `key_permissions` and refuses to run if `can_transfer == true`.

## 4. Universe (point-in-time)

### 4.1 Definition [DECISION]
At each decision date *t*, using only data that closed at or before *t*:
1. **Candidates:** Coinbase spot products quoted in USD, **including products later delisted**, that have at least 30 daily candles before *t*.
2. **Exclusions:** stablecoins and wrapped or pegged-derivative assets. The exclusion list is kept in code; each entry has a date and a reason.
3. **Liquidity:** 30-day mean of daily Coinbase USD dollar volume (volume × close) ≥ $5M. Days with no candle count as $0.
4. **Rank:** by 30-day Coinbase dollar volume; keep the top 50.

### 4.2 Why rank by volume instead of market cap
- Point-in-time market-cap history is not available within budget:
  - CoinGecko's free Demo plan gives 1 year of daily history. Basic ($35/month) gives 2 years. Full history starts at Analyst, $129/month (https://www.coingecko.com/en/api/pricing).
  - Historical supply is Enterprise-only.
  - CoinMarketCap's historical listings endpoint is on paid tiers only [SOURCE, secondary].
- The ranking choice rarely matters. **[MEASURED]** Since 2021-01, only **10 of 69** month-ends had more than 50 assets passing the $5M ADV filter. In the other 59, every eligible asset is in the universe whichever rank is used.
- **Validation (Phase 2):** for the trailing 365 days, where free CoinGecko data exists, report the monthly overlap between the volume-ranked universe and a market-cap-ranked universe.

### 4.3 Feasibility evidence [MEASURED]
Reproduce with: `uv run --with httpx --with pandas research/00_universe_feasibility.py`. Output: `research/results/00_universe_feasibility.csv`.

- Coinbase Exchange public `/products` returns 838 products, 324 of them `delisted`. Among USD-quoted products, 86 are delisted.
- Candles are still served for delisted products. Checked: UST-USD, MIR-USD, RGT-USD, KEEP-USD, NU-USD, TRIBE-USD, OMG-USD. This is the basis for survivorship safety.
- After exclusions: 470 USD products, 77 of them delisted.
- Month-end count of assets clearing $5M ADV since 2021-01: min **9**, median **33**, max **81**. In 2026 the range is 15–28. The 2026-09 value is as of 2026-09-23.
- The first month-end that closes 3 consecutive months with at least 10 eligible assets is **2020-09-30**.
- **Implication:** the realistic universe holds about 10–80 names, usually 15–45, not 50. The equal-weight benchmark and cross-sectional hypotheses have to live with that breadth.

### 4.4 Known residual biases
- Coinbase may have removed some very old delisted products from `/products`. Unknown; the probe cannot detect it [INFERENCE: low impact, because the pre-2020 universe is only 3–15 products].
- Volume counts only USD-quoted books. USDC- and USDT-quoted volume is ignored, which understates liquidity.
- Delisting in the backtest: a held asset whose candles stop is exited at its last close minus an extra **10%** haircut [DECISION]. Delistings are reported as their own line item.

## 5. Data sources (planned spend: $0/month)

| Need | Source | Point-in-time? | Use |
|---|---|---|---|
| Daily OHLCV, listings, delistings | Coinbase Exchange public API | Yes, as bars close | Backtest and live |
| Market cap, last 365 days | CoinGecko Demo (free) | Yes, 1 year only | Universe validation, research |
| TVL, fees, revenue, stablecoin supply | DefiLlama free API | **No**: history can be backfilled or revised | Research narrative. Any backtest feature from it gets a 7-day lag and is flagged as revision-prone |
| Unlock schedules | Tokenomist (formerly Token Unlocks) public pages | Schedule known in advance, but revisions are not archived | Research only, unless point-in-time snapshots are captured going forward |
| Funding and open interest | A derivatives venue with public market-data endpoints reachable from the US, chosen in Phase 2 | Yes | Regime research. **No VPN or ToS circumvention** of geo-blocked venues |

## 6. Trading rules (constraints for later phases)

### 6.1 Timing
- **Signal:** computed from the daily bar that closes at 00:00 UTC.
- **Backtest fill:** next bar's open (the same instant as that close) plus slippage.
- **Reported sensitivity, not a gate:** a one-day execution delay. If that flips the verdict, it is disclosed as look-ahead risk.
- **New entries:** only at the Monday 00:00 UTC rebalance.
- **Exits on any daily evaluation [DECISION]:** `risk_state == reduce`, `regime == crisis`, a hard-limit breach, or a thesis invalidation condition.
- **Exits only at the weekly rebalance:** calibrated probability < 0.52. This keeps signal turnover on the weekly clock.
- **Maximum hold [DECISION]:** at the first Monday on or after day 28, a position must pass the entry gate again or be exited.

### 6.2 Risk limits
All of these are enforced in deterministic code and checked before every order.
- **Equity:** marked with the latest close for decisions. Before each order it is re-marked at the latest ticker price.
- **Drawdown:** measured from the peak of daily equity marks, net of fees.
- **At the 15% drawdown limit [DECISION]:**
  1. Halt all entries.
  2. Flatten every position at the next daily evaluation, using limit orders with the Phase 3 timeout-and-fallback policy.
  3. Stay halted until the operator manually resets. There is no automatic resume.
- **Daily loss:** measured against equity at 00:00 UTC. Breaching 5% halts entries until the next 00:00 UTC.
- **Exposure:** the 10% cash buffer caps gross exposure at 90%. Five positions at the 20% cap would need 100%, so per-position sizes are scaled down to fit.
- **Stale data:** halt entries if the newest bar is more than 26 hours old or any required feature is missing.

### 6.3 The exact trading pipeline must itself pass the edge bar
Phase 2 tests rule-based hypotheses. Phase 4 adds a classifier, calibration, quarter-Kelly sizing, and the entry gate.
- **Before paper trading,** the full Phase 4 decision pipeline is backtested walk-forward against the same §7.3 bar. Its trials are added to the same trial ledger.
- **If the pipeline fails and the rules alone passed,** the system trades the rules alone, with the classifier dropped.

## 7. Research protocol (Phase 2)

### 7.1 Pre-registration
- Hypotheses (1–3), parameter grids, and evaluation code paths are written to EDGE_REPORT.md and committed **before** any backtest runs.
- That commit hash is quoted in the results.

### 7.2 Walk-forward design
- **Folds:** 12-month train, 3-month test, rolling in 3-month steps.
- **Data window:** 2020-07 to 2026-09.
- **Fold count:** about 20 out-of-sample folds [INFERENCE: exact count computed in Phase 2].
- **Rebalancing:** weekly. Features and universe are point-in-time only.
- **Sharpe:** daily net returns annualized by √365, with the risk-free rate set to 0 and stated as such.
- **Trial ledger:** every backtest run is appended automatically to `research/trials.csv`, recording hypothesis, parameters, fold, cost case, and git hash. Nobody edits it by hand.

### 7.3 Edge bar
A hypothesis shows an edge only if **all** of these hold, out-of-sample and net of costs:
1. **Beats both benchmarks:** strategy Sharpe beats both benchmarks' Sharpe in at least 60% of test folds.
2. **Drawdown:** aggregate out-of-sample max drawdown is no worse than BTC buy-and-hold's over the same span.
3. **Cost stress:** criteria 1 and 2 still hold with fees and slippage doubled.
4. **Multiple-testing correction [DECISION on method]:**
   - Test: one-sided stationary block bootstrap (Politis–Romano, mean block length 7 days, 10,000 resamples) of the aggregate out-of-sample daily Sharpe difference against the stronger benchmark.
   - Correction: Holm–Bonferroni at family-wise α = 0.05.
   - Family size: the **total number of trials in the ledger**, across all hypotheses and parameter sets, not just the final candidates.
   - Also reported, not gating: the Deflated Sharpe Ratio (Bailey & López de Prado, 2014).

### 7.4 Verdicts
- **Edge:** criteria 1–4 all pass.
- **Inconclusive:** criteria 1 and 2 pass at base cost, but criterion 3 or 4 fails. Also inconclusive if fewer than 8 test folds are available.
- **No edge:** anything else.

### 7.5 Reported, not gating
- One-day execution delay.
- After-tax illustration (§9).
- Turnover.
- Exposure to BTC beta.
- Delisting losses.
- Per-regime breakdown.

## 8. Paper period definition
- **Realized volatility:** σ₃₀(d) = annualized standard deviation of 30 daily log returns of Coinbase BTC-USD ending at day *d*.
- **Trigger:** the paper period contains a qualifying volatility change if, for some day *d* inside it, σ₃₀(d) / σ₃₀(d−30) ≥ 1.5 or ≤ 0.5.
- **End condition:** paper ends at the later of day 60 and the first day that trigger is met.
- **If not met by day 180,** the operator decides whether to extend or stop [DECISION].

## 9. Tax records (Maryland, US)
- **Lot records:** every fill creates or consumes lot records with acquisition timestamp, quantity, cost basis (fees included), disposal timestamp, proceeds (net of fees), holding-period class, and venue fill IDs. They export as CSV.
- **Lot method:** FIFO per account [DECISION: IRS default absent specific identification; not tax advice]. Records are reconciled against the venue's year-end tax forms.
- **Tax treatment [INFERENCE: verify with a tax professional]:** with a 1–4 week horizon, essentially every gain is short-term and taxed as ordinary income. Buy-and-hold BTC may qualify for long-term rates. Maryland state and county income tax also applies.
- **After-tax comparison:** reported as an illustration using operator-supplied marginal rates, labeled as an estimate. It is **not** part of the edge gate.

## 10. Success criteria

**Engineering**
- All required tests pass, verified by fresh output.
- A look-ahead test runs in CI: a GitHub Actions workflow committed locally, plus an identical local `make ci`. Nothing is pushed without approval.
- Any backtest reproduces from a single command with pinned dependencies and cached raw data hashes.
- ARCHITECTURE section in README.md and PLAN.md.

**Research**
- Hypotheses are stated before testing (git-verifiable).
- The trial count and correction method are reported.
- EDGE_REPORT.md reaches a clear per-hypothesis verdict.

**Trading** (only if an edge is found)
- Paper results fall within the backtest's expected range. The range is a bootstrap 5th–95th percentile band of 60-day returns and drawdown, computed before paper starts.
- Live results are tracked against paper weekly.

## 11. Kill criteria
1. No hypothesis passes §7.3. Stop after Phase 2 and report.
2. The full pipeline fails §7.3 (§6.3) and no rules-only fallback passes. Stop.
3. Paper Sharpe is below 0 over the full paper period, or paper drawdown exceeds 15%. Stop.
4. Live weekly return deviates from paper weekly return by more than 2σ of paper weekly returns for 3 consecutive weeks. Stop live and investigate.
5. Any hard limit is found to be bypassable by model output. Stop until fixed and re-reviewed.

## 12. Definition of done (per phase)

| Phase | Done when |
|---|---|
| 1 Frame | SPEC.md approved by operator |
| 2 Edge | EDGE_REPORT.md: pre-registered hypotheses, walk-forward results, trial count and correction, per-hypothesis verdict, "WHAT COULD I BE WRONG ABOUT?". Operator decides whether to continue |
| 3 Architecture | Framework evaluation (Freqtrade/FreqAI, NautilusTrader, Hummingbot) and PLAN.md with file paths, interfaces, tests, failure modes. Approved |
| 4 Build | All required tests (look-ahead, risk, decision parsing, sizing, execution, tax log) pass on fresh run; §6.3 pipeline backtest done; code review complete |
| 5 Paper | §8 period complete; returns, drawdown, slippage, fill rate, turnover, calibration (Brier score, reliability curve) compared to backtest; divergences explained; kill criteria applied |
| 6 Live | RUNBOOK.md; alerts at 80% of each limit; live-vs-paper tracking; capital unchanged without approval |

## 13. Gate check (final_check)
- **Organic or incentive-driven edge?** Unknown; no hypothesis exists yet. Incentive-driven flows (unlocks, emissions, listings) are treated as candidate *catalysts* whose persistence must be shown out-of-sample.
- **Catalyst priced in?** Tested only by the out-of-sample bar. Research alone cannot answer it.
- **Does value accrue to the token?** Assessed per asset in Phase 2 research. Not a backtest input unless point-in-time data exists.
- **Beats benchmarks after fees, slippage, and taxes?** Fees and slippage are in the gate, and doubled. Taxes are illustrative only. The short-term vs long-term tax gap favors buy-and-hold BTC [INFERENCE], so this bar is harder than the pre-tax gate shows.
- **Any hard limit delegated to a model?** No, by spec: §6.2 and kill criterion 5.
- **Look-ahead, survivorship, overfitting?**
  - Look-ahead: CI test, a strict causal feature timestamp, and the one-day-delay sensitivity.
  - Survivorship: delisted products included (measured).
  - Overfitting: trial ledger plus Holm correction over all trials.

## WHAT COULD I BE WRONG ABOUT?
- **Costs.** A 1.6% round trip is a very high bar for 1–4 week holds. Most plausible signals may simply not clear it. That would be a real finding, not a failure. The 0.60% fee is also only conservative if at least 75% of fills are maker, which is unmeasured.
- **Fees.** The Coinbase fee figures come from a news report of a 2026-09-16 change. The logged-in fee page is authoritative and was not read. Kraken figures come from Kraken's own page.
- **Universe proxy.** Coinbase volume rank is not market-cap rank. Venue volume includes listing-day spikes and incentive-driven activity. The 365-day overlap check covers only the most recent regime.
- **Deleted history.** Coinbase may have removed old delisted products from `/products`. The survivorship fix cannot detect deletions.
- **Statistical power.** About 20 test folds of about 91 days each give low power. A true small edge will likely show up as "inconclusive", and Holm over many trials makes that more likely. This is the conservative direction.
- **Data window.** The history is mostly one market structure (2020–2026, post-DeFi, ETF era). Regime diversity is limited.
- **Out-of-sample isn't unseen.** The operator and I have both seen this price history, so the walk-forward split is not truly unseen data. Pre-registration reduces this risk but does not remove it.
- **Tax.** The tax statements are general and not professional advice.
