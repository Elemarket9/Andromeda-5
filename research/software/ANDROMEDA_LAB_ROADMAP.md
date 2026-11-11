# ANDROMEDA-Lab — scientific software roadmap
Date: 2026-11-11
Status: proposed software, not an experimental discovery.

## Purpose
Build an open, reproducible platform for proposing, simulating, criticizing and experimentally constraining candidate physics theories. The Phase 10 two-component force model and synthetic torque tests are the first benchmark. The platform must not imply any observed faster-than-light transmission, new field, or fifth force.

## First release: model-to-data scientific validation
1. **Equation registry**: source equation, assumptions, units, action principle, free parameters, validity regime, references, change history.
2. **Simulation engine**: standard-wave vs hypothetical dispersion; source/detector calculations; convergence, boundary effects and conservation audits.
3. **Experimental data ingestion**: real published tables with original provenance, transcription checks, measurement uncertainties, geometry and calibration placeholders.
4. **Model comparison**: likelihood fits, uncertainty propagation, injection-recovery, posterior predictive checks, negative controls, preregistered falsification criteria.
5. **Adversarial agent reports**: derive competing predictions, find dimensional mistakes, propose counterexamples; flag hallucinated citations.
6. **Publish pipeline**: persist scripts, dependency lockfiles, datasets, test results, scientific status, immutable run manifest and hashes in GitHub.

## Technical choices
- Python + NumPy/SciPy for reproducible baseline calculations.
- JAX optionally for accelerated parameter scans and automatic differentiation, after a validated NumPy baseline. https://docs.jax.dev/en/latest/
- PyMC optionally for Bayesian model fitting and posterior predictive checks. https://www.pymc.io/
- FEniCSx optionally for finite-element treatment of geometries after suitable validation. https://fenicsproject.org/documentation/
- A lightweight browser UI showing equations, numerical diagnostics, real-vs-synthetic labels and evidence provenance.

## Research goals versus technology readiness
- Can build now: theory comparison, anomaly detection workflow, experimental design, educational visualization, reproducible research portal.
- Not established: actual FTL network, anti-inertia device, novel field detector with measured anomalies, commercial new-physics propulsion technology.
- Success means a distinct, independently testable prediction survives real measurements; no software-only output constitutes a physical discovery.

## Prototype milestones
A. Re-run and verify Phase 10 numerical tests from a clean environment, fix misleading or broken steps.
B. Import Phase 9 measured torque table, retain original rows and flag transcription ambiguities.
C. Implement geometry-aware forward-model interface with explicit missing-data gates.
D. Create transparent side-by-side comparisons of Newtonian, single-Yukawa and two-pole models using the **same** dataset and consistent uncertainties.
E. Add independent-code review and reproducible data manifest.
