# ANDROMEDA-5 Phase 10D — Adversarial Review and Conditional Experimental Recast

**Date:** 11 November 2026  
**Status:** mathematical reanalysis and synthetic sensitivity investigation, **not** an experimental detection or exclusion result.  
**Decision:** Major revision required for the Phase 10 scientific interpretation. The earlier model has **no established empirical support**. A gravitational-strength universal-mass version is **strongly disfavoured in a conditional screen**, subject to verifying the shared-likelihood assumptions.

## 1. Model and source

The Phase 10 *phenomenological* potential is

\[ U(r)=-\frac{Gm_1m_2}{r}\left[1+\frac{\alpha}{s}\big(e^{-ar}-e^{-br}\big)\right],\quad
s=\sqrt{1-4\ell^2\mu^2},\quad
a^2=\frac{1-s}{2\ell^2},\quad b^2=\frac{1+s}{2\ell^2}. \]

Benchmark assumptions: `ell = 2e-4 m`, `mu = 1000 m^-1`, giving `s = 0.916515139`, `1/a = 0.978906 mm`, `1/b = 0.204310 mm`. The *universal gravitational-mass coupling* is not derived from the earlier electron coupling. No real field, force, or FTL effect has been observed.

Independent published experiment: J. G. Lee et al., *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, **PRL 124, 101101 (2020)**, DOI [10.1103/PhysRevLett.124.101101](https://doi.org/10.1103/PhysRevLett.124.101101). It reports 95 runs, 285 harmonic torque measurements and a Newtonian fit χ²≈275 for 285 degrees of freedom. John G. Lee's 2020 UW dissertation **Table 11.4** is the original source for the four selected separately fitted single-Yukawa parameters below. These four numerical values were **transcribed in our earlier Phase 9 work**; this reanalysis did not independently visually verify the dissertation table.

| Single-Yukawa λ (mm) | α̂ | σ(α) |
|---:|---:|---:|
| 0.200 | -0.00235 | 0.01570 |
| 0.220 | -0.00351 | 0.01470 |
| 0.890 | -0.00612 | 0.00845 |
| 1.000 | -0.00569 | 0.00796 |

Our separately interpolated values at the two model ranges are approximately `(α̂, σ) = (-0.005769, 0.008050)` for the long mode and `(-0.002609, 0.015476)` for the short mode. Interpolation is **not** an independently published confidence limit.

## 2. Conditional common-likelihood recast (NOT an official limit)

If **and only if** the separate fits can be interpreted in the **same linearly projected, whitened-data space with a common nuisance-parameter model**, let `T_L`, `T_S` be the unit-strength data templates for the two Yukawas. Then `T_two = (T_L - T_S)/s`. If the marginal standard errors are `σ_L=1/||T_L||` and `σ_S=1/||T_S||`, with unknown normalized inner product ρ, the formal two-pole error is

\[ \sigma_{\rm two}(\rho)=\frac{s}{\sqrt{\sigma_L^{-2}+\sigma_S^{-2}-2\rho/(\sigma_L\sigma_S)}} .\]

In the same idealized linear model, the fitted amplitude is

\[\hat\alpha_{\rm two}(\rho)=\frac{s(\hat\alpha_L/\sigma_L^2-\hat\alpha_S/\sigma_S^2)}{\sigma_L^{-2}+\sigma_S^{-2}-2\rho/(\sigma_L\sigma_S)}.\]

Under these assumptions and `-1<=ρ<=1`, the triangle inequality implies

\[ \sigma_{\rm two}\le \frac{s}{|\sigma_L^{-1}-\sigma_S^{-1}|} \simeq 0.01537.\]

Selected **conditional** Gaussian results:

| Template correlation | α̂ two-pole | formal σ |
|---:|---:|---:|
| -1.0 | -0.002008 | 0.004853 |
| 0.0 | -0.003652 | 0.006545 |
| +0.9 | -0.013880 | 0.012760 |
| +1.0 | -0.020150 | 0.015374 |

Across this assumed envelope the upper endpoint of the *illustrative* Gaussian 95% interval never exceeds approximately `+0.0113` and the lower endpoint can be about `-0.0503`. The hypothetical **α=1** benchmark would therefore be dramatically inconsistent *if this shared-likelihood construction were valid*. This is **not** a 95%-CL experimental exclusion, because the actual instrument responses, parameter profiling, joint covariance and cross-template correlation were not recovered. No misleading '65σ real detection/exclusion' language is warranted.

### Why cancellation cannot be dismissed entirely

The **pairwise point-force** correction per unit α, relative to Newtonian force, is

\[ f_{\rm two}(r)=\frac{(1+ar)e^{-ar}-(1+br)e^{-br}}{s}.\]

Computed correction factors:

| Point separation (mm) | f_two(r) for α=1 |
|---:|---:|
| 0.052 | 0.0284 |
| 0.100 | 0.0896 |
| 0.200 | 0.2599 |
| 0.500 | 0.6636 |
| 1.000 | 0.7460 |
| 2.000 | 0.4297 |
| 3.000 | 0.2070 |

Thus the two components **do** cancel substantially at the shortest pairwise gaps; they do **not** remain cancelled at ~0.5–1 mm. Pairwise force calculations are not the harmonic torque response of the Eöt-Wash instrument and cannot replace it.

## 3. Injection and mis-specification audit

The original Phase 10 Python code *does* inject the 0.5 strength through `baseline = X @ [1, alpha, 0.25, -0.15]`. It draws a **different noise realization** for each amplitude; therefore recovered values near 0.150 for α=0 and 0.147 for α=0.5 are possible. New paired-noise regression checks that changing α from 0 to 0.5 produces **exactly a 0.5 change in the fitted coefficient**, up to floating-point accuracy. This is a code sanity check, not a physical discovery. The original term "blinded" was inappropriate.

We ran a **new adversarial synthetic stress test**, 3,000 trials for each scenario and each injected strength, against the *original* 16-point ring design. All data remain fabricated. The analyst always fits the *unmodified* model with diagonal Gaussian errors. The generator either uses the matched model or injects synthetic errors:

- `matched_independent`: exact model and independent Gaussian noise;
- `ar1_noise_rho_0p75`: within-harmonic AR(1) correlated noise with adjacent correlation 0.75;
- `gap_plus10um`: true signal evaluated at gap+10 μm using shape-preserving interpolation of the precomputed toy geometry, but fit as if the nominal gaps were correct;
- `geometry_drift_3pct`: an assumed Newtonian-template trend with peak-to-peak 3% scale distortion;
- `combined`: all three error types together.

Results for the synthetic **α_true=0** case:

| Synthetic scenario | Mean coefficient bias | Empirical SD | Naive 95% coverage | False-positive rate |
|---|---:|---:|---:|---:|
| matched independent | +0.002 | 0.291 | 95.1% | 4.9% |
| AR(1) correlated | -0.008 | 0.324 | 92.3% | 7.7% |
| gap +10 μm | +3.367 | 0.292 | 0.0% | 100% |
| 3% template trend | -0.021 | 0.295 | 95.2% | 4.8% |
| combined | +3.311 | 0.340 | 0.0% | 100% |

The large gap-error effects illustrate **catastrophic model mismatch in this invented setup**; they are not measured sensitivity or a claim about actual Eöt-Wash gap errors. Real experiments control or profile gap uncertainty. The earlier nominal false-positive exercise was a basic exact-model software check, not an independent blind validation.

The original toy torque amplitudes (~10^-20 to 10^-23 Nm) are many orders smaller than actual reported harmonics (~10^-15 Nm), but that **alone is not a defect in dimensional numerical testing**. It makes the toy error bars and derived σ(α) irrelevant to actual instrument sensitivity.

## 4. Does the static minus sign imply a ghost?

**Not by itself.** The quartic `+ell²*k⁴` arises from a term with **higher spatial derivatives only**, while the field equation remains **second order in time**. The free action may be chosen as

\[ L=\tfrac12\int d^3x\,[\dot\phi^2-c^2|\nabla\phi|^2-c^2\ell^2(\nabla^2\phi)^2-c^2\mu^2\phi^2], \]

with a positive definite free Hamiltonian for `ell² >= 0, mu² >= 0`. There is one positive-frequency dispersion branch per `k`; the two opposite static residues are poles in **spatial momentum** of the zero-frequency Green function. They are not two propagating time-pole excitations with one negative energy. Ostrogradsky ghosts usually arise from **nondegenerate higher time derivatives**. Sources: R. P. Woodard, Scholarpedia (2015), and Barvinsky et al., *Renormalization of Hořava gravity*, PRD 93, 064022 (2016). A *full coupled quantum theory* may have other instabilities and serious Lorentz-violation constraints, which have not been solved.

## 5. Verdict on the nine criticisms

1. **Likely exclusion at α~1:** serious, likely for the universal-gravitational coupling benchmark, but numerical values here are a conditional screen, not a real confidence bound.
2. **Exact-model circular validation:** agree; rerun with generator–fitter mismatch; old “blinded” label is withdrawn.
3. **Tiny toy vs measured torque:** agree that toy σ(α) is not a real sensitivity forecast; different scale alone does not negate a unit test.
4. **0.5 injection almost same recovered:** verified the injection is present; independent noise explains individual draws; paired-noise regression passes.
5. **Negative spatial static residue = ghost:** not established; distinguish higher spatial versus higher temporal derivatives, while avoiding unsupported claims of complete consistency.
6. **Static potential proves FTL:** agree; static data cannot test propagation or signaling speed.
7. **Selected p≈0.048 and <52 μm entries:** withdraw any evidence interpretation of the selected-window p-value. Transcription entries require source-page verification; do not declare them necessarily fabricated just because they conflict with an abstract's minimum.
8. **Universal coupling not derived:** agree; an electron-number coupling requires composition-aware predictions and separate equivalence-principle constraints.
9. **Numerical torque derivative is self-consistency only:** agree; not experimental corroboration.

## 6. Priority action and publication standard

1. Verify all Table 11.4 entries against images of the original dissertation; source manuscript currently cited but this run could not access original 16.58 MB PDF directly.
2. Obtain apparatus-response templates, calibration and correct joint nuisance likelihood, or do a clearly marked and documented approximate *geometry-aware* calculation to test whether α=1 can survive.
3. Treat α=1 as a deliberately challenged benchmark, **not** the best candidate. Do not tune parameters solely to avoid published limits.
4. Develop a justified microscopic coupling with composition-sensitive charges and independently check equivalence-principle limits.
5. Design a separate causality/signaling experiment; a static fifth-force null result says nothing about FTL propagation.
6. Preserve this work's negative findings and synthetic-vs-empirical labels in public releases.

**Public status:** No positive evidence for a novel force, superluminal information, or a viable FTL technology. The universal gravity-strength two-pole benchmark appears in serious tension with existing experimental data, subject to a proper common-likelihood recast.