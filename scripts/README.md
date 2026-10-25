# `scripts/` — Thin Orchestrators

Two scripts; each is a logic-free coordinator that calls `src/` modules and writes files. Run them from the repository root.

## `analyze.py`

Builds the manuscript-injection JSON.

```bash
uv run python scripts/analyze.py
# → output/data/manuscript_injection.json
```

## `generate_figures.py`

Renders all seven figures in light + dark themes (14 PNGs).

```bash
uv run python scripts/generate_figures.py
# → output/figures/<name>_{light,dark}.png
```

## Test the orchestrators

```bash
uv run pytest tests/test_analyze_script.py tests/test_generate_figures_script.py -v
```
