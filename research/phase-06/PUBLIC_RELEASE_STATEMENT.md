# ANDROMEDA-5 Phase 6 — Public research statement

**Release date:** 11 November 2026  
**Status:** Unreviewed theoretical/computational research; independently testable code provided.

ANDROMEDA-5 has derived an analytic static-force prediction for a *hypothetical* matter-coupled scalar field with higher-order spatial dispersion. An independent numerical Fourier calculation reproduces that analytic kernel to a maximum relative difference of approximately 1.4 × 10^-12 for the tested benchmark parameter range. A seeded synthetic-data exercise demonstrates the expected statistical recovery of an inserted force-template amplitude. The calculations and tests are reproducible with the enclosed Python script.

**These results do not show that the field exists. They do not experimentally demonstrate faster-than-light information or travel.** The proposed matter coupling is subject to existing fifth-force and precision-physics constraints that have not yet been fit to this model using measured likelihoods.

We invite researchers to check the mathematical derivation, replicate the numerical work, identify relevant prior art, test the gauge-invariant completion, and calculate the response of finite-size experimental masses. We particularly welcome adversarial critiques of the ultra-violet dispersion, coupling assumptions, causality, and existing experimental bounds.

**To reproduce:** `python -m pip install numpy scipy matplotlib`, then `python phase6_matter_field.py` and `python test_phase6.py`.

**Please cite/share accurately:** “ANDROMEDA-5 Phase 6 theoretical working paper, 11 November 2026, not peer reviewed.” Do not describe this as a discovery of faster-than-light signals or a new particle.