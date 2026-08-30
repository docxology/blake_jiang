# `.checkpoints/` — Pipeline Resume State

Holds `pipeline_checkpoint.json`, written by the template pipeline runner
after each successful stage and read by `--resume`. Disposable; safe to
delete when no pipeline is running.
