# ANDROMEDA-5 / Phase 7

Reproducible **empirical screening** of the Phase 6 hypothetical preferred-frame scalar against **published measurement summary statistics**. This is **not** a fit to the Eot-Wash raw torque measurements and **not** a faster-than-light discovery.

## Run

```bash
python -m pip install numpy scipy matplotlib
python phase7_empirical_screen.py
python test_phase7.py
```

Outputs: `published_benchmark.json`, `screening_summary.json`, `finite_sphere_predictions.csv`, `infinite_slab_predictions.csv`, `coupling_requirements.csv`, `finite_sphere_force.png`, `slab_ratio.png`.

## Distinguishing evidence

- **Published empirical evidence:** Lee et al. (2020) find no significant inverse-square-law anomaly for their apparatus. Their 95% constraint is on a **single Yukawa** force.
- **Derived theoretical results:** The proposed two-pole scalar interaction produces calculated forces on finite spherical bodies and slab approximations.
- **Unperformed work:** An exact two-pole experiment-level 95% confidence exclusion needs the full measured torque samples, source and detector geometry, nuisance parameters and error covariances or published likelihood. None were available in a form sufficient for this analysis.

No real spacecraft, source–receiver experiment, new force, physical FTL signal or matter-field interaction was observed.

## Primary sources

1. Lee et al., *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, PRL 124, 101101 (2020) — https://doi.org/10.1103/PhysRevLett.124.101101
2. Dzuba et al., *Constraints on the variation of physical constants, equivalence principle violation, and a fifth force from atomic experiments*, PRD 110, 055022 (2024) — https://doi.org/10.1103/PhysRevD.110.055022
3. Amaral et al., *Magnetic levitation as a new probe of non-Newtonian gravity*, PRD 113, L021101 (2026) — https://doi.org/10.1103/pqrs-bpgj (proposal only)
4. Banks et al., *Searching for screened scalar forces with long-baseline atom interferometers*, PRD 113, 084047 (2026) — https://doi.org/10.1103/3486-4m4t (proposal only)