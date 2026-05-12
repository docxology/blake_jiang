"""Three-vertex triangulation: Jiang, Blake, Friedman."""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


def render_triangulation(output_path: Path, dark: bool = False) -> None:
    """Render the Jiang/Blake/Friedman triangulation diagram."""
    fig, ax = plt.subplots(figsize=(12, 11), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    vertices = {
        "Jiang": (0.5, 0.92),
        "Blake": (0.08, 0.18),
        "Friedman": (0.92, 0.18),
    }
    vertex_colors = {
        "Jiang": COLORS["jiang"],
        "Blake": COLORS["blake"],
        "Friedman": COLORS["friedman"],
    }
    vertex_subtitles = {
        "Jiang": "Speculative public lecture\nGeopolitics · Religion · AI critique",
        "Blake": "Prophetic illuminated books\n1790-1820 · Four Zoas · Single Vision",
        "Friedman": "Active Inference synthesis\nZenodo 18600041 + 18807971",
    }

    edges = [
        ("Jiang", "Blake", "Diagnostic ↔ Mythological"),
        ("Blake", "Friedman", "Phenomenological ↔ Formal"),
        ("Friedman", "Jiang", "Architectural ↔ Rhetorical"),
    ]

    for a, b, label in edges:
        xa, ya = vertices[a]
        xb, yb = vertices[b]
        ax.plot(
            [xa, xb],
            [ya, yb],
            color=COLORS["text_muted"] if dark else "#6b7280",
            linewidth=2.5,
            alpha=0.85,
        )
        midx, midy = (xa + xb) / 2, (ya + yb) / 2
        ax.text(
            midx,
            midy,
            label,
            ha="center",
            va="center",
            fontsize=MIN_FONT,
            color=COLORS["text_light"] if dark else "black",
            fontstyle="italic",
            bbox=dict(
                facecolor=COLORS["box_fill_dark"] if dark else COLORS["box_fill_light"],
                edgecolor=COLORS["border"] if dark else "#9ca3af",
                boxstyle="round,pad=0.4",
                alpha=0.92,
            ),
        )

    centroid_x = float(np.mean([v[0] for v in vertices.values()]))
    centroid_y = float(np.mean([v[1] for v in vertices.values()]))
    ax.scatter(
        [centroid_x],
        [centroid_y],
        s=320,
        color=COLORS["accent"],
        zorder=5,
        edgecolor="white" if dark else "black",
        linewidth=1.5,
    )
    ax.text(
        centroid_x,
        centroid_y - 0.07,
        "Architecture of Intelligence",
        ha="center",
        va="top",
        fontsize=MIN_FONT + 2,
        fontweight="bold",
        color=COLORS["accent"],
    )

    for name, (x, y) in vertices.items():
        ax.scatter(
            [x],
            [y],
            s=900,
            color=vertex_colors[name],
            zorder=6,
            edgecolor="black",
            linewidth=2.0,
        )
        ax.text(
            x,
            y + 0.04,
            name,
            ha="center",
            va="bottom",
            fontsize=MIN_FONT + 4,
            fontweight="bold",
            color=vertex_colors[name],
        )
        ax.text(
            x,
            y - 0.045,
            vertex_subtitles[name],
            ha="center",
            va="top",
            fontsize=MIN_FONT - 1,
            color=COLORS["text_muted"] if dark else "#374151",
        )

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0.0, 1.05)
    ax.axis("off")
    ax.set_title(
        "Triangulating the Architecture of Intelligence",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        pad=18,
        color="white" if dark else "black",
    )

    legend_patches = [
        mpatches.Patch(color=COLORS["jiang"], label="Jiang Xueqin (2024–2026)"),
        mpatches.Patch(color=COLORS["blake"], label="William Blake (1790–1820)"),
        mpatches.Patch(color=COLORS["friedman"], label="Daniel A. Friedman (2026)"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower center",
        fontsize=MIN_FONT,
        ncol=3,
        frameon=True,
        facecolor=COLORS["background_light"] if dark else "white",
        edgecolor=COLORS["border"] if dark else "#9ca3af",
        labelcolor=COLORS["text_light"] if dark else "black",
    )

    save_and_close(output_path, dark=dark, fig=fig)
