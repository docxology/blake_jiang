# AGENTS.md — `projects/blake_jiang/tests/`

## Purpose

Zero-mock test suite for the Blake/Jiang project. Coverage floor: **≥ 90 %** of `src/` lines and branches, enforced by `--cov-fail-under=90`. Current measured figure: see `README.md` in this directory.

## Test files

| File | Tests | What it asserts |
| --- | --- | --- |
| `conftest.py` | — | Headless `MPLBACKEND`, isolated MPL cache, `sys.path` repair for `projects.blake_jiang.*`. |
| `test_quotations.py` | 15 | Quotation registry invariants — speaker whitelist, immutability, theme/id lookup, Jiang quotes carry timestamps. |
| `test_convergence.py` | 8 | Exactly 12 convergence nodes, all reference valid quotation IDs, node_id range validation, three-speaker constraint per node. |
| `test_generative_model.py` | 30 | Precision-allocation validation, Newton's-Sleep ratio bounds, fourfold-balance entropy maximum at equality, cleansed-doors score bounded in [0,1]. |
| `test_fourfold.py` | 6 | Four Zoas canonical set, unique faculties, six pair-wise coordination entries, full Active-Inference table. |
| `test_manuscript.py` | 6 | `ManuscriptBuilder` shape & ordering invariants (sleep metric > eden, eden cleansed-doors > sleep). |
| `test_viz_figures.py` | 3 | Every renderer writes a non-trivial PNG in light + dark variants; parent dirs auto-created (15 parametrized cases). |
| `test_analyze_script.py` | 3 | `scripts/analyze.py` writes expected keys, is idempotent, creates output dirs. |
| `test_generate_figures_script.py` | 2 | `scripts/generate_figures.py` produces all 14 PNGs (7 renderers × 2 themes). |

## Zero-Mock Policy

- **No `unittest.mock`, `mocker.patch`, `MagicMock`** — anywhere.
- **No HTTP mocking** beyond `pytest-httpserver` if we add network code (we don't).
- **No file-system mocking** — use `tmp_path` for ephemeral I/O.
- Numerical assertions use `pytest.approx` with explicit tolerances, never hand-waved equality.

## Architecture Rules

1. Tests import from `projects.blake_jiang.src.*` and `projects.blake_jiang.scripts.*` exclusively. They never import from sibling projects. The root `conftest.py` maps those names onto the standalone `src/`, `tests/`, and `scripts/` layout.
2. Every test file is independently runnable: `uv run pytest tests/test_foo.py -v`.
3. Tests cannot mutate `src/` data — registries and tuples are frozen; if a test would need mutation, the architecture is wrong.
4. New tests follow `test_<noun>_<assertion>` naming.

## Running

```bash
# Full suite with coverage
uv run pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=90

# Single file
uv run pytest tests/test_convergence.py -v

# Single test
uv run pytest tests/test_quotations.py::test_registry_count_matches_entries -v
```
