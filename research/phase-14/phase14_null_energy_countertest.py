#!/usr/bin/env python3
"""Phase 14 independent JAX Einstein tensor: positive Eulerian energy BUT NEC fails.

A mathematical spacetime is assumed, not a real matter source or FTL device.
"""
import json
import math
import jax
import jax.numpy as jnp
import numpy as np
jax.config.update("jax_enable_x64",True)
C=299792458.
G=6.67430e-11
R=100.
W=10.
A=.1
L=100.
B=.0045

def params(z):
    r=jnp.sqrt(z[1]**2+z[2]**2+z[3]**2+1e-24)
    psi=1+A/jnp.sqrt(r*r+L*L)
    t=jnp.clip((r-(R-W/2))/W,0.,1.)
    f=1-10*t**3+15*t**4-6*t**5
    return r,psi,f

def metric(z):
    r,psi,f=params(z)
    q=psi**4
    gm=jnp.diag(jnp.array([-1.,q,q,q]))
    gm=gm.at[0,0].add(q*B*B*f*f)
    gm=gm.at[0,1].set(-q*B*f)
    gm=gm.at[1,0].set(-q*B*f)
    return gm

def gamma(z):
    gm=metric(z)
    dg=jax.jacfwd(metric)(z) # dg[i,j,k]=partial_k(g_ij)
    term=jnp.transpose(dg,(0,2,1))+dg-jnp.transpose(dg,(2,0,1))
    return .5*jnp.einsum("ad,dbc->abc",jnp.linalg.inv(gm),term)

def einstein(z):
    gm=metric(z)
    ga=gamma(z)
    dga=jax.jacfwd(gamma)(z) # dga[a,b,c,k]
    Ric=(jnp.einsum("lmul->mu",dga)
        -jnp.einsum("lmln->mn",dga)
        +jnp.einsum("lls,smn->mn",ga,ga)
        -jnp.einsum("lns,sml->mn",ga,ga))
    scalar=jnp.einsum("ij,ij->",jnp.linalg.inv(gm),Ric)
    return Ric-.5*gm*scalar

def main():
    z=jnp.array([0.,0.,100.,0.]) # x0=ct, at equatorial bubble wall
    gm=np.asarray(metric(z))
    Eg=np.asarray(einstein(z))
    _,psi,f=map(float,params(z))
    n=np.array([1.,B*f,0.,0.])
    ex=np.array([0.,psi**-2,0.,0.])
    k=n+ex
    Gnn=float(n@Eg@n)
    Gkk=float(k@Eg@k)

    # Independent ADM Hamiltonian constraint for this equatorial point:
    R3=24*A*L*L/(math.sqrt(100.**2+L*L)+A)**5
    fp=-1.875/W
    H=R3-(B*B/2)*fp*fp
    assert math.isclose(Gnn,H/2,rel_tol=1e-9,abs_tol=1e-16)
    assert abs(n@gm@n+1)<1e-10
    assert abs(k@gm@k)<1e-10
    assert Gnn>0 and Gkk<0
    return dict(
      status="TOY METRIC: POSITIVE NORMAL ENERGY, NEC VIOLATION",
      coordinate_point_x0_x_y_z_m=[0,0,100,0],
      G_nn_inv_m2=Gnn,independent_H_over_2_inv_m2=H/2,
      G_kk_inv_m2=Gkk,null_direction="k=n+e_x, normalized Eulerian tetrad",
      energy_normal_J_m3=C**4/(8*math.pi*G)*Gnn,
      stress_null_J_m3=C**4/(8*math.pi*G)*Gkk,
      NEC_satisfied=False,all_observer_WEC_satisfied=False,
      operational_FTL=False,experimental_result=False)
if __name__=="__main__":
    print(json.dumps(main(),indent=2))
