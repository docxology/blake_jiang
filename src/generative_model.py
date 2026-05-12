"""Active-Inference style metrics for the Blake/Jiang argument.

Provides quantitative scaffolding for the manuscript's central thesis: that
"Newton's Sleep" is the pathology of rigid priors crushing sensory evidence,
and that "cleansed doors" is the rebalanced precision regime. Computations
are deterministic, numerically stable, and free of stochastic state.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class PrecisionAllocation:
    """A precision-weighting regime over a generative model.

    Attributes
    ----------
    prior_precision:
        Confidence assigned to top-down expectations (Urizen).
    sensory_precision:
        Confidence assigned to bottom-up evidence (Tharmas).
    affective_precision:
        Salience weight given to emotional / motivational signals (Luvah).
    imaginative_precision:
        Deep generative-model coupling, temporally extended (Urthona / Los).
    """

    prior_precision: float
    sensory_precision: float
    affective_precision: float
    imaginative_precision: float

    def __post_init__(self) -> None:
        for name, value in (
            ("prior_precision", self.prior_precision),
            ("sensory_precision", self.sensory_precision),
            ("affective_precision", self.affective_precision),
            ("imaginative_precision", self.imaginative_precision),
        ):
            if not isfinite(value):
                raise ValueError(f"{name} must be finite; got {value}.")
            if value < 0:
                raise ValueError(
                    f"{name} must be non-negative; got {value}."
                )
        if self.total() <= 0:
            raise ValueError(
                "At least one precision channel must be strictly positive."
            )

    def total(self) -> float:
        return (
            self.prior_precision
            + self.sensory_precision
            + self.affective_precision
            + self.imaginative_precision
        )

    def as_distribution(self) -> tuple[float, float, float, float]:
        """Return precisions normalized to a probability simplex."""
        z = self.total()
        return (
            self.prior_precision / z,
            self.sensory_precision / z,
            self.affective_precision / z,
            self.imaginative_precision / z,
        )


def newtons_sleep_metric(alloc: PrecisionAllocation) -> float:
    """Ratio of prior precision to non-prior precision.

    Higher values indicate Urizenic dominance — rigid priors crushing
    sensory, affective, and imaginative channels. A value of 1.0 indicates
    parity. Values strictly greater than 1.0 mark pathological prior
    dominance (Newton's Sleep). Returns ``float('inf')`` if every non-prior
    channel is zero, which is the structural definition of single vision.
    """
    non_prior = (
        alloc.sensory_precision
        + alloc.affective_precision
        + alloc.imaginative_precision
    )
    if non_prior == 0.0:
        return float("inf")
    return alloc.prior_precision / non_prior


def fourfold_balance(alloc: PrecisionAllocation) -> float:
    """Shannon entropy of the four-channel precision distribution, in nats.

    Reaches its maximum (``log 4`` ≈ 1.386) when all four Zoas carry equal
    precision (perfect Edenic balance). Approaches zero as any one channel
    dominates (Ulro / single vision).
    """
    eps = 1e-12
    h = 0.0
    for p in alloc.as_distribution():
        if p > eps:
            h -= p * log(p)
    return h


def cleansed_doors_score(alloc: PrecisionAllocation) -> float:
    """A bounded health score in [0, 1] combining balance and non-rigidity.

    score = fourfold_balance / log 4 * (1 - prior_share)

    Equals 1.0 only in the impossible limit of perfectly balanced precision
    with zero prior share, which the simplex constraint forbids; in practice
    the maximum is attained when every Zoa carries equal weight, yielding
    ``(1) * (3/4) = 0.75``.
    """
    max_h = log(4.0)
    prior_share = alloc.as_distribution()[0]
    return (fourfold_balance(alloc) / max_h) * (1.0 - prior_share)


def is_newtons_sleep(
    alloc: PrecisionAllocation, threshold: float = 1.0
) -> bool:
    """Return True when the metric exceeds the configured threshold."""
    if threshold < 0:
        raise ValueError(f"threshold must be non-negative; got {threshold}.")
    return newtons_sleep_metric(alloc) > threshold


def canonical_regimes() -> dict[str, PrecisionAllocation]:
    """A small palette of named precision regimes used by the manuscript."""
    return {
        "newtons_sleep": PrecisionAllocation(
            prior_precision=8.0,
            sensory_precision=1.0,
            affective_precision=0.5,
            imaginative_precision=0.5,
        ),
        "twofold_generation": PrecisionAllocation(
            prior_precision=3.0,
            sensory_precision=3.0,
            affective_precision=1.5,
            imaginative_precision=1.5,
        ),
        "threefold_beulah": PrecisionAllocation(
            prior_precision=2.0,
            sensory_precision=2.5,
            affective_precision=2.5,
            imaginative_precision=3.0,
        ),
        "fourfold_eden": PrecisionAllocation(
            prior_precision=2.5,
            sensory_precision=2.5,
            affective_precision=2.5,
            imaginative_precision=2.5,
        ),
    }


def regime_report() -> list[dict[str, float | str]]:
    """Tabular report of all canonical regimes with their scores."""
    report: list[dict[str, float | str]] = []
    for name, alloc in canonical_regimes().items():
        report.append(
            {
                "regime": name,
                "newtons_sleep_metric": round(newtons_sleep_metric(alloc), 4),
                "fourfold_balance_nats": round(fourfold_balance(alloc), 4),
                "cleansed_doors_score": round(cleansed_doors_score(alloc), 4),
                "is_newtons_sleep": is_newtons_sleep(alloc),
            }
        )
    logger.info("Generated regime report for %d regimes.", len(report))
    return report


# ---------------------------------------------------------------------------
# Variational free-energy mathematics
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class GaussianBelief:
    """A 1-D Gaussian distribution parameterised by mean and precision."""

    mean: float
    precision: float

    def __post_init__(self) -> None:
        if not isfinite(self.mean):
            raise ValueError(f"mean must be finite; got {self.mean}.")
        if not isfinite(self.precision):
            raise ValueError(f"precision must be finite; got {self.precision}.")
        if self.precision <= 0.0:
            raise ValueError(
                f"precision must be strictly positive; got {self.precision}."
            )

    @property
    def variance(self) -> float:
        return 1.0 / self.precision


def gaussian_kl(q: GaussianBelief, p: GaussianBelief) -> float:
    """KL divergence between two 1-D Gaussians, ``D_KL(q || p)``.

    Closed-form:

        D_KL(q || p) = 0.5 * [ log(var_p / var_q)
                             + (var_q + (mu_q - mu_p) ** 2) / var_p
                             - 1 ]
    """
    var_q = q.variance
    var_p = p.variance
    mean_term = (var_q + (q.mean - p.mean) ** 2) / var_p
    return 0.5 * (log(var_p / var_q) + mean_term - 1.0)


def precision_weighted_posterior(
    prior: GaussianBelief, evidence: GaussianBelief
) -> GaussianBelief:
    """Single-step Gaussian inference: precision-weighted average of prior and evidence.

    Posterior precision is the sum of prior and evidence precisions; the posterior
    mean is the precision-weighted average. This is the standard product-of-Gaussians
    update used as the unit cell of Bayesian / Active-Inference updating.
    """
    new_precision = prior.precision + evidence.precision
    new_mean = (
        prior.precision * prior.mean + evidence.precision * evidence.mean
    ) / new_precision
    return GaussianBelief(mean=new_mean, precision=new_precision)


def variational_free_energy(
    q: GaussianBelief, prior: GaussianBelief, evidence: GaussianBelief
) -> float:
    """Variational free energy under Gaussian approximations.

    Decomposes as ``accuracy + complexity``:

        F[q] = E_q[-log p(o | s)]  +  D_KL(q(s) || p(s))

    The first (accuracy) term penalises mismatch between predicted and observed
    sensory states. The second (complexity) term is the KL divergence between
    posterior and prior — exactly what dominates under pathological prior dominance.

    For 1-D Gaussians with ``p(o | s) = N(o; s, 1 / precision_o)`` and approximate
    posterior ``q(s) = N(s; mu_q, 1 / precision_q)``, the expected negative
    log-likelihood reduces to:

        E_q[-log p(o | s)]
            = 0.5 * [ log(2 * pi / precision_o)
                    + precision_o * (var_q + (mu_q - mu_o) ** 2) ]
    """
    import math

    var_q = q.variance
    accuracy = 0.5 * (
        math.log(2.0 * math.pi / evidence.precision)
        + evidence.precision * (var_q + (q.mean - evidence.mean) ** 2)
    )
    complexity = gaussian_kl(q, prior)
    return accuracy + complexity


def prior_dominance_index(prior: GaussianBelief, evidence: GaussianBelief) -> float:
    """Ratio of prior precision to evidence precision.

    Values >> 1 indicate the inference regime in which the prior dominates and
    the posterior is pulled toward ``prior.mean`` regardless of evidence — the
    formal analogue of Blake's Newton's Sleep at the level of a single
    inference channel.
    """
    return prior.precision / evidence.precision


def simulate_belief_trajectory(
    prior: GaussianBelief,
    evidence: GaussianBelief,
    steps: int = 8,
) -> list[GaussianBelief]:
    """Iteratively apply the precision-weighted update.

    Used to visualise how posterior beliefs evolve under repeated evidence under
    different prior-precision regimes (figure: precision_phase). The trajectory
    converges to a posterior whose precision grows linearly with ``steps`` and
    whose mean approaches a precision-weighted average of prior and evidence.
    """
    if steps < 1:
        raise ValueError(f"steps must be >= 1; got {steps}.")
    trajectory: list[GaussianBelief] = [prior]
    current = prior
    for _ in range(steps):
        current = precision_weighted_posterior(current, evidence)
        trajectory.append(current)
    return trajectory


def multi_agent_consensus(
    agents: list[GaussianBelief], weights: list[float] | None = None
) -> GaussianBelief:
    """Multi-agent belief alignment as a precision-weighted product of Gaussians.

    Implements the multi-agent Active-Inference / Peircean community-of-inquirers
    update: agents pool their beliefs through a precision-weighted average, with
    each agent contributing in proportion to its precision (or to an externally
    supplied weight). The consensus precision is the sum of the individual
    precisions (optionally weighted).
    """
    if not agents:
        raise ValueError("must supply at least one agent belief.")
    if weights is None:
        weights = [1.0] * len(agents)
    if len(weights) != len(agents):
        raise ValueError(
            f"weights ({len(weights)}) must align with agents ({len(agents)})."
        )
    if any(w < 0 for w in weights):
        raise ValueError("weights must be non-negative.")
    total_precision = sum(w * a.precision for w, a in zip(weights, agents))
    if total_precision <= 0.0:
        raise ValueError("total weighted precision must be strictly positive.")
    weighted_mean = (
        sum(w * a.precision * a.mean for w, a in zip(weights, agents))
        / total_precision
    )
    return GaussianBelief(mean=weighted_mean, precision=total_precision)
