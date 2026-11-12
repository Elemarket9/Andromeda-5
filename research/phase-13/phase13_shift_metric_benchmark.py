#!/usr/bin/env python3
"""Phase 13 benchmark of an idealized spacetime metric. Not observed FTL.

ds²=-c²dt²+[dx-v f(r)dt]²+dy²+dz². Metric is ASSUMED to pre-exist.
C2 quintic wall is default; lower-regularity C1 cubic is a sensitivity check.
Only Eulerian integrated energy and axial null travel times are computed.
"""
import json
from math import isclose
C=299792458.0
G=6.67430e-11

def simpson(fun,n=4000):
    if n<2 or n%2: raise ValueError("n must be even and >=2")
    h=1/n
    return (fun(0)+fun(1)+4*sum(fun(i*h) for i in range(1,n,2))
            +2*sum(fun(i*h) for i in range(2,n,2)))*h/3

def profile(t,shape="quintic"):
    if shape=="quintic": return 1-10*t**3+15*t**4-6*t**5
    if shape=="cubic": return 1-3*t*t+2*t*t*t
    raise ValueError(shape)

def compute(R_m=100.,wall_m=10.,v_over_c=.1,n=4000,wall_shape="quintic"):
    if not(R_m>wall_m/2>0 and v_over_c>=0):raise ValueError("invalid scale or speed")
    R,w=R_m,wall_m
    v=C*v_over_c
    r0,r1=R-w/2,R+w/2
    if wall_shape=="quintic":
        I=simpson(lambda t:900*(r0+w*t)**2*t**4*(1-t)**4/w,n)
        I_exact=10*R*R/(7*w)+5*w/154
    elif wall_shape=="cubic":
        I=simpson(lambda t:36*(r0+w*t)**2*t*t*(1-t)**2/w,n)
        I_exact=6*R*R/(5*w)+3*w/70
    else:raise ValueError(wall_shape)
    # Energy E=-c²v²/(12G)∫ r² f'(r)² dr from ADM Hamiltonian constraint.
    E=-C*C*v*v/(12*G)*I
    # Weighted Cauchy: ∫ r² f'^2 >= 1/(1/r0-1/r1).
    I_min=r0*r1/w
    E_min=C*C*v*v/(12*G)*I_min
    # Axial +x null ray: dx/dt=c+v*f(|x|). Endpoints ±r1.
    advantage=2*(r0*(1/C-1/(C+v))+w*simpson(
        lambda t:1/C-1/(C+v*profile(t,wall_shape)),n))
    flat_t=2*r1/C
    metric_t=flat_t-advantage
    assert isclose(I,I_exact,rel_tol=2e-12)
    assert I>=I_min-1e-9
    assert 0<=advantage<flat_t
    return dict(status="MATHEMATICAL PREBUILT METRIC ONLY — NOT PHYSICAL PROPULSION",
      parameters=dict(radius_m=R,wall_width_m=w,v_over_c=v_over_c,shape=wall_shape),
      radial_integral_m=I,radial_integral_analytic_m=I_exact,
      wall_profile_variational_lower_bound_integral_m=I_min,
      integrated_eulerian_energy_J=E,
      minimum_abs_integrated_energy_same_ansatz_J=E_min,
      abs_energy_mass_equivalent_kg=abs(E)/C**2,
      route_m=2*r1,flat_null_time_s=flat_t,
      metric_null_time_s=metric_t,time_advance_s=advantage,
      endpoint_effective_speed_over_c=2*r1/(C*metric_t),
      matter_source_realized=False,all_observer_conditions_tested=False,
      causality_and_creation_proven=False,FTL_experiment=False)

def selftest():
    a=compute()
    b=compute(n=2000)
    assert isclose(a["integrated_eulerian_energy_J"],
        -1.4411078838345363e44,rel_tol=1e-10)
    assert isclose(a["time_advance_s"],6.071056529217648e-8,rel_tol=1e-10)
    assert isclose(a["time_advance_s"],b["time_advance_s"],rel_tol=1e-11)
    assert isclose(a["integrated_eulerian_energy_J"],
        b["integrated_eulerian_energy_J"],rel_tol=1e-11)
    cubic=compute(wall_shape="cubic")
    assert isclose(cubic["integrated_eulerian_energy_J"],
        -1.2106877984683277e44,rel_tol=1e-10)
    zero=compute(v_over_c=0)
    assert zero["integrated_eulerian_energy_J"]==0
    assert zero["time_advance_s"]==0
    slow=compute(v_over_c=.01)
    assert isclose(slow["integrated_eulerian_energy_J"]/
        a["integrated_eulerian_energy_J"],.01,rel_tol=1e-10)
    return dict(C2_quintic=a,C1_cubic=cubic)
if __name__=="__main__":
    print(json.dumps(selftest(),indent=2))
