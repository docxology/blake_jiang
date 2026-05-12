# `scripts/` — Thin Orchestrators

Two scripts; each is a logic-free coordinator that calls `src/` modules and writes files.

## `analyze.py`

Builds the manuscript-injection JSON.

```bash
uv run python projects/blake_jiang/scripts/analyze.py
# → projects/blake_jiang/output/data/manuscript_injection.json
```

## `generate_figures.py`

Renders all six figures in light + dark themes (12 PNGs).

```bash
uv run python projects/blake_jiang/scripts/generate_figures.py
# → projects/blake_jiang/output/figures/<name>_{light,dark}.png
```

## Test the orchestrators

```bash
uv run pytest projects/blake_jiang/tests/test_analyze_script.py projects/blake_jiang/tests/test_generate_figures_script.py -v
```
