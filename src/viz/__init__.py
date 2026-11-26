"""Programmatic figure engine for the Blake/Jiang manuscript.

Each renderer is a pure function ``render_<name>(output_path, dark=False)``
that writes a single image to ``output_path`` and closes its matplotlib
figure cleanly.
"""

from .convergence_graph import render_convergence_graph
from .fourfold_model import render_fourfold_model
from .markov_blanket import render_markov_blanket
from .precision_dynamics import render_precision_dynamics
from .precision_phase import render_precision_phase
from .timeline import render_timeline
from .triangulation import render_triangulation

__all__ = [
    "render_convergence_graph",
    "render_fourfold_model",
    "render_markov_blanket",
    "render_precision_dynamics",
    "render_precision_phase",
    "render_timeline",
    "render_triangulation",
]
