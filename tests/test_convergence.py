"""Tests for the twelve-node convergence model."""

from __future__ import annotations

import pytest

from projects.blake_jiang.src.convergence import (
    ConvergenceNode,
    build_nodes,
    default_convergence_model,
    summarize_nodes,
    validate_nodes_against_registry,
)
from projects.blake_jiang.src.quotations import QuotationRegistry, build_registry


def test_build_nodes_has_exactly_twelve() -> None:
    nodes = build_nodes()
    assert len(nodes) == 12
    ids = [n.node_id for n in nodes]
    assert ids == list(range(1, 13))


def test_node_validates_id_range() -> None:
    with pytest.raises(ValueError):
        ConvergenceNode(
            node_id=0,
            name="bad",
            jiang_quote_id="a",
            blake_quote_id="b",
            friedman_quote_id="c",
            formal_counterpart="x",
            commentary="y",
        )
    with pytest.raises(ValueError):
        ConvergenceNode(
            node_id=13,
            name="bad",
            jiang_quote_id="a",
            blake_quote_id="b",
            friedman_quote_id="c",
            formal_counterpart="x",
            commentary="y",
        )


def test_node_rejects_empty_fields() -> None:
    with pytest.raises(ValueError):
        ConvergenceNode(
            node_id=1,
            name="ok",
            jiang_quote_id=" ",
            blake_quote_id="b",
            friedman_quote_id="c",
            formal_counterpart="x",
            commentary="y",
        )


def test_summarize_nodes_yields_counts() -> None:
    nodes = build_nodes()
    summary = summarize_nodes(nodes)
    assert summary["node_count"] == 12
    assert isinstance(summary["names"], list) and len(summary["names"]) == 12
    assert isinstance(summary["formal_counterparts"], list) and len(summary["formal_counterparts"]) == 12


def test_validate_nodes_against_registry_passes() -> None:
    nodes = build_nodes()
    registry = build_registry()
    validate_nodes_against_registry(nodes, registry)


def test_validate_nodes_against_registry_fails_on_missing_id() -> None:
    bad_registry = QuotationRegistry(entries=())
    nodes = build_nodes()
    with pytest.raises(KeyError):
        validate_nodes_against_registry(nodes, bad_registry)


def test_default_convergence_model_returns_consistent_pair() -> None:
    nodes, registry = default_convergence_model()
    assert len(nodes) == 12
    assert registry.count() > 0


def test_each_node_references_three_speakers() -> None:
    nodes, registry = default_convergence_model()
    for node in nodes:
        jiang = registry.by_id(node.jiang_quote_id)
        blake = registry.by_id(node.blake_quote_id)
        friedman = registry.by_id(node.friedman_quote_id)
        assert jiang.speaker == "Jiang"
        assert blake.speaker == "Blake"
        assert friedman.speaker == "Friedman"
