"""Chronology: Blake (1790s) → Pragmatism (1880s) → Active Inference (2003) → Jiang (2024)."""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


def render_timeline(output_path: Path, dark: bool = False) -> None:
    """Render the multi-century chronology of the convergence."""
    fig, ax = plt.subplots(figsize=(20, 9), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    ax.set_title(
        "Chronology: Prophecy · Pragmatism · Active Inference · Contemporary Critique",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        pad=18,
        color="white" if dark else "black",
    )

    ax.axhline(0, color=COLORS["text_muted"], linewidth=2.0, alpha=0.85)

    events = [
        (1789, "Songs of Innocence", COLORS["blake"], 0.9),
        (1793, "America: A Prophecy", COLORS["blake"], 1.5),
        (1794, "Songs of Experience\n& Book of Urizen", COLORS["blake"], -1.4),
        (1797, "Four Zoas (begun)", COLORS["blake"], 0.9),
        (1804, "Milton · Jerusalem (begun)", COLORS["blake"], -1.0),
        (1820, "Jerusalem (illuminated)", COLORS["blake"], 1.4),
        (1878, "Peirce: 'How to Make Our\nIdeas Clear'", COLORS["urizenic_blue"], -1.4),
        (1907, "James: Pragmatism", COLORS["urizenic_blue"], 1.0),
        (1925, "Mead: lectures on the\nself & generalized other", COLORS["urizenic_blue"], -1.0),
        (1929, "Dewey: The Quest for Certainty", COLORS["urizenic_blue"], 1.5),
        (2005, "Friston: Free Energy Principle", COLORS["eden"], -1.5),
        (2010, "Active Inference\nprocess theory", COLORS["eden"], 1.0),
        (2018, "Markov blankets of life", COLORS["eden"], -0.9),
        (2022, "Parr/Pezzulo/Friston:\nActive Inference textbook", COLORS["eden"], 1.5),
        (2024, "Jiang: Predictive History\nchannel begins", COLORS["jiang"], -1.4),
        (2026, "Friedman: Doors of Perception\n+ Before Pragmatism", COLORS["accent"], 1.3),
    ]

    for year, label, color, height in events:
        ax.vlines(year, 0, height, color=color, linewidth=2.0, alpha=0.85)
        ax.scatter([year], [height], s=120, color=color, zorder=5, edgecolor="black", linewidth=0.8)
        va = "bottom" if height > 0 else "top"
        offset = 0.12 if height > 0 else -0.12
        ax.text(
            year,
            height + offset,
            label,
            ha="center",
            va=va,
            fontsize=MIN_FONT - 1,
            color="black" if not dark else "white",
            bbox=dict(
                facecolor=COLORS["box_fill_dark"] if dark else COLORS["box_fill_light"],
                edgecolor=color,
                boxstyle="round,pad=0.35",
                alpha=0.94,
            ),
        )

    for tick in range(1780, 2031, 20):
        ax.text(
            tick,
            -0.2,
            str(tick),
            ha="center",
            va="top",
            fontsize=MIN_FONT - 1,
            color=COLORS["text_muted"],
        )
        ax.plot([tick, tick], [-0.04, 0.04], color=COLORS["text_muted"], linewidth=1.2)

    legend_patches = [
        mpatches.Patch(color=COLORS["blake"], label="Blake (1790-1820)"),
        mpatches.Patch(color=COLORS["urizenic_blue"], label="Pragmatism (Peirce, James, Mead, Dewey)"),
        mpatches.Patch(color=COLORS["eden"], label="Active Inference (Friston et al.)"),
        mpatches.Patch(color=COLORS["jiang"], label="Jiang (2024-)"),
        mpatches.Patch(color=COLORS["accent"], label="Friedman Zenodo synthesis (2026)"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower center",
        ncol=5,
        fontsize=MIN_FONT - 1,
        frameon=True,
        facecolor=COLORS["background_light"] if dark else "white",
        edgecolor=COLORS["border"] if dark else "#9ca3af",
        labelcolor=COLORS["text_light"] if dark else "black",
    )

    ax.set_xlim(1780, 2035)
    ax.set_ylim(-2.5, 2.3)
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    save_and_close(output_path, dark=dark, fig=fig)
