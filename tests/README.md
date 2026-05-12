# `tests/` — Zero-Mock Test Suite

66 tests across 8 files; 99.05 % line+branch coverage of `src/`.

## What we test

- **`test_quotations.py`** — the registry of 25 attributed quotations is immutable, speaker-whitelisted, indexable by id / speaker / theme.
- **`test_convergence.py`** — the twelve thematic convergence nodes exist, validate against the registry, and each references exactly one Jiang + Blake + Friedman quote.
- **`test_generative_model.py`** — `PrecisionAllocation` rejects invalid inputs; Newton's-Sleep metric behaves as expected at parity, dominance, and single-vision limits; fourfold-balance entropy maxes at `log 4` when channels are equal; cleansed-doors score is bounded in [0, 1].
- **`test_fourfold.py`** — exactly four Zoas with unique faculties; six pair-wise coordination entries; full Active-Inference role table.
- **`test_manuscript.py`** — `ManuscriptBuilder` produces all expected keys; Newton's-Sleep regime scores worse than the Eden regime on every health metric.
- **`test_viz_figures.py`** — every renderer writes a non-empty PNG in both light and dark themes; renderers create their parent directories.
- **`test_analyze_script.py`** + **`test_generate_figures_script.py`** — the thin orchestrators in `../scripts/` actually produce the expected artifacts.

## Run it

```bash
uv run pytest projects/blake_jiang/tests/ --cov=projects/blake_jiang/src --cov-fail-under=90
```

## Style

- `tmp_path` for any file I/O.
- `pytest.approx` for floating-point comparisons.
- Parametrize when the same assertion applies to every renderer.
- One-line docstrings only; the test name should already say what is being asserted.

## What a failure here usually means

| Failure pattern | Likely cause |
| --- | --- |
| `test_registry_count_matches_entries` fails | A quotation was added without bumping the speaker breakdown comment in `quotations.py`. |
| `test_build_nodes_has_exactly_twelve` fails | Convergence model was edited without updating the 12-row sanity check. |
| `test_fourfold_balance_max_when_equal` fails | Either the entropy formula changed or `log(4)` precision is off — check `math.log` import. |
| `test_render_writes_nonempty_*` fails | Renderer raised an exception, or `MPLBACKEND` isn't `Agg`. Check `conftest.py`. |
