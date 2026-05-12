"""Tests for the quotation registry (zero-mock)."""

from __future__ import annotations

import pytest

from projects.blake_jiang.src.quotations import (
    Quotation,
    QuotationRegistry,
    SPEAKERS,
    build_registry,
)


def test_speakers_constant() -> None:
    assert SPEAKERS == ("Jiang", "Blake", "Friedman")


def test_quotation_validates_speaker() -> None:
    with pytest.raises(ValueError, match="Unknown speaker"):
        Quotation(
            quotation_id="x",
            speaker="Aristotle",
            text="anything",
            source="src",
            theme="t",
        )


def test_quotation_validates_text_nonempty() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        Quotation(
            quotation_id="x",
            speaker="Jiang",
            text="   ",
            source="src",
            theme="t",
        )


def test_quotation_validates_id_nonempty() -> None:
    with pytest.raises(ValueError, match="quotation_id"):
        Quotation(
            quotation_id=" ",
            speaker="Blake",
            text="words",
            source="src",
            theme="t",
        )


def test_registry_round_trip_by_speaker() -> None:
    reg = build_registry()
    for speaker in SPEAKERS:
        items = reg.by_speaker(speaker)
        assert items, f"Expected at least one quotation from {speaker}"
        for q in items:
            assert q.speaker == speaker


def test_registry_rejects_bad_speaker() -> None:
    reg = build_registry()
    with pytest.raises(ValueError):
        reg.by_speaker("Plato")


def test_registry_by_theme_is_case_insensitive() -> None:
    reg = build_registry()
    lowered = reg.by_theme("fourfold_vision")
    upper = reg.by_theme("FOURFOLD_VISION")
    assert lowered == upper
    assert lowered, "expected at least one fourfold-vision quote"


def test_registry_rejects_empty_theme() -> None:
    reg = build_registry()
    with pytest.raises(ValueError):
        reg.by_theme("   ")


def test_registry_by_id_round_trip() -> None:
    reg = build_registry()
    q = reg.by_id("blake_imagination_01")
    assert q.speaker == "Blake"
    assert "real & eternal World" in q.text
    assert "plate 77" in q.source


def test_registry_orc_attribution_corrected() -> None:
    """The Orc line in America is plate 6, not Boston's Angel."""
    reg = build_registry()
    q = reg.by_id("blake_orc_01")
    assert "Orc speaks" in q.source
    assert "plate 6" in q.source


def test_registry_by_id_missing_raises() -> None:
    reg = build_registry()
    with pytest.raises(KeyError):
        reg.by_id("does_not_exist")


def test_registry_themes_unique_and_nonempty() -> None:
    reg = build_registry()
    themes = reg.themes()
    assert themes
    assert len(set(themes)) == len(themes)


def test_registry_count_matches_entries() -> None:
    reg = build_registry()
    assert reg.count() == len(reg.entries)
    assert reg.count() >= 12  # Jiang 12 + Blake 7 + Friedman 6 in the canonical build


def test_registry_returns_immutable_tuple() -> None:
    reg = build_registry()
    # Quotation is frozen; registry stores a tuple.
    assert isinstance(reg.entries, tuple)
    with pytest.raises((AttributeError, Exception)):
        reg.entries[0].text = "altered"  # type: ignore[misc]


def test_registry_jiang_has_timestamps() -> None:
    reg = build_registry()
    jiang_quotes = reg.by_speaker("Jiang")
    timestamped = [q for q in jiang_quotes if q.timestamp]
    assert len(timestamped) >= 5
