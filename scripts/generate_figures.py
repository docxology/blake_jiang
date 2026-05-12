"""Thin orchestrator: render all blake_jiang figures.

Calls every renderer in ``projects.blake_jiang.src.viz`` and writes both
light and dark PNG variants to ``output/figures/``.
"""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

from infrastructure.core.logging.utils import get_logger  # noqa: E402
from projects.blake_jiang.src.viz import (  # noqa: E402
    render_convergence_graph,
    render_fourfold_model,
    render_markov_blanket,
    render_precision_dynamics,
    render_precision_phase,
    render_timeline,
    render_triangulation,
)

logger = get_logger("blake_jiang.figures")


_RENDERERS = {
    "triangulation": render_triangulation,
    "convergence_graph": render_convergence_graph,
    "fourfold_model": render_fourfold_model,
    "precision_dynamics": render_precision_dynamics,
    "precision_phase": render_precision_phase,
    "timeline": render_timeline,
    "markov_blanket": render_markov_blanket,
}


def _project_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def main(output_dir: Path | None = None) -> list[Path]:
    """Render every figure in light + dark variants. Returns the file list."""
    logger.info("Starting blake_jiang figure generation pipeline...")

    figures_dir = (output_dir or _project_dir() / "output" / "figures").resolve()
    figures_dir.mkdir(parents=True, exist_ok=True)

    produced: list[Path] = []
    for name, render_fn in _RENDERERS.items():
        for dark in (False, True):
            theme = "dark" if dark else "light"
            png_path = figures_dir / f"{name}_{theme}.png"
            render_fn(png_path, dark=dark)
            produced.append(png_path)
            logger.info("Rendered %s [%s] -> %s", name, theme, png_path)
            print(str(png_path))
    return produced


if __name__ == "__main__":
    main()
