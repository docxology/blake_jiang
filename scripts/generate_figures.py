"""Thin orchestrator: render all blake_jiang figures.

Calls every renderer in ``src.viz`` and writes both
light and dark PNG variants to ``output/figures/``.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

if not __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from infrastructure.core.logging.utils import get_logger  # noqa: E402

if __package__ and "." in __package__:
    from ..src import viz
else:
    from src import viz

logger = get_logger("blake_jiang.figures")


_RENDERERS = {
    "triangulation": viz.render_triangulation,
    "convergence_graph": viz.render_convergence_graph,
    "fourfold_model": viz.render_fourfold_model,
    "precision_dynamics": viz.render_precision_dynamics,
    "precision_phase": viz.render_precision_phase,
    "timeline": viz.render_timeline,
    "markov_blanket": viz.render_markov_blanket,
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
