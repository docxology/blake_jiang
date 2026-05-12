# AGENTS.md — `projects/blake_jiang/scripts/`

## Purpose

**Thin orchestrators** only. Every script here must follow the Thin Orchestrator Pattern: no business logic, only I/O and orchestration.

## Scripts

| File | Imports from | Writes to | What it does |
| --- | --- | --- | --- |
| `analyze.py` | `projects.blake_jiang.src.manuscript.ManuscriptBuilder` | `output/data/manuscript_injection.json` | Builds the manuscript-injection dictionary (12-node summary, fourfold mapping, regime metrics) and serializes it. |
| `generate_figures.py` | `projects.blake_jiang.src.viz.*` | `output/figures/<name>_<theme>.png` | Renders all 6 figures in light + dark themes (12 PNG files total). |
| `__init__.py` | — | — | Package marker (empty). |

## Architecture Rules

1. **Logic-free.** Scripts coordinate; modules implement. Anything resembling analysis must move into `src/`.
2. **Deterministic output paths.** Both scripts accept an optional `output_dir` parameter so tests can redirect to `tmp_path`; if omitted, the script writes under `projects/blake_jiang/output/`.
3. **Headless matplotlib.** `generate_figures.py` sets `MPLBACKEND=Agg` before importing `matplotlib`.
4. **Print discoverable paths.** Each script prints absolute paths of artifacts produced to stdout so the root pipeline's manifest collector can pick them up.
5. **Idempotent.** Running a script twice with the same output dir must yield byte-identical (data) or visually-identical (figures) results.

## Don't

- Don't add a script that wraps a single call from `src/` — call the module directly.
- Don't read data from `output/` to drive another stage — the pipeline DAG, not the scripts, owns inter-stage data flow.
- Don't catch exceptions broadly — let failures propagate so the pipeline records them.
