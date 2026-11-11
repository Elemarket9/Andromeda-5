# ANDROMEDA-5 — Phase 10: Forward-Model and Synthetic Falsification Gate

**Date:** 11 November 2026  
**Research status:** Unreviewed theory and numerical demonstration. No independently measured new field, fifth force, superluminal signal, inertial modification or experimental challenge to established relativity is claimed.

## Executive finding

The Phase 8/9 proposed static two-pole interaction has now been given an **explicit, finite-point-mass forward torque model**. Analytic torque expressions agree with independent finite-angle numerical derivatives. In an invented ring geometry, a multivariate fitting pipeline can recover deliberately injected two-pole signals and delivers approximately nominal false-positive rates. These are validations of the **calculations and software**, **not tests of nature**. The real Eöt-Wash apparatus response and full joint statistical likelihood remain unreconstructed. Thus **no real-data exclusion or positive detection for the two-pole model is available**.

## Hypothesis and its unproven assumptions

As a *phenomenological surrogate*, not an experimentally derived electron coupling, the point-mass potential is

\[
U(r)=-\frac{Gm_1m_2}{r}\left[1+\frac{\alpha}{s}\left(e^{-ar}-e^{-br}\right)\right],\quad
s=\sqrt{1-4\ell^2\mu^2},\quad
a^2=\frac{1-s}{2\ell^2},\quad b^2=\frac{1+s}{2\ell^2}.
\]

The formula is defined for positive \(\ell\), \(\mu\ge0\) and \(4\ell^2\mu^2<1\). **Crucial:** the use of \(Gm_1m_2\) assumes a universal mass coupling for convenience. The Phase 6 electron interaction needs number-density integrals and does **not** automatically predict this potential normalization or universality. A physically consistent microscopic source coupling has **not** been derived. The higher-derivative dispersion relation is assumed, not observed.

For assumed \(\ell=2\times10^{-4}\) m and \(\mu=10^3\) m\(^{-1}\):

- \(s=0.916515139\);
- \(a=1021.548218\) m\(^{-1}\), long-range scale \(a^{-1}=0.9789063\) mm;
- \(b=4894.531565\) m\(^{-1}\), short-range scale \(b^{-1}=0.2043096\) mm.

These numerical values are **assumed hypothetical parameters** selected in previous phases; they were not fitted to measured data.

## Phase 10A — Torque-level validation

A pair of point masses \(m_d,m_s\) at detector and source positions \(\mathbf r_d,\mathbf r_s\) produces an assumed torque \(\tau_z=-\partial U/\partial\phi_d\) for a detector rotation \(\phi_d\). We implemented the analytic torque and independently checked against the centered finite-angle derivative of the assumed potential.

**Executed results:** 200 random geometries × 5 terms = **1,000 derivative comparisons**, with maximum relative discrepancy \(4.95\times10^{-9}\) under the stated numerical cutoff and median discrepancy \(5.83\times10^{-11}\). This tests differentiation and software implementation, not empirical validity.

Two invented point-ring systems were then evaluated. They are **NOT representations of the as-built 2020 Eöt-Wash apparatus**:

| Toy symmetry | Calculated Newtonian harmonic (N m) | Two-pole harmonic at \(\alpha=1\) (N m) | Magnitude ratio |
|---|---:|---:|---:|
| 18-fold | 4.955 × 10^-20 | 1.240 × 10^-20 | 0.2503 |
| 120-fold | 7.293 × 10^-23 | 1.115 × 10^-24 | 0.01529 |

Ratios are geometry dependent. Nothing here can be compared directly with the actual 18/120 harmonic torques without reconstructing the laboratory geometry, calibration, phase, sample shape and nuisance model.

## Phase 10B — A blinded-style *synthetic* signal recovery test

A toy design matrix used 16 invented observations (two harmonics × eight gap settings). Four parameters were fitted jointly: Newtonian scale, two-pole coefficient \(\alpha\), and two per-harmonic offsets. Noise was independent Gaussian at **assumed** levels, with fixed random seed 20261111. The full design and executable implementation are in `phase10_injection.py`.

| Injected \(\alpha\) | Recovered \(\alpha\) | Formal 1-sigma | Approximate 95% interval |
|---:|---:|---:|---:|
| 0.0 | 0.150 | 0.291 | [-0.421, 0.721] |
| 0.5 | 0.147 | 0.291 | [-0.425, 0.718] |
| 1.0 | 1.313 | 0.291 | [0.742, 1.884] |

Single draws can miss an injected signal, as the \(\alpha=0.5\) example illustrates. Over 2,000 independently simulated data draws per strength (using the code's random seed), the two-sided \(|z|>1.96\) detection rate was **5.65%** at zero injection, **38.4%** at 0.5 and **92.7%** at 1.0. The nominal intervals covered the injected coefficient about 94–95% of the time. The whitened design matrix condition number was **106**, signaling nontrivial parameter correlation; different geometry/noise assumptions could change sensitivity substantially.

**These 6,000 trial datasets are simulated. No real apparatus was used.** A 5.65% false-positive rate is consistent with sampling variability near a nominal 5% level; it does not imply an unexplained force.

## Phase 10C — What the third-party experiment does say

We also rechecked a subset of the **published, corrected** 2020 Lee torsion-balance torque table (95 runs / 285 harmonic amplitudes) at 68.0–70.2 micrometres. The previously reported local weighted estimates at 69 micrometres were:

- 120-fold harmonic: 1.46205 ± 0.00877 fN m;
- 18-fold harmonic: 1.04942 ± 0.00513 fN m;
- 54-fold harmonic: 0.11745 ± 0.00448 fN m.

Errors here are *formal* diagonal weighted-fit errors, not the full experimental covariance. The 18-fold local linear-fit check has a naive \(p\) near 0.048, which **is not evidence for the proposed field**: the window was selected, correlations/systematics have not been incorporated, and several model checks could affect the result. The original Eöt-Wash analysis found excellent agreement with Newtonian gravity (reported \(\chi^2\approx274.99\) for 285 degrees of freedom, goodness-of-fit \(p\approx0.654\)). See the 2020 primary sources.

The transcription contains several separations below 52 micrometres despite that value appearing in the headline measurement range; these entries require exact visual verification against original table pages before stronger claims.

## Current falsification gate — unsatisfied

Before comparing our force model with published experimental results, we must obtain or reconstruct all of the following:

1. **As-built test-body geometry** (including 18- and 120-fold wedge shapes, densities, cutouts, orientations, attractor layers, and gaps);
2. **Torque response templates** for Newtonian and two-pole interactions, in the correct harmonic phase conventions;
3. **Calibrations and systematics**, uncertainty on absolute separation, angular registration, density, instrument drift and noise covariance;
4. **A common joint likelihood** that fits instrument nuisance parameters and the model coupling simultaneously;
5. **Independent replication and audit** of calculation and source-data transcription.

Without these, neither a 95% exclusion nor a detection of our hypothetical force is justified. The toy fitted sensitivity is **not** an experimental limit.

## Request for expert review

We specifically invite an experimental gravitational physicist to challenge: (a) the physical legitimacy of interpreting the toy mass-coupling potential as a field-mediated force, (b) the analytic torque differentiation, (c) the proposed apparatus-model reconstruction, and (d) whether the original laboratory response templates/covariance can be made available for a proper two-pole likelihood fit.

Suggested external contact: Prof. Jens Gundlach, University of Washington Eöt-Wash Group, via the group's publicly listed research contact email `gundlach@uw.edu`. **No contact, review, affiliation or endorsement is claimed at publication.**

## Reproduction

Run from this directory with Python 3.11+, NumPy and SciPy:

```bash
python phase10_forward_model.py
python phase10_injection.py
python -m unittest -v test_phase10.py
python make_phase10_figures.py  # matplotlib required
```

Expected output files: `phase10_results.json`, `phase10_injection_results.json`, `phase10_synthetic_ring.csv`, `phase10_synthetic_design.csv`, `phase10_local_repeatability.csv`, `phase10_injection_runs.csv`, plus two plots. The **source input** `lee2020_dissertation_appendix_A1_transcribed.csv` is a third-party processed torque transcription, not an original experiment performed by ANDROMEDA-5.

## Primary sources and attribution

- J. G. Lee, E. G. Adelberger, T. S. Cook, S. M. Fleischer, B. R. Heckel (2020), "New Test of the Gravitational 1/r² Law at Separations down to 52 μm", *Physical Review Letters* 124, 101101. https://doi.org/10.1103/PhysRevLett.124.101101
- J. G. Lee (2020), *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*, University of Washington dissertation. https://digital.lib.washington.edu/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download
- Eöt-Wash research programme and group contact page: https://www.npl.washington.edu/eotwash/

**Bottom line:** This phase builds a reproducible *toy experiment analysis method*. It neither supports nor falsifies a physical superluminal field. The next significant empirical step is a properly calibrated two-pole fit to original experimental data, followed by a physically defined source and detector experiment.