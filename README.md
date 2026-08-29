# Blake, Jiang, and the Architecture of Intelligence

**A rapid-publication, AI-augmented scholarly response to Professor Jiang Xueqin's *Game Theory #24: The AI Apocalypse* (12 May 2026), triangulating Jiang's contemporary commentary on artificial intelligence with William Blake's perceptual diagnostics of the 1790s and Karl Friston's Active Inference framework.**

> ⚠️ **A note on form.** This paper is an experiment in rapid AI-augmented scholarly publication with society-in-the-loop. It was drafted on 12 May 2026 in response to a YouTube lecture published the same day. The drafting process used contemporary AI assistance for transcript research, structural mapping, formal derivation, and figure rendering, while editorial judgment, quotation provenance, scholarly framing, and the final synthetic argument remained with the author. The methodology is not standard peer-reviewed scholarship; it is an attempt to see what becomes available when publication latency is collapsed from months to hours. Readers are invited to read in that spirit: a working draft, posted in the open, inviting correction.

## The Paper

The combined manuscript PDF is checked in at the repository root:

- 📕 **[`blake_jiang_DAF_v1_05-12-2026.pdf`](blake_jiang_DAF_v1_05-12-2026.pdf)** — ~17,000-word essay with 7 numbered equations, 14 figures (light + dark), 12-node convergence analysis, mathematical formalism for Newton's Sleep as precision misallocation, a multi-agent cooperation-off-ramp chapter, and a glossary of cross-vocabulary terms.

The author's earlier related work (cited throughout):

- *The Doors of Perception are the Threshold of Prediction: Active Inference and William Blake's Theory of Seeing* — Zenodo [10.5281/zenodo.18600041](https://zenodo.org/records/18600041)
- *Before Pragmatism Had a Name: Blake's "America A Prophecy" Anticipates American Anticipatory Epistemology* — Zenodo [10.5281/zenodo.18807971](https://zenodo.org/records/18807971)

## Argument in One Paragraph

Three independent vocabularies — Jiang's polemical lecture form, Blake's mythopoetic visionary apparatus, and the mathematical synthesis developed in the author's earlier Zenodo papers — appear, on the reading offered here, to pick out the same architectural failure mode. That failure mode is what Blake calls *Single Vision* and what cognitive science sometimes describes as *pathological prior dominance*: a perceiving system whose top-down expectations have come to outweigh incoming sensory evidence, so that the model becomes a closed loop confirming itself regardless of what actually happens. Naming this pattern across three vocabularies — Romantic poetics, contemporary public-intellectual polemic, and variational cognitive science — is what the paper attempts, with explicit acknowledgment that the mapping is a *functional analogy across incompatible metaphysics*, not a translation. The Free Energy Principle is itself contested; Jiang's lecture corpus is a speculative source, not a scholarly one. The reading is offered as a working draft, not a finished argument.

## Repository Layout

```
blake_jiang/
├── blake_jiang_DAF_v1_05-12-2026.pdf   ← THE PAPER
├── manuscript/                         12 Markdown sections + config.yaml + references.bib
├── src/                                Domain modules
│   ├── convergence.py                  Twelve-node convergence model
│   ├── quotations.py                   Jiang / Blake / earlier-work quotation registry
│   ├── generative_model.py             Active-Inference precision dynamics + variational math
│   ├── fourfold.py                     Four Zoas as factorized generative model
│   ├── manuscript.py                   Manuscript-injection builder
│   └── viz/                            7 programmatic figure renderers
├── tests/                              85 zero-mock tests; coverage ≥ 98.5 %
├── scripts/                            Thin orchestrators (analyze.py, generate_figures.py)
├── docs/                                Methodology + quotation-provenance notes
├── output/                             Disposable build artefacts (gitignored except final deliverables)
├── pyproject.toml
├── AGENTS.md                           Repository conventions for AI agents
└── README.md
```

Each subdirectory carries its own `AGENTS.md` and `README.md` describing its purpose, conventions, and contribution surface.

## Running Locally

The project is structured to integrate with the [`docxology/template`](https://github.com/docxology/template) research-project pipeline; when run inside that workspace, it executes through the template's 10-stage DAG. Run standalone with `uv`:

```bash
# install
uv sync --dev

# render figures + manuscript-injection JSON
uv run python scripts/analyze.py
uv run python scripts/generate_figures.py

# run the zero-mock test suite (≥ 98.5 % coverage)
uv run pytest tests/ --cov=src --cov-fail-under=90
```

The 12 PNG figures are produced under `output/figures/`; the JSON metrics under `output/data/`. Rendering the full PDF requires the [template](https://github.com/docxology/template) pipeline's pandoc/xelatex stage.

## Citation

```bibtex
@misc{friedman_blake_jiang_2026,
  author = {Friedman, Daniel Ari},
  title = {Blake, Jiang, and the Architecture of Intelligence:
           A Rapid-Publication Response to {Game Theory \#24: The AI Apocalypse}},
  year = {2026},
  month = may,
  day = {12},
  doi = {10.5281/zenodo.20144984},
  url = {https://github.com/docxology/blake_jiang}
}
```

## License

- **Manuscript and figures** are released under [Creative Commons Attribution 4.0 International](LICENSE-CC-BY-4.0) (CC-BY-4.0).
- **Source code** is released under the [MIT License](LICENSE-MIT).

See [`LICENSE`](LICENSE) for the combined statement.

## Acknowledgments

This rapid response responds, with appreciation and disagreement, to Professor Jiang Xueqin's *Predictive History* lecture corpus and to the Active Inference research community at the Active Inference Institute and adjacent communities. AI drafting assistance was provided by Anthropic Claude. All editorial judgment, quotation provenance, scholarly framing, and the final synthetic argument remain with the author.
