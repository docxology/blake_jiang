# AGENTS.md — `projects/blake_jiang/`

## Directory Overview

This directory houses the `blake_jiang` research project: a multi-section scholarly manuscript synthesizing William Blake's prophetic critique of single vision, Professor Jiang Xueqin's contemporary speculative critique of AI, and Daniel Ari Friedman's two Zenodo publications grounding Blake in Active Inference and American pragmatism. The project follows the repository's Two-Layer Architecture, Thin Orchestrator Pattern, and Zero-Mock Testing Policy.

## Architecture Rules

### 1. Two-Layer Architecture

- **Generic infrastructure** lives only in `/infrastructure/`; this project never reimplements logging, rendering, validation, or LLM logic.
- **Domain logic** lives in `projects/blake_jiang/src/`:
  - `convergence.py` — the twelve-node convergence analysis between Jiang and Friedman/Blake.
  - `quotations.py` — authoritative quotation registry with timestamps and sources.
  - `generative_model.py` — Active-Inference-style metrics: prior dominance, precision allocation, fourfold balance.
  - `fourfold.py` — Four Zoas as factorized generative-model factors.
  - `manuscript.py` — manuscript injection data builder.
  - `viz/` — programmatic figure engine.
- **Tests** live in `tests/` (zero-mock, real I/O, real numerical computation).
- **Orchestration** lives in `scripts/` (thin, importing from `src/`).

### 2. Thin Orchestrators

`scripts/analyze.py` and `scripts/generate_figures.py` MUST NOT contain analytical logic. They import from `projects.blake_jiang.src.*` and write serialized outputs to `output/`.

### 3. Zero-Mock Testing

All tests in `tests/test_*.py` operate without mocking. Mathematical models, manuscript file integrity, quotation registry consistency, and figure renderers are asserted against real outputs.

## Directory Structure

```
projects/blake_jiang/
├── src/
│   ├── __init__.py
│   ├── convergence.py        Twelve-node convergence model
│   ├── quotations.py         Jiang / Blake / Friedman quotation registry
│   ├── generative_model.py   Precision dynamics, Newton's Sleep metric
│   ├── fourfold.py           Four-Zoas factorized model
│   ├── manuscript.py         Injection-data builder
│   └── viz/                  Programmatic figure engine
├── tests/                    Zero-mock test suite (>=90 % cov target)
├── scripts/                  analyze.py + generate_figures.py
├── manuscript/               12 ordered Markdown sections + config + bib
├── docs/                      Internal scholarly notes
└── output/                   Disposable working outputs
```

## Execution

```bash
./secure_run.sh --project blake_jiang
./run.sh --pipeline --project blake_jiang
```
