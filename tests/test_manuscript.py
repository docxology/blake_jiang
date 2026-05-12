"""Tests for the manuscript injection-data builder."""

from __future__ import annotations

from projects.blake_jiang.src.manuscript import ManuscriptBuilder


def test_builder_produces_required_keys() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    expected = {
        "node_count",
        "quotation_count",
        "speakers",
        "theme_count",
        "node_names",
        "fourfold_rows",
        "regimes",
        "newtons_sleep_metric_at_sleep",
        "newtons_sleep_metric_at_eden",
        "cleansed_doors_score_at_eden",
        "cleansed_doors_score_at_sleep",
    }
    assert expected.issubset(set(data.keys()))


def test_builder_node_count_is_twelve() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    assert data["node_count"] == 12
    assert len(data["node_names"]) == 12


def test_builder_speakers_are_three() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    assert set(data["speakers"]) == {"Jiang", "Blake", "Friedman"}


def test_builder_metrics_are_ordered_by_health() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    # Sleep metric strictly greater than Eden metric (rigid priors vs balance)
    assert data["newtons_sleep_metric_at_sleep"] > data["newtons_sleep_metric_at_eden"]
    # Eden cleansed-doors score strictly greater than Sleep score
    assert data["cleansed_doors_score_at_eden"] > data["cleansed_doors_score_at_sleep"]


def test_builder_includes_four_regime_rows() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    assert len(data["regimes"]) == 4
    keys = {row["regime"] for row in data["regimes"]}
    assert keys == {
        "newtons_sleep",
        "twofold_generation",
        "threefold_beulah",
        "fourfold_eden",
    }


def test_builder_fourfold_rows_match_zoas() -> None:
    data = ManuscriptBuilder().generate_injection_data()
    zoa_names = {row["zoa"] for row in data["fourfold_rows"]}
    assert zoa_names == {"Urizen", "Luvah", "Tharmas", "Urthona"}
