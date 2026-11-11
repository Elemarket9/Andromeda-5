# Phase 10D — adversarial recast and model-misspecification checks

This package is an **unreviewed secondary scientific analysis** of ANDROMEDA-5 Phase 10. It tests nine methodological criticisms. No new interaction or faster-than-light transmission is observed or claimed.

## Contents

- `PHASE10D_ADVERSARIAL_AUDIT.md` — interpreted findings and detailed caveats.
- `adversarial_recast.py` — publicly reproducible conditional two-pole screening, point-force ratios, and synthetic misspecification tests.
- `test_adversarial.py` — independent arithmetic and paired-noise injection checks (6 tests).
- `source_table11_4_selected_rows.csv` — four rows transcribed from Lee's 2020 dissertation Table 11.4 in prior Phase 9; **not independently source-image-verified here**.
- `phase10_synthetic_design_source.csv` — original synthetic ring design input; **not physical instrument data**.
- `recast_correlation_envelope.csv`, `point_force_ratios.csv`, `misspecification_stress_test.csv`, `adversarial_validation.json` — generated artifacts.

## Run

Python 3 with NumPy and SciPy:

```bash
python adversarial_recast.py
python -m unittest -v test_adversarial.py
```

The exact-geometry, common-Gaussian, jointly profiled nuisance assumptions for the two-pole recast have **not** been independently established for the original experiment. Do not quote the conditional strength limits as 95%-confidence observed experimental exclusions.

## Primary references
- Lee et al., Phys Rev Lett 124, 101101 (2020), https://doi.org/10.1103/PhysRevLett.124.101101
- J. G. Lee, *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*, University of Washington (2020), https://digital.lib.washington.edu/researchworks/items/971237d1-100a-41ae-9027-d1bbce8cf315
- R. P. Woodard, *Ostrogradsky's theorem on Hamiltonian instability*, Scholarpedia 10(8):32243 (2015), https://www.scholarpedia.org/article/Ostrogradsky%27s_theorem_on_Hamiltonian_instability
- *Renormalization of Hořava gravity*, Phys Rev D 93, 064022 (2016), https://doi.org/10.1103/PhysRevD.93.064022