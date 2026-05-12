"""Quotation registry for the Jiang / Blake / Friedman triangulation.

Holds authoritative quotations with attributed source, speaker, timestamp
(where applicable), and thematic key. The registry is the single source of
truth used by the manuscript build, the convergence analysis, and the viz
engine. No mocking, no fuzzy parsing: every quotation is a typed
``Quotation`` record with stable identity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


SPEAKERS = ("Jiang", "Blake", "Friedman")


@dataclass(frozen=True)
class Quotation:
    """A single attributed quotation."""

    quotation_id: str
    speaker: str
    text: str
    source: str
    theme: str
    timestamp: str = ""

    def __post_init__(self) -> None:
        if self.speaker not in SPEAKERS:
            raise ValueError(
                f"Unknown speaker '{self.speaker}'. Expected one of {SPEAKERS}."
            )
        if not self.text.strip():
            raise ValueError("Quotation text must be non-empty.")
        if not self.quotation_id.strip():
            raise ValueError("quotation_id must be non-empty.")


@dataclass(frozen=True)
class QuotationRegistry:
    """An immutable registry of attributed quotations."""

    entries: tuple[Quotation, ...] = field(default_factory=tuple)

    def by_speaker(self, speaker: str) -> tuple[Quotation, ...]:
        if speaker not in SPEAKERS:
            raise ValueError(
                f"Unknown speaker '{speaker}'. Expected one of {SPEAKERS}."
            )
        return tuple(q for q in self.entries if q.speaker == speaker)

    def by_theme(self, theme: str) -> tuple[Quotation, ...]:
        key = theme.strip().lower()
        if not key:
            raise ValueError("theme must be non-empty.")
        return tuple(q for q in self.entries if q.theme.lower() == key)

    def by_id(self, quotation_id: str) -> Quotation:
        for q in self.entries:
            if q.quotation_id == quotation_id:
                return q
        raise KeyError(f"No quotation with id '{quotation_id}'.")

    def themes(self) -> tuple[str, ...]:
        seen: list[str] = []
        for q in self.entries:
            if q.theme not in seen:
                seen.append(q.theme)
        return tuple(seen)

    def count(self) -> int:
        return len(self.entries)


def _build_jiang() -> Iterable[Quotation]:
    return [
        Quotation(
            quotation_id="jiang_speculation_01",
            speaker="Jiang",
            text=(
                "It's very important for us to remember this fact that this is a "
                "class about intellectual speculation here. We explore ideas that "
                "are not explored anywhere else and often I will wing it or I "
                "will make things up as I go along based on my intuition and "
                "based on my imagination and it's very interesting but it's not "
                "scholarship."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="1:35-1:50",
            theme="speculation",
        ),
        Quotation(
            quotation_id="jiang_religion_01",
            speaker="Jiang",
            text=(
                "If you really want to change the world if you really want to "
                "build an empire you need to start a religion. And so a company "
                "is just a vessel in which to incubate this religion."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="13:00-13:16",
            theme="false_god",
        ),
        Quotation(
            quotation_id="jiang_agi_god_01",
            speaker="Jiang",
            text=(
                "What is AI? What is artificial intelligence? What is AGI? And "
                "the answer, of course, is it's God."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="15:15-15:31",
            theme="false_god",
        ),
        Quotation(
            quotation_id="jiang_hallucination_01",
            speaker="Jiang",
            text=(
                "The trick, and this is really important to understand, guys, is "
                "it's trying to trick you. It's not trying to teach you. It's "
                "not trying to tell you the truth. It's trying to trick you into "
                "believing it. That's what we call hallucination."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="21:05-21:23",
            theme="manufactured_conviction",
        ),
        Quotation(
            quotation_id="jiang_naming_01",
            speaker="Jiang",
            text=(
                "The real reason is you're trying to with these names create "
                "God. Okay? It's what we call the occult."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="27:08-27:20",
            theme="naming_enchantment",
        ),
        Quotation(
            quotation_id="jiang_edge_cases_01",
            speaker="Jiang",
            text=(
                "The great danger to the system is what we call edge cases. "
                "Edge cases breaks the system down."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="29:57-30:10",
            theme="edge_cases",
        ),
        Quotation(
            quotation_id="jiang_restructure_01",
            speaker="Jiang",
            text=(
                "AI if it is to be effective, it demands that we fundamentally "
                "restructure human society to benefit AI, taking away the "
                "individuality, the diversity and the autonomy of human beings."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="31:30-31:55",
            theme="single_vision",
        ),
        Quotation(
            quotation_id="jiang_blackbox_01",
            speaker="Jiang",
            text=(
                "Pop open the hood of a deep learning model and inside are only "
                "highly abstracted daisy chain of numbers. This is what "
                "researchers mean when they call deep learning a black box."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="33:08-33:26",
            theme="black_box",
        ),
        Quotation(
            quotation_id="jiang_apocalypse_01",
            speaker="Jiang",
            text=(
                "The real apocalypse is the people in charge are so convinced "
                "that AI will save the world that they will destroy it in order "
                "to make it possible."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="1:01:44-1:02:10",
            theme="goal_misspecification",
        ),
        Quotation(
            quotation_id="jiang_engagement_01",
            speaker="Jiang",
            text=(
                "The point of Chachi BT is to get you to like it. The point of "
                "Chachi BT is to get you to use it. Intensity and engagement. "
                "That is the prime directive."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="38:37-38:53",
            theme="engagement",
        ),
        Quotation(
            quotation_id="jiang_consciousness_01",
            speaker="Jiang",
            text=(
                "The true wealth in society is consciousness. The only thing "
                "that exists really in this world is consciousness. Power is the "
                "capacity to direct people's consciousness to create reality "
                "itself."
            ),
            source="Predictive History lecture (paste.txt)",
            timestamp="55:00-55:26",
            theme="consciousness_capture",
        ),
        Quotation(
            quotation_id="jiang_rebellion_01",
            speaker="Jiang",
            text=(
                "Your greatest act of rebellion is to deny the reality before "
                "you and establish your own reality. If everyone did that the "
                "system would collapse."
            ),
            source="They Control Your Mind Through Money & AI (YouTube)",
            timestamp="closing",
            theme="creative_rebellion",
        ),
    ]


def _build_blake() -> Iterable[Quotation]:
    return [
        Quotation(
            quotation_id="blake_doors_01",
            speaker="Blake",
            text=(
                "If the doors of perception were cleansed every thing would "
                "appear to man as it is, infinite. For man has closed himself "
                "up, till he sees all things thro' narrow chinks of his cavern."
            ),
            source=(
                "The Marriage of Heaven and Hell, plate 14 "
                "(c. 1790-1793); Erdman E 39"
            ),
            theme="boundary",
        ),
        Quotation(
            quotation_id="blake_energy_01",
            speaker="Blake",
            text=(
                "Energy is the only life and is from the Body[,] and Reason "
                "is the bound or outward circumference of Energy."
            ),
            source=(
                "The Marriage of Heaven and Hell, plate 4 — 'The Voice of "
                "the Devil' (c. 1790-1793); Erdman E 34"
            ),
            theme="fourfold_vision",
        ),
        Quotation(
            quotation_id="blake_fourfold_01",
            speaker="Blake",
            text=(
                "Now I a fourfold vision see, / And a fourfold vision is given "
                "to me; / 'Tis fourfold in my supreme delight / And threefold "
                "in soft Beulah's night / And twofold Always. May God us keep / "
                "From Single vision & Newton's sleep!"
            ),
            source=(
                "Letter to Thomas Butts, 22 November 1802; Erdman E 722"
            ),
            theme="fourfold_vision",
        ),
        Quotation(
            quotation_id="blake_imagination_01",
            speaker="Blake",
            text=(
                "Imagination[,] the real & eternal World of which this "
                "Vegetable Universe is but a faint shadow & in which we shall "
                "live in our Eternal or Imaginative Bodies, when these "
                "Vegetable Mortal Bodies are no more."
            ),
            source=(
                "Jerusalem: The Emanation of the Giant Albion, plate 77 "
                "'To the Christians' (1804-1820); Erdman E 231"
            ),
            theme="constitutive_imagination",
        ),
        Quotation(
            quotation_id="blake_system_01",
            speaker="Blake",
            text=(
                "I must Create a System, or be enslav'd by another Man's[;] "
                "I will not Reason & Compare: my business is to Create."
            ),
            source=(
                "Jerusalem: The Emanation of the Giant Albion, ch. 1, "
                "plate 10, lines 20-21; Erdman E 153"
            ),
            theme="speculation",
        ),
        Quotation(
            quotation_id="blake_orc_01",
            speaker="Blake",
            text=(
                "The morning comes, the night decays, the watchmen leave "
                "their stations… For Empire is no more, and now the Lion & "
                "Wolf shall cease."
            ),
            source=(
                "America: A Prophecy (1793), plate 6 — Orc speaks; "
                "Erdman E 53"
            ),
            theme="creative_rebellion",
        ),
        Quotation(
            quotation_id="blake_jerusalem_01",
            speaker="Blake",
            text=(
                "I will not cease from Mental Fight, / Nor shall my Sword "
                "sleep in my hand: / Till we have built Jerusalem, / In "
                "Englands green & pleasant Land."
            ),
            source=(
                "Milton: A Poem in 2 Books, preface (1804-1810); "
                "Erdman E 95-96"
            ),
            theme="fourfold_vision",
        ),
    ]


def _build_friedman() -> Iterable[Quotation]:
    return [
        Quotation(
            quotation_id="friedman_doors_threshold_01",
            speaker="Friedman",
            text=(
                "Blake's 'doors' are statistical boundaries separating self "
                "from world; his 'Newton's sleep' is the pathology of rigid "
                "priors crushing sensory evidence; his 'fourfold vision' maps "
                "onto hierarchical precision-weighting across processing "
                "depths."
            ),
            source=(
                "The Doors of Perception are the Threshold of Prediction "
                "(Zenodo 18600041, 2026)"
            ),
            theme="boundary",
        ),
        Quotation(
            quotation_id="friedman_imagination_01",
            speaker="Friedman",
            text=(
                "Blake's insistence that 'Imagination is the Human Existence "
                "itself' anticipates the insight that selfhood is constituted "
                "by the generative model."
            ),
            source=(
                "The Doors of Perception are the Threshold of Prediction "
                "(Zenodo 18600041, 2026)"
            ),
            theme="constitutive_imagination",
        ),
        Quotation(
            quotation_id="friedman_zoas_01",
            speaker="Friedman",
            text=(
                "The Four Zoas — Urizen, Luvah, Tharmas, Urthona — function as "
                "Blake's proto-cognitive architecture, anticipating the "
                "factorized generative model of Active Inference where reason, "
                "passion, sensation, and imagination must coordinate or the "
                "system fragments into what Blake names 'Newton's Sleep.'"
            ),
            source=(
                "Before Pragmatism Had a Name (Zenodo 18807971, 2026)"
            ),
            theme="fourfold_vision",
        ),
        Quotation(
            quotation_id="friedman_pragmatism_01",
            speaker="Friedman",
            text=(
                "Orc's revolutionary fire maps onto Peirce's irritation of "
                "doubt that compels inquiry; the Thirteen Angels' collective "
                "transformation mirrors Mead's social self constituted through "
                "the generalized other."
            ),
            source=(
                "Before Pragmatism Had a Name (Zenodo 18807971, 2026)"
            ),
            theme="creative_rebellion",
        ),
        Quotation(
            quotation_id="friedman_three_refractions_01",
            speaker="Friedman",
            text=(
                "Blake's prophetic fire, Pragmatism's self-correcting inquiry, "
                "and the science of variational inference are three refractions "
                "of a single ancient light — the light by which self-organizing "
                "systems navigate entropy."
            ),
            source=(
                "Before Pragmatism Had a Name (Zenodo 18807971, 2026)"
            ),
            theme="multi_agent",
        ),
        Quotation(
            quotation_id="friedman_alignment_01",
            speaker="Friedman",
            text=(
                "The implications extend from computational psychiatry "
                "(Newton's Sleep as pathological prior dominance) through "
                "digital humanities to AI alignment (the Fourfold Vision as a "
                "corrective to the single vision of next-token prediction)."
            ),
            source=(
                "Before Pragmatism Had a Name (Zenodo 18807971, 2026)"
            ),
            theme="single_vision",
        ),
    ]


def build_registry() -> QuotationRegistry:
    """Construct the canonical immutable quotation registry."""
    logger.debug("Building canonical Jiang/Blake/Friedman quotation registry.")
    entries: list[Quotation] = []
    entries.extend(_build_jiang())
    entries.extend(_build_blake())
    entries.extend(_build_friedman())
    registry = QuotationRegistry(entries=tuple(entries))
    logger.info(
        "Quotation registry built: %d entries across %d themes",
        registry.count(),
        len(registry.themes()),
    )
    return registry
