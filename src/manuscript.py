"""Manuscript injection-data builder for the Blake/Jiang project.

Collects deterministic figures and tabular data from the analysis modules
into a single dictionary suitable for templating into Markdown and LaTeX.
"""

from __future__ import annotations

from typing import Any

from infrastructure.core.logging.utils import get_logger

from projects.blake_jiang.src.convergence import default_convergence_model
from projects.blake_jiang.src.fourfold import fourfold_to_active_inference_table
from projects.blake_jiang.src.generative_model import (
    canonical_regimes,
    cleansed_doors_score,
    newtons_sleep_metric,
    regime_report,
)

logger = get_logger(__name__)


class ManuscriptBuilder:
    """Build a single serializable dictionary for manuscript injection."""

    def __init__(self) -> None:
        self.nodes, self.registry = default_convergence_model()
        logger.debug(
            "ManuscriptBuilder initialized with %d nodes and %d quotations",
            len(self.nodes),
            self.registry.count(),
        )

    def generate_injection_data(self) -> dict[str, Any]:
        """Return the full set of computed manuscript figures."""
        regimes = canonical_regimes()
        eden = regimes["fourfold_eden"]
        sleep = regimes["newtons_sleep"]

        payload: dict[str, Any] = {
            "node_count": len(self.nodes),
            "quotation_count": self.registry.count(),
            "speakers": list(set(q.speaker for q in self.registry.entries)),
            "theme_count": len(self.registry.themes()),
            "node_names": [n.name for n in self.nodes],
            "fourfold_rows": fourfold_to_active_inference_table(),
            "regimes": regime_report(),
            "newtons_sleep_metric_at_sleep": round(
                newtons_sleep_metric(sleep), 4
            ),
            "newtons_sleep_metric_at_eden": round(
                newtons_sleep_metric(eden), 4
            ),
            "cleansed_doors_score_at_eden": round(
                cleansed_doors_score(eden), 4
            ),
            "cleansed_doors_score_at_sleep": round(
                cleansed_doors_score(sleep), 4
            ),
        }
        logger.info(
            "Generated manuscript injection data with %d keys",
            len(payload),
        )
        return payload
