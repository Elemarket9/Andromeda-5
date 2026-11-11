# ANDROMEDA-5 — Phase 4 independent source–receiver investigation

**Research status:** Numerical mathematics only — not laboratory evidence or a discovered physical faster-than-light channel.  
**Project objective at this stage:** Determine whether the *submitted Phase 3 quartic-dispersion equation*, when equipped with a controllable localized source, produces an early **distinguishable receiver response**, rather than just a fast-moving wave-packet peak.

## Origin and provenance

This phase continues `phase3_sims.py`, provided by the user. Simulation 3 in that file defines

\[\omega^2=k^2+\ell^2 k^4,\quad c=1.\]

Phase 4 extends it by adding an explicit source to the one-dimensional real scalar field:

\[\partial_t^2\phi-\partial_x^2\phi+\ell^2\partial_x^4\phi=J(x,t).\]

One possible quadratic toy action in a **preferred frame** is

\[S=\int dt\,dx\left[\tfrac12 (\partial_t\phi)^2-\tfrac12(\partial_x\phi)^2-\tfrac12\ell^2(\partial_x^2\phi)^2+J\phi\right].\]

This expression is a *postulated model*, not a derived microscopic theory of nature. Its exact higher-spatial-derivative structure is closely related to existing Lifshitz-type scalar-field research (see literature).

## Controlled source and detector

- Space periodic computational box length **80** (checked again at lengths 40, 160, 320).
- Source centered at **x = 0**, strictly supported in \(|x|<0.35\) using a smooth compact bump.
- On for \(0<t<0.35\), with raised-cosine temporal envelope \(s(t)=\sin^2(\pi t/0.35)\); off otherwise.
- Receiver is at **x = 2**.
- For ordinary waves with speed \(c=1\), the earliest arrival is \(t=(2-0.35)/1=1.65\).
- Encoded bit 1: source pulse active. Encoded bit 0: source absent. Difference between the resulting receiver fields is the signal.
- Exact spectral evolution is used for each spatial Fourier mode, with an independently checked analytic integral over the temporal pulse; no finite-time-step PDE integration is required.

For \(t\geq0.35\), the retarded response of a mode is

\[\phi_k(t)=\frac{J_k}{\omega_k}\int_0^{0.35}\!ds\,\sin[\omega_k(t-s)]\sin^2(\pi s/0.35),\quad \omega_k=|k|\sqrt{1+\ell^2 k^2}.\]

The \(k=0\) limit is evaluated separately.

## Results: independent model computation

At \(t=1\), *before* the standard wave would arrive at \(t=1.65\):

| Model | Calculated receiver response |
|---|---:|
| \(\ell=0\) (ordinary-wave control) | \(6.94\times10^{-18}\) |
| \(\ell=0.05\) | \(+4.07952699\times 10^{-5}\) |
| \(\ell=0.15\) | \(+1.98395408\times10^{-3}\) |
| \(\ell=0.30\) | \(-5.33433985\times10^{-3}\) |

The \(\ell=0.15\) value changes by less than \(10^{-9}\) across the tested spatial grid resolutions \(N=8,192\) to \(65,536\), and across periodic-box lengths 40–320 at fixed grid spacing. The ordinary-wave control approaches numerical zero. This substantially reduces concerns about spatial discretization and wraparound producing the effect.

The quadratic free-field energy after the source turns off is

\[E=\tfrac12\int dx\left[(\partial_t\phi)^2+(\partial_x\phi)^2+\ell^2(\partial_x^2\phi)^2\right]\geq0.\]

It is conserved in the free evolution because the action is invariant under translations in preferred-frame time. Energy *during* source activation comes from the external source: \(dE/dt=\int J\partial_t\phi\,dx\). In the tested mode-evolution code, post-pulse energy is constant to floating-point precision. This checks internal consistency; it does **not** prove that a physical source can excite such a field.

## Synthetic one-bit challenge

A simulated Gaussian receiver-noise amplitude of **0.0005** was chosen arbitrarily and fixed in code, with 1,000 seeded source bits.

| Assumed field | Correctly decoded | Accuracy |
|---|---:|---:|
| Ordinary-wave control (\(\ell=0\)) | 496 / 1,000 | 49.6% |
| Quartic field (\(\ell=0.15\)) | 972 / 1,000 | 97.2% |

The result shows that *if this toy field, source coupling and noise model existed*, a receiver could distinguish a source choice before the ordinary-light arrival. It is **not** an empirical communication result: even the noise level is an assumption, and field amplitude has no established conversion to physically measurable units.

## Strongest physical obstacles

**1. No known field / source / detector:** The action stipulates a scalar excitation and a source \(J\), but does not identify a real substance or experimental interaction capable of launching or detecting it. The simulation cannot establish existence.

**2. Incomplete ultraviolet theory:** The group velocity

\[v_g=\frac{1+2\ell^2 k^2}{\sqrt{1+\ell^2 k^2}}\]

is unbounded as \(k\to\infty\). This signals a nonstandard causal structure and demands a high-frequency completion and carefully specified preferred temporal ordering. Truncating modes or smearing sources introduces bandwidth/localization tradeoffs; the present effective model is not a complete high-energy theory.

**3. Existing prior art:** Preferred foliations and higher-spatial-derivative dispersion have already been developed in Hořava–Lifshitz and related field theories. Finding early model responses is therefore **not** the discovery of an original physical principle.

**4. Astronomical bounds if this applies to light:** LHAASO's 2024 analysis places model-dependent constraints on quadratic energy-dependent photon speed, e.g. \(E_{\rm QG,2}>6\times10^{-8} E_{\rm Pl}\). Under the *specific identification* \(\ell=\hbar c/E_{\rm QG,2}\), this is approximately \(\ell<2.7\times10^{-28}\,\mathrm m\). At 500 nm wavelength, a small-\(k\ell\) estimate gives \((v_g-c)/c\lesssim1.7\times10^{-41}\). This conversion is only applicable if the field represents photons and the same dispersion law applies; it does **not** directly constrain an entirely separate hypothetical hidden field.

**5. Causality and frames:** A preferred frame can impose a time ordering in such a toy theory, but selecting a preferred frame is not an experimentally established feature of nature. The consequences for moving observers, interactions, and loops need explicit analysis.

**6. Scaling:** The simulated \(\ell=0.15\) is 7.5% of source-to-receiver centre distance (2 model units). It is a deliberately large illustrative modification, not evidence of a macroscopic physical length scale.

## Next adversarial gate: Phase 5

Before spending money on hardware, request from other research agents:

1. **Derive** a UV-consistent field with a physical coupling \(J\) to known matter and quantify emitted power and detector cross-section; state if impossible.
2. **Independent numerical implementation** using a second mathematical method (e.g. finite differences with converged CFL limits), and explicit UV cutoff / source bandwidth sensitivity.
3. **Preferred-frame causal consistency** for two transmitters in relative motion, including whether closed signalling loops are permitted.
4. **Existing constraints** on the proposed field from astrophysics, gravity, laboratory detectors, fifth-force searches, Cherenkov radiation and Lorentz-violation measurements, without importing photon limits unless coupling assumptions warrant it.
5. **Unique new physical prediction** that separates the proposal from established Lifshitz-type field theories and has a realistic measurement route.

The current answer is a confirmed **mathematical early-response result conditioned on a postulated equation**, not a confirmed faster-than-light physical phenomenon. The appropriate next stage is foundational theory and experimental coupling, not spacecraft design.

## Literature and source trail

- Submitted user source: `phase3_sims.py`, Simulation 3 (quartic dispersion).
- Suyama, *Notes on Matter in Horava-Lifshitz Gravity* (2009), arXiv:0909.4833: https://arxiv.org/abs/0909.4833
- Carballo-Rubio et al., *Causal hierarchy in modified gravity* (2020): https://link.springer.com/article/10.1007/JHEP12%282020%29055
- LHAASO Collaboration, *Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A* (2024): https://doi.org/10.1103/PhysRevLett.133.071501
- Herrero-Valea, *The Status of Horava Gravity* (2023): https://arxiv.org/abs/2307.13039

## Reproduction

```sh
python -m pip install -r requirements.txt
python phase4_source_receiver.py
```

Outputs include the grid/periodic-box convergence CSVs, energy checks, receiver traces, the synthetic-bit results, the source code and a PNG plot. Requires NumPy; Matplotlib is optional for the plot. Random generation uses the fixed seed **20261111**.