# `infrastructure/core/logging/` — Logging Helper

`utils.py` provides `get_logger(name=None)` plus `_ensure_root_configured()`,
which lazily configures the root logger so every module gets consistent,
pipeline-friendly logging without per-module setup.

```python
from infrastructure.core.logging.utils import get_logger
log = get_logger(__name__)
```
