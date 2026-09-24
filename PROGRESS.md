# PROGRESS

## Current phase
**CLOSED after Phase 2.**
- **Decision:** on 2026-09-24 the operator accepted the recommendation (EDGE_REPORT §5.1, option 1): stop and package.
- **Verdict:** no edge for H1, H2 and H3 (EDGE_REPORT.md §5).
- **Not done:** Phases 3–6 (architecture, build, paper, live), per SPEC kill criterion 1.

## Process note
The superpowers skills are not installed in this environment. Their intent was followed manually:
- brainstorming
- writing-plans (docs/plans/phase-2.md)
- git worktrees (one per phase)
- TDD (51 tests, each written first)
- parallel agents (4 research tracks)
- systematic debugging (engine cross-check, fragility analysis, look-ahead mutation testing)
- code review (reviewer agent; 5 findings, all fixed)

## Decisions (Phase 2)
- **Pre-registration:** committed at `c24ad22`. H1 BTC trend gate, H2 per-asset trend, H3 trend composite. The Holm family is the 11 base-cost out-of-sample trials.
- **Why only price/volume rules:** fundamental/valuation/unlock hypotheses were rejected as not honestly backtestable with free point-in-time data (EDGE_REPORT §1.4).
- **Canonical run:** `9446793`, after the review fixes. Run 1 (`d216e6e`) is kept in the ledger.
- **Packaging:**
  - CI added: `make ci` and `.github/workflows/ci.yml` run the look-ahead gate first, then the full suite.
  - The engine look-ahead test was strengthened after mutation testing showed it missed a one-bar leak.
  - Engine code is unchanged, so results stand.

## Measured facts
- **Benchmarks** (out-of-sample 2021-07..2026-06, net):
  - BTC buy-and-hold: Sharpe 0.47, max drawdown 77%.
  - Equal-weight PIT universe: Sharpe −0.19, max drawdown 95%.
- **Primaries fail on fold wins:** 20–30% against the 60% bar. Raw p = 0.88–0.97.
- **No signal before costs either:** gross Sharpe −0.03 to 0.10 vs BTC 0.475.

## Open questions
None. Reopening requires a new, separately pre-registered study, or a SPEC revision made **before** any new test (EDGE_REPORT §5.1, options 2–3).

## Next step
None scheduled. The repository is local only; publishing or pushing needs operator approval.
