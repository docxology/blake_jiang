# AGENTS.md — `projects/blake_jiang/manuscript/`

## Purpose

The scholarly manuscript itself, in Markdown sections that the root pipeline assembles into LaTeX / PDF / HTML.

## File order

Sections are processed in lexicographic order; the leading two-digit prefix is the canonical sort key.

| File | Role | Approx. words |
| --- | --- | --- |
| `config.yaml` | Paper metadata (title, authors, keywords, license, geometry). | — |
| `00_abstract.md` | Abstract + keywords. | — |
| `01_introduction.md` | Convergence framing; method statement; outline. | — |
| `02_jiang_diagnosis.md` | Jiang lecture diagnosis with timestamps. | — |
| `03_blake_architecture.md` | Blake's perceptual hierarchy, Four Zoas, doors of perception, Newton's Sleep. | — |
| `04_synthesis.md` | Active Inference scaffolding; structural correspondences. | — |
| `05_twelve_nodes.md` | Each of the twelve thematic convergence nodes. | — |
| `06_cooperation_off_ramp.md` | Multi-agent cooperation-off-ramp chapter. | — |
| `07_critical_assessment.md` | Defensible claims vs conspiratorial framing; bounded speculation. | — |
| `08_implications.md` | AI alignment, cognitive security, Blake scholarship, public discourse. | — |
| `09_conclusion.md` | Closing synthesis. | — |
| `10_glossary.md` | Glossary of cross-vocabulary terms. | — |
| `99_references.md` | Pointer to references.bib. | — |
| `references.bib` | All citations in BibTeX. | — |
| `preamble.md` | Front-matter prose prepended at assembly. | — |
| `legal_claim_ledger.yaml` | Rights/claims ledger for quoted material. | — |

## Architecture Rules

1. **Cite, don't re-quote.** Every Blake / Jiang / Friedman quotation must trace to an entry in `../src/quotations.py`. Add it there first; reference its content here.
2. **Stable BibTeX keys.** Keys in `references.bib` are used by every section's `[@key]` references. Renaming a key is a refactor that touches every section.
3. **No generated content.** Section files are hand-authored prose. Numerical figures (e.g., precision-regime scores) are written explicitly in prose, not interpolated at build time — but they must match the values produced by `../src/generative_model.py`.
4. **Plain Markdown.** No JavaScript, no shortcodes, no hidden HTML. Tables use plain pipe-syntax; figures are referenced by relative path to `../output/figures/`.
5. **Inline metric checking.** If a section quotes a numeric metric (e.g., "fourfold-balance entropy of approximately 0.78 nats"), that number must be reproducible from `src/`; the regression test that demonstrates this lives in `../tests/test_manuscript.py`.

## When extending

- Add a new section between `09_conclusion.md` and `99_references.md` (e.g., `08a_appendix.md`) to keep the conclusion (`09_conclusion.md`) followed by glossary/references.
- New citation: add a BibTeX entry, give it a kebab-case key, and reference it as `[@key]`.
- New quoted Blake / Jiang / Friedman line: register the `Quotation` in `../src/quotations.py` first.

## Don't

- Don't introduce metrics in the prose that the code can't reproduce.
- Don't put figures in the manuscript — figures live in `../output/figures/` and are referenced from there at render time.
- Don't introduce internal cross-references by section number (e.g., "see §4.3"). Sections must read self-sufficiently; refer to content thematically ("the formal synthesis," "the convergence analysis") rather than by index.
