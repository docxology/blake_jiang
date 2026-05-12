"""Thin orchestrator: emit manuscript injection JSON for blake_jiang.

Computes convergence, fourfold, and generative-model figures via the domain
modules in ``projects.blake_jiang.src`` and serializes the result to
``output/data/manuscript_injection.json``.
"""

from __future__ import annotations

import json
from pathlib import Path

from infrastructure.core.logging.utils import get_logger
from projects.blake_jiang.src.manuscript import ManuscriptBuilder

logger = get_logger("blake_jiang.analyze")


def _project_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def main(output_dir: Path | None = None) -> Path:
    """Compute injection data and write JSON. Returns the output file path."""
    logger.info("Starting blake_jiang analysis pipeline...")

    target_dir = (output_dir or _project_dir() / "output" / "data").resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    payload = ManuscriptBuilder().generate_injection_data()
    out_file = target_dir / "manuscript_injection.json"
    with out_file.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)

    logger.info("Wrote manuscript injection data to %s", out_file)
    print(str(out_file))
    return out_file


if __name__ == "__main__":
    main()
