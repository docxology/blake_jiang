# `output/` — Agent Notes

Disposable. Never treat anything here as evidence or commit it. Parent:
`../AGENTS.md`. Repo-wide policy: See the lane-level policy at `/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md` (local-only tree, symlinked into the template checkout; never commit).

- `.checkpoints/pipeline_checkpoint.json` records the last completed pipeline
  stage for resume (`--resume`); it is a resume artifact, not a result. The
  checked-in snapshot is from a 2026-05-12 run completing through "Copy
  Outputs" — stale by definition; a fresh run overwrites it.
