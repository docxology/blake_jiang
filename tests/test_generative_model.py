"""Tests for the Active-Inference precision-dynamics helpers."""

from __future__ import annotations

from math import isfinite, log

import pytest

from projects.blake_jiang.src.generative_model import (
    GaussianBelief,
    PrecisionAllocation,
    canonical_regimes,
    cleansed_doors_score,
    fourfold_balance,
    gaussian_kl,
    is_newtons_sleep,
    multi_agent_consensus,
    newtons_sleep_metric,
    precision_weighted_posterior,
    prior_dominance_index,
    regime_report,
    simulate_belief_trajectory,
    variational_free_energy,
)


def test_precision_allocation_rejects_negative() -> None:
    with pytest.raises(ValueError):
        PrecisionAllocation(-1.0, 1.0, 1.0, 1.0)


def test_precision_allocation_rejects_nonfinite() -> None:
    with pytest.raises(ValueError):
        PrecisionAllocation(float("nan"), 1.0, 1.0, 1.0)


def test_precision_allocation_rejects_all_zero() -> None:
    with pytest.raises(ValueError):
        PrecisionAllocation(0.0, 0.0, 0.0, 0.0)


def test_total_and_distribution_sum_to_one() -> None:
    alloc = PrecisionAllocation(2.0, 2.0, 2.0, 2.0)
    assert alloc.total() == 8.0
    dist = alloc.as_distribution()
    assert sum(dist) == pytest.approx(1.0)
    for p in dist:
        assert p == pytest.approx(0.25)


def test_newtons_sleep_metric_parity_at_eden() -> None:
    eden = PrecisionAllocation(2.5, 2.5, 2.5, 2.5)
    # prior / (sum of three non-prior) = 2.5 / 7.5
    assert newtons_sleep_metric(eden) == pytest.approx(1.0 / 3.0)


def test_newtons_sleep_metric_dominant_prior() -> None:
    alloc = PrecisionAllocation(8.0, 1.0, 0.5, 0.5)
    # 8 / 2 = 4
    assert newtons_sleep_metric(alloc) == pytest.approx(4.0)
    assert is_newtons_sleep(alloc)


def test_newtons_sleep_metric_single_vision_infinite() -> None:
    alloc = PrecisionAllocation(5.0, 0.0, 0.0, 0.0)
    assert newtons_sleep_metric(alloc) == float("inf")
    assert is_newtons_sleep(alloc)


def test_is_newtons_sleep_rejects_negative_threshold() -> None:
    eden = PrecisionAllocation(2.5, 2.5, 2.5, 2.5)
    with pytest.raises(ValueError):
        is_newtons_sleep(eden, threshold=-0.5)


def test_fourfold_balance_max_when_equal() -> None:
    eden = PrecisionAllocation(2.5, 2.5, 2.5, 2.5)
    assert fourfold_balance(eden) == pytest.approx(log(4.0))


def test_fourfold_balance_decreases_with_dominance() -> None:
    eden = PrecisionAllocation(2.5, 2.5, 2.5, 2.5)
    sleep = PrecisionAllocation(8.0, 1.0, 0.5, 0.5)
    assert fourfold_balance(eden) > fourfold_balance(sleep)
    assert isfinite(fourfold_balance(sleep))


def test_cleansed_doors_score_bounded() -> None:
    for name, alloc in canonical_regimes().items():
        score = cleansed_doors_score(alloc)
        assert 0.0 <= score <= 1.0, f"{name} score out of bounds: {score}"


def test_cleansed_doors_score_eden_beats_sleep() -> None:
    eden = canonical_regimes()["fourfold_eden"]
    sleep = canonical_regimes()["newtons_sleep"]
    assert cleansed_doors_score(eden) > cleansed_doors_score(sleep)


def test_regime_report_shape() -> None:
    report = regime_report()
    assert len(report) == 4
    expected_keys = {
        "regime",
        "newtons_sleep_metric",
        "fourfold_balance_nats",
        "cleansed_doors_score",
        "is_newtons_sleep",
    }
    for row in report:
        assert set(row.keys()) == expected_keys
        assert isinstance(row["regime"], str)


def test_canonical_regimes_palette() -> None:
    regimes = canonical_regimes()
    assert set(regimes.keys()) == {
        "newtons_sleep",
        "twofold_generation",
        "threefold_beulah",
        "fourfold_eden",
    }


# ---------------------------------------------------------------------------
# Variational free-energy math
# ---------------------------------------------------------------------------


def test_gaussian_belief_validates_inputs() -> None:
    with pytest.raises(ValueError):
        GaussianBelief(mean=float("nan"), precision=1.0)
    with pytest.raises(ValueError):
        GaussianBelief(mean=0.0, precision=0.0)
    with pytest.raises(ValueError):
        GaussianBelief(mean=0.0, precision=-2.0)


def test_gaussian_belief_variance_inverse_precision() -> None:
    b = GaussianBelief(mean=0.0, precision=4.0)
    assert b.variance == 0.25


def test_gaussian_kl_zero_for_identical_distributions() -> None:
    b = GaussianBelief(mean=1.0, precision=2.0)
    assert gaussian_kl(b, b) == pytest.approx(0.0, abs=1e-12)


def test_gaussian_kl_positive_when_different() -> None:
    q = GaussianBelief(mean=0.0, precision=1.0)
    p = GaussianBelief(mean=2.0, precision=1.0)
    assert gaussian_kl(q, p) > 0.0


def test_precision_weighted_posterior_balanced() -> None:
    prior = GaussianBelief(mean=0.0, precision=1.0)
    evidence = GaussianBelief(mean=4.0, precision=1.0)
    post = precision_weighted_posterior(prior, evidence)
    assert post.mean == pytest.approx(2.0)
    assert post.precision == pytest.approx(2.0)


def test_precision_weighted_posterior_prior_dominant() -> None:
    """Newton's-Sleep regime: prior precision >> evidence precision → posterior ≈ prior."""
    prior = GaussianBelief(mean=0.0, precision=100.0)
    evidence = GaussianBelief(mean=10.0, precision=1.0)
    post = precision_weighted_posterior(prior, evidence)
    # Posterior mean should remain very close to the prior mean
    assert abs(post.mean - prior.mean) < 0.2
    # Posterior precision is sum of inputs
    assert post.precision == pytest.approx(101.0)


def test_variational_free_energy_finite_and_positive_at_mismatch() -> None:
    prior = GaussianBelief(mean=0.0, precision=1.0)
    evidence = GaussianBelief(mean=2.0, precision=2.0)
    q_match = precision_weighted_posterior(prior, evidence)
    F = variational_free_energy(q_match, prior, evidence)
    assert isfinite(F)


def test_variational_free_energy_decomposition_consistency() -> None:
    """A mismatched posterior should produce higher free energy than the optimal posterior."""
    prior = GaussianBelief(mean=0.0, precision=1.0)
    evidence = GaussianBelief(mean=3.0, precision=2.0)
    q_optimal = precision_weighted_posterior(prior, evidence)
    q_bad = GaussianBelief(mean=-5.0, precision=1.0)
    F_opt = variational_free_energy(q_optimal, prior, evidence)
    F_bad = variational_free_energy(q_bad, prior, evidence)
    assert F_bad > F_opt


def test_prior_dominance_index() -> None:
    prior = GaussianBelief(mean=0.0, precision=10.0)
    evidence = GaussianBelief(mean=1.0, precision=2.0)
    assert prior_dominance_index(prior, evidence) == pytest.approx(5.0)


def test_simulate_belief_trajectory_lengths_and_convergence() -> None:
    prior = GaussianBelief(mean=0.0, precision=1.0)
    evidence = GaussianBelief(mean=5.0, precision=1.0)
    traj = simulate_belief_trajectory(prior, evidence, steps=5)
    assert len(traj) == 6  # starting prior + 5 updates
    # precision grows monotonically with each absorption of evidence
    for a, b in zip(traj, traj[1:]):
        assert b.precision > a.precision
    # mean approaches evidence mean as posterior absorbs repeated evidence
    assert abs(traj[-1].mean - evidence.mean) < abs(traj[0].mean - evidence.mean)


def test_simulate_belief_trajectory_rejects_zero_steps() -> None:
    prior = GaussianBelief(mean=0.0, precision=1.0)
    evidence = GaussianBelief(mean=1.0, precision=1.0)
    with pytest.raises(ValueError):
        simulate_belief_trajectory(prior, evidence, steps=0)


def test_multi_agent_consensus_equal_weights() -> None:
    """Two equally precise agents converge on their mean midpoint."""
    a1 = GaussianBelief(mean=-1.0, precision=1.0)
    a2 = GaussianBelief(mean=1.0, precision=1.0)
    consensus = multi_agent_consensus([a1, a2])
    assert consensus.mean == pytest.approx(0.0, abs=1e-9)
    assert consensus.precision == pytest.approx(2.0)


def test_multi_agent_consensus_precision_weighted() -> None:
    """An agent with higher precision pulls the consensus toward its mean."""
    a1 = GaussianBelief(mean=0.0, precision=1.0)
    a2 = GaussianBelief(mean=10.0, precision=9.0)
    consensus = multi_agent_consensus([a1, a2])
    # 9/10 of weight on a2 → consensus near 9.0
    assert consensus.mean == pytest.approx(9.0)
    assert consensus.precision == pytest.approx(10.0)


def test_multi_agent_consensus_rejects_empty() -> None:
    with pytest.raises(ValueError):
        multi_agent_consensus([])


def test_multi_agent_consensus_rejects_mismatched_weights() -> None:
    a = GaussianBelief(mean=0.0, precision=1.0)
    with pytest.raises(ValueError):
        multi_agent_consensus([a, a], weights=[1.0])


def test_multi_agent_consensus_rejects_negative_weights() -> None:
    a = GaussianBelief(mean=0.0, precision=1.0)
    with pytest.raises(ValueError):
        multi_agent_consensus([a, a], weights=[1.0, -0.5])
