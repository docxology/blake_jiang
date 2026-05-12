"""Zero-mock tests for the analyze.py thin orchestrator."""

from __future__ import annotations

import json
from pathlib import Path

from projects.blake_jiang.scripts.analyze import main as analyze_main


def test_analyze_writes_expected_keys(tmp_path: Path) -> None:
    out_file = analyze_main(output_dir=tmp_path)
    assert out_file.exists()
    payload = json.loads(out_file.read_text(encoding="utf-8"))
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
    assert expected.issubset(set(payload.keys()))
    assert payload["node_count"] == 12


def test_analyze_is_idempotent(tmp_path: Path) -> None:
    first = analyze_main(output_dir=tmp_path)
    payload1 = json.loads(first.read_text(encoding="utf-8"))
    second = analyze_main(output_dir=tmp_path)
    payload2 = json.loads(second.read_text(encoding="utf-8"))
    assert payload1 == payload2


def test_analyze_creates_output_directory(tmp_path: Path) -> None:
    deep_dir = tmp_path / "deeper" / "still"
    out_file = analyze_main(output_dir=deep_dir)
    assert out_file.parent == deep_dir.resolve()
    assert out_file.exists()
