# Phase 2 plan: edge test

Scope: SPEC.md §4, §6.1–6.2 (as backtest mechanics), §7. This is research code, but a bug in it would invalidate the verdict, so the harness is built test-first. No production trading code is written in this phase.

## Order (the pre-registration boundary is enforced by git history)
1. Four research tracks run in parallel, one note each: `research/notes/01_regime.md`, `02_candidates_defi_apps.md`, `03_candidates_l1_payments.md`, `04_anomaly_literature.md`.
2. Build the harness with TDD, testing only on synthetic data. No strategy is evaluated on real prices at this step.
3. Write EDGE_REPORT.md §1 (regime and candidates, from the notes) and §2 (pre-registered hypotheses: rules, parameter grids, trial accounting). **Commit this before any backtest.** Results cite the commit hash.
4. `uv run python -m edge.run_phase2` runs every pre-registered trial at base cost, 2× cost, and with a one-day delay. It appends each trial to `research/trials.csv` and writes `research/results/phase2/`.
5. Verdicts go in EDGE_REPORT.md §3–5, followed by the WHAT COULD I BE WRONG ABOUT? section.

## Conventions
- **Bar index:** the UTC bar-open date *T*. A bar is complete once `T + 1 day <= now`. Incomplete bars are dropped.
- **Decision date d:** the last completed bar. Decision time is `d + 1 day 00:00 UTC`.
- **Weekly decisions:** d is a Sunday, so orders execute at the open of Monday's bar.
- **Fills:** at `open[d + 1 + delay]`. Cost per side = (fee + slippage) × |Δ notional|.
- **Daily accounting:** mark positions to the open, trade, then mark to the close. Daily return = close equity / prior close equity − 1.

## Files and interfaces
| File | Interface |
|---|---|
| `src/edge/fetch.py` | `fetch_all(cache_dir) -> None`. Downloads Coinbase USD daily candles, listed and delisted. Moved here from the probe script, which now imports it |
| `src/edge/data.py` | `Panel` (open/high/low/close/volume/dollar_volume as wide DataFrames). `load_panel(cache_dir, now)`. `panel_from_frames(...)`. `manifest(cache_dir) -> dict[file, sha256]` |
| `src/edge/universe.py` | `EXCLUDED: dict[base, reason]`. `eligibility(panel, min_adv=5e6, window=30, min_history=30, top_n=50) -> DataFrame[bool]` |
| `src/edge/engine.py` | `CostModel(fee, slippage).scaled(k)`. `Limits(max_positions, max_weight, max_gross, daily_loss, max_drawdown)`. `Strategy` protocol: `target_weights(view, d) -> Series` and `exits(view, d, held) -> set[str]`. `run(panel, strategy, start, end, decision_days, costs, limits, delay=0, dd_reset_dates=()) -> Result`. The strategy only ever receives `view = panel.upto(d)` |
| `src/edge/folds.py` | `walk_forward(start, end, train_months=12, test_months=3) -> list[Fold]`. Only full test folds are returned |
| `src/edge/metrics.py` | `sharpe`, `max_drawdown`, `stationary_bootstrap_pvalue(a, b, mean_block=7, n_boot=10_000, seed)` (H0: SR(a) ≤ SR(b)), `holm(p)`, `deflated_sharpe(...)` |
| `src/edge/benchmarks.py` | `BuyHoldBTC`, `EqualWeightMonthly`. Both run through the same engine and cost model; SPEC position limits do not apply to them |
| `src/edge/ledger.py` | `append_trial(path, record)`. Append-only CSV with a fixed header |
| `src/edge/hypotheses/*.py` | One module per pre-registered hypothesis (written after step 3) |
| `src/edge/run_phase2.py` | Orchestration: folds → trials → edge-bar table → outputs |

## Tests (all written before implementation)
- **data:**
  - The incomplete last bar is dropped.
  - A missing day gives a NaN price and $0 dollar volume.
  - `dollar_volume = volume × close`.
  - The manifest is deterministic.
- **universe:**
  - Exclusions are applied.
  - The minimum-history rule holds.
  - ADV uses only rows ≤ d: perturbing the future leaves the mask unchanged.
  - The top_n cut is applied.
  - A delisted asset drops out.
- **engine:**
  - Hand-computed P&L with costs.
  - A fill happens at the next open, not the same close.
  - `delay` shifts the fill.
  - `CostModel.scaled` doubles costs.
  - The 5-position cap holds.
  - The 20% weight cap holds.
  - The 90% gross cap holds.
  - The daily-loss halt blocks entries on the next execution.
  - The drawdown breaker flattens and stays halted until a reset date.
  - A delisting haircut of 10% is applied after the last bar.
  - A gap day holds the last price.
  - Untradeable targets are skipped.
  - **Look-ahead:** perturbing all data after d leaves every decision at or before d unchanged.
  - A strategy cannot see bars after d.
- **folds:**
  - Boundaries are correct.
  - Train and test never overlap.
  - `test_end <= end`.
  - The fold count is right.
- **metrics:**
  - Sharpe and max drawdown on known series.
  - The bootstrap p-value is near 0 for a dominant series and large for identical series.
  - Holm matches a textbook example.
  - DSR matches a hand-computed value.
- **ledger:**
  - Appends keep the header.
  - Existing rows are never rewritten.

## Failure modes this guards against
- Look-ahead through universe selection, features, or fills.
- Survivorship: delisted assets are included and exits are haircut.
- Selection bias: every run is in the ledger and Holm uses the full family.
- Cost optimism: 2× stress is gated.
- Incomplete bars.
- Silent data changes: the manifest records the sha256 of the data.
