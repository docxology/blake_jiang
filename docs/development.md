# Development and rendering

Use uv and Python 3.11 or later. From the repository root, install the
development extra and run the native commands:

```bash
uv sync --extra dev
uv run python -m scripts.analyze
uv run python -m scripts.generate_figures
uv run pytest tests/ --cov=src --cov-fail-under=90
```

The analysis writes `output/data/manuscript_injection.json` with the convergence
summary, fourfold mapping, and illustrative model metrics. The figure command
writes seven illustrations in both light and dark variants under
`output/figures/`. The [canonical manuscript](manuscript/README.md) embeds the
seven light variants. The calculations illustrate the paper's model and the
quoted source attributions are documented in [quotation provenance](quotation_provenance.md).

## Render the manuscript

The separate [docxology/template](https://github.com/docxology/template) renderer
assembles the Markdown sections, configuration, bibliography, and generated light
figures. Run the commands above first from a committed checkout named
`blake_jiang`. The external engine needs Python 3.14, Pandoc, a compatible
`pandoc-crossref`, and XeLaTeX with its packages.

From the project root, choose an unused location for the engine clone:

```bash
BLAKE_JIANG_ROOT="$(pwd -P)"
TEMPLATE_ROOT="$BLAKE_JIANG_ROOT/../blake-jiang-render-template"
git clone https://github.com/docxology/template.git "$TEMPLATE_ROOT"
git -C "$TEMPLATE_ROOT" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
cd "$TEMPLATE_ROOT"
uv sync --locked --no-dev --python 3.14
mkdir -p projects/working
ln -s "$BLAKE_JIANG_ROOT" projects/working/blake_jiang
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/blake_jiang --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/blake_jiang
```

The managed alias and both Git indexes supply the renderer's provenance inputs.
The hydration flag preserves the authored source. Find the current artifacts
in the project checkout:

- `output/pdf/blake_jiang_combined.pdf`
- `output/web/index.html`
- `output/reports/validation_report.json`
- `output/reports/rendered_provenance.json`

Use rendering validation to check structure, references, and artifact
provenance. The [historical version 1 PDF](../blake_jiang_DAF_v1_05-12-2026.pdf)
remains the May 12, 2026 artifact.
