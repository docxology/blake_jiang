"""Markov-blanket diagram with Blakean labels."""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


def render_markov_blanket(output_path: Path, dark: bool = False) -> None:
    """Render the Markov blanket as Blake's doors of perception."""
    fig, ax = plt.subplots(figsize=(13, 11), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    ax.set_title(
        "The Doors of Perception are the Threshold of Prediction",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        pad=18,
        color="white" if dark else "black",
    )
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)

    outer = mpatches.Circle(
        (0, 0),
        1.25,
        facecolor=COLORS["box_fill_dark"] if dark else "#eef2ff",
        edgecolor=COLORS["urizenic_blue"],
        linewidth=2.0,
        alpha=0.45,
    )
    inner = mpatches.Circle(
        (0, 0),
        0.55,
        facecolor=COLORS["box_fill_dark"] if dark else "#fef3c7",
        edgecolor=COLORS["accent"],
        linewidth=2.0,
        alpha=0.55,
    )
    blanket = mpatches.Annulus(
        (0, 0),
        (0.95, 0.95),
        0.30,
        facecolor=COLORS["beulah"],
        edgecolor=COLORS["blake"],
        linewidth=2.2,
        alpha=0.45,
    )
    ax.add_patch(outer)
    ax.add_patch(blanket)
    ax.add_patch(inner)

    ax.text(
        0,
        0,
        "Internal\nstates\n(self / model)",
        ha="center",
        va="center",
        fontsize=MIN_FONT + 1,
        fontweight="bold",
        color=COLORS["accent"],
    )
    ax.text(
        0,
        0.78,
        "Sensory states\n(perception)",
        ha="center",
        va="center",
        fontsize=MIN_FONT,
        color=COLORS["text_light"] if dark else "black",
    )
    ax.text(
        0,
        -0.78,
        "Active states\n(action)",
        ha="center",
        va="center",
        fontsize=MIN_FONT,
        color=COLORS["text_light"] if dark else "black",
    )
    ax.text(
        0,
        1.15,
        "External states (world / other agents)",
        ha="center",
        va="center",
        fontsize=MIN_FONT,
        fontstyle="italic",
        color=COLORS["urizenic_blue"],
    )
    ax.text(
        0,
        -1.18,
        '"If the doors of perception were cleansed, every thing would appear\n'
        'to man as it is: infinite." — Blake, Marriage of Heaven & Hell',
        ha="center",
        va="center",
        fontsize=MIN_FONT - 1,
        color=COLORS["text_muted"] if dark else "#4b5563",
        fontstyle="italic",
    )

    theta = np.linspace(0.1, 2 * np.pi - 0.1, 16)
    for t in theta:
        x_out = 1.05 * np.cos(t)
        y_out = 1.05 * np.sin(t)
        x_in = 0.6 * np.cos(t)
        y_in = 0.6 * np.sin(t)
        ax.annotate(
            "",
            xy=(x_in, y_in),
            xytext=(x_out, y_out),
            arrowprops=dict(arrowstyle="->", color=COLORS["text_muted"], lw=0.9, alpha=0.7),
        )

    ax.axis("off")

    save_and_close(output_path, dark=dark, fig=fig)
