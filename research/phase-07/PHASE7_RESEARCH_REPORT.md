# ANDROMEDA-5 Phase 7 — Published-Evidence Screening and Experimental Constraints

**Date:** 11 November 2026  
**Status:** Independent computational audit of a hypothetical field against published measurement summaries; **not** a peer-reviewed discovery or a laboratory test.

## Executive finding

No evidence of faster-than-light transmission or of a new matter-coupled scalar field has been established. Phase 7 goes beyond Phase 6's point-body model to derive finite-body predictions and reproduce a published experimental summary statistic. The benchmark experiment's established single-Yukawa 95% exclusion **cannot be applied verbatim** to our different two-pole potential. An exact test requires its 3D torsion-balance geometry and torque-level likelihood.

## Model under evaluation

In a preferred frame, a postulated scalar has 

```
omega^2(k) = c^2 (k^2 + ell^2 k^4 + mu^2)
ell = 0.0002 m ; mu = 1000 m^-1
```

Its static propagator has a two-pole form

```
G(r) = [exp(-a*r) - exp(-b*r)] / [4*pi*r*sqrt(1-4*ell^2*mu^2)]
a = 1021.548218 m^-1
b = 4894.531565 m^-1
```

so characteristic lengths are **0.978906 mm** and **0.204310 mm**. This is a mathematical consequence of the *postulated* field, not observed new physics.

For finite homogeneous gold spheres, mass 1 mg each, density 19,320 kg/m^3, radius **0.231189 mm**, center separation r > 2R, define the Yukawa spherical form factor

```
B(z) = 3 [z cosh(z) - sinh(z)] / z^3.
F_5(r)/(alpha_AuAu * F_N(r)) =
 {B(a R)^2 (1+a*r) exp(-a*r) - B(b R)^2 (1+b*r) exp(-b*r)}
 / sqrt(1-4*ell^2*mu^2).
```

At r=1.0 mm, Newtonian F_N=**6.6743e-17 N**, extra F_5=**4.9463e-17 N** if the hypothetical normalisation alpha_AuAu=1, or **4.9463e-19 N** for alpha_AuAu=0.01.

For two nominally infinite homogeneous gold slabs, each 0.10 mm thick and with a 0.10 mm vacuum gap, a separate analytic benchmark gives an extra pressure **7.3890e-10 Pa** for alpha_AuAu=1. This is about **57.9%** of the pressure predicted by the long-range single-Yukawa component alone. It is NOT the torque response of the actual experimental apparatus.

## Independent numerical validation

`test_phase7.py` checks the finite-sphere form factor against independent radial-volume quadrature (5 cases) and the finite-slab pressure against independent double integrals (4 cases). Both pass. `phase7_empirical_screen.py` creates all CSV files and plots.

## Published experimental comparison

Lee et al., *Physical Review Letters* **124**, 101101 (2020), took data at detector-attractor separations of **52 micrometres to 3.0 mm** and reported an excellent Newtonian fit. Their published test statistic is chi-square **275.0 for 285 degrees of freedom**. Our independent survival-function calculation gives **p=0.6538902312**, consistent with the paper's displayed **0.654**.

The researchers excluded a *single-Yukawa*, gravitational-strength interaction with a range longer than **38.6 micrometres at 95% confidence**. That number is **not** a 95% limit on the present *difference of two Yukawa terms*: the competing terms can partly cancel and the response must be integrated through the actual detector and attractor shapes.

The experiment measured harmonic **torsional torques**, not the simple force between point masses or infinite plates. The model would need predictions for their 18-fold and 120-fold azimuthal geometries and the experiment's nuisance-parameter covariance. We do not have those likelihood inputs here. **No model-specific confidence interval or exclusion claim was calculated in Phase 7.**

Other relevant constraints include scalar coupling bounds from atomic spectroscopy (Dzuba, Flambaum and Mansour, 2024). In 2026 Amaral et al. proposed a new magnetically levitated fifth-force experiment around the millimetre scale, and Banks et al. proposed atom-interferometer tests of *screened* scalars. These proposals are **not** completed measurements.

## Coupling normalization is not a discovery

For neutral gold, Z/A=79/197, a hypothesized scalar-electron Yukawa coupling would have illustrative g_e~**6.7445e-19** for an Au-Au fifth-force strength alpha_AuAu=1 in the point-body long-distance normalization. Different materials and exact microscopic interactions can alter composition dependence. No experimental bound on this g_e was derived from the available public summary statistics.

## FTL propagation has a separate, unmet proof burden

Even detecting an additional static force would not establish that perturbations propagate faster than light. The quartic field's group velocity exceeds c at large k within its **assumed equation**, but the high-k physics is unverified and cannot be extrapolated beyond an effective theory's range without justification. A superluminal claim requires (i) an identified physical field; (ii) a calibrated source with time-encoded new information; (iii) an independent receiver; (iv) a demonstrated arrival earlier than the appropriate electromagnetic light-front control; (v) noise/latency controls; and (vi) independent replication.

## Phase 8 external scientific gate

1. Obtain numerical torque data / likelihood and as-built geometry from a published gravity experiment; request confirmation from experimental authors if missing.
2. Implement a physically normalized three-dimensional Fourier-Bessel torque template for both poles, reusing a common nuisance-parameter covariance.
3. Fit the actual measured torques to the two-pole model; publish confidence limits with statistical coverage tests and robustness to systematic fields.
4. Separately formulate a finite-bandwidth *propagating* signal model with physically accessible source/detector coupling and realistic instrumental noise, not arbitrary dimensionless thresholds.
5. Seek independent peer scrutiny before public claims about new physics.

## Source list

1. Lee et al. (2020), https://doi.org/10.1103/PhysRevLett.124.101101 ; preprint https://arxiv.org/abs/2002.11761
2. Eot-Wash project explanation, https://www.npl.washington.edu/eotwash/inverse-square-law
3. Dzuba et al. (2024), https://doi.org/10.1103/PhysRevD.110.055022
4. Amaral et al. (2026), https://doi.org/10.1103/pqrs-bpgj — **proposal**
5. Banks et al. (2026), https://doi.org/10.1103/3486-4m4t — **proposal**

**Public statement:** ANDROMEDA-5 Phase 7 is a theoretical/computational model comparison, not empirical evidence that a new field or faster-than-light transport exists.