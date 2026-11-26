# AGENTS.md — `docs/`

## Purpose

Maintain the canonical paper, user guides, and scholarly notes here. Keep
implementation and test fixtures with their own modules.

## Convention

| File | Role |
| --- | --- |
| `methodology.md` | Method, scope, exclusions, epistemic stance. |
| `quotation_provenance.md` | Source-by-source provenance for every quotation in `src/quotations.py`. |
| `README.md` | Documentation index. |
| `development.md` | Standalone checks and pinned manuscript rendering. |
| `manuscript/` | Canonical manuscript source and render inputs. |

Add a row here when a new note lands (e.g. a per-node design history, or figure-design rationale for the seven renderers in `src/viz/`).

## Architecture Rules

1. Keep executable code and test fixtures outside this tree.
2. Reference modules by relative path.
3. Never duplicate the manuscript here; if content belongs in the paper, move it there.
