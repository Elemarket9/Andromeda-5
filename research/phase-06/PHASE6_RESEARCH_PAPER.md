# ANDROMEDA-5 — Phase 6 Working Paper

**Matter-coupled preferred-frame scalar with quartic dispersion: a falsifiable static-force benchmark**  
**Date:** 11 November 2026  
**Status:** Publicly shareable theoretical/computational working paper. **Not peer reviewed. No experimental evidence of a new particle or faster-than-light communication.**

## Abstract

ANDROMEDA-5 Phase 5 used a postulated real scalar field obeying a higher-spatial-derivative dispersion law to calculate early responses in a mathematical oscillator detector. Phase 6 investigates a plausible matter portal and derives a correlated static-force signature. We consider a scalar singlet coupled to electrons, with a preferred-frame free-field dispersion omega^2 = c^2[k^2 + ell^2 k^4 + mu^2]. The static three-dimensional propagator admits an analytic two-pole decomposition for 4 ell^2 mu^2 < 1. We numerically verify the resulting Green function by independent oscillatory Fourier integration, finding maximum relative discrepancy 1.38e-12 over the stated benchmark distances. In synthetic null and injected-amplitude datasets, a one-parameter fit recovers the stipulated signal amplitude at the expected precision; these datasets are algorithmically generated and are **not observed measurements**. A real scalar–matter coupling would generally imply new forces and is constrained by published inverse-square-law, equivalence-principle, and atomic-spectroscopy measurements. Our example does not demonstrate an existing field, physical faster-than-light signaling, or a novel fundamental law. The next scientific gate is an experimentally admissible, fully normalized source–field–detector model and an independently replicated measurement.

## 1. Scope and relationship to Phase 5

**What is established by the script:** a chosen quadratic mathematical field has stable free modes for nonnegative ell^2 and mu^2; its 3D static Green function can be derived analytically and independently checked numerically; an idealized coupling to electron number would produce a specific force-distance template.

**What is *not* established:** the existence of the scalar field; a physical source that excites it; a matter detector with a real voltage/noise calibration; the energy scale of the preferred-frame physics; a quantum-consistent ultraviolet completion; or any superluminal experiment.

Phase 5's early receiver result depends on the assumed quartic high-frequency dispersion and its UV continuation. Phase 6's purpose is to expose an independently testable consequence of coupling that hypothetical field to ordinary matter. A static fifth-force test alone **would not verify superluminal information transfer**, even if it discovered an unexplained signal.

## 2. Candidate action and matter portal

In a designated preferred inertial frame and natural units (hbar=c=1), consider the *postulated* free action

    S_phi = (1/2) integral dt d^3x [ (partial_t phi)^2
                 - (grad phi)^2 - ell^2 (nabla^2 phi)^2 - mu^2 phi^2 ].

The Euler–Lagrange field equation in the presence of a source J is

    partial_t^2 phi - nabla^2 phi + ell^2 nabla^4 phi + mu^2 phi = J.

A Fourier wave has

    omega^2(k) = k^2 + ell^2 k^4 + mu^2.

The group velocity is

    v_g = d omega/dk = (k + 2 ell^2 k^3)/sqrt(k^2 + ell^2 k^4 + mu^2)

in c=1 units. This mathematical group velocity becomes unbounded as k grows. The extrapolation to arbitrarily large k is **not justified**, and this equation is not evidence of a real new field or information channel.

For an electron Dirac field e, one *candidate* low-energy interaction is

    L_int = -g_e phi (e_bar e).

Here g_e is dimensionless in 3+1 natural units. A real electroweak-gauge-invariant effective operator before symmetry breaking could be written as

    L_portal = -(c_e/Lambda) phi (L_bar H e_R) + h.c.,

with singlet phi, lepton doublet L, Higgs doublet H and a high-energy scale Lambda. In the broken phase the effective electron coupling is g_e=c_e v/(sqrt(2) Lambda). This is **a permitted illustrative portal, not a derived physical mechanism or proof of UV consistency**. Additional induced operators and Lorentz-violating effects must be studied.

## 3. Analytic static Green function

The static momentum-space response to a point source is

    G_tilde(k) = 1 / (k^2 + ell^2 k^4 + mu^2).

For D = 1 - 4 ell^2 mu^2 > 0, define

    a^2 = [1-sqrt(D)]/(2 ell^2),
    b^2 = [1+sqrt(D)]/(2 ell^2),

so that a^2+b^2=1/ell^2 and a^2 b^2=mu^2/ell^2. Then

    G_tilde(k) = [1/sqrt(D)] [1/(k^2+a^2) - 1/(k^2+b^2)].

Using the standard 3D radial Fourier transform gives

    G(r) = [exp(-a r) - exp(-b r)] / [4 pi r sqrt(D)].

For two idealized point bodies of masses M_A,M_B and electron counts N_A,N_B, the static scalar interaction would be

    V_5(r) = -g_e^2 hbar c N_A N_B G(r).

Define a dimensionless reference strength, relative to Newtonian gravity,

    alpha_5 = [g_e^2 hbar c/(4 pi G_N)] [(N_A/M_A)(N_B/M_B)].

Thus for the same bodies

    V_total(r) = -G_N M_A M_B/r * [1 + alpha_5 K(r)],
    K(r) = [exp(-a r) - exp(-b r)]/sqrt(D).

The ratio of the additional attractive force to alpha_5 times the Newtonian force is

    F_5/(alpha_5 F_N)
      = [(1+a r)exp(-a r) - (1+b r)exp(-b r)]/sqrt(D).

The ell -> 0 limit at fixed nonzero r reduces to the ordinary Yukawa result (1+mu r)exp(-mu r). For actual laboratory objects one must integrate the Green function over their **finite three-dimensional electron-density distributions**; point-body numbers at sub-millimetre separation are not literal laboratory force predictions.

The analytic decomposition does not require new physics to exist. It is simply a mathematical consequence of the postulated propagator. For 4 ell^2 mu^2 >= 1, the real-pole formula above must be replaced with its complex-pole/oscillatory continuation.

## 4. Reproducible numerical validation

The script phase6_matter_field.py independently computes the dimensionless radial transform:

    4 pi r G(r) = (2/pi) integral_0^infinity
                 [k sin(k r)/(k^2+ell^2 k^4+mu^2)] dk.

The integral is evaluated with an oscillatory quadrature algorithm rather than reusing the partial-fraction decomposition. The tested benchmark uses **illustrative, not observed** parameters:

| Input or derived quantity | Value |
|---|---:|
| ell | 0.0002 m (0.2 mm) |
| mu | 1,000 m^-1 |
| sqrt(1-4 ell^2 mu^2) | 0.91651514 |
| a | 1,021.5482 m^-1 |
| b | 4,894.5316 m^-1 |
| Corresponding hbar*c*mu | 1.973e-4 eV |
| Maximum analytic-vs-quadrature relative discrepancy (21 separations) | 1.375e-12 |

The numerical agreement is evidence that **the static Green-function calculation is correct within the defined model**. It is not evidence that the model describes nature.

For roughly neutral matter with electron number per mass approximated by (Z/A)/atomic mass unit, using Z/A=0.5 for **both** idealized bodies, alpha_5=1 corresponds to g_e≈5.409e-19. This is a normalization calculation, **not a measured or permitted value**. The actual g_e bounds require the correct source composition, body geometry, mass range and published experimental likelihoods.

![The force-distance signature predicted by the postulated two-pole scalar kernel.](fifth_force_shape.png)

## 5. Synthetic null and signal-injection audit

To test whether the model's *shape* could be recovered from a noisy benchmark, we generated two **synthetic** 32-point datasets at separations 0.10 to 2.0 mm. The assumed standard deviation for each dimensionless fractional residual was 0.010. One dataset has zero injected new-force amplitude; the other contains an arbitrarily selected alpha_5 = 0.040. Random seed: 20261111.

The fitted amplitude for a template h_i = F_5(r_i)/(alpha_5 F_N(r_i)) is

    alpha_hat = sum_i[h_i y_i]/sum_i[h_i^2],
    sigma_alpha = sigma/sqrt(sum_i[h_i^2]).

| Synthetic benchmark | Fitted alpha_5 | Formal one-sigma toy uncertainty |
|---|---:|---:|
| Null injection (true alpha=0) | +0.001727 | 0.003317 |
| Injected alpha=0.040 | +0.045278 | 0.003317 |

For the synthetic injected set, the fitted quartic potential produces chi-square 27.447; at the same fixed mu, a standard-Yukawa shape produces chi-square 78.644. The 51.197 difference **only describes how distinguishable those assumed templates can be in synthetic data with assigned errors**. It is not a likelihood ratio from real measurements and does not prove discovery.

![Synthetic-data benchmark, not a laboratory measurement.](synthetic_force_test.png)

## 6. Published empirical constraints and novelty

**Short-distance gravity:** Lee et al., Physical Review Letters 124, 101101 (2020), report torsion-balance tests at detector-attractor separations from 52 micrometres to 3.0 millimetres and no detected Yukawa deviation. For a gravitational-strength *ordinary Yukawa* force their analysis limits the characteristic range to below 38.6 micrometres at 95% confidence. Our two-pole kernel is **not identical** to their one-Yukawa fit, so their 38.6 micrometre cutoff must **not** be copied as a derived exclusion boundary for this model. It is a strong reason to request raw likelihoods or reproduce their apparatus geometry.

**Equivalence principle:** MICROSCOPE's final result constrains composition-dependent differential accelerations at the ~10^-15 level for its titanium/platinum comparison. Whether an electron-number coupling is constrained by a particular test depends on range and composition; no blanket g_e limit is claimed here.

**Atomic spectroscopy:** Dzuba, Flambaum and Mansour (Phys. Rev. D 110, 055022, 2024) analyze electron, nucleon and photon scalar couplings from measured atomic transitions, providing directly relevant parameter-space constraints for a real scalar portal.

**Photon propagation:** LHAASO Collaboration (Phys. Rev. Lett. 133, 071501, 2024) reports strong bounds on specific energy-dependent *photon* speed modifications. Those bounds do not automatically constrain an independent hidden scalar. However, matter couplings could radiatively communicate preferred-frame physics to known particles; a complete calculation is still required.

**Prior art:** Higher-spatial-derivative propagation and nonstandard static exchange kernels are not invented by this project. Related 2026 work includes Araújo Filho et al., 'Higher derivative Hořava-Lifshitz fermions: from superconductivity to atomic spectroscopy' (arXiv:2609.25236). A genuine novelty claim must precisely identify an observable or coupling structure not already published.

## 7. Experimental proposal — no laboratory claims

The most direct first *real* target is an additional static force or composition-dependent shift, not a superluminal message.

1. **Pre-register an observable:** select a separation-dependent differential force, frequency shift or acceleration comparing at least two compositions with different electron-number-to-mass ratios.
2. **Predict the complete apparatus response:** integrate the proposed Green function over measured finite body shapes and material electron densities; account for mechanical transfer functions and sensor calibration.
3. **Measure null backgrounds:** electrostatic patch potentials, magnetic leakage, thermal drift, Casimir/van der Waals forces, vibrations, cross-talk and alignment errors.
4. **Use blinded signal injection:** insert *synthetic electronic calibration* signals unknown to analysts, alongside genuine no-injection datasets. A software-injected signal is never called a physical discovery.
5. **Compare to published bounds:** either use experimental collaborations' likelihoods or openly release an independently validated reproduction of their geometric response.
6. **Independent replication:** require an external group and ideally a different apparatus before making a new-field claim.

No physical apparatus has been constructed or tested in this phase. The numerical noise sigma=0.010 and example ell and mu are **not instrument specifications or justified sensitivity claims**. Any practical design needs measured backgrounds and demonstrated calibration first.

## 8. Phase 6 adversarial verdict

| Claim | Current verdict |
|---|---|
| A quartic-dispersion scalar can be written with a positive free Hamiltonian | Mathematically consistent toy model |
| Such a scalar can be coupled to electrons by a candidate low-energy operator | Formally possible, but not UV-validated |
| The coupled scalar predicts a distinctive two-pole static-force kernel | Derived mathematically |
| The force kernel survives an independent Fourier-integration check | Numerically validated to ~1.4e-12 relative error |
| The chosen electron coupling is allowed by actual experiments | **Not established; likely constrained** |
| This project has experimentally found a scalar particle | **No** |
| Phase 6 demonstrates faster-than-light signaling | **No** |

**Research gate:** Do not publish a claim of faster-than-light travel, communication or a novel discovered particle from these results. Do publish the equations, assumptions, computation, negative findings and invitation to reproduce or falsify the candidate.

## 9. Phase 7 research questions

1. Can we derive the preferred spatial fourth-derivative operator from a consistent microscopic (or explicitly effective) action, with its domain of validity and cutoff?
2. Can radiative corrections to ordinary electrons/photons remain within measured Lorentz-symmetry bounds for a source–detector coupling large enough to be detected?
3. Can we derive and numerically validate the force for finite shapes matching a published torsion-balance geometry, then translate that instrument's data into an exclusion curve in (ell,mu,g_e)?
4. If static-force constraints leave any open parameter region, could a realistically band-limited source/detector demonstrate a signal at a speed exceeding an ordinary electromagnetic control? Without a measured source and detector response, the answer is unknown.

## Reproduction

```bash
python -m pip install numpy scipy matplotlib
python phase6_matter_field.py
```

The code writes static_green_validation.csv, group_velocity_hypothesis.csv, coupling_normalization.csv, synthetic_injection_benchmark.csv, validation_summary.json, fifth_force_shape.png and synthetic_force_test.png. The random-number generator seed and all postulated parameters are hard-coded only in this **reproducible research benchmark**, not in a proposed spacecraft design. Change them for sensitivity analyses.

## References (primary/technical sources)

1. Lee, J. G., et al. (2020). New Test of the Gravitational 1/r^2 Law at Separations down to 52 um. *Physical Review Letters* 124, 101101. https://doi.org/10.1103/PhysRevLett.124.101101
2. Touboul, P., et al. (2022). MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle. *Physical Review Letters* 129, 121102. https://doi.org/10.1103/PhysRevLett.129.121102
3. Dzuba, V. A., Flambaum, V. V., and Mansour, A. J. (2024). Constraints on the variation of physical constants, equivalence principle violation, and a fifth force from atomic experiments. *Physical Review D* 110, 055022. https://doi.org/10.1103/PhysRevD.110.055022
4. LHAASO Collaboration (2024). Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A. *Physical Review Letters* 133, 071501. https://doi.org/10.1103/PhysRevLett.133.071501
5. Araújo Filho, A. A., et al. (2026). Higher derivative Hořava-Lifshitz fermions: from superconductivity to atomic spectroscopy. https://arxiv.org/abs/2609.25236

**Document authorship/status:** ANDROMEDA-5 research working draft compiled with computational assistance. The analysis is not externally peer-reviewed. Anyone sharing this work should preserve the status and simulation-only disclaimers. No person's credentials or independent laboratory affiliations are asserted.