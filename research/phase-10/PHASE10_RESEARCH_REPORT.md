# ANDROMEDA-5 Phase 10 — Forward-model and Falsification Gate

11 November 2026. **Unreviewed theoretical/numerical work. No new force or FTL signal observed.**

## Objective and limits

Phases 6–9 proposed a hypothetical higher-spatial-derivative scalar with a two-pole static response. We now derive torques from a *chosen* phenomenological potential, cross-check analytical derivatives, and run a controlled synthetic source/recovery procedure. A real, as-built Eöt-Wash apparatus model and nuisance covariance are unavailable: **no full two-pole experimental fit or exclusion has been performed.**

## Proposed potential, not experimentally established

Using point-mass coupling as an illustrative normalization:

```text
U(r) = -G*m1*m2/r * [1 + alpha/s * (exp(-a*r) - exp(-b*r))]
s = sqrt(1 - 4*ell**2*mu**2)
a**2 = (1-s)/(2*ell**2)
b**2 = (1+s)/(2*ell**2)
```

Domain: ell > 0, mu >= 0, 4 ell² mu² < 1. For **assumed** ell=0.0002 m and mu=1000/m: s=0.916515139, a=1021.548218/m, b=4894.531565/m, ranges 0.9789063 mm and 0.2043096 mm.

**Crucial assumption:** This universal-mass potential is *not derived from* our earlier scalar–electron coupling. Its normalization and source charges remain unverified; a genuine microscopic matter coupling has not been obtained.

## Reproduced torque calculations

For detector angle theta, tau_z = -dU/dtheta. In 200 random point geometries times five potential terms, independent centered finite differences matched the analytic expression in **1,000 comparisons**, with maximum relative discrepancy **4.95e-9** and median discrepancy **5.83e-11**.

Two **invented point-ring designs**, with alpha=1 at a 100 micrometre separation, gave:

| Toy symmetry | Newtonian amplitude N m | Two-pole amplitude N m | Ratio |
|---|---:|---:|---:|
| 18-fold | 4.955e-20 | 1.240e-20 | 0.2503 |
| 120-fold | 7.293e-23 | 1.115e-24 | 0.01529 |

These values cannot be compared directly with laboratory torques; the real bodies have wedge patterns, material layers, mass distributions, and instrumental phase/geometry calibration.

## Synthetic injection-and-recovery validation

An illustrative 16-row design includes two harmonic templates over eight gaps, fitted jointly with a Newtonian amplitude and two harmonic offsets. Assuming independent Gaussian errors (an **invented** noise model) gave 1-sigma(alpha)=0.2914 and design condition number 106.

| Synthetic alpha inserted | Recovered alpha ± 1 sigma |
|---|---|
| 0 | 0.150 ± 0.291 |
| 0.5 | 0.147 ± 0.291 |
| 1.0 | 1.313 ± 0.291 |

Using 2,000 simulated datasets per injected strength, the two-sided nominal 5% significance test triggered 5.65% of the time under the **synthetic null**, 38.4% for alpha=0.5 and 92.7% for alpha=1. The Monte Carlo confidence intervals covered the inserted strength about 94–95% of the time.

This checks the fit pipeline. It does **not** imply that real forces exist or that any real experimental bound is 0.2914.

## Real third-party data

We previously transcribed **95 published corrected torque runs**, three harmonics each, from the 2020 John G. Lee University of Washington dissertation. The original Eöt-Wash result agreed with ordinary gravity; its published Newtonian goodness-of-fit chi-square was about 274.99 for 285 degrees of freedom (p≈0.654). Our own local weighted checks are descriptive and incomplete. Some transcribed separations below the paper's headline 52-micrometre minimum still require visual verification.

**Missing for real inference:** calibrated 18/54/120 harmonic torque response templates from the as-built geometry, full covariance, nuisance-parameter profiling, uncertainty in absolute gap and angular alignment, and independent source-data transcription audit.

## Research judgement

- **Numerical cross-check: passed** for the assumed formula and toy apparatus.
- **Evidence of a physical new force: none.**
- **Evidence of faster-than-light matter or information propagation: none.**
- **Two-pole force excluded or detected with real torsion-balance data: not calculated.**
- **Independent professor endorsement: not obtained.**

## Requested independent challenge

A precision-gravity experimentalist could test whether the source coupling is physically justified, advise how to reconstruct the actual torque response, and determine what existing experiment constrains or excludes this proposal. A critical review or rejection would be valuable and should be documented.

## Sources

1. Lee et al. (2020), *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, PRL 124, 101101, https://doi.org/10.1103/PhysRevLett.124.101101
2. J. G. Lee (2020), *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*, University of Washington dissertation: https://digital.lib.washington.edu/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download
3. Eöt-Wash research group and research contacts: https://www.npl.washington.edu/eotwash/

## Next gate

Produce a complete, independently verified apparatus-specific two-pole torque response and joint likelihood from the original measurement geometry, then request external replication. Until then, do not claim a real-data discovery or exclusion.
