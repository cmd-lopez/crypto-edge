# PROGRESS

## Current phase
**Phase 2 (edge test) is complete.** Verdict: **NO EDGE** for H1, H2 and H3 (EDGE_REPORT.md §5).
**Blocked: waiting for the operator's decision** at the Phase 2 gate. Per SPEC kill criterion 1, Phases 3–6 do not proceed.

## Process note
The superpowers skills are not installed in this environment. Their intent is followed manually:
- brainstorming
- writing-plans (docs/plans/phase-2.md)
- git worktrees (one per phase)
- TDD (51 tests, each written first)
- parallel agents (4 research tracks)
- systematic debugging (engine cross-check, fragility analysis)
- code review (reviewer agent; 5 findings, all fixed)

## Decisions (Phase 2)
- **Pre-registration:** committed at `c24ad22`. H1 BTC trend gate, H2 per-asset trend, H3 trend composite. The Holm family is the 11 base-cost out-of-sample trials.
- **Why only price/volume rules:** fundamental/valuation/unlock hypotheses were rejected as not honestly backtestable with free point-in-time data (EDGE_REPORT §1.4).
- **Canonical run:** `9446793`, after the review fixes. Run 1 (`d216e6e`) is kept in the ledger.

## Measured facts
- **Benchmarks** (out-of-sample 2021-07..2026-06, net):
  - BTC buy-and-hold: Sharpe 0.47, max drawdown 77%.
  - Equal-weight PIT universe: Sharpe −0.19, max drawdown 95%.
- **Primaries fail on fold wins:** 20–30% against the 60% bar. Raw p = 0.88–0.97.
- **No signal before costs either:** gross Sharpe −0.03 to 0.10 vs BTC 0.475.

## Open questions for operator
Choose one of the options in EDGE_REPORT §5.1:
1. Stop and package (recommended).
2. Run one new pre-registered study with a fresh multiple-testing family.
3. Revise SPEC constraints *before* any new test.

## Next step
Waiting for the operator's decision. If option 1: polish README/EDGE_REPORT for publication. No code is pushed without approval.
