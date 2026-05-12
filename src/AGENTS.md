# AGENTS.md — `projects/blake_jiang/src/`

## Purpose

This directory holds **all domain logic** for the Blake/Jiang study. By the Two-Layer Architecture, business logic lives *only* here (for project-specific work) or in `/infrastructure/` (for generic, reusable work). Scripts in `../scripts/` are forbidden from carrying analytical logic and must import from this package.

## Modules

| File | Responsibility | Key public symbols |
| --- | --- | --- |
| `__init__.py` | Package marker; declares public sub-modules. | `__all__` |
| `quotations.py` | Authoritative immutable registry of attributed quotations. Every Blake / Jiang / Friedman quote used by the paper is built here. | `Quotation`, `QuotationRegistry`, `SPEAKERS`, `build_registry()` |
| `convergence.py` | The twelve-node thematic convergence model linking the three voices. | `ConvergenceNode`, `build_nodes()`, `default_convergence_model()`, `validate_nodes_against_registry()` |
| `generative_model.py` | Active-Inference precision dynamics: Newton's-Sleep ratio, fourfold balance, cleansed-doors score. | `PrecisionAllocation`, `newtons_sleep_metric()`, `fourfold_balance()`, `cleansed_doors_score()`, `canonical_regimes()`, `regime_report()` |
| `fourfold.py` | The Four Zoas as a factorized generative-model architecture. | `Zoa`, `four_zoas()`, `coordination_matrix()`, `fourfold_to_active_inference_table()` |
| `manuscript.py` | Manuscript-injection builder; orchestrates the other modules into one serializable dict. | `ManuscriptBuilder` |
| `viz/` | Programmatic figure engine (see `viz/AGENTS.md`). | `render_*` functions |

## Architecture Rules

1. **Determinism.** Every public function must produce the same output for the same input across runs. No stochastic state, no hidden globals.
2. **Strict validation.** Dataclasses validate fields in `__post_init__`; raise `ValueError` / `KeyError` rather than silently accepting bad data.
3. **No mocks downstream.** Tests against this code must exercise real computations and assert on numerical / structural invariants.
4. **Infrastructure imports only.** Inside this package, the only external Layer-1 imports allowed are from `infrastructure.core.*` (logging, exceptions). No project-to-project imports.
5. **Type hints.** All public functions carry type annotations on parameters and return values.

## When extending

If you add a module: update `__all__` in `__init__.py`, add a row to the table above, write zero-mock tests in `../tests/`, and bump coverage if the new module would otherwise drop below the 90 % project floor.

If you change a public function signature: update the dependent scripts (`../scripts/`), tests (`../tests/`), and any manuscript section that quotes a numerical value derived from the function.
