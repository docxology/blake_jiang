# `src/` — Domain Logic for the Blake/Jiang Study

This package is the **only place** where project-specific computation lives. Scripts in `../scripts/` import from here; tests in `../tests/` exercise these modules; manuscript figures in `../manuscript/` are templated from data produced here.

## Quick orientation

```
src/
├── __init__.py
├── quotations.py        # 25 attributed quotations across Jiang, Blake, Friedman
├── convergence.py       # The 12 thematic convergence nodes
├── generative_model.py  # Precision-allocation metrics (Active Inference)
├── fourfold.py          # Four Zoas as a factorized generative model
├── manuscript.py        # ManuscriptBuilder: gathers everything into one dict
└── viz/                 # Six figure renderers (see viz/README.md)
```

## What lives where

- **Quotation registry** is in `quotations.py`. If you need to add or correct a quotation, edit it there — never re-quote in manuscript markdown without registering it.
- **Numerical metrics** for the Newton's-Sleep / Cleansed-Doors / Fourfold-Balance argument live in `generative_model.py`. Tests assert exact bounds on these metrics; do not change the formulas without updating tests.
- **Convergence nodes** link Jiang/Blake/Friedman quotations to formal counterparts in Active Inference. Each node references three quotation IDs by string; `validate_nodes_against_registry` enforces consistency at build time.

## Local sanity check

```bash
uv run pytest projects/blake_jiang/tests/ -k "quotations or convergence or generative or fourfold" -v
```

## Style

- Type hints on every public function.
- Dataclasses with `frozen=True` for value objects.
- Logging via `infrastructure.core.logging.utils.get_logger`.
- No comments restating obvious code; comments only mark genuine non-obvious invariants or scholarly references.

## Don't

- Don't add stochastic / time-dependent state.
- Don't import from sibling `projects.*` packages.
- Don't bypass `quotations.py` to embed a "quick quote" in convergence or manuscript.
- Don't reach into `viz/` from outside the engine — call public renderers via `from projects.blake_jiang.src.viz import …`.
