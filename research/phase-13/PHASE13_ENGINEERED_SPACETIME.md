# ANDROMEDA-5 — Phase 13: engineered-spacetime research, analytical energy floor and metric travel-time benchmark

**Date:** 12 November 2026  
**Scientific status:** Original calculations and an independent derivation using *established general relativity*. No independent new physical interaction, realizable warp device, FTL signal or original spacetime solution has been demonstrated. The original Alcubierre-type ansatz and its negative energy are prior art. The algebraic wall bound and comparative numerical benchmark here are applied research checks, **not claimed as new theorems in the literature**.

## Executive result: screen geometries before investing in their optimization

We tested a restricted, asymptotically Minkowski spacetime of the Alcubierre/Natário *shift-only* type. It produces a coordinate light-travel-time advantage over a comparable flat-space route **if the metric already exists**, but it has **provably negative energy density** in the bubble wall. This holds for any positive lapse with spatially flat slices and this specific \(x\)-directed shift. Merely changing a bubble's smooth wall profile cannot change the sign. Weighted Cauchy–Schwarz provides a lower bound on the integrated negative energy required by any radial transition of the specified radius and thickness.

This explicitly eliminates **flat-slice, pure-\(x\)-shift, positive-energy warp designs** from ANDROMEDA-5's search within ordinary Einstein gravity, while leaving more general geometries and other theories unresolved. A productive next candidate must include nontrivial spatial geometry or a genuinely different shift structure, and it must be tested for **all** timelike/null observers, not only one observer family.

## 1. Physical context and literature

- Alcubierre (1994) proposed the original warp-style metric and explicitly recognized exotic-matter requirements: https://doi.org/10.1088/0264-9381/11/5/001.
- Olum (1998) established a weak-energy-condition obstruction to a well-defined notion of superluminal travel under stated assumptions: https://doi.org/10.1103/PhysRevLett.81.3567.
- Santiago, Schuster & Visser (2022) developed generic-warp-field energy-condition no-go arguments, with their stated subsidiary assumptions: https://doi.org/10.1103/PhysRevD.105.064038.
- Fuchs *et al.* (2024) numerically demonstrated a **subluminal** positive-mass-shell warp geometry reported to satisfy energy conditions in their model; not superluminal propulsion. This uses a more general matter/geometry configuration than the constrained benchmark below: https://doi.org/10.1088/1361-6382/ad26aa.
- An T. Le (2026) released WarpAX, observer-robust energy-condition analysis and related geodesic computations; preprint versions are evolving and not independent evidence of FTL technology: https://arxiv.org/abs/2602.18023; software https://github.com/anindex/warpax; archived release https://doi.org/10.5281/zenodo.22728088.

These are external researchers' contributions, not discoveries of ANDROMEDA-5.

## 2. Our specific benchmark and assumptions

Use coordinates \(t,x,y,z\), physical speed \(c\), and a *pre-established stationary* metric

\[
ds^2=-c^2dt^2+[dx-vf(r)\,dt]^2+dy^2+dz^2,\qquad r=\sqrt{x^2+y^2+z^2}.
\]

We assume fixed spatial slices \(\gamma_{ij}=\delta_{ij}\), ADM lapse \(N=1\), shift only along \(x\), \(\beta^x=-v f(r)\), and \(f=1\) inside \(r_-=R-w/2\) and \(f=0\) outside \(r_+=R+w/2\).

Because it is initially *posited* rather than obtained from a constructed matter source, this line element is a geometric thought experiment, not a propulsion design.

### Two profile regularities

A numerical C1 baseline uses \(f_\mathrm{cubic}(t)=1-3t^2+2t^3\), \(t=(r-r_-)/w\). It is only globally C1 when joined to constant regions. Thus it is retained as a lower-regularity sensitivity check, **not** the preferred classical GR source model.

The default smoother C2 wall uses \(f_\mathrm{quintic}(t)=1-10t^3+15t^4-6t^5\). It has \(f'=f''=0\) at both transition boundaries and is at least C2 when joined to constant regions. This meets the usual classical curvature differentiability requirement, but does **not** demonstrate a physically realizable stress-energy source.

## 3. Exact restricted-ansatz energy obstruction

The ADM Hamiltonian constraint in general relativity is

\[
\frac{16\pi G}{c^4}\epsilon =
{}^{(3)}R + K^2-K_{ij}K^{ij},
\]

when \(K_{ij}\) is defined with \(x^0=ct\), so it has units m\(^{-1}\), and \(\epsilon=T_{\mu\nu}n^\mu n^\nu\) is physical energy density. On spatially flat slices \( {}^{(3)}R=0\).

For \(\beta^x=-(v/c)f(r)\) and unit lapse,
\[
K_{xx}=-(v/c)\partial_x f,\quad
K_{xy}=-(v/2c)\partial_yf,\quad
K_{xz}=-(v/2c)\partial_zf,
\]
so
\[
K^2-K_{ij}K^{ij}
=-\frac{v^2}{2c^2}
\left[(\partial_y f)^2+(\partial_z f)^2\right].
\]
Therefore
\[
\boxed{\epsilon=-\frac{c^2v^2}{32\pi G}
       \left[(\partial_y f)^2+(\partial_z f)^2\right]\le0.}
\]
It is **strictly negative** wherever the wall has a transverse gradient for nonzero \(v\). Hence the WEC is violated for the slice-normal physical observer there. One counterexample observer suffices to disprove WEC: it is unnecessary to check every observer before rejecting this *specific* candidate.

The result persists if flat slices are kept but the ADM lapse is replaced by any finite positive \(N(x)\): each \(K\) term acquires \(1/N\), and the density becomes \(\epsilon=-(c^2v^2/(32\pi G N^2))|\nabla_\perp f|^2\). **Changing the lapse alone cannot make this restricted shift geometry WEC-positive.**

This is **not** a theorem excluding all warp geometries, all shift vector fields, or modified gravity; a nonflat \(\gamma_{ij}\), changed shift structure or different field equations requires a new calculation.

## 4. Integrated negative Eulerian energy

For a spherical radial wall, \(|\nabla_\perp f|^2=\sin^2\theta\, f'(r)^2\) and the angular integral of \(\sin^2\theta\) is \(8\pi/3\). The spatial integral of the Eulerian energy density is

\[
E_\mathrm{Eulerian}=-\frac{c^2v^2}{12G}\, I,\qquad
I=\int_0^\infty r^2[f'(r)]^2dr.
\]

**Interpretation:** This is the integral of local Eulerian matter energy on the chosen slice, *not* the ADM mass, the total energy of a physical apparatus or a demonstrated energy source.

For \(R>w/2>0\), \(\int_{r_-}^{r_+}f'(r)dr=-1\). Weighted Cauchy–Schwarz yields

\[
1\le I\int_{r_-}^{r_+}r^{-2}dr
=I\left(\frac{1}{r_-}-\frac{1}{r_+}\right).
\]
Thus **every sufficiently regular radial wall with these fixed boundary values and thickness obeys**
\[
\boxed{I\ge I_{\inf}=\frac{r_-r_+}{w}=\frac{R^2-w^2/4}{w}.}
\]
Equality corresponds to \(f'\propto-r^{-2}\) on the open wall and generally cannot be reached exactly with the imposed smooth junction derivatives; this is a lower bound/infimum, not a fully constructed smooth saturating profile.

The two polynomial integrals are analytically exact:

\[
I_\mathrm{cubic}=\frac{6R^2}{5w}+\frac{3w}{70},
\qquad
I_\mathrm{quintic}=\frac{10R^2}{7w}+\frac{5w}{154}.
\]

For \(R=100\) m, \(w=10\) m:

- Universal radial-wall lower bound \(I_{\inf}=997.5\ \mathrm m\).
- Cubic C1 profile \(I=1200.42857143\ \mathrm m\).
- Preferred quintic C2 profile \(I=1428.89610390\ \mathrm m\).
- Even optimized over *all* wall profiles within this fixed ansatz, the negative energy magnitude cannot fall below \(1.0060\times10^{44}\) J at \(v=0.1c\). That is 69.81% of the preferred C2 example's energy magnitude; wall smoothing or optimization cannot remove the negative-energy sign.

The C1 numerical baseline earlier gave \(-1.21069\times10^{44}\) J, but the more regular C2 wall requires \(-1.44111\times10^{44}\) J. This regularity difference is important and must not be silently mixed.

## 5. Geometric transit-time test, **not operational FTL**

Along the symmetry axis \(y=z=0\), the positive-directed null branch satisfies
\[
\frac{dx}{dt}=c+v f(|x|).
\]
The assumed metric is Minkowski outside the bubble. Fix two exterior endpoints \(x=\pm r_+\) and use the same asymptotic \(t\)-coordinate. The axis null crossing time is
\[
T_{\rm assumed}=2\int_0^{r_+}\frac{dr}{c+v f(r)};\qquad
T_{\rm flat}=\frac{2r_+}{c};\qquad
\Delta T=T_{\rm flat}-T_{\rm assumed}.
\]

For \(R=100\) m, \(w=10\) m and \(v=0.1c\):

| Metric assumption | Flat light time across 210 m | Assumed metric null time | Coordinate time advantage | Integrated Eulerian energy |
|---|---:|---:|---:|---:|
| Cubic C1 baseline | 700.4846 ns | 639.7623 ns | 60.7223 ns | \(-1.21069\times10^{44}\) J |
| Quintic C2 preferred | 700.4846 ns | 639.7740 ns | 60.7106 ns | \(-1.44111\times10^{44}\) J |

The inferred endpoint effective speed for the quintic case is about \(1.09489c\), **which is not a measured local velocity and is not evidence of a usable FTL channel**. The assumed geometry already contains the superluminal-looking endpoint shortcut. This calculation neither creates such a metric nor accounts for causal construction, horizons, backreaction, matter dynamics, quantum inequalities or experimental testability. A complete operational claim must compare causally accessible setup, emitted signals and registered reception with physically constructible asymptotic observers, per Olum's caveats.

For \(v=0\), the script confirms zero time advantage and zero integrated negative energy. With a fixed wall and shape, \(|E|\propto v^2\) exactly in this ansatz.

## 6. Design conclusion: change the metric family, not merely the profile

### Excluded by the exact restricted-ansatz argument
- Flat spatial metric, pure x-directed radial shift and positive lapse cannot give a WEC-positive bubble wall with \(v\ne0\).
- Varying \(N(x)>0\) while keeping this slice/shift structure cannot reverse the local negative Eulerian energy.
- Optimizing only the smooth radial transition cannot evade the integrated negative energy floor.

### Next credible research track
Start from a general stationary ADM metric
\[
ds^2=-N(\mathbf x)^2c^2dt^2+
\gamma_{ij}(\mathbf x)(dx^i+\beta^i cdt)(dx^j+\beta^j cdt)
\]
with nonflat spatial metric, for example \(\gamma_{ij}=\psi(\mathbf x)^4\delta_{ij}\), plus a physically motivated positive-mass shell. First **reproduce** the published Fuchs *et al.* subluminal positive-shell benchmark, rather than claim it as our discovery. Compute \(G_{\mu\nu}\) and \(T_{\mu\nu}=(c^4/8\pi G)G_{\mu\nu}\); check source conservation, asymptotic flatness, ADM mass, all-observer WEC/NEC/DEC/SEC, physical source stress components, tidal acceleration, integrated energy, time-of-flight and causal creation/formation.

Only *after* independent reproduction should we propose an explicitly different metric or a falsifiable optimization algorithm. WarpAX (2026) is a candidate cross-check, not a substitute for independent code or a claim of positive energy. If constraints cannot be satisfied, report the negative result and identify which assumption fails.

**Actual Phase 13 finding:** quantitative and analytic rejection of a simple flat-slice search family, a wall-shape energy floor, and a tested light-time/energy benchmark. **Not** a new spacetime theory, a positive-energy superluminal drive or a demonstration of FTL travel.

## Reproducibility and provenance

The repository includes \`research/phase-13/phase13_shift_metric_benchmark.py\`, with Python standard library only and explicit assertions for:
1. exact analytic vs Simpson wall energy integral,
2. independent grid-resolution agreement,
3. C1 vs C2 regularity sensitivity,
4. \(v=0\) zero-response control,
5. \(v^2\) integrated energy scaling.
Run: \`python research/phase-13/phase13_shift_metric_benchmark.py\`.
The Phase 13 numbers are calculated from these geometric assumptions and are **not original laboratory measurements**. There is no validated stress-energy source or physical warp construction.
