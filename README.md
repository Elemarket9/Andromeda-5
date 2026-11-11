# ANDROMEDA-5 — Exploratory Fundamental Physics Research

**Status: unreviewed theoretical and numerical research. No faster-than-light signal, new particle, fifth force, or inertial-mass modification has been observed.**

ANDROMEDA-5 investigates whether a hypothetical scalar-field model with higher-spatial-derivative dispersion could support signaling faster than vacuum light, and whether the same candidate field is consistent with published laboratory measurements. The original Andromeda transport objective is **not** a demonstrated capability or an immediate engineering result.

## Research history

| Phase | Focus | Result |
|---|---|---|
| 1–2 | Hypotheses and adversarial audit | Baseline calculations, not evidence of new physics |
| 3 | Higher-order dispersion and fast-light controls | Simulations of assumed equations |
| 4 | Source–receiver simulations | Early responses in a hypothetical model |
| 5 | Coupled field and detector | Mathematical checks, no identified physical field |
| 6 | Matter–field interaction | Candidate coupling and force calculations |
| 7–8 | Constraints and paired observables | Theoretical predictions, not observations |
| 9 | Published torque-data evidence screen | Secondary analysis of selected torsion-balance results; **no valid two-pole exclusion bound yet** |

## Reproducibility

Python 3.11+, NumPy, SciPy and Matplotlib are used for various phases. Each research-phase directory holds local instructions, code, data, reports, and limitations where available.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Phase 9
cd research/phase-09
python transcribe_lee_appendix.py
python phase9_public_data_screen.py
python phase9_integrated_evidence.py
python -m unittest -v test_phase9.py test_phase9_integrated.py
```

**Passing tests validates a numerical calculation, not the existence of a physical field.**

## Evidence and limitations

- No laboratory faster-than-light transmission, matter coupling, novel force, or controllable inertia has been observed by this project.
- The higher-derivative wave equation is a theoretical assumption, related to models studied previously.
- The published Eöt-Wash torque results are independent third-party work. Phase 9 data are transcriptions of printed calibrated values, not raw laboratory data.
- Single-Yukawa parameter summaries do not by themselves give a statistically valid exclusion of our proposed two-pole force.
- No independent peer review is claimed.

## Primary sources

- John G. Lee et al., *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, Physical Review Letters **124**, 101101 (2020): https://doi.org/10.1103/PhysRevLett.124.101101
- John G. Lee, *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*, University of Washington dissertation (2020): https://digital.lib.washington.edu/researchworks/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download

## Feedback

Critical independent review is welcome. Submit a reproducible counterexample, corrected derivation or transcription, or an instrument-specific experimental constraint. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Rights

The project owner has not yet selected a project-wide open-source license. Third-party work retains its original rights. See [LICENSE_NOTICE.md](LICENSE_NOTICE.md).
