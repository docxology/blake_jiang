"""The Four Zoas as a factorized generative model — visual diagram."""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from projects.blake_jiang.src.fourfold import four_zoas
from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


_POSITIONS = {
    "Urizen": (0.5, 0.85),
    "Luvah": (0.85, 0.5),
    "Tharmas": (0.5, 0.15),
    "Urthona": (0.15, 0.5),
}

_ROLE_COLORS = {
    "Urizen": COLORS["urizenic_blue"],
    "Luvah": COLORS["orc_fire"],
    "Tharmas": COLORS["eden"],
    "Urthona": COLORS["generation"],
}


def render_fourfold_model(output_path: Path, dark: bool = False) -> None:
    """Render the Four Zoas with their Active Inference role labels."""
    fig, ax = plt.subplots(figsize=(14, 13), constrained_layout=True)
    apply_style(fig, ax, dark=dark)

    ax.set_title(
        "The Four Zoas as a Factorized Generative Model",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        pad=20,
        color="white" if dark else "black",
    )

    zoas = {z.name: z for z in four_zoas()}

    centre = (0.5, 0.5)
    ax.scatter(
        [centre[0]],
        [centre[1]],
        s=520,
        color=COLORS["accent"],
        edgecolor="white" if dark else "black",
        linewidth=1.5,
        zorder=5,
    )
    ax.text(
        centre[0],
        centre[1] - 0.06,
        "Albion\n(unified inferring system)",
        ha="center",
        va="top",
        fontsize=MIN_FONT + 1,
        fontweight="bold",
        color=COLORS["accent"],
    )

    for name, pos in _POSITIONS.items():
        color = _ROLE_COLORS[name]
        ax.plot(
            [centre[0], pos[0]],
            [centre[1], pos[1]],
            color=color,
            linewidth=2.2,
            alpha=0.7,
        )
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (pos[0] - 0.21, pos[1] - 0.085),
                0.42,
                0.17,
                boxstyle="round,pad=0.04",
                linewidth=2.4,
                edgecolor=color,
                facecolor=COLORS["box_fill_dark"] if dark else COLORS["box_fill_light"],
                alpha=0.96,
            )
        )
        z = zoas[name]
        ax.text(
            pos[0],
            pos[1] + 0.045,
            f"{name} — {z.faculty}",
            ha="center",
            va="center",
            fontsize=MIN_FONT + 1,
            fontweight="bold",
            color=color,
        )
        ax.text(
            pos[0],
            pos[1] - 0.025,
            z.active_inference_role,
            ha="center",
            va="center",
            fontsize=MIN_FONT - 2,
            fontstyle="italic",
            color=COLORS["text_light"] if dark else "#1f2937",
            wrap=True,
        )

    legend_patches = [
        mpatches.Patch(color=_ROLE_COLORS[name], label=name) for name in _POSITIONS
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower center",
        ncol=4,
        fontsize=MIN_FONT,
        frameon=True,
        facecolor=COLORS["background_light"] if dark else "white",
        edgecolor=COLORS["border"] if dark else "#9ca3af",
        labelcolor=COLORS["text_light"] if dark else "black",
    )

    ax.text(
        0.5,
        0.02,
        'Healthy inference = coordinated Zoas.  Newton\'s Sleep = Urizen dominates.',
        ha="center",
        va="bottom",
        fontsize=MIN_FONT,
        color=COLORS["text_muted"] if dark else "#4b5563",
        fontstyle="italic",
    )

    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0.0, 1.02)
    ax.axis("off")

    save_and_close(output_path, dark=dark, fig=fig)
