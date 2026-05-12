"""Precision-phase trajectories under different prior-dominance regimes.

Shows belief trajectories converging to a fixed sensory observation under
three prior-precision regimes: pathological (Newton's Sleep), balanced
(twofold), and evidence-dominant (cleansed doors). The geometry of the
trajectories in (mean, precision) space makes the Blake/Active-Inference
mapping legible at a glance.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from projects.blake_jiang.src.generative_model import (
    GaussianBelief,
    simulate_belief_trajectory,
)
from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


def render_precision_phase(output_path: Path, dark: bool = False) -> None:
    """Render belief trajectories in (mean, precision) phase space."""
    fig, ax = plt.subplots(figsize=(12, 9), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    ax.set_title(
        "Belief Trajectories Under Three Prior-Precision Regimes",
        fontsize=20,
        fontweight="bold",
        fontfamily="serif",
        pad=18,
        color="white" if dark else "black",
    )

    evidence = GaussianBelief(mean=5.0, precision=1.0)

    regimes = [
        (
            "Newton's Sleep (prior dominant)",
            GaussianBelief(mean=0.0, precision=8.0),
            COLORS["ulro"],
        ),
        (
            "Twofold (parity)",
            GaussianBelief(mean=0.0, precision=1.0),
            COLORS["generation"],
        ),
        (
            "Cleansed Doors (evidence-weighted)",
            GaussianBelief(mean=0.0, precision=0.25),
            COLORS["eden"],
        ),
    ]

    for label, prior, color in regimes:
        traj = simulate_belief_trajectory(prior, evidence, steps=10)
        means = [b.mean for b in traj]
        precisions = [b.precision for b in traj]
        ax.plot(
            means,
            precisions,
            "-o",
            color=color,
            linewidth=2.2,
            markersize=8,
            markeredgecolor="black",
            markeredgewidth=0.8,
            label=label,
            alpha=0.92,
        )
        # Annotate start
        ax.annotate(
            "prior",
            xy=(means[0], precisions[0]),
            xytext=(means[0] - 0.6, precisions[0] + 0.4),
            fontsize=MIN_FONT - 2,
            color=color,
        )

    # Evidence mean line
    ax.axvline(
        evidence.mean,
        color=COLORS["accent"],
        linestyle="--",
        linewidth=1.6,
        alpha=0.75,
    )
    ax.text(
        evidence.mean + 0.05,
        ax.get_ylim()[1] if ax.get_ylim()[1] > 1 else 12,
        "evidence mean (μ = 5)",
        ha="left",
        va="top",
        color=COLORS["accent"],
        fontsize=MIN_FONT - 1,
        rotation=90,
    )

    ax.set_xlabel(
        "Posterior mean μ_q",
        fontsize=MIN_FONT,
        color=COLORS["text_light"] if dark else "black",
    )
    ax.set_ylabel(
        "Posterior precision π_q",
        fontsize=MIN_FONT,
        color=COLORS["text_light"] if dark else "black",
    )
    ax.tick_params(axis="both", colors=COLORS["text_light"] if dark else "black")
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("bottom", "left"):
        ax.spines[spine].set_color(COLORS["border"] if dark else "black")

    ax.grid(True, alpha=0.18, linestyle=":")
    ax.legend(
        loc="upper left",
        fontsize=MIN_FONT - 1,
        frameon=True,
        facecolor=COLORS["background_light"] if dark else "white",
        edgecolor=COLORS["border"] if dark else "#9ca3af",
        labelcolor=COLORS["text_light"] if dark else "black",
    )

    ax.text(
        0.5,
        -0.12,
        "Each trajectory is 10 steps of precision-weighted Bayesian update on a fixed evidence stream.\n"
        "Newton's Sleep stays anchored to the prior; Cleansed Doors converges to the evidence mean within a few updates.",
        ha="center",
        va="top",
        transform=ax.transAxes,
        fontsize=MIN_FONT - 2,
        color=COLORS["text_muted"] if dark else "#4b5563",
        fontstyle="italic",
    )

    save_and_close(output_path, dark=dark, fig=fig)
