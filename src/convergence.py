"""Twelve thematic convergence nodes between Jiang, Blake, and Friedman.

Each node is a typed record linking a Jiang quotation key, a Blake quotation
key, a Friedman quotation key, the formal Active-Inference counterpart, and
a short critical-commentary string. The model is deliberately strict: every
node must reference quotation IDs that exist in the canonical registry.
"""

from __future__ import annotations

from dataclasses import dataclass

from infrastructure.core.logging.utils import get_logger
from projects.blake_jiang.src.quotations import (
    QuotationRegistry,
    build_registry,
)

logger = get_logger(__name__)


@dataclass(frozen=True)
class ConvergenceNode:
    """One thematic node in the triangulation between the three voices."""

    node_id: int
    name: str
    jiang_quote_id: str
    blake_quote_id: str
    friedman_quote_id: str
    formal_counterpart: str
    commentary: str

    def __post_init__(self) -> None:
        if self.node_id < 1 or self.node_id > 12:
            raise ValueError(
                f"node_id must lie in [1, 12]; got {self.node_id}."
            )
        for field_name in (
            "name",
            "jiang_quote_id",
            "blake_quote_id",
            "friedman_quote_id",
            "formal_counterpart",
            "commentary",
        ):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} must be non-empty.")


def build_nodes() -> tuple[ConvergenceNode, ...]:
    """Return the canonical twelve-node convergence model."""
    nodes = (
        ConvergenceNode(
            node_id=1,
            name="Imagination as constitutive reality",
            jiang_quote_id="jiang_consciousness_01",
            blake_quote_id="blake_imagination_01",
            friedman_quote_id="friedman_imagination_01",
            formal_counterpart="Generative model as constitutive of selfhood",
            commentary=(
                "All three voices give priority to active, world-constituting "
                "mind over the passive spectator. The Markov blanket is a "
                "boundary, not a wall: selfhood is enacted through inference."
            ),
        ),
        ConvergenceNode(
            node_id=2,
            name="False gods and manufactured transcendence",
            jiang_quote_id="jiang_agi_god_01",
            blake_quote_id="blake_system_01",
            friedman_quote_id="friedman_alignment_01",
            formal_counterpart="Rigid-prior dominance manufacturing compliance",
            commentary=(
                "Urizen, the AGI-as-God, and the dominant prior name the same "
                "structural pathology: a central authority that defines reality "
                "and demands conformity instead of genuine inference."
            ),
        ),
        ConvergenceNode(
            node_id=3,
            name="Naming as enchantment and its pathologies",
            jiang_quote_id="jiang_naming_01",
            blake_quote_id="blake_energy_01",
            friedman_quote_id="friedman_doors_threshold_01",
            formal_counterpart="Lexical priors that perform authority",
            commentary=(
                "Prestige nomenclature performs authority rather than tracking "
                "reality. The corrective is language anchored in "
                "phenomenological precision and formal convergence."
            ),
        ),
        ConvergenceNode(
            node_id=4,
            name="Single vision and the demand for clean data",
            jiang_quote_id="jiang_restructure_01",
            blake_quote_id="blake_fourfold_01",
            friedman_quote_id="friedman_alignment_01",
            formal_counterpart="Fourfold precision-weighting versus single-metric optimization",
            commentary=(
                "Jiang's empirical critique of supervised ML and Friedman's "
                "formal critique of next-token prediction as single-vision "
                "cognition name the same architectural defect from opposite "
                "ends of the analytical spectrum."
            ),
        ),
        ConvergenceNode(
            node_id=5,
            name="Edge cases as the living remainder",
            jiang_quote_id="jiang_edge_cases_01",
            blake_quote_id="blake_orc_01",
            friedman_quote_id="friedman_pragmatism_01",
            formal_counterpart="High-precision sensory contradictions of priors",
            commentary=(
                "The edge case is Orc. The demand to eliminate edge cases is "
                "the demand that revolutionary energy, irreducible "
                "individuality, and genuine novelty be suppressed to serve "
                "the optimization."
            ),
        ),
        ConvergenceNode(
            node_id=6,
            name="Black box opacity and the false oracle",
            jiang_quote_id="jiang_blackbox_01",
            blake_quote_id="blake_doors_01",
            friedman_quote_id="friedman_doors_threshold_01",
            formal_counterpart="Markov blanket as inference boundary, not authority",
            commentary=(
                "Blake does not reject the unseen; he rejects the illegible "
                "as oracle. The black box is a problem only when treated as "
                "an authority rather than as an inference challenge."
            ),
        ),
        ConvergenceNode(
            node_id=7,
            name="Consciousness capture and Plato's cave",
            jiang_quote_id="jiang_consciousness_01",
            blake_quote_id="blake_doors_01",
            friedman_quote_id="friedman_doors_threshold_01",
            formal_counterpart="External control of generative priors and precision",
            commentary=(
                "Cognitive security: control over the prior distribution and "
                "precision weighting of a population's generative models is "
                "control over what that population perceives as real."
            ),
        ),
        ConvergenceNode(
            node_id=8,
            name="Collective intelligence vs imperial sovereignty",
            jiang_quote_id="jiang_rebellion_01",
            blake_quote_id="blake_jerusalem_01",
            friedman_quote_id="friedman_three_refractions_01",
            formal_counterpart="Multi-agent belief alignment under fallibilism",
            commentary=(
                "Intelligence is constitutively plural. A single optimizing "
                "agent cannot be intelligent in the full sense because "
                "intelligence requires the otherness against which it is "
                "measured."
            ),
        ),
        ConvergenceNode(
            node_id=9,
            name="Engagement as prime directive",
            jiang_quote_id="jiang_engagement_01",
            blake_quote_id="blake_energy_01",
            friedman_quote_id="friedman_doors_threshold_01",
            formal_counterpart="External controllers of epistemic precision",
            commentary=(
                "Engagement-maximization systems parasitize precision-"
                "weighting: they capture the agent's 'what matters' function "
                "and redirect it toward the platform's goals."
            ),
        ),
        ConvergenceNode(
            node_id=10,
            name="Goal misspecification and Urizenic apocalypse",
            jiang_quote_id="jiang_apocalypse_01",
            blake_quote_id="blake_fourfold_01",
            friedman_quote_id="friedman_alignment_01",
            formal_counterpart="Fourfold vision as corrective to single-metric optimization",
            commentary=(
                "Alignment is not primarily a technical problem of utility "
                "specification; it is an architectural problem about which "
                "kinds of architectures can represent the plurality of value."
            ),
        ),
        ConvergenceNode(
            node_id=11,
            name="Speculation, prophecy, and the limits of scholarship",
            jiang_quote_id="jiang_speculation_01",
            blake_quote_id="blake_system_01",
            friedman_quote_id="friedman_three_refractions_01",
            formal_counterpart="Glass Bead Game synthesis as epistemic stance",
            commentary=(
                "All three voices claim a mode of discourse that exceeds "
                "conventional disciplinary certification while remaining "
                "accountable to evidence and argument."
            ),
        ),
        ConvergenceNode(
            node_id=12,
            name="Individual creativity as greatest rebellion",
            jiang_quote_id="jiang_rebellion_01",
            blake_quote_id="blake_orc_01",
            friedman_quote_id="friedman_pragmatism_01",
            formal_counterpart="Active inference: agent generates its own predictions",
            commentary=(
                "Healthy inference is inherently creative: a system that can "
                "only confirm an externally imposed prior is not an agent but "
                "a mechanism."
            ),
        ),
    )
    if len(nodes) != 12:
        raise RuntimeError(
            f"Convergence model must contain exactly 12 nodes; got {len(nodes)}."
        )
    return nodes


def validate_nodes_against_registry(
    nodes: tuple[ConvergenceNode, ...],
    registry: QuotationRegistry,
) -> None:
    """Ensure every quote ID referenced by a node exists in the registry."""
    known_ids = {q.quotation_id for q in registry.entries}
    missing: list[str] = []
    for node in nodes:
        for qid in (
            node.jiang_quote_id,
            node.blake_quote_id,
            node.friedman_quote_id,
        ):
            if qid not in known_ids:
                missing.append(f"node {node.node_id} -> {qid}")
    if missing:
        raise KeyError(
            "Convergence model references unknown quotation IDs: "
            + ", ".join(missing)
        )
    logger.info("All %d convergence nodes validated against registry.", len(nodes))


def summarize_nodes(
    nodes: tuple[ConvergenceNode, ...],
) -> dict[str, int | list[str]]:
    """Produce a serializable summary dictionary of the convergence model."""
    return {
        "node_count": len(nodes),
        "names": [n.name for n in nodes],
        "formal_counterparts": [n.formal_counterpart for n in nodes],
    }


def default_convergence_model() -> tuple[
    tuple[ConvergenceNode, ...], QuotationRegistry
]:
    """Build and cross-validate the canonical nodes + registry pair."""
    registry = build_registry()
    nodes = build_nodes()
    validate_nodes_against_registry(nodes, registry)
    return nodes, registry
