# ANDROMEDA-5 — Phase 11: Independent Adversarial Recast & Misspecification Tests

**Date:** 12 November 2026  
**Classification:** Unreviewed theoretical inference and independent numerical tests. No measured fifth force, superluminal signal, or novel physical effect.  
**Key decision:** The \(\alpha=1\) universal-mass-coupled benchmark is *strongly challenged by published measurements* and should not be treated as a plausible experimental value. We produce a conditional, quantitatively justified constraint instead of claiming an exact experimental exclusion.

## 1. Inputs and provenance

We reviewed the existing [Phase 10 source report](../phase-10/PHASE10_RESEARCH_REPORT.md) and used these original, published sources:

1. J. G. Lee *et al.*, *New Test of the Gravitational 1/r² Law at Separations down to 52 μm*, **Phys. Rev. Lett. 124**, 101101 (2020), DOI: <https://doi.org/10.1103/PhysRevLett.124.101101>. Reports Newtonian \(\chi^2\approx275\) for 285 DOF, measures 52 μm–3 mm, and gives limits for *single* Yukawa terms.
2. John G. Lee, *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*, University of Washington PhD dissertation (2020), particularly **Chapter 11 §11.4, Table 11.4** (single-Yukawa \(\hat\alpha\pm\sigma\) and positive/negative limits). Original: <https://digital.lib.washington.edu/researchworks/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download>.
3. Lee *et al.* (2021), *The Fourier–Bessel expansion: application to experimental probes of gravity and feeble short-range interactions*, DOI: <https://doi.org/10.1088/1361-6382/abebf2>. Relevant to geometry-specific torque modeling.
4. Gavassino, *Dispersion Relations Alone Cannot Guarantee Causality*, **Phys. Rev. Lett. 132**, 162301 (2024), DOI: <https://doi.org/10.1103/PhysRevLett.132.162301>. Important warning against equating a dispersion curve with an information channel.

**Third-party data reused:** only a handful of published Table 11.4 numerical values are transcribed. No private lab data, credentials or correspondence. **All force and toy numerical outputs below are derived by us, not measurements.**

## 2. Exact model algebra and point-mass no-cancellation theorem

Use Phase 10's hypothesized phenomenological universal-mass potential:

\[
U(r)=-\frac{Gm_1m_2}{r}\left[1+\frac{\alpha}{s}(e^{-ar}-e^{-br})\right],\quad
s=\sqrt{1-4\ell^2\mu^2},\quad a^2=\frac{1-s}{2\ell^2},\quad b^2=\frac{1+s}{2\ell^2}.
\]

Assumed—not fitted—parameters \(\ell=0.2\,\mathrm{mm}\) and \(\mu=1000\,\mathrm{m^{-1}}\) give \(s=0.916515138991\), \(1/a=0.9789063\,\mathrm{mm}\) and \(1/b=0.2043096\,\mathrm{mm}\).

For point masses,

\[
\frac{\Delta F}{F_N}=\frac{\alpha}{s}\big[(1+ar)e^{-ar}-(1+br)e^{-br}\big].
\]

**Proof:** \(f(x)=(1+x)e^{-x}\) has \(f'(x)=-xe^{-x}<0\) for \(x>0\). Since \(0<a<b\), the bracket is strictly positive at \(r>0\). Thus there is *no exact point-mass force cancellation* for \(\alpha>0\), and the correction is attractive at all separations. At \(r\to0\), \(\Delta F/F_N=\alpha r^2/(2\ell^2)+O(r^3)\), so the *new* force is finite at the origin, unlike Newtonian gravity.

With \(\alpha=1\), the correction is 2.8393% at 52 μm, 74.5975% at 1 mm; maximum is 76.8873% near 0.80909 mm. **These are point-mass forces, not torque predictions of the Eöt-Wash apparatus.** Such large effects make order-one coupling implausible but do not by themselves yield a formal confidence interval.

## 3. New conditional recast from the experiment's published Table 11.4

The published single-Yukawa fits include the following entries (strength \(\hat\beta\), published standard error \(\sigma_\beta\)):

| Published range (mm) | Best-fit single-Yukawa strength | Published 1σ |
|---:|---:|---:|
| 0.200 | −0.00235 | 0.01570 |
| 0.220 | −0.00351 | 0.01470 |
| 0.890 | −0.00612 | 0.00845 |
| 1.000 | −0.00569 | 0.00796 |

Straight-line interpolation **only between the adjacent published grid points** at our two ranges gives:

- long pole 0.978906 mm: \(\hat\beta_a=-0.00577246\), \(\sigma_a=0.00805396\);
- short pole 0.204310 mm: \(\hat\beta_b=-0.00259996\), \(\sigma_b=0.01548452\).

The combined response is exactly linear in Yukawa *forward responses*:

\[
\mathbf T_\mathrm{2pole}(\alpha)=\frac{\alpha}{s}\,[\mathbf T_Y(1/a)-\mathbf T_Y(1/b)].
\]

**Additional conditions, not established:** Approximate *the original experiment's joint likelihood* as one shared linear-Gaussian model with a fixed covariance and one common linear nuisance subspace. After whitening and projecting out the nuisance subspace, let \(u_a,u_b\) be the two unit-strength Yukawa templates. Then a single-template regression implies \(\|u_i\|=1/\sigma_i\) and \(r\cdot u_i=\hat\beta_i/\sigma_i^2\), for the *same* whitened residual \(r\). This fails if the source fit's nonlinear nuisance changes or model-dependent uncertainties cause different effective projected spaces. Treat this as a local Fisher/likelihood approximation, not as a faithful reconstruction of the instrument.

Set \(A=1/\sigma_a=124.1625\), \(B=1/\sigma_b=64.5806\), and \(D=\hat\beta_a/\sigma_a^2-\hat\beta_b/\sigma_b^2=-78.1465\). The unknown template correlation \(\rho\in[-1,1]\) yields

\[
Q=\|u_a-u_b\|^2=A^2+B^2-2\rho AB \in [(A-B)^2,(A+B)^2].
\]

For the two-pole coefficient \(\alpha\), this hypothetical likelihood gives

\[
\widehat\alpha(Q)=sD/Q,\qquad \sigma_\alpha(Q)=s/\sqrt Q.
\]

Applying the dissertation's stated \(\Delta\chi^2=6.17\) threshold as a **conservative comparison criterion** and maximizing \(\widehat\alpha(Q)+\sqrt{6.17}\,\sigma_\alpha(Q)\) over *every possible correlation* \(\rho\) gives

\[
\boxed{\alpha_{+}^{\mathrm{envelope}}\simeq0.01809\quad \text{(conditional linear-Gaussian approximation)}}.
\]

Corresponding maximum formal uncertainty: \(\sigma_\alpha\le0.01538\). The *minimum* increase in the hypothesized \(\chi^2\) for \(\alpha=1\) versus \(\alpha=0\) is about **4397** under these assumptions. This shows that order-one coupling is not rescued by simply choosing an unknown cross-pole correlation **within the approximated common linear likelihood**.

**IMPORTANT:** This is NOT an instrument-validated 95% exclusion. The original laboratory's Yukawa fits use nonlinear parameters \(x_0,y_0,s_0,\epsilon,\gamma\); they also account for model-dependent gap error in the \(\chi^2\) denominator. The exact single-Yukawa positive confidence bounds in Table 11.4 are not in general equal to \(\hat\beta+\sqrt{6.17}\sigma\). As a result, neither the number 0.01809 nor its nominal confidence level should be presented as an official Eöt-Wash two-pole result. Robust interpolation and full nuisance profiling are required. The **conservative scientific reading** is that a shared-linear-model approximation yields a coupling scale of \(\sim10^{-2}\), not order unity, and motivates a genuine joint recast.

## 4. Source-geometry matters even when point forces cannot cancel

We reproduced Phase 10's invented 18/120 point-ring design with 16 hypothetical gap/harmonic observations and four fitted parameters, using its 2.5%-of-maximum synthetic per-harmonic noise. The marginal synthetic uncertainty is \(\sigma_\alpha=0.2914216\). After projecting out the Newtonian normalization and two per-harmonic offsets, the *whitened template norms* are:

- long Yukawa component: \(0.19331\);
- short Yukawa component: \(3.62465\);
- their difference: \(3.43145\).

Thus in this specific toy design, **the long-range torque signature is largely absorbed by fitted nuisance/normalization terms**, even though point forces near 1 mm are strongly affected. This reverses the naive assumption that the longer-range term is necessarily the more constraining *observable*. Do **not** export this geometry-dependent observation to the actual Eöt-Wash experiment.

## 5. Misspecification falsification of Phase 10B

The original Phase 10B analysis used a correctly specified independent Gaussian linear model for its synthetic recovery and estimated \(\sigma_\alpha=0.2914216\). We independently recalculated the same ring design, then shifted *true* gaps while fitting *nominal* gaps, keeping **true \(\alpha=0\)**.

| Hidden experimental-model error | Noiseless bias in fitted α | Nominal z | Two-sided false-positive probability with the original 1.96σ cutoff |
|---|---:|---:|---:|
| Correct assumed gaps and Gaussian noise | 0.000 | 0.00 | 5.00% |
| True gaps systematically +2 μm | +1.01037 | +3.467 | 93.41% |
| True gaps systematically +5 μm | +2.16480 | +7.428 | >99.99999% |

The probabilities above are derived by integrating the *assumed* normal noise distribution around the model-induced bias, not empirical trial frequencies. For correlated noise without gap error, imposing within-harmonic covariance \(C_{ij}=\sigma_i\sigma_j\exp(-|z_i-z_j|/40\mu\mathrm m)\) makes true \(\sigma_\alpha=0.345927\) rather than the reported 0.291422, inflating the nominal 5% false-positive probability to **9.87%**.

**Conclusion:** Original false-positive calibration is fragile. A small geometry miscalibration can mimic a compelling 'new force' in the invented design. Any genuine instrument analysis must profile calibration and correlations; tests must inject misspecification.

## 6. Dynamical consistency check, and what it does NOT prove

For the suggested higher-spatial-derivative free scalar action (without source coupling),

\[
\mathcal L=\tfrac12[c^{-2}\dot\phi^2-(\nabla\phi)^2-\ell^2(\nabla^2\phi)^2-\mu^2\phi^2],
\]

the Hamiltonian density \(\mathcal H=\tfrac12[c^{-2}\dot\phi^2+(\nabla\phi)^2+\ell^2(\nabla^2\phi)^2+\mu^2\phi^2]\) is nonnegative if \(\ell^2>0\) and \(\mu^2\ge0\). The field equation contains only second time derivatives. Consequently the opposite **static spatial** Yukawa residues do not, alone, prove a propagating Ostrogradsky ghost. This model does break Lorentz invariance by using a preferred time direction; interaction and quantum consistency are unproven, and one cannot reinterpret the static partial fractions as a conventional positive-mass spectral representation of a Lorentz-invariant quantum field without checking positivity.

With \(\omega(k)=c\sqrt{k^2+\ell^2k^4+\mu^2}\), the mathematical group speed exceeds \(c\) once \(k\gtrsim1642.87\,\mathrm{m^{-1}}\) (wavelength \(\sim3.82\,\mathrm{mm}\)), and \(v_g/c=2.10042\) at \(k=5000\,\mathrm{m^{-1}}\). These are purely **model outputs**, not measured signal, information-front, or physical causality speeds. The continuum's high-frequency validity is unestablished. A retarded-response model, a source/detector mechanism, a stable UV completion and direct laboratory falsification remain necessary.

## 7. Release-quality issue in Phase 10

The published Phase 10 report's Reproduction section names `phase10_forward_model.py`, `phase10_injection.py`, `test_phase10.py`, and `make_phase10_figures.py`; **those four named scripts are not present in the current GitHub `research/phase-10/` directory** as checked on 12 November 2026. Available substitutes include `phase10_minimal_repro.py` and `test_phase10_minimal.py`; thus the report's full reproduction commands are not runnable exactly as published. This is a documentation/reproducibility defect, not evidence of fraudulent source data. Phase 11 includes a self-contained script, with explicit test outputs.

## 8. Final decision and narrower research target

**Empirically confirmed:** Published Eöt-Wash torque measurements agree well with Newtonian gravity; the original single-Yukawa fit table exists; its reported uncertainty is in the 0.01 range for millimetre/submillimetre couplings.  
**Theoretically derived:** No point-force cancellation for positive α; static and dispersive field mathematics are internally analyzable.  
**Conditional inference:** Under a fixed shared linear-Gaussian model, the published fit coefficients imply a correlation-robust approximate positive upper envelope \(\alpha\lesssim0.0181\).  
**Synthetic countertest:** 2 μm systematic geometry error produces a 3.47σ *false signal* in the original toy design.  
**Unresolved:** A physical mass/electron source law; the true nonlinear two-pole Eöt-Wash likelihood; public-data extraction/trancription ambiguities; preferred-frame consistency; physical signal-front propagation and detection.

**Actionable research priority:** Reproduce Table 11.4's single-Yukawa fitted coefficients with the dissertation's actual geometry and uncertainty model, then replace \(T_Y(\lambda)\) by \([T_Y(1/a)-T_Y(1/b)]/s\) and refit all 285 published torque measurements jointly. Seek independent replication. Do not claim a new force or faster-than-light physics until such a program produces experimentally meaningful evidence.

## Reproduce

```bash
python -m pip install numpy
python research/phase-11/phase11_adversarial_recast.py
```

Executed on 12 November 2026; `python phase11_adversarial_recast.py` completed with assertions and JSON results in `phase11_results.json`.