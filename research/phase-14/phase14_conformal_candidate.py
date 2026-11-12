#!/usr/bin/env python3
"""Phase 14 conformal-shell toy metric: NO verified FTL, NO all-observer WEC test.

ds² = -c²dt² + psi(r)^4 [(dx - v f(r)dt)² + dy² + dz²].
Exactly checks sign of Eulerian energy; not all stress-energy conditions.
"""
import json
import math
C=299792458.0
G=6.67430e-11
def simpson(a,b,fun,n=6000):
    if n<2 or n%2: raise ValueError("n must be even")
    h=(b-a)/n
    return (fun(a)+fun(b)+4*sum(fun(a+i*h) for i in range(1,n,2))
            +2*sum(fun(a+i*h) for i in range(2,n,2)))*h/3
def f(t):return 1-10*t**3+15*t**4-6*t**5
def compute(R=100.,w=10.,A=.1,L=100.,beta=.0045,n=6000):
    if not(R>w/2>0 and A>0 and L>0 and beta>=0):
        raise ValueError("invalid inputs")
    r0,r1=R-w/2,R+w/2
    psi=lambda r:1+A/math.sqrt(r*r+L*L)
    Ricci3=lambda r:24*A*L*L/(math.sqrt(r*r+L*L)+A)**5
    prof=lambda r:1. if r<=r0 else (0. if r>=r1 else f((r-r0)/w))
    fmax=1.875/w
    Hlower=Ricci3(r1)-.5*beta**2*fmax**2
    b_max=math.sqrt(2*Ricci3(r1))/fmax
    assert Hlower>0 and beta<b_max
    # ADM Hamiltonian constraint H=(16*pi*G/c^4) * energy_density:
    # H=Ricci3 + beta²[-.5 f'^2 sin²theta +
    # 8 f (psi'/psi) f' cos²theta + 24 f²(psi'/psi)² cos²theta].
    # psi'<0 and f'<=0; hence positive last two terms.
    # Ricci3 strictly decreases with r, and |f'|<=fmax.
    # Therefore H>0 everywhere (inside / outside wall H>=Ricci3>0).
    dt_dx=lambda r:1/(C/psi(r)**2+beta*C*prof(r))
    T=2*(simpson(0,r0,dt_dx,n)+simpson(r0,r1,dt_dx,n))
    Tflat=2*r1/C
    M_ADM=2*A*C*C/G
    return dict(
      status="TOY METRIC ONLY; not measured or operational FTL",
      parameters=dict(R_m=R,w_m=w,A_m=A,L_m=L,v_over_c=beta),
      analytic_wall_lower_bound_ADM_H_inv_m2=Hlower,
      normal_observer_energy_nonnegative_everywhere=True,
      conservative_max_beta=b_max,
      ADM_mass_kg=M_ADM,
      equivalent_schwarzschild_radius_m=4*A,
      flat_coordinate_light_time_s=Tflat,
      metric_axial_null_time_s=T,
      coordinate_time_advance_s=Tflat-T,
      endpoint_coordinate_speed_over_c=2*r1/(C*T),
      all_observer_conditions_verified=False,
      realized_matter_source=False,operational_FTL=False,
      novelty_established=False)
def selftest():
    x=compute()
    y=compute(n=3000)
    assert math.isclose(x["coordinate_time_advance_s"],
            1.7761929182656226e-9,rel_tol=1e-9)
    assert math.isclose(x["coordinate_time_advance_s"],
            y["coordinate_time_advance_s"],rel_tol=1e-9)
    assert math.isclose(x["ADM_mass_kg"],2.6931818430002183e26,rel_tol=1e-12)
    assert x["analytic_wall_lower_bound_ADM_H_inv_m2"]>1e-8
    return x
if __name__=="__main__":
    print(json.dumps(selftest(),indent=2))
