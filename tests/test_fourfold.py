"""Tests for the Four-Zoas factorized-model module."""

from __future__ import annotations

import pytest

from projects.blake_jiang.src.fourfold import (
    Zoa,
    coordination_matrix,
    four_zoas,
    fourfold_to_active_inference_table,
)


def test_zoa_validates_nonempty_fields() -> None:
    with pytest.raises(ValueError):
        Zoa(
            name=" ",
            faculty="x",
            active_inference_role="y",
            pathology_when_dominant="z",
            pathology_when_silent="w",
        )


def test_four_zoas_returns_canonical_set() -> None:
    zoas = four_zoas()
    assert len(zoas) == 4
    names = [z.name for z in zoas]
    assert names == ["Urizen", "Luvah", "Tharmas", "Urthona"]


def test_four_zoas_have_unique_faculties() -> None:
    zoas = four_zoas()
    faculties = [z.faculty for z in zoas]
    assert len(set(faculties)) == len(faculties)


def test_coordination_matrix_has_six_pairs() -> None:
    pairs = coordination_matrix()
    assert len(pairs) == 6
    seen_names: set[str] = set()
    for a, b in pairs.keys():
        seen_names.add(a)
        seen_names.add(b)
    assert seen_names == {"Urizen", "Luvah", "Tharmas", "Urthona"}


def test_coordination_matrix_descriptions_nonempty() -> None:
    pairs = coordination_matrix()
    for description in pairs.values():
        assert description.strip()


def test_fourfold_table_has_four_rows() -> None:
    rows = fourfold_to_active_inference_table()
    assert len(rows) == 4
    expected_keys = {
        "zoa",
        "faculty",
        "active_inference_role",
        "pathology_when_dominant",
        "pathology_when_silent",
    }
    for row in rows:
        assert set(row.keys()) == expected_keys
        for value in row.values():
            assert value.strip()
