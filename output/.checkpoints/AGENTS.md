# `.checkpoints/` — Agent Notes

Single file: `pipeline_checkpoint.json` (schema: `pipeline_start_time`,
`last_stage_completed`, `stage_results[]`, `total_stages`, `checkpoint_time`).
Corrupted checkpoints are handled gracefully by the runner. Parent:
`../AGENTS.md`. Repo-wide policy: the repository root `AGENTS.md`.
