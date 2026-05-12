"""Twelve-node convergence graph rendered as a tripartite bipartite-style chart."""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from projects.blake_jiang.src.convergence import build_nodes
from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


def render_convergence_graph(output_path: Path, dark: bool = False) -> None:
    """Render the 12 thematic convergence nodes as horizontal bands."""
    nodes = build_nodes()

    fig, ax = plt.subplots(figsize=(16, 13), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    ax.set_title(
        "Twelve Thematic Convergences: Jiang · Blake · Friedman / Active Inference",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        pad=20,
        color="white" if dark else "black",
    )

    n = len(nodes)
    row_height = 1.0
    band_color_a = COLORS["box_fill_dark"] if dark else "#f3f4f6"
    band_color_b = COLORS["background_light"] if dark else "#ffffff"

    for i, node in enumerate(nodes):
        y = (n - 1 - i) * row_height
        band_color = band_color_a if i % 2 == 0 else band_color_b
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (0.0, y - 0.42),
                10.0,
                0.85,
                boxstyle="round,pad=0.05",
                linewidth=0.6,
                edgecolor=COLORS["border"] if dark else "#cbd5e1",
                facecolor=band_color,
                alpha=0.95,
            )
        )

        ax.text(
            0.18,
            y,
            f"#{node.node_id:02d}",
            ha="left",
            va="center",
            fontsize=MIN_FONT + 1,
            fontweight="bold",
            color=COLORS["accent"],
        )
        ax.text(
            0.7,
            y,
            node.name,
            ha="left",
            va="center",
            fontsize=MIN_FONT + 1,
            fontweight="bold",
            color=COLORS["text_light"] if dark else "black",
        )

        ax.scatter([4.4], [y], s=190, color=COLORS["jiang"], zorder=4)
        ax.scatter([5.4], [y], s=190, color=COLORS["blake"], zorder=4)
        ax.scatter([6.4], [y], s=190, color=COLORS["friedman"], zorder=4)
        ax.plot(
            [4.4, 6.4],
            [y, y],
            color=COLORS["text_muted"] if dark else "#9ca3af",
            linewidth=1.2,
            alpha=0.75,
            zorder=3,
        )

        ax.text(
            7.0,
            y,
            node.formal_counterpart,
            ha="left",
            va="center",
            fontsize=MIN_FONT - 1,
            fontstyle="italic",
            color=COLORS["text_light"] if dark else "#1f2937",
        )

    ax.text(
        0.18,
        n * row_height - 0.2,
        "Node",
        ha="left",
        va="bottom",
        fontsize=MIN_FONT,
        fontweight="bold",
        color=COLORS["text_muted"],
    )
    ax.text(
        0.7,
        n * row_height - 0.2,
        "Thematic name",
        ha="left",
        va="bottom",
        fontsize=MIN_FONT,
        fontweight="bold",
        color=COLORS["text_muted"],
    )
    ax.text(
        5.4,
        n * row_height - 0.2,
        "Three voices",
        ha="center",
        va="bottom",
        fontsize=MIN_FONT,
        fontweight="bold",
        color=COLORS["text_muted"],
    )
    ax.text(
        7.0,
        n * row_height - 0.2,
        "Active Inference counterpart",
        ha="left",
        va="bottom",
        fontsize=MIN_FONT,
        fontweight="bold",
        color=COLORS["text_muted"],
    )

    legend_patches = [
        mpatches.Patch(color=COLORS["jiang"], label="Jiang"),
        mpatches.Patch(color=COLORS["blake"], label="Blake"),
        mpatches.Patch(color=COLORS["friedman"], label="Friedman"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower center",
        ncol=3,
        fontsize=MIN_FONT,
        frameon=True,
        facecolor=COLORS["background_light"] if dark else "white",
        edgecolor=COLORS["border"] if dark else "#9ca3af",
        labelcolor=COLORS["text_light"] if dark else "black",
    )

    ax.set_xlim(-0.1, 10.2)
    ax.set_ylim(-0.7, n * row_height + 0.4)
    ax.axis("off")

    save_and_close(output_path, dark=dark, fig=fig)
