# AGENTS.md — `projects/blake_jiang/src/viz/`

## Purpose

Programmatic figure engine. Every published figure in the Blake/Jiang manuscript is produced by a pure function here. Renderers are **deterministic**, take a single `output_path: Path` argument, accept `dark: bool = False`, and write a single PNG / PDF / SVG depending on the path's suffix.

## Renderers

| File | Public function | What it shows |
| --- | --- | --- |
| `core.py` | `apply_style`, `save_and_close`, `COLORS`, `MIN_FONT` | Shared style primitives — colors, font floor, headless save path. |
| `triangulation.py` | `render_triangulation` | Three-vertex Jiang/Blake/Friedman diagram with centroid label "Architecture of Intelligence". |
| `convergence_graph.py` | `render_convergence_graph` | Twelve-row table of convergence nodes with three-voice markers and AI counterpart text. |
| `fourfold_model.py` | `render_fourfold_model` | Four Zoas (Urizen / Luvah / Tharmas / Urthona) around the central Albion node with AI role labels. |
| `precision_dynamics.py` | `render_precision_dynamics` | Three-panel bar chart: Newton's-Sleep metric, fourfold-balance entropy, cleansed-doors score across four canonical regimes. |
| `timeline.py` | `render_timeline` | Multi-century chronology — Blake (1789-1820) → Pragmatism (1878-1929) → Active Inference (2005-2022) → Jiang (2024) → Friedman (2026). |
| `markov_blanket.py` | `render_markov_blanket` | Concentric Markov-blanket diagram with Blake's "doors of perception" quotation. |

## Architecture Rules

1. **Pure functions only.** No module-level state beyond the constants in `core.py`. Each renderer receives `output_path` and writes exactly one file.
2. **Color discipline.** Use the `COLORS` palette in `core.py`. Add new entries there rather than inlining hex codes.
3. **Light + dark variants.** Every renderer must respect `dark=False` (default) and `dark=True`. `apply_style()` and `save_and_close()` already handle the facecolor logic.
4. **Headless safety.** Renderers assume `MPLBACKEND=Agg`. Scripts and tests set this; never call `plt.show()`.
5. **Close the figure.** Every renderer must close its `Figure` (via `save_and_close`) before returning.
6. **Pull from `src/`.** Renderers may import from sibling `src/` modules to obtain canonical data; they must not re-define quotations or metrics.

## When extending

- New renderer: add a module file, expose a single `render_<name>(output_path, dark=False)` function, re-export it in `__init__.py`, add a regression test in `../../tests/test_viz_figures.py` and a row in `../../scripts/generate_figures.py`'s `_RENDERERS` dict.
- Style change: edit `core.py` once; never duplicate palette entries inline.

## Don't

- Don't use `pyplot`'s global state across function boundaries (every renderer constructs its own `fig, ax`).
- Don't embed text that re-quotes Blake / Jiang / Friedman verbatim without that quotation living in `quotations.py` — figure-text drift is a real failure mode.
