#!/usr/bin/env python3
"""ANDROMEDA-5 Phase 10D adversarial falsification screen.

Published input: four marginal, single-Yukawa fits transcribed from Lee (2020)
Thesis, Table 11.4. We have NOT reproduced the joint experimental likelihood.
The correlation envelope assumes a shared, linearized nuisance projection and
common Gaussian whitened data. It is NOT a valid 95% exclusion from real data.
Misspecification tests are synthetic; none are experimental measurements.
"""
from __future__ import annotations
import csv, json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ELL, MU = 2.e-4, 1000.0
S = math.sqrt(1. - 4. * ELL**2 * MU**2)
A = math.sqrt((1. - S)/(2*ELL**2))
B = math.sqrt((1. + S)/(2*ELL**2))
LAM_LONG_MM, LAM_SHORT_MM = 1000/A, 1000/B


def interpolate(log_lambda_mm, rows):
    rows = sorted(rows, key=lambda r:r['lambda_mm'])
    x, y = rows
    t = (math.log(log_lambda_mm)-math.log(x['lambda_mm']))/(math.log(y['lambda_mm'])-math.log(x['lambda_mm']))
    return {key:(1-t)*x[key]+t*y[key] for key in ('alpha_hat','sigma_alpha')}


def marginal_screen(long_fit, short_fit, rho):
    """Conditional shared-likelihood correlation model, NOT real-data limit."""
    al,sl = long_fit['alpha_hat'],long_fit['sigma_alpha']
    ash,ssh=short_fit['alpha_hat'],short_fit['sigma_alpha']
    den=1/sl**2 + 1/ssh**2 - 2*rho/(sl*ssh)
    mean=S*(al/sl**2 - ash/ssh**2)/den
    sigma=S/math.sqrt(den)
    return dict(rho=float(rho),alpha_hat=float(mean),sigma=float(sigma),lower_95=float(mean-1.96*sigma),upper_95=float(mean+1.96*sigma))


def force_ratio(mm):
    r = mm/1000.
    f=lambda k:(1+k*r)*math.exp(-k*r)
    return (f(A)-f(B))/S


def design_from_csv():
    with (HERE/'phase10_synthetic_design_source.csv').open(newline='') as f:rows=list(csv.DictReader(f))
    n = np.array([int(r['harmonic']) for r in rows])
    z = np.array([float(r['gap_um']) for r in rows])
    N = np.array([float(r['newton']) for r in rows])
    Y = np.array([float(r['two_pole']) for r in rows])
    sigma=np.array([.025*np.max(np.abs(N[n==k])) for k in n])
    X=np.column_stack((N,Y,(n==18)*sigma,(n==120)*sigma))
    return n,z,N,Y,sigma,X


def estimate_data_alpha(X,sigma,observations):
    W = X / sigma[:,None]
    t=np.linalg.pinv(W) @ (observations / sigma[:,None] if observations.ndim==2 else observations/sigma)
    return t[1]


def shifted_templates(z,n,N,Y,shift_um):
    """PCHIP interpolation of the *toy* 16-point numerical design only.
    Each harmonic is treated independently. This is a synthetic error test,
    not a reconstruction of an experimental gap offset.
    """
    from scipy.interpolate import PchipInterpolator
    ns,ys=[],[]
    for harmonic in [18,120]:
        mask=n==harmonic
        xn=z[mask]
        ns.extend(PchipInterpolator(xn,N[mask],extrapolate=True)(xn+shift_um))
        ys.extend(PchipInterpolator(xn,Y[mask],extrapolate=True)(xn+shift_um))
    return np.array(ns),np.array(ys)


def stress_tests(n_trials=3000,seed=20261111):
    n,z,N,Y,sigma,X=design_from_csv()
    W=X/sigma[:,None]
    s_a=float(np.sqrt(np.linalg.inv(W.T@W)[1,1]))
    rng=np.random.default_rng(seed)
    out=[]
    # Baseline correct model, wrong gap correction, correlated noise, and drift.
    # Gap offset is synthetic +10 micrometres, drawn from interpolated toy data.
    configurations=(
      ('matched_independent',0.,0.,0.),
      ('gap_plus10um',10.,0.,0.),
      ('ar1_noise_rho_0p75',0.,.75,0.),
      ('geometry_drift_3pct',0.,0.,.03),
      ('combined',10.,.75,.03),
    )
    for name,gap_shift,rho,drift in configurations:
        Nt,Yt=shifted_templates(z,n,N,Y,gap_shift) if gap_shift else (N,Y)
        # systematic mismatch of the Newtonian geometry template at small gaps
        shape=(z-z.min())/(z.max()-z.min()) - .5
        Nt=Nt*(1+drift*shape)
        R=np.eye(len(n))
        if rho:
            for k in (18,120):
                ids=np.where(n==k)[0]
                for i in ids:
                    for j in ids:
                        R[i,j]=rho**abs(i-j)
        L=np.linalg.cholesky(R)
        # identically scaled per-harmonic offset nuisance columns
        nuisance=X[:,2]*.25 + X[:,3]*(-.15)
        noise=(rng.normal(size=(len(n),n_trials)).T@L.T).T * sigma[:,None]
        for strength in (0., .5, 1.):
            y=(Nt+strength*Yt+nuisance)[:,None] + noise
            estimates=estimate_data_alpha(X,sigma,y)
            out.append(dict(scenario=name,injected_alpha=strength,n_trials=n_trials,
                            bias=float(np.mean(estimates-strength)),
                            empirical_sd=float(np.std(estimates,ddof=1)),
                            naive_reported_se=s_a,
                            coverage_naive_95=float(np.mean(np.abs(estimates-strength)<=1.96*s_a)),
                            false_positive_or_detection=float(np.mean(np.abs(estimates/s_a)>1.96))))
    return out


def main():
    with (HERE/'source_table11_4_selected_rows.csv').open(newline='') as f: rows=[{k:float(v) for k,v in r.items()} for r in csv.DictReader(f)]
    long = interpolate(LAM_LONG_MM, [r for r in rows if r['lambda_mm']>0.5])
    short = interpolate(LAM_SHORT_MM, [r for r in rows if r['lambda_mm']<0.5])
    envelope=[marginal_screen(long,short,float(rho)) for rho in np.linspace(-1,1,401)]
    # Cauchy/triangle lower bound for template norm in the *same* projected-data
    # Hilbert space: ||T_l-T_s|| >= ||T_l|| - ||T_s||.
    # The published marginal errors alone do not validate that common space.
    sig_triangle=S/abs(1/long['sigma_alpha']-1/short['sigma_alpha'])
    force=[dict(r_mm=r,force_correction_alpha_one=force_ratio(r)) for r in [.052,.1,.2,.5,1,2,3]]
    stress=stress_tests()
    for filename,rows in [('recast_correlation_envelope.csv',envelope),('point_force_ratios.csv',force),('misspecification_stress_test.csv',stress)]:
        with (HERE/filename).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    result=dict(assumed_ell_m=ELL,assumed_mu_inv_m=MU,s=S,
                long_range_mm=LAM_LONG_MM,short_range_mm=LAM_SHORT_MM,
                published_marginal_interpolated_long=long,published_marginal_interpolated_short=short,
                conditional_sigma_upper_bound_triangle=sig_triangle,
                conditional_rho0=marginal_screen(long,short,0.),
                conditional_rho1=marginal_screen(long,short,1.),
                min_conditional_upper95=min(x['upper_95'] for x in envelope),
                max_conditional_upper95=max(x['upper_95'] for x in envelope),
                warning='NO official 95% confidence limit: assumes common linearized profiled nuisance likelihood; unknown actual covariance.',
                test_n_trials_per_scenario=3000,
                stress_tests=stress)
    (HERE/'adversarial_validation.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
    return result


if __name__=='__main__':main()
