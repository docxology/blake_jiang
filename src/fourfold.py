"""The Four Zoas as a factorized generative-model architecture.

The Zoas — Urizen (reason), Luvah (passion), Tharmas (sensation), Urthona /
Los (imagination) — function as Blake's proto-cognitive architecture. This
module makes the correspondence explicit and provides utilities for the
manuscript and the viz engine.
"""

from __future__ import annotations

from dataclasses import dataclass

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class Zoa:
    """A single Zoa and its formal counterpart in Active Inference."""

    name: str
    faculty: str
    active_inference_role: str
    pathology_when_dominant: str
    pathology_when_silent: str

    def __post_init__(self) -> None:
        for value in (
            self.name,
            self.faculty,
            self.active_inference_role,
            self.pathology_when_dominant,
            self.pathology_when_silent,
        ):
            if not value.strip():
                raise ValueError("All Zoa fields must be non-empty.")


def four_zoas() -> tuple[Zoa, Zoa, Zoa, Zoa]:
    """Return the canonical four Zoas in their architectural roles."""
    zoas = (
        Zoa(
            name="Urizen",
            faculty="Reason / law",
            active_inference_role=(
                "Prior beliefs and top-down generative-model expectations"
            ),
            pathology_when_dominant=(
                "Newton's Sleep: rigid priors crush sensory evidence"
            ),
            pathology_when_silent=(
                "Loss of structural coherence; flooded by uninterpreted "
                "sensation"
            ),
        ),
        Zoa(
            name="Luvah",
            faculty="Passion / emotion",
            active_inference_role=(
                "Affective precision-weighting and motivational salience"
            ),
            pathology_when_dominant=(
                "Affective dysregulation; surrender to volatile valuation"
            ),
            pathology_when_silent=(
                "Anhedonia; loss of motivational selection over policies"
            ),
        ),
        Zoa(
            name="Tharmas",
            faculty="Bodily sensation",
            active_inference_role=(
                "Sensory evidence integration at the Markov blanket"
            ),
            pathology_when_dominant=(
                "Overweighting of raw sensation; failure to abstract"
            ),
            pathology_when_silent=(
                "Disembodied abstraction; loss of grounding"
            ),
        ),
        Zoa(
            name="Urthona",
            faculty="Imagination (Los as its temporal-incarnate aspect)",
            active_inference_role=(
                "Deep generative model: temporally extended imagination "
                "that constitutes selfhood"
            ),
            pathology_when_dominant=(
                "Untethered fantasy; loss of fit with sensory evidence"
            ),
            pathology_when_silent=(
                "Mechanism without mind; loss of counterfactual planning"
            ),
        ),
    )
    return zoas


def coordination_matrix() -> dict[tuple[str, str], str]:
    """Pairwise coordination requirements among the Zoas.

    Each entry describes the structural function served when the two Zoas
    co-vary in healthy precision, articulating the Blakean insistence that
    no Zoa can stand alone.
    """
    z = four_zoas()
    names = [zoa.name for zoa in z]
    pairs = {
        ("Urizen", "Luvah"): (
            "Reason tempered by motivational salience: priors that follow "
            "what matters."
        ),
        ("Urizen", "Tharmas"): (
            "Top-down expectations meeting bottom-up evidence at the blanket."
        ),
        ("Urizen", "Urthona"): (
            "Law informed by imaginative possibility; structure that allows "
            "counterfactual planning."
        ),
        ("Luvah", "Tharmas"): (
            "Embodied affect: feelings grounded in sensory states."
        ),
        ("Luvah", "Urthona"): (
            "Desire animating imagination; valuation guiding policy search."
        ),
        ("Tharmas", "Urthona"): (
            "Sensory evidence informing deep generative inference."
        ),
    }
    if set(p[0] for p in pairs) | set(p[1] for p in pairs) != set(names):
        raise RuntimeError("Coordination matrix missing a Zoa.")
    return pairs


def fourfold_to_active_inference_table() -> list[dict[str, str]]:
    """Tabular mapping used by the manuscript and figure renderers."""
    rows: list[dict[str, str]] = []
    for zoa in four_zoas():
        rows.append(
            {
                "zoa": zoa.name,
                "faculty": zoa.faculty,
                "active_inference_role": zoa.active_inference_role,
                "pathology_when_dominant": zoa.pathology_when_dominant,
                "pathology_when_silent": zoa.pathology_when_silent,
            }
        )
    logger.info("Generated fourfold-to-AI mapping table with %d rows", len(rows))
    return rows
