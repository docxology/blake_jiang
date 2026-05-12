# AGENTS.md — `projects/blake_jiang/doc/`

## Purpose

Internal scholarly notes, design records, and module-level deep-dives that don't belong in the manuscript and don't belong in module docstrings. Optional but versioned with the project.

## Convention

| File | Role |
| --- | --- |
| `methodology.md` | Method, scope, exclusions, epistemic stance. |
| `quotation_provenance.md` | Source-by-source provenance for every quotation in `src/quotations.py`. |
| `convergence_node_log.md` | Per-node design history; why each was selected; rejected alternatives. |
| `figure_design.md` | Visual-design decisions for the six figures. |

## Architecture Rules

1. Scholarly notes only — no code, no test fixtures.
2. Reference modules by relative path.
3. Never duplicate the manuscript here; if content belongs in the paper, move it there.
