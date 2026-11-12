#!/usr/bin/env python3
"""ANDROMEDA-5 Phase 11 independent, CONDITIONAL sensitivity recast.

Requires: Python 3.10+, numpy. No real experiment performed here.
The publication-derived single-Yukawa fits are Table 11.4 of John G. Lee's
2020 UW dissertation (https://digital.lib.washington.edu/researchworks/
bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download).
Conditional bounds require common linear-Gaussian nuisance projection and fixed
covariance, NOT proven for Lee's original nonlinear fitting pipeline.
"""
import math
import json
import numpy as np

ELL=2e-4; MU=1000.; G=6.67430e-11; C_LIGHT=299792458.
S=math.sqrt(1-4*ELL**2*MU**2)
A=math.sqrt((1-S)/(2*ELL**2))
B=math.sqrt((1+S)/(2*ELL**2))
L_LONG=1/A*1000  # mm
L_SHORT=1/B*1000 # mm

# Published original single-Yukawa data: range mm, alpha_hat, sigma_alpha.
# Independently reported fits, not a joint cross-range covariance.
TABLE=np.array([
    [0.200,-0.00235,0.01570],
    [0.220,-0.00351,0.01470],
    [0.890,-0.00612,0.00845],
    [1.000,-0.00569,0.00796],
])

def force_fraction(r_m, alpha=1.):
    return alpha/S*((1+A*r_m)*np.exp(-A*r_m) -
                    (1+B*r_m)*np.exp(-B*r_m))

def phase_velocity_group_ratio(k):
    return (k+2*ELL**2*k**3)/math.sqrt(k*k+ELL**2*k**4+MU**2)

def bisect(f, low, high, iters=85):
    if f(low)*f(high)>0:raise ValueError('non-bracketing interval')
    for _ in range(iters):
        mid=(low+high)/2
        if f(low)*f(mid)<=0:high=mid
        else:low=mid
    return (low+high)/2

def fmax():
    # Golden-section maximizer, point-particle force ratio on (0, 5 mm).
    lo=1e-9; hi=.005; h=(math.sqrt(5)-1)/2
    x1=hi-h*(hi-lo); x2=lo+h*(hi-lo)
    for _ in range(100):
        if force_fraction(x1)<force_fraction(x2):lo=x1; x1=x2; x2=lo+h*(hi-lo)
        else:hi=x2; x2=x1; x1=hi-h*(hi-lo)
    loc=(lo+hi)/2
    return loc, float(force_fraction(loc))

def interp(x, x0, v0, x1, v1):
    return v0+(v1-v0)*(x-x0)/(x1-x0)

def pubfit(long=True):
    (x0,a0,s0),(x1,a1,s1)=(TABLE[2],TABLE[3]) if long else (TABLE[0],TABLE[1])
    x=L_LONG if long else L_SHORT
    return interp(x,x0,a0,x1,a1),interp(x,x0,s0,x1,s1)

def conditional_bound():
    """Unknown cross-template correlation bounded by Cauchy-Schwarz.

    Let u1,u2 be whitened, nuisance-projected Yukawa responses. Published
    fits under the SHARED LINEAR MODEL imply norms N1=1/sigma1, N2=1/sigma2;
    residual projections R_i=alpha_hat_i/sigma_i**2. Define
      Q=||u1-u2||**2 in [(N1-N2)**2,(N1+N2)**2]
      D=R1-R2
      alpha_hat_combined=S*D/Q, sigma_combined=S/sqrt(Q).
    Maximizing alpha_hat + sqrt(6.17)*sigma over this Q interval gives
    a conservative correlation-free upper *profile* envelope in this model.
    """
    ah1,se1=pubfit(True);ah2,se2=pubfit(False)
    norm1,norm2=1/se1,1/se2
    D=ah1/se1**2-ah2/se2**2
    qmin=(norm1-norm2)**2;qmax=(norm1+norm2)**2
    t=math.sqrt(6.17)
    def upper(q):return S*D/q+S*t/math.sqrt(q)
    candidate=[qmin,qmax]
    if D<0:
        qstar=(-2*D/t)**2
        if qmin<=qstar<=qmax:candidate.append(qstar)
    return {'lambda_long_mm':L_LONG,'lambda_short_mm':L_SHORT,
            'published_interpolated_long_hat_sigma':[ah1,se1],
            'published_interpolated_short_hat_sigma':[ah2,se2],
            'nuisance_projected_template_norms':[norm1,norm2],
            'D':D,'Q_min':qmin,'Q_max':qmax,
            'conditional_95_like_positive_alpha_upper_envelope':max(upper(q) for q in candidate),
            'conditional_sigma_alpha_upper_envelope':S/math.sqrt(qmin),
            'delta_chisq_alpha_1_vs_null_lower_envelope':qmin/S**2-2*D/S,
            'NOTE':'NOT a real two-Yukawa 95% exclusion: covariance and nuisance model assumed common and linear.'}

def ring_coefficient(n,z_um,kind,angles=48):
    """Same invented ring geometry as public Phase 10 minimal reproducer."""
    radius=.003 if n==18 else .0014
    m=5e-7/n
    th=np.arange(n)*2*np.pi/n
    source=np.stack([radius*np.cos(th),radius*np.sin(th),np.full(n,z_um*1e-6)],axis=-1)[None,:,:]
    torques=[]
    for phase in np.arange(angles)*2*np.pi/n/angles:
        ph=th+phase+.007/n
        detector=np.stack([radius*np.cos(ph),radius*np.sin(ph),np.zeros(n)],axis=-1)[:,None,:]
        dr=source-detector
        dist=np.linalg.norm(dr,axis=-1)
        base=G*m*m*(detector[...,0]*source[...,1]-detector[...,1]*source[...,0])/dist**3
        if kind=='long':base=base*(1+A*dist)*np.exp(-A*dist)/S
        elif kind=='short':base=base*(1+B*dist)*np.exp(-B*dist)/S
        elif kind=='two':base=base*force_fraction(dist)
        elif kind!='newton':raise ValueError(kind)
        torques.append(base.sum())
    return float(2*np.fft.rfft(torques)[1].imag/angles)

def toy_stress():
    gaps=(55,65,80,100,130,170,220,300)
    rows=[(n,z) for n in (18,120) for z in gaps]
    harmonic=np.array([n for n,_ in rows]);gap=np.array([z for _,z in rows])
    N=np.array([ring_coefficient(n,z,'newton') for n,z in rows])
    Ylong=np.array([ring_coefficient(n,z,'long') for n,z in rows])
    Yshort=np.array([ring_coefficient(n,z,'short') for n,z in rows])
    Y=Ylong-Yshort
    sigma=np.array([.025*np.max(abs(N[harmonic==n])) for n in harmonic])
    X=np.column_stack([N,Y,(harmonic==18)*sigma,(harmonic==120)*sigma])
    W=X/sigma[:,None]; covariance=np.linalg.inv(W.T@W)
    estimator=covariance@W.T/sigma[None,:]
    formal_sigma=math.sqrt(covariance[1,1])
    # Null injected: alpha=0, with deliberately incorrect gap calibration.
    shifts={}
    for dz in (0,2,5):
        Ntrue=np.array([ring_coefficient(n,z+dz,'newton') for n,z in rows])
        true=Ntrue+X@np.array([0.,0.,.25,-.15])
        b=float((estimator@true)[1])
        zscore=b/formal_sigma
        # For unit-variance Gaussian statistics, exact two-sided false positive
        # from deterministic model bias (threshold 1.96 reported sigma).
        normal_cdf=lambda x:.5*math.erfc(-x/math.sqrt(2))
        p=normal_cdf(-1.96-zscore)+1-normal_cdf(1.96-zscore)
        shifts[str(dz)]={'fitted_alpha_with_zero_real_signal':b,
                         'reported_zscore':zscore,'false_positive_probability':p}
    corr_scale=40.
    Corr=np.exp(-abs(gap[:,None]-gap[None,:])/corr_scale)
    Corr*=(harmonic[:,None]==harmonic[None,:])
    physical_cov=(sigma[:,None]*Corr)*sigma[None,:]
    true_sigma=math.sqrt(float(estimator[1]@physical_cov@estimator[1]))
    falsepos=math.erfc(1.96*formal_sigma/(true_sigma*math.sqrt(2)))
    # Profile N and offsets to understand why point force amplitudes are not
    # equal to measurable torque sensitivities.
    Bnuis=np.column_stack([N/sigma,(harmonic==18).astype(float),(harmonic==120).astype(float)])
    Proj=np.eye(len(rows))-Bnuis@np.linalg.pinv(Bnuis)
    norms=[float(np.linalg.norm(Proj@(v/sigma))) for v in (Ylong,Yshort,Y)]
    return {'toy_only':True,'reported_sigma_alpha':formal_sigma,
            'correct_model_condition_number':float(np.linalg.cond(W)),
            'calibration_shift_um':shifts,
            'correlated_noise_length_um':corr_scale,
            'correlated_noise_actual_sigma_alpha':true_sigma,
            'correlated_noise_false_positive_probability':falsepos,
            'projected_long_short_pair_response_norms':norms,
            'max_abs_decomposition_error':float(np.max(abs(Y-(Ylong-Yshort))))}

def main():
    rmax,maxf=fmax()
    crit=bisect(lambda k:phase_velocity_group_ratio(k)-1,100,5000)
    result={'model':'ANDROMEDA-5 hypothetical two-pole force, NOT observed',
            'pole_s':S,'pole_a_inv_m':A,'pole_b_inv_m':B,
            'point_force_alpha1_at_52um':float(force_fraction(52e-6)),
            'point_force_alpha1_at_1mm':float(force_fraction(.001)),
            'point_force_max_fraction_and_distance_mm':[maxf,rmax*1000],
            'group_velocity_crosses_c_k_inv_m':crit,
            'group_velocity_c_at_k5000':phase_velocity_group_ratio(5000),
            'group_velocity_is_not_a_measured_signal_speed':True,
            'conditional_published_fit_recast':conditional_bound(),
            'adversarial_toy_stress':toy_stress()}
    assert abs(formal:=result['adversarial_toy_stress']['reported_sigma_alpha']-.2914216258057527)<1e-8
    assert abs(result['point_force_alpha1_at_1mm']-.74597516722)<1e-9
    assert result['conditional_published_fit_recast']['conditional_95_like_positive_alpha_upper_envelope']<.02
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()