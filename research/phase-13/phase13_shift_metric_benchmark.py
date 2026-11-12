#!/usr/bin/env python3
"""Phase 13 ADM-shift benchmark: mathematical metric, NOT FTL propulsion."""
import json
from math import isclose
C=299792458.0
G=6.67430e-11
def simpson(fun,n=4000):
    assert n>0 and n%2==0
    h=1/n
    return (fun(0)+fun(1)+4*sum(fun(i*h) for i in range(1,n,2))
            +2*sum(fun(i*h) for i in range(2,n,2)))*h/3
def profile(t):
    return 1-3*t*t+2*t*t*t
def compute(R_m=100.,wall_m=10.,v_over_c=.1,n=4000):
    if not (R_m > wall_m/2 > 0 and v_over_c>=0):
        raise ValueError("Require R > wall/2 > 0, v/c >= 0")
    R,w=R_m,wall_m
    v=C*v_over_c
    r0,r1=R-w/2,R+w/2
    # Metric ds²=-c²dt²+[dx-vf(r)dt]²+dy²+dz².
    # Eulerian E= -c² v²/(12G) * integral_0^infinity r² f'(r)² dr.
    I=simpson(lambda t:36*(r0+w*t)**2*t*t*(1-t)**2/w,n)
    I_exact=6*R*R/(5*w)+3*w/70
    # Weighted Cauchy-Schwarz yields I >= 1/(1/r0 - 1/r1).
    I_lower=r0*r1/w
    dt=2*(r0*(1/C-1/(C+v))+w*simpson(
        lambda t:1/C-1/(C+v*profile(t)),n))
    length=2*r1
    tflat=length/C
    tmetric=tflat-dt
    E= -C*C*v*v/(12*G)*I
    E_min_abs=C*C*v*v/(12*G)*I_lower
    assert isclose(I,I_exact,rel_tol=2e-12)
    assert I>=I_lower-1e-9
    assert 0<=dt<tflat
    return dict(
      status="IDEALIZED PREBUILT METRIC; NO OBSERVED FTL",
      inputs=dict(R_m=R,wall_m=w,v_over_c=v_over_c),
      radial_integral_m=I,radial_integral_exact_m=I_exact,
      cauchy_min_integral_m=I_lower,
      negative_eulerian_energy_integral_J=E,
      minimum_abs_eulerian_energy_same_ansatz_J=E_min_abs,
      negative_energy_abs_mass_equivalent_kg=abs(E)/C**2,
      route_m=length,flat_light_time_s=tflat,
      assumed_metric_null_time_s=tmetric,
      assumed_metric_time_advance_s=dt,
      effective_endpoint_speed_over_c=length/(C*tmetric),
      independently_measured=False,physically_constructed=False,
      all_observer_energy_conditions_tested=False,
      operational_FTL_demonstrated=False)
def test():
    a=compute()
    b=compute(n=2000)
    assert isclose(a['negative_eulerian_energy_integral_J'],
                   b['negative_eulerian_energy_integral_J'],rel_tol=1e-11)
    assert isclose(a['assumed_metric_time_advance_s'],
                   b['assumed_metric_time_advance_s'],rel_tol=1e-11)
    assert isclose(a['negative_eulerian_energy_integral_J'],
                   -1.2106877984683277e44,rel_tol=1e-10)
    assert isclose(a['assumed_metric_time_advance_s'],
                   6.072232144923481e-8,rel_tol=1e-10)
    zero=compute(v_over_c=0)
    assert zero['negative_eulerian_energy_integral_J']==0
    assert zero['assumed_metric_time_advance_s']==0
    slow=compute(v_over_c=.01)
    assert isclose(slow['negative_eulerian_energy_integral_J']/
                   a['negative_eulerian_energy_integral_J'],.01,rel_tol=1e-10)
    return a
if __name__=='__main__':
    print(json.dumps(test(),indent=2))
