# ANDROMEDA-5 Phase 6 — public computational research package

A reproducible **theoretical** candidate matter–field coupling and a numerical audit of its hypothetical static force. It is **not evidence that faster-than-light signals or an unknown particle have been observed**.

## Quick start

```bash
python -m pip install numpy scipy matplotlib
python phase6_matter_field.py
```

Compare the newly generated CSV files and `validation_summary.json` with the packaged versions. `execution_log.txt` records the run supplied with this release.

## Deliverables

- `ANDROMEDA5_Phase6_Working_Paper.pdf` — shareable scientific working paper.
- `PHASE6_RESEARCH_PAPER.md` — editable source and links to primary literature.
- `phase6_matter_field.py` — reproducible analytical/numerical calculations.
- `static_green_validation.csv` — Fourier integral versus analytic Green function.
- `group_velocity_hypothesis.csv` — group velocity *inside assumed model*, not a physical observation.
- `coupling_normalization.csv` — hypothetical electron coupling versus fifth-force strength.
- `synthetic_injection_benchmark.csv` — synthetic null and injection data only.
- `validation_summary.json`, `execution_log.txt` — exact summary and recorded run.
- `fifth_force_shape.png`, `synthetic_force_test.png` — scientifically labeled figures.

## Release note for public dissemination

"This work derives and numerically cross-checks a static-force signature of a hypothesized matter-coupled preferred-frame scalar with quartic dispersion. It reports theoretical and synthetic numerical results, not experimental evidence for the existence of the scalar or for faster-than-light communication. Independent review and tests against fifth-force measurements are requested."

## Scientific constraints

Do not turn the simulation's input values into claimed laboratory measurements. Ordinary Yukawa-force bounds require an apparatus-specific re-analysis for this two-pole kernel. Novelty remains unestablished; similar higher-spatial-derivative models exist in prior physics literature.