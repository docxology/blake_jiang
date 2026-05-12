# `src/viz/` — Figure Engine

Six renderers; one figure per module. Each is a pure function with the signature

```python
def render_<name>(output_path: Path, dark: bool = False) -> None
```

## The six figures

1. **`triangulation`** — Jiang ⊳ Blake ⊳ Friedman as a labeled triangle around the "Architecture of Intelligence" centroid.
2. **`convergence_graph`** — Twelve thematic convergence nodes as a bipartite-style table mapping nodes to formal Active Inference counterparts.
3. **`fourfold_model`** — The Four Zoas (Urizen / Luvah / Tharmas / Urthona) arranged around the Albion node, each annotated with its Active Inference role.
4. **`precision_dynamics`** — Three-panel bar chart comparing four precision regimes (Newton's Sleep → Twofold Generation → Threefold Beulah → Fourfold Eden) across Newton's-Sleep ratio, fourfold-balance entropy, and cleansed-doors score.
5. **`timeline`** — Multi-century chronology of the convergence: Blake 1789-1820, Pragmatism 1878-1929, Active Inference 2005-2022, Jiang 2024, Friedman 2026.
6. **`markov_blanket`** — Concentric Markov-blanket diagram with Blake's "doors of perception" quotation as the legend.

## Adding a renderer

1. Add `my_new_figure.py` defining `render_my_new_figure(output_path, dark=False)`.
2. Reuse `COLORS`, `MIN_FONT`, `apply_style`, `save_and_close` from `core.py`.
3. Re-export from `__init__.py`.
4. Add it to `_RENDERERS` in `../../scripts/generate_figures.py`.
5. Add it to `_RENDERERS` in `../../tests/test_viz_figures.py`.
6. Run `uv run pytest projects/blake_jiang/tests/test_viz_figures.py -v` to confirm.

## Determinism

Renderers are deterministic — the same call produces a byte-identical PNG given matplotlib version stability. We do not hash test PNGs (matplotlib's anti-aliasing varies across platforms), but we assert non-trivial file size as a smoke check.
