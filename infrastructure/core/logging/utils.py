"""Logging shim for standalone use of blake_jiang.

Re-exports a logger factory compatible with ``infrastructure.core.logging.utils``
as it exists in the docxology/template workspace. Falls back to the standard
library ``logging`` module so the project's modules and tests do not need to
know which environment they are running in.
"""

from __future__ import annotations

import logging

_DEFAULT_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
_DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

_handler_installed = False


def _ensure_root_configured() -> None:
    global _handler_installed
    if _handler_installed:
        return
    root = logging.getLogger()
    if not root.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(fmt=_DEFAULT_FORMAT, datefmt=_DEFAULT_DATEFMT)
        )
        root.addHandler(handler)
        root.setLevel(logging.INFO)
    _handler_installed = True


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured logger.

    Mirrors the ``get_logger`` signature used by the docxology/template
    infrastructure package. Configures a stream handler on the root logger on
    first call so that ``info``/``debug`` calls from blake_jiang modules
    produce visible, timestamped output when run standalone.
    """
    _ensure_root_configured()
    return logging.getLogger(name or "blake_jiang")
