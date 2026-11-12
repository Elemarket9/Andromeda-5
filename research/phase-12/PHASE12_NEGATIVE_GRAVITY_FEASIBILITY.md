# ANDROMEDA-5 — Phase 12 feasibility check: negative gravitational objects, repulsive forces and superluminal travel
**Date:** 12 November 2026
**Status:** Internal research continuation, mathematical deductions and literature review. **No new interaction, negative-gravitational-mass object, warp mechanism, or faster-than-light information/transport has been discovered or demonstrated.**

## Executive decision
**A universally coupled stable real scalar based on the existing Phase 10–11 static kernel cannot generate net point-mass repulsion by changing the sign of its real coupling.** Its extra pair potential has an attractive sign for like positive-mass sources. If a hypothetical *phenomenological* negative \(\alpha\) is permitted without that microscopic completion, point-mass repulsion first requires \(\alpha<-1.3006056\) for the selected \(\ell=0.2\) mm, \(\mu=1000\ {\rm m}^{-1}\). That threshold is mathematically exact within this fixed two-pole formula, not a realizable or experimentally allowed device parameter. Even a repulsive force would not by itself allow massive objects to exceed the local speed of light. Thus the current model is **not a defensible route to an antigravity propulsion device or FTL**.

## 1. Distinguish four phenomena
1. **Negative gravitational mass:** a negative gravitational source charge (possibly negative total gravitating energy), which has not been observed as a controllable isolated laboratory object.
2. **Repulsive fifth-force interaction:** can arise from different source charges or field structures without either object having negative gravitational mass. It need not overcome Newtonian attraction.
3. **Negative effective inertial mass:** a band/dispersion property of excitations in engineered media. Khamehchi *et al.*, PRL **118**, 155301 (2017), https://doi.org/10.1103/PhysRevLett.118.155301, demonstrated this in a Bose–Einstein condensate; it is **not negative gravitational mass** and does not create a gravity drive.
4. **Negative local quantum energy density:** occurs in certain quantum states (e.g. Casimir phenomena), but does not imply net negative gravitational mass. Costa & Matsas, PRD **105**, 085016 (2022), https://doi.org/10.1103/PhysRevD.105.085016, derive conditions making the total mass of a static Casimir apparatus nonnegative.

CERN ALPHA-g measured antihydrogen falling *down* rather than an antigravity rise; repulsive \(\sim1g\) antimatter–Earth gravity is excluded in their setup: Anderson *et al.*, *Nature* **621**, 716 (2023), https://doi.org/10.1038/s41586-023-06527-1. This is not a test of every conceivable exotic-field model.

## 2. Exact point-mass theorem for the current model
From the Phase 10 assumed potential,
\[
U=-\frac{Gm_1m_2}{r}\left[1+\frac{\alpha}{s}(e^{-ar}-e^{-br})\right],\qquad
s=\sqrt{1-4\ell^2\mu^2},\
a^2=\frac{1-s}{2\ell^2},\
b^2=\frac{1+s}{2\ell^2},
\]
the inward radial force magnitude divided by the inward Newtonian magnitude is
\[
\frac{F_\text{inward}}{F_N}=1+\alpha B(r),\qquad
B(r)=\frac{(1+ar)e^{-ar}-(1+br)e^{-br}}{s}.
\]
For \(0<a<b\), \(B(r)>0\) for all \(r>0\) because \(f(x)=(1+x)e^{-x}\) is strictly decreasing. Its derivative is
\[
B'(r)=\frac{r}{s}\big(b^2e^{-br}-a^2e^{-ar}\big).
\]
There is precisely one positive maximum, at
\[
r_*=\frac{2\ln(b/a)}{b-a}.
\]
For \(\ell=2\times10^{-4}\ {\rm m}\) and \(\mu=1000\ {\rm m}^{-1}\):
- \(s=0.916515138991168\);
- \(a=1021.5482184461\ {\rm m}^{-1}\), \(b=4894.5315646535\ {\rm m}^{-1}\);
- \(r_*=0.80909164688595\ {\rm mm}\);
- \(B(r_*)=0.7688725894578924\);
- **net point-mass repulsion exists somewhere only for \(\alpha<-1/B(r_*)=-1.30060560580664\)**. Equality gives zero net force at one radius, not repulsion.
For \(\alpha=0\), ordinary Newtonian attraction remains. For \(\alpha>0\), the correction is always additional attraction. A phenomenological \(\alpha=-0.0181\) would merely reduce inward force by at most 1.3917%, far short of changing its sign. These statements concern point sources and an assumed static kernel, **not gravitational mass reversal or an experimental result**.

## 3. A stronger obstruction: real scalar source coupling fixes the sign
Consider the possible *microscopic* completion, explicitly **not yet established as the actual Phase 6 mass coupling**:
\[
\mathcal{L}=\frac12\left[c^{-2}\dot\phi^2-(\nabla\phi)^2-\ell^2(\nabla^2\phi)^2-\mu^2\phi^2\right]+J\phi,
\qquad J=g\rho_m,
\]
with real universal \(g\), \(\ell>0\), \(\mu\ge0\). Define \(A=-\nabla^2+\ell^2\nabla^4+\mu^2\). In Fourier space \(A(k)=k^2+\ell^2k^4+\mu^2>0\) for nonzero k (and positive for all k when \(\mu>0\)). For a static source the energy functional is
\[
E[\phi]=\frac12\langle\phi,A\phi\rangle-\langle J,\phi\rangle.
\]
Minimizing gives \(\phi=A^{-1}J\) and \(E_\text{min}=-\frac12\langle J,A^{-1}J\rangle\).
The source-pair Green function is
\[
A^{-1}(r)=\frac{e^{-ar}-e^{-br}}{4\pi s r}>0,\quad r>0.
\]
Therefore two like universal point sources \(J_i=gm_i\delta(x-x_i)\) have cross-interaction
\[
U_\phi(r)=-\frac{g^2m_1m_2}{4\pi s r}(e^{-ar}-e^{-br}).
\]
Comparing with the Phase 10 mass-normalized potential gives \(\alpha=g^2/(4\pi G)\ge0\), in this field normalization. Flipping \(g\rightarrow-g\) for *every* object does not make \(\alpha\) negative: the product \(g^2\) remains nonnegative.

**Conditional no-go:** This class of stable, real scalar field with same-sign universal mass sources does **not** produce a negative-gravity object or repulsion between ordinary masses. A negative phenomenological \(\alpha\) requires changing the source/field theory (e.g., opposite source-charge signs for selected materials, vector-like repulsion, a wrong-sign kinetic term with stability concerns, or another well-defined theory). Not all repulsive field theories are excluded by this scalar argument.

The dispersive operator uses higher *spatial* derivatives and a preferred rest frame; a positive static operator does not by itself establish Lorentz invariance, a UV-complete quantum theory, gravitational backreaction or causality.

## 4. Contact with Phase 11 constraints
Phase 11 inferred a **conditional approximate** positive envelope \(\alpha\lesssim 0.01809\) from published single-Yukawa fits using an unverified shared, projected linear-Gaussian likelihood and unknown cross-template correlation. That number is **not** the Eöt-Wash experiment's measured two-pole 95% exclusion. Extending the *same hypothetical likelihood* to negative \(\alpha\) yields a conservative lower envelope of approximately \(-0.0583846\) using its published intermediate \(D=-78.1465135\), \(Q_{\min}=3549.9963\), \(s=0.91651514\) and \(\Delta\chi^2=6.17\):
\[
\alpha_\mathrm{lower,approx}=\frac{sD}{Q_{\min}}-\frac{s\sqrt{6.17}}{\sqrt{Q_{\min}}}\simeq -0.058385.
\]
This indicative coupling scale is over **22 times** smaller in magnitude than \(|\alpha|=1.3006\), but it is **not an experimental exclusion of negative \(\alpha\)** until original geometry, model-specific nuisance fits, covariance and published data are used to fit the *combined two-pole* model. This negative-parameter calculation is a stress test of the approximation, not an authorized new limit.

## 5. Repulsion does not imply faster-than-light travel
A force causing outward acceleration is not the same as (a) negative gravitational mass, (b) a metric shortcut, or (c) an information signal outside the light cone. In ordinary local relativistic dynamics, an accelerating massive object remains at speeds below c relative to a local inertial observer.

Alcubierre-style effective FTL depends on *spacetime geometry*, not merely on the sign of a two-point potential. Olum (PRL **81**, 3567, 1998, https://doi.org/10.1103/PhysRevLett.81.3567) proved a weak-energy-condition obstruction for a well-defined superluminal travel notion under stated assumptions. Santiago, Schuster & Visser (PRD **105**, 064038, 2022, https://doi.org/10.1103/PhysRevD.105.064038) carefully tested energy conditions of generic warp geometries. Positive-energy constant-velocity **subluminal** geometries have been modeled by Fuchs *et al.* (*Class. Quantum Grav.* **41**, 095013, 2024, https://doi.org/10.1088/1361-6382/ad26aa), but do not demonstrate FTL transportation. Published positive-energy superluminal proposals (e.g., Lentz 2021, https://doi.org/10.1088/1361-6382/abe692) have substantial unresolved physical and energy-condition critiques; a paper's metric is not a device.

## 6. Credible continuation: two separate testable tracks
**Track A: model-internal falsification.** Derive the matter coupling from an explicit healthy action (not by manually choosing negative \(\alpha\)); calculate static Green function, conserved stress-energy, energy-condition tests, and experimental signed-template fits. If the scalar remains universally coupled with real \(g\), record the repulsion obstruction as a negative result and do not claim a device.

**Track B: spacetime geometry.** Independently reproduce a published positive-energy *subluminal* metric, computing Einstein tensor \(G_{\mu\nu}\) and stress-energy \(T_{\mu\nu}=(c^4/8\pi G)G_{\mu\nu}\); test WEC, NEC and DEC for **all** relevant observers, global causality, horizons, tidal loads, energy scale, source formation and controllability. Then apply identical audits to a candidate superluminal geometry. No metric construction or feasible engineering breakthrough is claimed in this phase.

Decision criteria for claiming progress:
1. A mathematically consistent action and source law, not a manually signed force parameter.
2. Stability and quantitative experimental compatibility.
3. Physically plausible sources and stress-energy (including all apparatus contributions).
4. Operational definition and calculation of transport/signal time in full dynamical spacetime, beyond wave group velocity.
5. Independent reproduction before public claims.

## Reproduction and integrity
Run \`python research/phase-12/negative_gravity_threshold.py\` (Python standard library only).
No instrument data were newly fitted; no simulations of a real physical negative-mass object or propulsion system were run. Phase 12's contribution is a conditional mathematical deduction from an existing phenomenological model plus verified literature context. Do not call this a fundamentally novel theory, an experimental discovery, or proof that all FTL mechanisms are impossible.

## References
- Anderson *et al.*, Nature 621, 716–722 (2023), https://doi.org/10.1038/s41586-023-06527-1
- Khamehchi *et al.*, Phys. Rev. Lett. 118, 155301 (2017), https://doi.org/10.1103/PhysRevLett.118.155301
- Costa & Matsas, Phys. Rev. D 105, 085016 (2022), https://doi.org/10.1103/PhysRevD.105.085016
- Olum, Phys. Rev. Lett. 81, 3567 (1998), https://doi.org/10.1103/PhysRevLett.81.3567
- Santiago, Schuster & Visser, Phys. Rev. D 105, 064038 (2022), https://doi.org/10.1103/PhysRevD.105.064038
- Bobrick & Martire, Class. Quantum Grav. 38, 105009 (2021), https://doi.org/10.1088/1361-6382/abdf6e
- Fuchs *et al.*, Class. Quantum Grav. 41, 095013 (2024), https://doi.org/10.1088/1361-6382/ad26aa
- Lentz, Class. Quantum Grav. 38, 075015 (2021), https://doi.org/10.1088/1361-6382/abe692
