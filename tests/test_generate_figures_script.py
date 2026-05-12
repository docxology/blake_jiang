"""Zero-mock tests for the generate_figures.py thin orchestrator."""

from __future__ import annotations

from pathlib import Path

from projects.blake_jiang.scripts.generate_figures import main as figures_main


def test_generate_figures_produces_fourteen_files(tmp_path: Path) -> None:
    """Seven renderers × {light, dark} = 14 PNG files."""
    produced = figures_main(output_dir=tmp_path)
    assert len(produced) == 14
    for path in produced:
        assert path.is_file()
        assert path.stat().st_size > 1000


def test_generate_figures_creates_expected_names(tmp_path: Path) -> None:
    produced = figures_main(output_dir=tmp_path)
    names = sorted(p.name for p in produced)
    expected_prefixes = {
        "triangulation",
        "convergence_graph",
        "fourfold_model",
        "precision_dynamics",
        "precision_phase",
        "timeline",
        "markov_blanket",
    }
    for prefix in expected_prefixes:
        assert f"{prefix}_light.png" in names
        assert f"{prefix}_dark.png" in names
