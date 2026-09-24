# History rewrite (2026-09-24)

All commits were rewritten with `git filter-repo --mailmap` so that every commit is authored and committed by Andres Lopez under a GitHub noreply address. Commit messages were scanned for AI-attribution trailers; none existed.

What was preserved:
- **File contents:** the tree at the pre-rewrite HEAD is byte-identical to the rewritten one.
- **Author and committer dates.**
- **Commit order.** The pre-registration commit still precedes every backtest commit.

What changed: every commit hash. Prose and code now cite the new hashes.

Recorded outputs keep the hashes they were produced with, because the ledger is append-only and results are not edited:
- `research/trials.csv` (`git_hash` column)
- `research/results/phase2/verdicts.json`
- `research/results/phase2/manifest.json`

Use this table to translate them.

| Original | Rewritten | Subject |
|---|---|---|
| `106cb81` | `140b3c2` | Initialize repository |
| `f42ff4f` | `01f5f41` | Phase 1: draft SPEC.md, universe feasibility probe, PROGRESS.md |
| `272d187` | `163afc8` | Phase 1: SPEC.md approved by operator |
| `2157266` | `6a3f639` | Phase 2: TDD backtest harness (data, PIT universe, engine, folds, metrics, ledger, benchmarks) + plan |
| `a90f587` | `299060b` | Move candle fetcher to edge.fetch; probe uses shared exclusion list (results unchanged) |
| `2369cc9` | `1b928c2` | Engine: no-trade band (entries/exits always trade) |
| `b1874a8` | `80aa496` | Engine passes actual holdings to strategies |
| `c24ad22` | `7c879de` | Phase 2: research notes + EDGE_REPORT pre-registration (H1-H3), before any hypothesis backtest |
| `d216e6e` | `2d264ed` | Phase 2: hypotheses H1-H3 (per pre-registration 7c879de), evaluation, single-command runner |
| `9446793` | `fb8695e` | Review fixes: universe requires a bar on d; band cannot hold above weight cap; execution enforces position/gross limits and retries unsold; H3 fill per pre-registration; EW benchmark uses same band; post-hoc diagnostics script |
| `81f8e5b` | `492897e` | Phase 2: results, verdicts (no edge x3), README, PROGRESS |
| `e564eab` | `586522e` | Package: CI (make ci + GitHub Actions look-ahead gate), strengthened engine look-ahead test, architecture docs, project closed after Phase 2 |
| `95566c4` | `ec5ac7f` | Add MIT license |
| `1f94e16` | `5caf663` | CI: actions/checkout@v7 and astral-sh/setup-uv@v10.2.0 (Node 24 runtime) |
| `32ea1b2` | `ba91e2a` | README: question, method, verdict and out-of-sample equity chart; chart script |
