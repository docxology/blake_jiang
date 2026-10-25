# `infrastructure/` — Agent Notes

Minimal vendored Layer-1 surface (`core/logging/utils.py` → `get_logger`).
Do not grow this casually: the blake_jiang root `AGENTS.md` says generic
infrastructure lives here and domain logic in `src/`; anything reusable
beyond logging should go upstream to the template's real `infrastructure/`,
not be reimplemented per project. Human overview: `README.md` here.
Repo-wide policy: the repository root `AGENTS.md`.
