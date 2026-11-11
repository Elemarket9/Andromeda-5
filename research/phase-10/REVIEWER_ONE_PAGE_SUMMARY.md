# External physics reviewer brief — ANDROMEDA-5 Phase 10

**Independent, unreviewed theoretical research; no FTL or novel force detection claimed.**

**Repository:** https://github.com/Elemarket9/Andromeda-5

**Question:** Can a hypothetical two-exponential static force (difference of Yukawa terms) be derived from a consistent matter coupling, and can it be rigorously compared with the 2020 Eöt-Wash torsion-balance dataset?

## The proposed force

`U = -(G m1 m2 / r) [1 + alpha (exp(-a*r)-exp(-b*r))/s]`, where `s=sqrt(1-4 ell² mu²)`, `a²=(1-s)/(2 ell²)`, and `b²=(1+s)/(2 ell²)`.

Assumed ell=0.2 mm and mu=1000/m imply scales 0.979 mm and 0.204 mm. **The universal mass coupling is a phenomenological choice; it is not derived from the earlier electron–scalar interaction.**

## What passed numerically

- 1,000 independent finite-difference torque derivative checks, worst relative discrepancy 4.95e-9.
- Synthetic two-harmonic, 16-observation Monte Carlo pipeline with injected alpha values 0, 0.5 and 1.
- Synthetic null false-positive rate 5.65% in 2,000 trials against a nominal 5% reference.

## What we have not done

We have not reconstructed the actual 2020 Eöt-Wash mass geometry, Fourier-Bessel torque templates, nuisance covariance, or joint two-pole likelihood. We have not fit the proposed two-pole force against actual torque measurements. No professor has reviewed or endorsed this research.

## Four requested critiques

1. Does this static force meaningfully follow from a consistent scalar–matter interaction, or does the mass coupling create a fatal conceptual error?
2. Are there theoretical problems with the assumed higher-order dispersion, including its high-frequency validity?
3. What experimental geometry, calibration, nuisance parameters and covariance information would be needed to fit a difference-of-Yukawa force against the Lee 2020 measurements?
4. Which prior measurements or published analyses would already exclude the candidate interaction?

We seek constructive criticism or a referral to an appropriate experimental specialist, **not an endorsement**.

**Cited experiment:** Lee et al. PRL 124, 101101 (2020), https://doi.org/10.1103/PhysRevLett.124.101101
