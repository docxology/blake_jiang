# `.checkpoints/` — Agent Notes

Single file: `pipeline_checkpoint.json` (schema: `pipeline_start_time`,
`last_stage_completed`, `stage_results[]`, `total_stages`, `checkpoint_time`).
Corrupted checkpoints are handled gracefully by the runner. Parent:
`../AGENTS.md`. Repo-wide policy: See the lane-level policy at `/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md` (local-only tree, symlinked into the template checkout; never commit).
