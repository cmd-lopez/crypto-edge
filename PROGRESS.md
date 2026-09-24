# PROGRESS

## Current phase
Phase 1 (Frame). SPEC.md is drafted on branch `phase-1-spec` (worktree `.worktrees/phase-1-spec`). **Blocked: waiting for operator approval of SPEC.md.**

## Process note
The superpowers skills (using-superpowers, brainstorming, writing-plans, using-git-worktrees, TDD, etc.) are not installed in this environment. Their intent is followed manually, and each use is announced in the session.

## Decisions (proposed in SPEC.md, pending approval)
- **Venue:** Coinbase Advanced is primary. Kraken is the fallback; its fees are about 0.10% per side lower, but Coinbase's public API is better for survivorship-safe history.
- **Universe rank proxy:** 30-day Coinbase USD dollar volume, because free point-in-time market-cap history is not available. Checked against CoinGecko market cap over the trailing 365 days.
- **Cost model:**
  - Base: 0.60% fee + 0.20% slippage per side.
  - Stress: both doubled, which is higher than an all-taker scenario at 0.90% + 0.20%.
- **Multiple-testing correction:** Holm–Bonferroni over every trial in the ledger, on stationary-bootstrap p-values. The Deflated Sharpe Ratio is reported but does not gate.
- **Risk-exit timing:** risk-driven exits can happen on any day; probability exits (below 0.52) happen weekly; max hold is re-gated at day 28.
- **Drawdown breach:** flatten, then stay halted until the operator manually resets.
- **Delisting haircut in backtests:** 10%.

## Measured facts
Reproduce with `research/00_universe_feasibility.py`.
- Coinbase lists 86 delisted USD products and still serves their daily candles.
- Since 2021, 9–81 assets per month-end clear the $5M 30-day ADV filter (median 33). In 2026 the range is 15–28.

## Open questions for operator
See the Phase 1 gate message and SPEC.md items tagged [DECISION].

## Next step
Once SPEC.md is approved: merge `phase-1-spec` into `main` locally, then start Phase 2 on its own branch/worktree. Phase 2 order: parallel research tracks, then pre-registered hypotheses in EDGE_REPORT.md, then walk-forward backtests.
