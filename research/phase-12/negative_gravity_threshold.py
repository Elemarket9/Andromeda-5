#!/usr/bin/env python3
"""ANDROMEDA-5 Phase 12: static two-pole repulsion threshold.

Only a mathematical analysis of an UNOBSERVED force law.
No new force, negative mass, exotic matter or FTL travel is demonstrated.
No external Python packages are required.
"""
import json
from math import sqrt, log, exp

ELL_M = 2e-4
MU_INV_M = 1000.0
DELTA_CHI2_CONDITIONAL = 6.17

def poles(ell=ELL_M, mu=MU_INV_M):
    assert ell > 0 and mu >= 0 and 4*ell*ell*mu*mu < 1
    s = sqrt(1 - 4*ell*ell*mu*mu)
    a = sqrt((1-s)/(2*ell*ell))
    b = sqrt((1+s)/(2*ell*ell))
    assert a < b and s > 0
    return s, a, b

def B(r, s, a, b):
    assert r >= 0
    f = lambda x: (1+x)*exp(-x)
    return (f(a*r)-f(b*r))/s

def exact_peak(s, a, b):
    r = 2*log(b/a)/(b-a)
    return r, B(r,s,a,b)

def conditional_negative_envelope():
    """NOT a valid lab confidence interval without a shared linear likelihood."""
    D = -78.14651349016431
    qmin = 3549.996296415541
    qmax = 35623.96392724559
    s,_,_ = poles()
    threshold = sqrt(DELTA_CHI2_CONDITIONAL)
    lower = s*D/qmin - threshold*s/sqrt(qmin)
    assert lower < 0
    return {"lower_envelope_at_Q_min":lower,
            "Q_min":qmin,"Q_max":qmax,
            "assumptions":"Phase 11 shared Gaussian covariance, nuisance subspace, and interpolation; NOT an empirical two-pole 95% confidence bound"}

def main():
    s,a,b = poles()
    r,peak = exact_peak(s,a,b)
    alpha_transition = -1/peak
    assert abs(r-0.0008090916468859514) < 1e-15
    assert abs(peak-0.7688725894578924) < 1e-12
    assert abs(alpha_transition+1.3006056058066373) < 1e-12
    grid = [1e-9*10**(i/50) for i in range(0,360)]
    # The peak is the unique stationary maximum. For r>0, B(r)>0.
    assert all(B(x,s,a,b)>0 and B(x,s,a,b)<=peak+1e-12 for x in grid)
    # For positive alpha there is no point-mass repulsion anywhere.
    assert all(1+alpha*B(x,s,a,b)>0 for alpha in (0,0.0181,1) for x in grid)
    # Negative alpha must cross threshold strictly to make net force repulsive.
    assert 1-1.3*peak>0
    assert 1-1.301*peak<0
    cond=conditional_negative_envelope()
    print(json.dumps({
      "status":"HYPOTHETICAL STATIC MODEL ONLY; NOT EVIDENCE OF NEGATIVE MASS OR FTL",
      "inputs":{"ell_m":ELL_M,"mu_inv_m":MU_INV_M},
      "s":s,"a_inv_m":a,"b_inv_m":b,
      "peak_B":peak,"peak_separation_mm":1000*r,
      "repulsive_force_requires_alpha_below":alpha_transition,
      "healthy_real_universal_scalar_source":"alpha = g^2/(4*pi*G) >= 0 (in specified normalization)",
      "point_mass_repulsion_cannot_arise_with_that_source":True,
      "conditional_negative_alpha_envelope":cond,
      "experimental_limit_proven":False,
      "negative_gravitational_mass_constructed":False,
      "faster_than_light_travel_demonstrated":False
    },indent=2))

if __name__=="__main__":
    main()
