"""Pytest configuration for blake_jiang tests.

Forces a headless matplotlib backend, isolates the font cache, and adds the
project ``src/`` directory to ``sys.path`` for direct package imports.
"""

from __future__ import annotations

import atexit
import os
import shutil
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

if not os.environ.get("MPLCONFIGDIR"):
    _tmp_mpl_dir = tempfile.mkdtemp(prefix="matplotlib_blake_jiang_tests_")
    os.environ["MPLCONFIGDIR"] = _tmp_mpl_dir

    def _cleanup_mpl_dir() -> None:
        if os.path.exists(_tmp_mpl_dir):
            shutil.rmtree(_tmp_mpl_dir, ignore_errors=True)

    atexit.register(_cleanup_mpl_dir)


_ROOT = Path(__file__).resolve().parent.parent
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

# Also expose the repository root so ``projects.blake_jiang`` resolves.
_REPO_ROOT = _ROOT.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
