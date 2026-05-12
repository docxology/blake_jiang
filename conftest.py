"""Root pytest configuration: register the standalone package aliases.

This file lets the project run both inside the docxology/template workspace
(where modules are addressed as ``projects.blake_jiang.src.<X>``) and as a
standalone repository (where the same modules live under ``src.<X>``). It
maps ``projects.blake_jiang.src``, ``projects.blake_jiang.tests``, and
``projects.blake_jiang.scripts`` onto the local layout via ``sys.modules``
aliasing, so existing imports continue to resolve without modification.
"""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
import types
from pathlib import Path

_ROOT = Path(__file__).resolve().parent

# Ensure the standalone repo root is on sys.path so that ``src``, ``tests``,
# ``scripts``, and the local ``infrastructure`` shim all resolve.
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# Headless matplotlib backend for figure tests.
os.environ.setdefault("MPLBACKEND", "Agg")


def _load_dir_as_package(name: str, path: Path) -> types.ModuleType:
    """Load a filesystem directory as a Python package, even without __init__.py."""
    pkg = types.ModuleType(name)
    pkg.__path__ = [str(path)]
    init = path / "__init__.py"
    if init.is_file():
        spec = importlib.util.spec_from_file_location(
            name, init, submodule_search_locations=pkg.__path__
        )
        if spec and spec.loader:
            spec.loader.exec_module(pkg)
    sys.modules[name] = pkg
    return pkg


def _register_alias(parent_name: str, child: str, target_dir: Path) -> None:
    """Register parent_name.child as an alias for the module loaded from target_dir."""
    if not target_dir.is_dir():
        return
    full = f"{parent_name}.{child}"
    if full in sys.modules:
        return
    try:
        loaded = importlib.import_module(child)
    except ModuleNotFoundError:
        loaded = _load_dir_as_package(child, target_dir)
    sys.modules[full] = loaded


# Build a virtual ``projects.blake_jiang`` namespace that resolves to the
# standalone layout. This preserves template-style imports such as
# ``from projects.blake_jiang.src.quotations import build_registry``.
_projects = types.ModuleType("projects")
_projects.__path__ = []  # namespace-like package
sys.modules.setdefault("projects", _projects)

_blake_jiang = types.ModuleType("projects.blake_jiang")
_blake_jiang.__path__ = [str(_ROOT)]
sys.modules["projects.blake_jiang"] = _blake_jiang

_register_alias("projects.blake_jiang", "src", _ROOT / "src")
_register_alias("projects.blake_jiang", "tests", _ROOT / "tests")
_register_alias("projects.blake_jiang", "scripts", _ROOT / "scripts")
