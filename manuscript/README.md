# `manuscript/` — Scholarly Prose

Eleven ordered Markdown sections + `99_references.md` + `references.bib` + `config.yaml`. The root pipeline assembles these into the final paper.

## Reading order (files as of 2026-10-25):

1. **`00_abstract.md`** — what the paper argues, in ~500 words.
2. **`01_introduction.md`** — three voices, three registers, why triangulation is the method.
3. **`02_jiang_diagnosis.md`** — Jiang's AI critique, source-attributed with timestamps.
4. **`03_blake_architecture.md`** — Blake's fourfold vision, Four Zoas, Newton's Sleep, doors of perception.
5. **`04_synthesis.md`** — Active Inference scaffolding; structural correspondences between the three vocabularies.
6. **`05_twelve_nodes.md`** — node-by-node walkthrough of the twelve convergences.
7. **`06_cooperation_off_ramp.md`** — multi-agent cooperation-off-ramp chapter.
8. **`07_critical_assessment.md`** — separating Jiang's defensible claims from his conspiratorial framing.
9. **`08_implications.md`** — AI alignment, cognitive security, Blake scholarship, public discourse.
10. **`09_conclusion.md`** — closing synthesis.
11. **`10_glossary.md`** — glossary of cross-vocabulary terms.
12. **`99_references.md`** — references.

## Build

```bash
# From the repository root — refresh derived data and figures
uv run python scripts/analyze.py
uv run python scripts/generate_figures.py
```

The PDF itself is assembled by the `docxology/template` workspace pipeline (pandoc/xelatex), which consumes these sections together with `config.yaml` and `references.bib`. The last assembled build is checked in at the repository root as `blake_jiang_DAF_v1_05-12-2026.pdf`.

## Tone

- Open scholarly publication register; not journalistic, not academic-jargon-heavy.
- Quotations attributed with timestamps (Jiang) or canonical source + plate (Blake).
- Honest about uncertainty; the paper claims convergence, not equivalence.
- Critical of Jiang's conspiratorial scaffolding while preserving the architectural insight.
