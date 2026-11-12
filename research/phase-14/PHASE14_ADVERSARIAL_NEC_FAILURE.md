# Phase 14 adversarial addendum — the conformal candidate FAILS the null energy condition

**Date:** 12 November 2026  
**Status:** Executed mathematical curvature calculation, no experimental observation. This addendum supersedes the earlier "all-observer conditions not yet tested" uncertainty for the *specific* candidate parameters and point tested. The original positive **Eulerian** energy result remains true, but does not imply a physically positive-energy warp drive.

## Candidate audited

Use the exact constructed geometry in \`PHASE14_CONFORMAL_GEOMETRY_REPORT.md\`:
\[
ds^2=-c^2dt^2+\psi(r)^4[(dx-vf(r)dt)^2+dy^2+dz^2],
\qquad
\psi(r)=1+\frac{A}{\sqrt{r^2+L^2}},
\]
where \(R=100\) m, \(w=10\) m, \(A=0.1\) m, \(L=100\) m and \(v/c=0.0045\). Wall profile is the C2 quintic step.

## A single null vector decisively falsifies NEC

We independently computed the full \(4\times4\) Einstein tensor \(G_{\mu\nu}\) in coordinates \(x^\mu=(ct,x,y,z)\), using JAX 64-bit forward automatic differentiation of the metric, Christoffel symbols and Ricci tensor. At the equatorial midpoint of the shell, \((ct,x,y,z)=(0,0,100,0)\ {\rm m}\), construct the **local orthonormal** Eulerian frame:

\[
n^\mu=(1,bf,0,0),\qquad e_{\hat x}^\mu=(0,\psi^{-2},0,0),\qquad k^\mu=n^\mu+e_{\hat x}^\mu,\quad b=v/c.
\]
This satisfies \(g(n,n)=-1\), \(g(e_{\hat x},e_{\hat x})=1\), \(g(n,e_{\hat x})=0\), and \(g(k,k)=0\). The chosen \(k\) is a future-directed null direction.

The automatic-differentiation calculation finds

\[
G_{\mu\nu}n^\mu n^\nu=+3.34051070999\times10^{-8}\ {\rm m}^{-2},
\]
but
\[
\boxed{G_{\mu\nu}k^\mu k^\nu=-8.94286966642\times10^{-6}\ {\rm m}^{-2}<0.}
\]
The ordinary Einstein equation implies \(T_{\mu\nu}k^\mu k^\nu=(c^4/8\pi G)G_{\mu\nu}k^\mu k^\nu <0\): **the null energy condition (NEC) is violated**. Thus the weak energy condition (WEC), which requires nonnegative energy for every timelike observer, is also violated (by continuity toward the negative null direction). It is unnecessary to search every direction: **one explicit normalized null direction is decisive**.

Physical-stress-unit cross-check:
- \(T_{\mu\nu}n^\mu n^\nu\approx +1.6086075\times10^{35}\ {\rm J\,m^{-3}}\) (Eulerian energy positive);
- \(T_{\mu\nu}k^\mu k^\nu\approx -4.3063976\times10^{37}\ {\rm J\,m^{-3}}\) for this normalized null vector (NEC violated).

## Independent internal numerical check

The earlier Phase 14 analytic ADM Hamiltonian expression gives \(H={}^{(3)}R+K^2-K_{ij}K^{ij}\). At the chosen point:
\[
H/2=3.340510709992958\times10^{-8}\ {\rm m}^{-2}.
\]
The full differentiable Einstein tensor instead yields \(G_{\mu\nu}n^\mu n^\nu=3.340510709992933\times10^{-8}\ {\rm m}^{-2}\), matching to approximately \(2.5\times10^{-22}\ {\rm m}^{-2}\). The frame norm and null norm are also independently asserted to numerical precision.

This is a powerful internal consistency check, **not** a substitute for external review. Full tensor calculations still warrant independent implementation and systematic precision tests.

## Research decision

- Retain the **true** Phase 14 analytic result that Eulerian energy is positive everywhere for this metric.
- **Reject** any inference that this candidate provides an all-observer positive-energy/NEC-preserving warp geometry.
- **Do not** claim a physical superluminal solution from the \(1.776\) ns flat-coordinate comparison: the route comparison is not operational/invariant and the candidate NEC fails.
- A positive gravitational ADM mass and positive energy for one observer are *not enough*. This directly illustrates the caution emphasized by Santiago–Schuster–Visser (2022) and newer observer-robust methods in WarpAX (2026).
- Continue only after reproducing a published physically consistent **subluminal** reference, testing all-observer conditions, causal formation, and physical matter stress. If a candidate fails, preserve that result rather than massaging the design to create a visual FTL claim.

## Source and reproduction

\`python research/phase-14/phase14_null_energy_countertest.py\`

Requires \`jax\` and \`numpy\`; double precision enabled. This is an independent **automatically differentiated** tensor calculation, not a source-matched finite-difference fit and not laboratory data.

References:
- https://doi.org/10.1088/1361-6382/ad26aa
- https://doi.org/10.1103/PhysRevD.105.064038
- https://arxiv.org/abs/2602.18023
