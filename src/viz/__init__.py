"""Programmatic figure engine for the Blake/Jiang manuscript.

Each renderer is a pure function ``render_<name>(output_path, dark=False)``
that writes a single image to ``output_path`` and closes its matplotlib
figure cleanly.
"""

from projects.blake_jiang.src.viz.convergence_graph import render_convergence_graph
from projects.blake_jiang.src.viz.fourfold_model import render_fourfold_model
from projects.blake_jiang.src.viz.markov_blanket import render_markov_blanket
from projects.blake_jiang.src.viz.precision_dynamics import render_precision_dynamics
from projects.blake_jiang.src.viz.precision_phase import render_precision_phase
from projects.blake_jiang.src.viz.timeline import render_timeline
from projects.blake_jiang.src.viz.triangulation import render_triangulation

__all__ = [
    "render_convergence_graph",
    "render_fourfold_model",
    "render_markov_blanket",
    "render_precision_dynamics",
    "render_precision_phase",
    "render_timeline",
    "render_triangulation",
]
