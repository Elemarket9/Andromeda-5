# ANDROMEDA-5 — Phase 5: Physical field, source coupling, detector backreaction and causal audit

**Research date:** 11 November 2026  
**Status:** Independently programmed numerical study of a *postulated* field theory. Not an experimental verification of faster-than-light communication, a new particle, a quantum-vacuum engine, or an original physical law.

## Executive finding

We extended the Phase 4 source-to-field calculation into a fully coupled one-dimensional source–field–oscillator model. The source drives the scalar field and the receiver is a dynamical oscillator whose position also drives the field (backreaction). The **chosen mathematical model** shows a nonzero receiver response before an ordinary wave could cross the same separation; ordinary-field, source-off and coupling-off controls are zero. Numerical refinements and field-plus-detector energy accounting support this calculation. It remains an assumption that any such field can interact with actual matter.

**Most important limitation:** the early response varies with the postulated ultraviolet (high-wavenumber) dispersion. The physical field, its matter coupling, its experimentally permissible strength, a quantum-consistent ultraviolet completion and a realizable detector are all missing.

## 1. Precise source model and action

Units are normalized with ordinary vacuum light speed `c=1`. Spatial length, elapsed time, field amplitude, coupling and energy are **model units**, not metres, seconds, newtons, or joules. The field propagates in an expressly preferred frame.

The candidate action, using a localized receiver profile `w_d(x)` and source profile `w_s(x)`, is:

```text
S = int dt { int dx [1/2 phi_t^2 - 1/2 phi_x^2
                     - 1/2 ell^2 phi_xx^2 - 1/2 mu^2 phi^2]
             + 1/2 (q_t^2 - Omega^2 q^2)
             + lambda q int dx w_d(x) phi(x,t)
             + A s(t) int dx w_s(x) phi(x,t) }
```

The Euler–Lagrange equations are:

```text
phi_tt - phi_xx + ell^2 phi_xxxx + mu^2 phi
     = A s(t) w_s(x) + lambda q w_d(x)

q_tt + Omega^2 q = lambda int dx w_d(x) phi(x,t).
```

- `phi` = hypothetical scalar field.
- `ell` = dispersion length in model units; its value is chosen, not inferred from experiment.
- `mu` = field mass-gap parameter, set to 0.2 in the example.
- `q` = a modeled detector oscillator, natural frequency `Omega=2`.
- `lambda` = *assumed* coupling of detector and field, 0.3 in the reference run.
- `A s(t) w_s(x)` = user-controlled source; the source is spatially compact and on only for `0<t<0.35`.

The source is centered at `x=0`, width 0.35. The detector is at `x=2`, width 0.15. Thus the earliest possible ordinary-wave response is `t=2-0.35-0.15=1.50`. All model comparisons use the same setup and detector response at `t=1.00`.

The free-field dispersion is:

```text
omega^2(k) = mu^2 + k^2 + ell^2 k^4.
```

When `ell>0`, high-wavenumber group velocities exceed `c` in this preferred-frame mathematical model. This relationship is NOT a new discovery: higher-spatial-derivative and preferred-foliation models exist in the literature. It does not follow that the universe contains the postulated field.

## 2. Full energy accounting and dynamical stability

The total source-free Hamiltonian is:

```text
E = 1/2 int dx [phi_t^2 + phi_x^2 + ell^2 phi_xx^2 + mu^2 phi^2]
    + 1/2 [q_t^2 + Omega^2 q^2]
    - lambda q int dx w_d(x) phi(x).
```

After the external source is turned off, time-translation symmetry implies `dE/dt=0`. During the source pulse, the change in model energy equals work supplied by the external source:

```text
dE/dt = A s(t) int dx w_s(x) phi_t(x,t).
```

The coupled system does not have automatic positive energy for arbitrarily large `lambda`, even though the isolated field and oscillator do. Completing the square shows that a sufficient-and-in-this-quadratic-case necessary condition for positive potential energy is:

```text
lambda^2 < Omega^2 / S,
S = int dx w_d(x) [(-partial_xx + ell^2 partial_xxxx + mu^2)^(-1) w_d](x).
```

For the reference numerical discretization `S≈2.4194` and `lambda_critical≈1.2858`. The chosen `lambda=0.3` lies below this model stability threshold. This is a *classical quadratic* stability check, not a proof of quantum consistency.

A Fourier-mode exact free propagator with time-symmetric interaction kicks is used to integrate the coupled Hamiltonian, avoiding the high-frequency instability of a basic finite-step integrator. The source-off post-pulse energy drift in the reference run was about `9.2e-9` (fractional), and the energy/work mismatch was about `2.0e-8`. These are numerical error estimates.

## 3. Computed source–detector results

At `t=1.0`, before the control's ordinary-wave light cone (`t=1.5`):

| Assumed field or control | Receiver oscillator displacement q (arbitrary units) |
|---|---:|
| Ordinary wave, `ell=0` | -1.45e-19 |
| Modified field, `ell=0.05` | -2.01673e-8 |
| Modified field, `ell=0.15` | -3.15898e-7 |
| Modified field, `ell=0.30` | +1.82412e-5 |
| Source off | 0 |
| Detector coupling off | 0 |

**Resolution caveat:** Those figures use step `dt=0.004`. The early signal is small enough that timestepping refinement matters; for the `ell=0.15` reference it moves from `-3.15898e-7` at `dt=0.004` toward approximately `-3.142e-7` as `dt` is reduced. At fixed `dt=0.004`, spatial grids of 8,192 and 16,384 points differ by `0.028%`; low-resolution grids are misleading because they under-resolve the narrow detector. The initial failed convergence attempt and corrected method are both included in the research package.

An important engineering point: this 'receiver' is a **mathematical oscillator**, not a known matter detector. Its `q` has no established calibration in metres or volts, and no source technology is identified.

## 4. Coupling strength: a measurable prediction is still missing

A sweep in the *assumed coupling* found that `q(t=1)` is approximately proportional to `lambda` for weak interactions:

| lambda | q(t=1), model units |
|---:|---:|
| 0.03 | -3.15879e-8 |
| 0.10 | -1.05294e-7 |
| 0.30 | -3.15898e-7 |
| 0.60 | -6.31908e-7 |

In a physical source/detector, the transmitted signal would depend on *both* the source's and the receiver's coupling to the new field. We do not know either coupling. An arbitrary modeled detector noise floor or simulated bit accuracy cannot establish a realistic signal-to-noise ratio. **Before claiming a laboratory test, the theory must provide the source operator, detector operator, coupling dimensions and strength, expected physical units, and instrument backgrounds.**

One candidate portal for further scrutiny would be a scalar coupled to ordinary matter, `g phi psi_bar psi` (or a specified gauge-invariant completion). This is *not* a proposal of a verified new particle. Such a coupling also induces additional forces and is therefore constrained by laboratory searches.

## 5. New analytic constraint: a fifth-force signature

Under a three-dimensional, isotropic-in-the-preferred-space extension, a matter-coupled scalar with this static dispersion gives a momentum-space potential proportional to

```text
G_static(k) = 1/(k^2 + ell^2 k^4 + mu^2).
```

For `4 ell^2 mu^2 < 1`, partial fractions imply a potential shape:

```text
G_static(r) = [exp(-a*r) - exp(-b*r)]/(4*pi*r*sqrt(1-4 ell^2 mu^2)),

a^2 = [1-sqrt(1-4 ell^2 mu^2)]/(2 ell^2),
b^2 = [1+sqrt(1-4 ell^2 mu^2)]/(2 ell^2).
```

At `ell=0.15`, `mu=0.2`, the two inverse-length poles are `a≈0.20009` and `b≈6.66366`, in model inverse-length units. Coupling `g` to real matter would scale the measurable potential with `g^2`; a fifth-force signature would need to be checked against experiments. **This expression is a derived signature of the *postulated* 3D extension, not evidence the scalar exists.** It provides an important adversarial filter: a field strongly enough coupled to be easily generated and detected may also have produced detectable nonstandard forces already.

## 6. UV dependence — the most serious model vulnerability

The original equation has `omega≈ell*k^2` for large `k`, so its group speed grows without bound. A fundamental theory needs to specify how the high-wavenumber behaviour continues or changes.

We tested an explicitly assumed *different* high-k interpolation:

```text
omega^2 = mu^2 + k^2 + [ell^2 k^4/(1+(k/K)^4)].
```

This interpolation is **not derived** from local microphysics and itself changes spatial locality properties; it is only a sensitivity test. The received early value changes substantially as the assumed scale `K` varies:

| K, model inverse-length | q(t=1) |
|---:|---:|
| Original unbounded quartic | -3.15898e-7 |
| 3 | -6.44299e-6 |
| 5 | +8.83230e-7 |
| 10 | +2.54457e-6 |
| 20 | -2.56508e-7 |
| 80 | -3.15787e-7 |

Some values even change the sign. **A numerically convergent result in one freely chosen high-frequency equation is not robust evidence for a physical superluminal information channel.** A high-k cutoff or interpolation may itself be nonlocal; the microscopic theory must determine both the front behavior and the allowed source bandwidth.

## 7. Causality: coordinate reversal versus actual paradox

Suppose in a preferred frame a hypothetical signal moves at `2c` over distance 2, arriving at `t=1`. A Lorentz-coordinate transformation to an observer moving at `0.75c` gives `delta_t'=-0.75593`, reversing its apparent time ordering. This is a kinematic coordinate calculation. If the new field is truly restricted to propagation toward **increasing preferred time**, a signal exchange cannot form a backward-preferred-time loop merely because another coordinate system assigns opposite event order.

But this is not a completed causal theory. We would need to show that all source/detector interactions honor one global preferred foliation, including moving receivers and curved spacetimes, and that the preferred frame does not conflict with established experiments. Published work on Hořava-type gravity examines similarly altered causal structures, so this topic has substantial prior art.

## 8. Evidence constraints and novelty

- **Photon sector:** LHAASO's 2024 gamma-ray-burst study places strong model-dependent bounds on quadratic energy-dependent photon propagation. These constraints are relevant if the proposed mode is identified with photons or mixes appreciably with photons; do not automatically transfer the same numerical bound to an unrelated hidden scalar.
- **Matter sector:** Nonstandard scalar couplings create new effective forces. The Eöt-Wash inverse-square-law programme and contemporary atom-interferometry proposals constrain or target such physics. Bounds depend on mass, coupling and screening details.
- **Lorentz/preferred-frame sector:** Precision experiments constrain symmetry breaking. A preferred frame must be a part of a viable theory, not merely assumed to prevent time-loop paradoxes.
- **Novelty:** This quartic-spatial-derivative free field is not a newly discovered concept. Our contribution so far is the explicit coupled numerical benchmark, mathematical energy test, potential-kernel derivation and adversarial audit; independent expert review is outstanding.

## 9. What would genuinely advance ANDROMEDA-5 next?

**Gate A — Real matter coupling.** Specify a gauge-compatible, dimensionally complete action that explains how an electrical or mechanical laboratory source excites `phi` and how an instrument detects it. Include unavoidable fifth-force and radiative effects.

**Gate B — UV and quantum stability.** Derive a high-energy completion (not an arbitrarily adjusted factor). Test ghost absence, interactions, loop corrections, high-frequency signal behavior and microcausality in its preferred frame.

**Gate C — Experimental limits.** Translate model length `ell`, mass-gap `mu`, and matter couplings into SI/particle-physics units and confront published fifth-force, Lorentz-violation and astrophysical observations without selectively omitting constraints.

**Gate D — Falsifiable prediction.** Only after A–C, specify a detector observable, predicted magnitude, controls and minimum sensitivity. A purely analog laboratory wave system would validate a numerical analogy, not superluminal propagation in vacuum.

**Gate E — Independent reproduction.** Have a different researcher or AI agent derive both the numerical evolution and energy accounting, with separate code and randomized source decoding that includes physically justified detector noise.

**Decision:** Continue mathematical study; **do not fund or claim a physical faster-than-light transmitter** on the current evidence. This is not a judgment about future discoveries; it reflects precisely which assumptions remain unverified.

## Reproducibility

```bash
python -m pip install -r requirements.txt
python phase5_coupled_field.py
python phase5_adversarial.py
```

The scripts save the coupled detector data, UV and time sensitivity, static kernel, causality example and PNG plots. Numpy is required; plotting additionally requires matplotlib and pandas. Numerical integrations were executed for this report. The early failed-convergence log is retained to document what was corrected.

## References to verify and extend

1. Herrero-Valea, *The Status of Hořava Gravity* (2023), https://arxiv.org/abs/2307.13039
2. Rinaldi, *Momentum-space representation of Green's functions with modified dispersion on ultrastatic space-time* (2007), https://doi.org/10.1103/PhysRevD.76.104027
3. LHAASO Collaboration, *Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A*, Phys. Rev. Lett. 133, 071501 (2024), https://doi.org/10.1103/PhysRevLett.133.071501
4. Eöt-Wash inverse-square-law experimental programme, https://www.npl.washington.edu/eotwash/inverse-square-law
5. Banks et al., *Searching for screened scalar forces with long-baseline atom interferometers*, Phys. Rev. D 113, 084047 (2026), https://doi.org/10.1103/3486-4m4t
6. *Superluminal propagation from IR physics*, Phys. Rev. D 107, 016011 (2023), https://doi.org/10.1103/PhysRevD.107.016011