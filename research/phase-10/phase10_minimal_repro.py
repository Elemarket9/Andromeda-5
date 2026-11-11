#!/usr/bin/env python3
"""ANDROMEDA-5 Phase 10 self-contained reproducibility check.

Only mathematical and synthetic-data calculations; NO empirical FTL or new-force finding.
"""
import json
import numpy as np

G = 6.67430e-11
ELL = 2e-4  # assumed meters
MU = 1e3    # assumed inverse meters

def poles():
    s = np.sqrt(1-4*ELL**2*MU**2)
    return (np.sqrt((1-s)/(2*ELL**2)), np.sqrt((1+s)/(2*ELL**2)), s)

def potential(rd, rs, m1, m2, strength=1):
    a,b,s=poles(); d=np.linalg.norm(np.asarray(rd)-np.asarray(rs),axis=-1)
    return -G*m1*m2/d*(1+strength*(np.exp(-a*d)-np.exp(-b*d))/s)

def torque(rd, rs, m1, m2, strength=1, term='total'):
    rd=np.asarray(rd);rs=np.asarray(rs);a,b,s=poles()
    d=np.linalg.norm(rs-rd,axis=-1)
    base=G*m1*m2*(rd[...,0]*rs[...,1]-rd[...,1]*rs[...,0])/d**3
    tail=lambda k:(1+k*d)*np.exp(-k*d)
    if term=='newton':return base
    if term=='two':return base*strength*(tail(a)-tail(b))/s
    return base*(1+strength*(tail(a)-tail(b))/s)

def ring_coefficient(n,z_um,part,angles=48):
    radius=0.003 if n==18 else .0014
    md=ms=5e-7/n
    th0=np.arange(n)*2*np.pi/n
    rs=np.stack([radius*np.cos(th0),radius*np.sin(th0),np.full(n,z_um*1e-6)],axis=-1)[None,:,:]
    values=[]
    for phase in np.arange(angles)*2*np.pi/n/angles:
        d=th0+phase+0.007/n
        rd=np.stack([radius*np.cos(d),radius*np.sin(d),np.zeros(n)],axis=-1)[:,None,:]
        values.append(float(torque(rd,rs,md,ms,term=part).sum()))
    return 2*np.fft.rfft(values)[1].imag/angles

def synthetic_fit(seed=20261111,ntrials=2000):
    rng=np.random.default_rng(seed)
    rows=[(n,z,ring_coefficient(n,z,'newton'),ring_coefficient(n,z,'two'))
          for n in (18,120) for z in (55,65,80,100,130,170,220,300)]
    n=np.array([r[0] for r in rows]);N=np.array([r[2] for r in rows]);Y=np.array([r[3] for r in rows])
    sigma=np.array([0.025*max(abs(N[n==h])) for h in n]); a=(n==18).astype(float);b=(n==120).astype(float)
    X=np.column_stack([N,Y,a*sigma,b*sigma]);W=X/sigma[:,None]
    C=np.linalg.inv(W.T@W);s_alpha=float(np.sqrt(C[1,1]));condition=float(np.linalg.cond(W))
    result={}
    for alpha in (0.0,0.5,1.0):
        base=X@np.array([1.,alpha,.25,-.15]);zscore=[];coverage=[]
        for _ in range(ntrials):
            y=base+rng.normal(0,1,len(N))*sigma
            estimate=C@W.T@(y/sigma)
            zscore.append(float(estimate[1]/s_alpha))
            coverage.append(abs(estimate[1]-alpha)<1.96*s_alpha)
        result[str(alpha)]={'detection_rate_abs_z_gt_1p96':float(np.mean(np.abs(zscore)>1.96)),
                            'nominal_95pct_interval_coverage':float(np.mean(coverage))}
    return s_alpha,condition,result

def main():
    a,b,s=poles()
    rd=np.array([0.002,0.001,0]);rs=np.array([-0.001,0.003,0.00012]);h=1e-5
    rotate=lambda theta:np.array([rd[0]*np.cos(theta)-rd[1]*np.sin(theta),rd[0]*np.sin(theta)+rd[1]*np.cos(theta),rd[2]])
    tdiff=-(potential(rotate(h),rs,.002,.003,.09)-potential(rotate(-h),rs,.002,.003,.09))/(2*h)
    texact=float(torque(rd,rs,.002,.003,.09))
    assert abs(tdiff-texact)/abs(texact)<1e-7
    sa,cond,mc=synthetic_fit()
    print(json.dumps({'status':'NUMERICAL TOY MODEL ONLY — NO REAL FORCE DETECTED',
         'long_range_mm':1000/a,'short_range_mm':1000/b,
         'torque_check_rel_err':abs(tdiff-texact)/abs(texact),
         'synthetic_sigma_alpha':sa,'synthetic_design_condition':cond,
         'synthetic_trials_per_alpha':2000,'synthetic_monte_carlo':mc},indent=2))

if __name__=='__main__':main()
