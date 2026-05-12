"""Precision-dynamics bar chart contrasting four named regimes."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from projects.blake_jiang.src.generative_model import (
    canonical_regimes,
    cleansed_doors_score,
    fourfold_balance,
    newtons_sleep_metric,
)
from projects.blake_jiang.src.viz.core import COLORS, MIN_FONT, apply_style, save_and_close


_REGIME_DISPLAY = [
    ("newtons_sleep", "Newton's Sleep\n(Urizen dominant)", COLORS["ulro"]),
    ("twofold_generation", "Twofold\nGeneration", COLORS["generation"]),
    ("threefold_beulah", "Threefold\nBeulah", COLORS["beulah"]),
    ("fourfold_eden", "Fourfold\nEden", COLORS["eden"]),
]


def render_precision_dynamics(output_path: Path, dark: bool = False) -> None:
    """Render three metrics across the four canonical precision regimes."""
    regimes = canonical_regimes()

    fig, axes = plt.subplots(1, 3, figsize=(20, 7), constrained_layout=True)
    apply_style(fig, axes[0], dark=dark)
    apply_style(fig, axes[1], dark=dark)
    apply_style(fig, axes[2], dark=dark)

    fig.suptitle(
        "Precision Dynamics: from Newton's Sleep to Fourfold Eden",
        fontsize=22,
        fontweight="bold",
        fontfamily="serif",
        color="white" if dark else "black",
    )

    labels = [d[1] for d in _REGIME_DISPLAY]
    colors = [d[2] for d in _REGIME_DISPLAY]

    sleep_vals = []
    balance_vals = []
    cleansed_vals = []
    for key, _, _ in _REGIME_DISPLAY:
        alloc = regimes[key]
        sleep_vals.append(newtons_sleep_metric(alloc))
        balance_vals.append(fourfold_balance(alloc))
        cleansed_vals.append(cleansed_doors_score(alloc))

    x = np.arange(len(labels))

    axes[0].bar(x, sleep_vals, color=colors, edgecolor="black", linewidth=0.8)
    axes[0].set_title(
        "Newton's Sleep metric\n(prior / non-prior precision ratio)",
        fontsize=MIN_FONT + 1,
        color="white" if dark else "black",
    )
    axes[0].axhline(
        1.0, color=COLORS["accent"], linestyle="--", linewidth=1.5, alpha=0.85
    )
    axes[0].text(
        len(labels) - 0.5,
        1.05,
        "parity = 1.0",
        ha="right",
        va="bottom",
        color=COLORS["accent"],
        fontsize=MIN_FONT - 1,
    )

    axes[1].bar(x, balance_vals, color=colors, edgecolor="black", linewidth=0.8)
    axes[1].set_title(
        "Fourfold balance\n(Shannon entropy of precision, nats)",
        fontsize=MIN_FONT + 1,
        color="white" if dark else "black",
    )
    axes[1].axhline(
        np.log(4),
        color=COLORS["accent"],
        linestyle="--",
        linewidth=1.5,
        alpha=0.85,
    )
    axes[1].text(
        len(labels) - 0.5,
        np.log(4) + 0.02,
        "max = log 4",
        ha="right",
        va="bottom",
        color=COLORS["accent"],
        fontsize=MIN_FONT - 1,
    )

    axes[2].bar(x, cleansed_vals, color=colors, edgecolor="black", linewidth=0.8)
    axes[2].set_title(
        "Cleansed Doors score\n(balance × non-rigidity)",
        fontsize=MIN_FONT + 1,
        color="white" if dark else "black",
    )
    axes[2].set_ylim(0, 1.0)

    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=MIN_FONT - 1, color=COLORS["text_light"] if dark else "black")
        ax.tick_params(axis="y", colors=COLORS["text_light"] if dark else "black")
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        for spine in ("bottom", "left"):
            ax.spines[spine].set_color(COLORS["border"] if dark else "black")

    save_and_close(output_path, dark=dark, fig=fig)
