# `manuscript/` — Scholarly Prose

Nine ordered Markdown sections + `99_references.md` + `references.bib` + `config.yaml`. The root pipeline assembles these into the final paper.

## Reading order

1. **`00_abstract.md`** — what the paper argues, in ~500 words.
2. **`01_introduction.md`** — three voices, three registers, why triangulation is the method.
3. **`02_jiang_diagnosis.md`** — Jiang's full AI critique, source-attributed with timestamps.
4. **`03_blake_architecture.md`** — Blake's fourfold vision, Four Zoas, Newton's Sleep, doors of perception.
5. **`04_friedman_synthesis.md`** — Active Inference scaffolding; the eight + six structural correspondences; synergetics; cognitive security.
6. **`05_twelve_nodes.md`** — node-by-node walkthrough of the twelve convergences.
7. **`06_critical_assessment.md`** — separating Jiang's defensible empirical claims from his conspiratorial framing.
8. **`07_implications.md`** — AI alignment, cognitive security, Blake scholarship, cognitive science, public discourse.
9. **`08_conclusion.md`** — three refractions of a single light.

## Build

```bash
# From the repo root
./run.sh --pipeline --project blake_jiang
# Output PDFs land in output/blake_jiang/pdf/
```

## Tone

- Open scholarly publication register; not journalistic, not academic-jargon-heavy.
- Quotations attributed with timestamps (Jiang) or canonical source + plate (Blake).
- Honest about uncertainty; the paper claims convergence, not equivalence.
- Critical of Jiang's conspiratorial scaffolding while preserving the architectural insight.
