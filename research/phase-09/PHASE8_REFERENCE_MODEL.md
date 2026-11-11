# ANDROMEDA-5 — Phase 8: Adversarial Physics Challenge

**Date:** 11 November 2026  
**Document status:** Unreviewed theoretical research memorandum; numerical calculations only.  
**Central conclusion:** No current evidence establishes faster-than-light (FTL) transport, a new scalar field or a new physical force. The next credible step is a **paired-observable consistency test** which forces our hypothetical model to make linked, potentially falsifiable predictions.

## 1. Research integrity: what cannot be claimed

Scientific progress does not follow from *declaring* all previous research disproved. A candidate alternative theory must quantitatively reproduce established observations or explain precisely where the data and their error analyses fail. In particular:

- The Eöt-Wash short-range torsion balance experiment tested 52 μm–3 mm separations and found no signal outside Newtonian gravity at its sensitivity. Its 38.6 μm 95% limit is for a *single* gravitational-strength Yukawa potential, not the ANDROMEDA-5 two-pole potential. An exact limit on our model cannot be inferred from this single headline number.
- MICROSCOPE measured differential free-fall of titanium and platinum alloys with no detected violation at ~10^-15 sensitivity. This does not universally exclude a very-short-range new force but rules out many unscreened long-range composition-dependent models.
- LHAASO's GRB 221009A observations constrain specified energy-dependent photon propagation models. These bounds do not directly exclude a separate postulated scalar, but its matter coupling would require its own precision constraints.
- Higher spatial derivative and superluminal group-velocity models are established *prior art*. No uniqueness claim is made for the quartic dispersion model.

Sources: Lee et al., PRL 124, 101101 (2020), DOI: 10.1103/PhysRevLett.124.101101; Touboul et al., PRL 129, 121102 (2022); LHAASO Collaboration, PRL 133, 071501 (2024); Rubio et al., arXiv:2307.13041; Phys. Rev. D 107, 016011 (2023).

## 2. Model and assumptions under renewed challenge

Postulate a scalar φ in a preferred reference frame with free dispersion

**ω² = c²(k² + ℓ²k⁴ + μ²)**.

A possible quadratic action is

**S₀ = ½ ∫dt d³x [(∂tφ)²/c² − |∇φ|² − ℓ²(∇²φ)² − μ²φ²]**.

A separate, unverified portal to electrons might be represented schematically by **gₑ φ ψ̄ₑ ψₑ**, with normalization and units fixed by an actual microscopic quantum field theory. This coupling is **assumed**, not experimentally observed. No ultraviolet (UV) completion is supplied.

For nonzero ℓ, μ with **4 ℓ² μ² < 1**, the static response has inverse lengths a and b:

**a² = [1 − √(1−4ℓ²μ²)]/(2ℓ²)**;
**b² = [1 + √(1−4ℓ²μ²)]/(2ℓ²)**.

Its dimensionless point-source kernel is proportional to

**[exp(−a r) − exp(−b r)]/[r √(1−4ℓ²μ²)]**.

*Important:* The mathematics of a static potential is not evidence of that potential in nature.

## 3. A paired-observable falsification test

A key consistency identity follows directly:

**ℓ = 1/√(a²+b²)**; **μ = ab/√(a²+b²)**.

Therefore, the two static-range parameters (if ever actually measured) uniquely determine the dispersion parameters for this model. There is **no independent, freely adjustable faster-than-light factor**.

The group velocity for positive k is

**v_g/c = (k + 2ℓ² k³)/√(μ²+k²+ℓ²k⁴)**.

Let **x = ℓk** and **e = ℓμ**. The threshold where the calculated group velocity first equals c is

**4x⁶ + 3x⁴ = e²**.

This conclusion is a mathematical testable *cross-prediction* within the candidate theory. It is not established that these group velocities can transmit a time-encoded bit; front, group, phase and information velocities must be distinguished.

## 4. Numerical benchmark — expressly hypothetical

Using the same illustrative parameters from Phase 6–7 (**ℓ = 0.2 mm, μ = 1000 m^-1**):

| Quantity | Numerically calculated result |
|---|---:|
| Static long characteristic length 1/a | 0.978906 mm |
| Static short characteristic length 1/b | 0.204310 mm |
| First crossing v_g=c, x=ℓk | 0.328574 |
| Frequency at crossing | 95.3124 GHz |
| Group speed at ℓk=0.1 | 0.455702 c |
| Group speed at ℓk=0.5 | 1.263228 c |
| Group speed at ℓk=1 | 2.100420 c |
| Group speed at ℓk=2 | 4.020903 c |
| Independent static Fourier-integral check | maximum relative error 2.02×10^-13 (5 points) |

The speed at ℓk=1 is a **model group velocity**, **not** an observed signal speed. Its associated oscillation frequency is ~340.742 GHz. The model would need a valid theory in this frequency regime, an identified source, a detector, finite-bandwidth signaling tests, and a demonstrated matter coupling before a physical claim becomes possible.

The formula for a hypothetical group-delay difference over distance L (narrowband idealization) is **Δt = L(1/c − 1/v_g)**; for ℓk=1 it gives ~1.748 ns/m. This is *only* a conditional kinematic number and cannot be described as a measured early information arrival or a proposed laboratory sensitivity.

![Linked static-force shape and group velocity predictions](paired_observable_predictions.png)

## 5. Third predicted signature: composition dependence

For a truly electron-coupled scalar with neutral macroscopic test bodies, a simplified point-body charge per unit mass scales as Z/A (proton number over atomic mass number). Consequently, at fixed equal test-body masses and separations, the *hypothetical fractional fifth-force amplitude* changes by the product of these ratios. Relative to an idealized gold–gold point-body configuration:

| Pair | Predicted coupling ratio |
|---|---:|
| Gold–gold | 1.000 |
| Gold–SiO₂ | 1.245 |
| SiO₂–SiO₂ | 1.550 |

These are point-body composition factors only; actual apparatus bodies have different density and geometry and must be integrated. Other new-force interactions could have different composition dependence; therefore, this is a potential discriminator, not a unique proof of our theory.

## 6. Strongest adversarial objections — unresolved

1. **Physical origin missing:** The quartic term and preferred frame are postulates. No independently derived, experimentally motivated microscopic dynamics are supplied.
2. **Signal versus group velocity:** A group velocity above c does not itself prove faster-than-light information transmission. Sources and detectors must send new messages in a controlled setup, including switch-on fronts and all instrumental delays.
3. **Unbounded group speed:** As k→∞, the postulated model's v_g grows without bound. But the prediction at arbitrarily high k may be physically meaningless if the equation is only an effective low-energy model. An ultraviolet completion or cutoff must be specified.
4. **Bandwidth and localization:** Bandlimited wave packets possess noncompact tails; an apparently early threshold crossing can reflect an already-existing precursor. No real-world measured earliest-information time has been established.
5. **Static interaction constraint:** If the same field couples to ordinary electrons, a fifth-force signal is expected. Null experimental results already constrain many choices of coupling; exact exclusion needs the experiment's real geometry and likelihood, not an illustrative point-body calculation.
6. **Radiative effects:** A Lorentz-violating hidden scalar interacting with electrons may generate tightly constrained corrections to electron/photon propagation. No loop calculation, renormalization scheme or naturalness analysis is available.
7. **Causality:** A preferred frame can organize chronology in some models but does not itself demonstrate consistency under interactions, moving emitters and realistic boundary conditions.
8. **Model identifiability:** Two-pole force profiles can be challenging to distinguish from competing force laws at finite noise and limited separations. An adversarial model comparison with nuisance parameters must precede any detection claim.

## 7. New project position, stated precisely

**ANDROMEDA-5 Cross-Observable Hypothesis:** *If a physically realized scalar with preferred-frame quartic dispersion interacts measurably with electrons, then its measured two-range static-force profile and the frequency-dependent propagation of deliberately encoded field disturbances must obey the common parameter identities in Section 3. Failure to match falsifies this specific simple model, subject to measured uncertainties and apparatus effects.*

This is an explicit hypothesis designed to be falsified, not a claim that the field exists, that existing science has been disproved, or that the linked-prediction concept is globally novel. A substantive novelty determination needs specialist prior-art review.

## 8. Phase 9 — proposed empirical gate

**Gate A: published data and valid exclusions.** Seek Eöt-Wash torque-level data, full detector/attractor geometry, calibration uncertainties and covariance; reconstruct the actual harmonic torque response for the two-pole model; profile over nuisance parameters to obtain a model-specific confidence region for (a,b,α). If adequate data are not public, request collaboration rather than inventing results.

**Gate B: second observable before FTL claims.** Derive a dimensionally and renormalization-consistent electron-field interaction. Determine whether any coupling that survives Gate A could produce a calibrated field emission and a measured detector response. Evaluate laboratory backgrounds and existing atomic precision bounds.

**Gate C: pre-registered signaling.** Design blinded, time-encoded source–detector trials with source-off controls, light-front controls, synchronized clocks and independently recorded timestamps. Specify a finite spectrum and derive source/detector response; require independent replication and access to raw instrument logs.

**Stop conditions:** No physical coupling, contradiction with validated data, energy instability, or an unresolvable causality contradiction means withdraw or reformulate the model. Negative results are to be publicly preserved.

## 9. Reproducibility and limitations

Run `python phase8_cross_observable.py` with NumPy, SciPy and Matplotlib. The script creates a JSON summary, five CSV datasets, and a paired-prediction plot. It performs a separate numerical Fourier integral rather than only reusing the analytic two-pole decomposition. Inputs are **illustrative**. No measured laboratory data were processed. No statistical bound on the new field's parameters is claimed.

## 10. Verified references / further reading

- Lee, J. G., et al. (2020), *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, PRL 124, 101101. https://doi.org/10.1103/PhysRevLett.124.101101
- Touboul, P., et al. (2022), *MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle*, PRL 129, 121102. https://doi.org/10.1103/PhysRevLett.129.121102
- LHAASO Collaboration (2024), *Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A*, PRL 133, 071501. https://doi.org/10.1103/PhysRevLett.133.071501
- Dzuba, V. A., Flambaum, V. V., Mansour, A. J. (2024), *Constraints on the variation of physical constants, equivalence principle violation, and a fifth force from atomic experiments*, PRD 110, 055022. https://doi.org/10.1103/PhysRevD.110.055022
- *Superluminal propagation from IR physics*, PRD 107, 016011 (2023). https://doi.org/10.1103/PhysRevD.107.016011
- Rubio, M. E., et al. (2023), *Well-posed evolution of field theories with anisotropic scaling: the Lifshitz scalar field in a black hole space-time*, arXiv:2307.13041. https://arxiv.org/abs/2307.13041
- Amaral, D., et al. (2026), *Searching for screened scalar forces with long-baseline atom interferometers*, PRD 113, 084047. https://doi.org/10.1103/3486-4m4t

**Reproducibility status:** Internally calculated and source-linked, not independently peer-reviewed. This report should be shared as a research invitation, **not** as evidence of actual faster-than-light transmission.