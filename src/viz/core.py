"""Shared styling and persistence helpers for the Blake/Jiang figures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt


COLORS = {
    "primary": "#1D3557",
    "accent": "#E63946",
    "background": "#0d1117",
    "background_light": "#1a202c",
    "ulro": "#d9534f",
    "generation": "#f0ad4e",
    "beulah": "#5bc0de",
    "eden": "#5cb85c",
    "orc_fire": "#fc8181",
    "urizenic_blue": "#63b3ed",
    "text_light": "#e2e8f0",
    "text_muted": "#a0aec0",
    "grid": "#2d3748",
    "border": "#4a5568",
    "jiang": "#ed64a6",
    "blake": "#f6e05e",
    "friedman": "#5bc0de",
    "box_fill_dark": "#1a202c",
    "box_fill_light": "#f7fafc",
}

MIN_FONT = 14


def apply_style(fig: plt.Figure, ax: plt.Axes, dark: bool = False) -> None:
    """Apply the shared facecolor + style to a matplotlib figure/axes pair."""
    if dark:
        plt.style.use("dark_background")
        bg = COLORS["background"]
    else:
        plt.style.use("default")
        bg = "white"
    fig.set_facecolor(bg)
    ax.set_facecolor(bg)


def save_and_close(
    output_path: Path,
    dark: bool = False,
    fig: plt.Figure | None = None,
    **savefig_kwargs: Any,
) -> None:
    """Save the figure at 200 DPI and close it cleanly."""
    bg = COLORS["background"] if dark else "white"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    target = fig if fig is not None else plt.gcf()
    kwargs = {"dpi": 200, "bbox_inches": "tight", "facecolor": bg}
    kwargs.update(savefig_kwargs)
    target.savefig(output_path, **kwargs)
    plt.close(target)
