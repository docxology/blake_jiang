"""Regression tests for the figure renderers (real PNG I/O, no mocks)."""

from __future__ import annotations

from pathlib import Path

import pytest

from projects.blake_jiang.src.viz import (
    render_convergence_graph,
    render_fourfold_model,
    render_markov_blanket,
    render_precision_dynamics,
    render_precision_phase,
    render_timeline,
    render_triangulation,
)


_RENDERERS = [
    ("convergence_graph", render_convergence_graph),
    ("fourfold_model", render_fourfold_model),
    ("markov_blanket", render_markov_blanket),
    ("precision_dynamics", render_precision_dynamics),
    ("precision_phase", render_precision_phase),
    ("timeline", render_timeline),
    ("triangulation", render_triangulation),
]


@pytest.mark.parametrize("name,render_fn", _RENDERERS)
def test_render_writes_nonempty_light_png(tmp_path: Path, name: str, render_fn) -> None:
    out = tmp_path / f"{name}_light.png"
    render_fn(out, dark=False)
    assert out.is_file()
    assert out.stat().st_size > 1000


@pytest.mark.parametrize("name,render_fn", _RENDERERS)
def test_render_writes_nonempty_dark_png(tmp_path: Path, name: str, render_fn) -> None:
    out = tmp_path / f"{name}_dark.png"
    render_fn(out, dark=True)
    assert out.is_file()
    assert out.stat().st_size > 1000


def test_renderers_create_parent_dirs(tmp_path: Path) -> None:
    out = tmp_path / "nested" / "sub" / "convergence.png"
    render_convergence_graph(out)
    assert out.is_file()
