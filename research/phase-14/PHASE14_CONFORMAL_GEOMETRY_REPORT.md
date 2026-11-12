# ANDROMEDA-5 — Phase 14: conformal positive-mass geometry, Eulerian constraint and coordinate light-time test

**Date:** 12 November 2026  
**Classification:** A constructed *mathematical example within known general relativity*, not an independently peer-reviewed novel physical discovery, feasible matter source, warp drive, or experimentally demonstrated FTL travel. The benchmark has not passed all-observer energy conditions, complete stress-energy source tests, horizon/causal tests, or operational end-to-end comparison.

## 1. Motivation and research boundary

Phase 13 showed that the spatially flat, pure-\(x\)-shift warp metric produces negative Eulerian energy at every bubble wall with a nonzero transverse gradient. We now test an explicitly **different metric family** with nontrivial spatial curvature, which can make the *single Eulerian observer family* measure nonnegative energy even with a small coordinate-time advantage. The question is whether this mathematical change is sufficient for a healthy physical spacetime. **It is not known to be.**

The idea of a positive-mass shell around a subluminal warp-like geometry is not ours: see Fuchs *et al.* (2024), https://doi.org/10.1088/1361-6382/ad26aa. The all-observer distinction is stressed by Santiago, Schuster and Visser (2022), https://doi.org/10.1103/PhysRevD.105.064038, and explored with mathematical/software certification by An T. Le (2026), https://arxiv.org/abs/2602.18023. Olum's causal definition is important, https://doi.org/10.1103/PhysRevLett.81.3567.

## 2. New candidate ansatz

Use a time-independent ADM metric with unit lapse, radial conformally flat spatial metric and an \(x\)-directed shift:
\[
ds^2=-c^2dt^2+\psi(r)^4[(dx-vf(r)dt)^2+dy^2+dz^2],\quad
r=\sqrt{x^2+y^2+z^2},\quad b=v/c.
\]

Set
\[
\psi(r)=1+\frac{A}{\sqrt{r^2+L^2}},\quad A>0,\ L>0.
\]
A positive conformal parameter \(A\) gives asymptotic ADM mass
\[
M_\mathrm{ADM}=\frac{2Ac^2}{G}.
\]
This is an inferred mass from the asymptotic three-metric, not a fabricated measured shell or a proof of a physically stable material source.

The wall \(f(r)\) is 1 inside radius \(r_-=R-w/2\), 0 outside \(r_+=R+w/2\), with globally C2 fifth-order smoothstep
\[
f(t)=1-10t^3+15t^4-6t^5,\quad t=(r-r_-)/w,\quad0\le t\le1.
\]
Thus \(0\le f\le1\), \(f'\le0\), \(\max |f'|=1.875/w\).

## 3. Exact proof of positivity for *normal observers only*

In coordinates \(x^0=ct\), \(N=1\), spatial metric \(\gamma_{ij}=\psi^4\delta_{ij}\), shift \(\beta^x=-b f\), the Einstein Hamiltonian constraint relates Eulerian energy density \(\epsilon=T_{\mu\nu}n^\mu n^\nu\) to
\[
H={16\pi G\epsilon\over c^4}={}^{(3)}R+K^2-K_{ij}K^{ij}.
\]

The conformally flat scalar curvature is
\[
{}^{(3)}R=-8\psi^{-5}\nabla^2\psi
=\frac{24 A L^2}{(\sqrt{r^2+L^2}+A)^5}>0.
\]
This is strictly decreasing in \(r\) for \(r>0\). Set \(h(r)=\psi'(r)/\psi(r)\le0\) and \(\theta\) the polar angle relative to the \(x\)-axis. Direct extrinsic-curvature contraction gives
\[
K^2-K_{ij}K^{ij}=
b^2\left[-\frac12 f'^2\sin^2\theta+
8f h f'\cos^2\theta+24 f^2h^2\cos^2\theta\right].
\]
The second and third terms are **nonnegative** since \(f\ge0\), \(f'\le0\), \(h\le0\).

In the wall \(r_-\le r\le r_+\), a conservative pointwise lower bound valid at **every polar angle** is
\[
H(r,\theta)\ge \frac{24AL^2}{(\sqrt{r_+^2+L^2}+A)^5}
-\frac{b^2}{2}\left(\frac{1.875}{w}\right)^2.
\]
Outside the wall \(f'=0\); the remaining shift terms are nonnegative, and \({}^{(3)}R>0\). Therefore if the right-hand side above is positive, \(\epsilon>0\) **everywhere** (for finite \(r\)) in this analytical metric. This proves positivity of the Eulerian energy density only. It does NOT establish the all-observer weak/null/dominant/strong energy conditions.

## 4. Concrete candidate, tested numerically and analytically

Assume \(R=100\) m, \(w=10\) m, \(L=100\) m, \(A=0.1\) m, \(b=0.0045\) (\(v=0.45\%\,c\)). Then:

- Minimum scalar-curvature contribution on the wall: \(3.73142038276\times10^{-7}\,{\rm m}^{-2}\).
- Conservative maximum negative shift term: \(3.55957031250\times10^{-7}\,{\rm m}^{-2}\).
- **Strictly positive wall lower bound:** \(H\ge1.71850070261\times10^{-8}\,{\rm m}^{-2}>0\), in all directions.
- Certified conservative maximum shift speed \(b_{\max}\approx0.00460734587\) for these geometry parameters.
- ADM mass \(M_\mathrm{ADM}=2.693181843\times10^{26}\ {\rm kg}\). This is about 0.14 Jupiter masses and is astronomically large for a 100 m-scale model. Its Schwarzschild-radius scale for the same mass is \(4A=0.4\ {\rm m}\); this comparison is not a horizon determination for our nonvacuum metric.

This provides a **non-flat geometry counterexample** to an overbroad interpretation of Phase 13's negative-energy result. Phase 13's no-go is restricted to *flat slices*, not all general relativity.

## 5. Coordinate null transit calculation

On the symmetry axis \(y=z=0\), the forward null ray obeys
\[
\frac{dx}{dt}=vf(|x|)+\frac{c}{\psi(|x|)^2}.
\]
For coordinate endpoints \(x=\pm(R+w/2)=\pm105\) m:
\[
T_\mathrm{metric}=2\int_0^{105m}\frac{dr}{vf(r)+c/\psi(r)^2}.
\]
The flat-coordinate comparison \(T_\mathrm{flat}=210m/c\) produces:

| Quantity | Computed value |
|---|---:|
| Flat-coordinate light time | \(700.48460\) ns |
| Metric axial null time | \(698.70841\) ns |
| **Coordinate time advantage** | **\(1.77619\) ns** |
| Endpoint coordinate speed normalized to \(c\) | \(1.0025421\) |

**Critical caveat:** The conformal metric is not flat even near these endpoints; the physical proper distance along a spatial slice differs from their 210 m coordinate separation. Comparing coordinate travel times with flat space alone is **not an invariant, operational definition of superluminal travel**. Source formation, full null geodesic accessibility and comparison of physically defined emitter/detector worldlines are also untested. Do not describe the 1.776 ns result as experimental FTL, a device speed, or a demonstrated causal shortcut.

## 6. Research verdict and what would be necessary for a physical breakthrough

**Established within the assumed metric:** An explicit, everywhere-positive Eulerian energy density with positive asymptotic ADM mass, plus a small calculated coordinate-time advance over a flat-coordinate benchmark. The Eulerian bound is *analytic*, not inferred merely from finite-grid samples.

**Not established:** Valid matter equations of state or constitutive relations, realizability, energy conservation under source dynamics, all-observer WEC/NEC/DEC/SEC, null geodesic operational FTL, absence of horizons and singularities, absence of quantum-instability/quantum-inequality obstructions, or literature novelty. These are decisive prerequisites, not optional implementation tasks.

**Immediate adversarial continuation:**
1. Independently derive the complete 4D Einstein tensor and validate \(\nabla_\mu T^{\mu\nu}=0\).
2. Compute orthonormal \(T_{\hat a\hat b}\), test energy conditions over all timelike/null observers (WarpAX can cross-check).
3. Compute null geodesics and invariant time-of-flight with operationally defined physical endpoints; compare spacetime curvature and geometric lengths, not coordinate distance alone.
4. Identify source physics and stress/pressure magnitudes required for \(M_\mathrm{ADM}\sim2.7\times10^{26}\) kg.
5. Compare with the Fuchs 2024 subluminal positive-shell geometry and the 2026 observer-robust studies; avoid claiming old ideas as discoveries.
6. If any energy condition or causal requirement fails, publish that precise negative result rather than optimizing a misleading apparent advance.

## Reproduction

- Script: \`research/phase-14/phase14_conformal_candidate.py\`
- Dependencies: Python standard library only.
- Command: \`python research/phase-14/phase14_conformal_candidate.py\`
- Checks in code: analytic positive lower bound; conservative \(b\) threshold; Newtonian mass parameter; Simpson grid convergence against independent grid; expected null time.
- Source data: *none*; this is a constructed mathematical geometry, not a new measurement.
