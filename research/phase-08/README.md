# ANDROMEDA-5 Phase 8 — Reproducibility Package

The Phase 8 report derives an internally testable relationship between the characteristic scales of a **hypothetical** static fifth force and the dispersion relation of the **same** hypothetical scalar field.

No physical fifth-force, superluminal signal or new particle was detected.

## Files
- `PHASE8_RESEARCH_REPORT.md` — detailed technical report and bibliography
- `ANDROMEDA5_Phase8_Adversarial_Report.pdf` — shareable PDF
- `phase8_cross_observable.py` — independent computation
- `validation.json` — calculated benchmark and caveats
- `run_log.txt` — script output
- `independent_static_checks.csv` — numeric quadrature validation
- `dispersion_parameter_predictions.csv` — theoretical mode frequencies/velocities
- `composition_contrast_ideal_point_bodies.csv` — electron-number scaling illustration
- `pole_sensitivity_assumed.csv` — sensitivity to assumed pole-length changes
- `paired_observable_predictions.png` — paired theoretical predictions
- `PUBLIC_SUMMARY.md` — short publication-safe statement
- `SHA256SUMS.txt` — manifest

## How to reproduce

```bash
python -m pip install numpy scipy matplotlib
python phase8_cross_observable.py
```

Check `validation.json` and compare to the paper. The script does not analyze experimental data and does not calculate exclusion curves.