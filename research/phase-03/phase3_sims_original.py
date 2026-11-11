#!/usr/bin/env python3
"""Andromeda-5 Phase 3 simulations. Units: c = 1 unless stated. Requires numpy, scipy."""
import numpy as np
from scipy.signal import hilbert


# ---------------------------------------------------------------- SIM 1
def sim1_fast_light():
    """Gain-doublet 'fast light' medium: group velocity > c, front velocity = c."""
    dt, N = 0.002, 2**19
    t = (np.arange(N) - N // 4) * dt              # time axis, t=0 at index N/4
    w = 2 * np.pi * np.fft.fftfreq(N, dt)
    wc, Delta, gam, f, L = 200.0, 3.0, 1.0, -2.0, 10.0   # f<0 => gain
    n2 = np.ones(N, complex)
    for wj in (wc - Delta, wc + Delta):
        n2 += f / (wj**2 - w**2 + 1j * gam * w)   # causal for e^{+iwt} convention
    n = np.sqrt(n2)
    H = np.exp(-1j * w * n * L)

    def propagate(s):
        return np.fft.ifft(np.fft.fft(s) * H).real

    # (a) smooth pulse: where does the envelope peak arrive?
    tau, tp = 1.5, 20.0
    s = np.exp(-((t - tp) ** 2) / (2 * tau**2)) * np.cos(wc * t)
    out = propagate(s)
    env = np.abs(hilbert(out))
    t_peak = t[np.argmax(env)]
    ng_pred = 1 + f / (2 * Delta**2)
    print("SIM 1  fast-light gain doublet")
    print(f"  predicted group index n_g = {ng_pred:.3f} (v_g = {1/ng_pred:.2f} c)")
    print(f"  vacuum peak arrival      t = {tp + L:.3f}")
    print(f"  medium peak arrival      t = {t_peak:.3f}  (advance {tp + L - t_peak:.3f})")
    print(f"  peak amplitude gain        = {env.max():.2f}")

    # (b) same pulse switched on abruptly at t=0 (a new, non-analytic point)
    tp2 = 1.0
    s2 = np.exp(-((t - tp2) ** 2) / (2 * tau**2)) * np.cos(wc * t) * (t >= 0)
    out2 = propagate(s2)
    before = np.abs(out2[(t > -50) & (t < L - 2 * dt)]).max()
    after = np.abs(out2[(t >= L) & (t < L + 0.5)]).max()
    print(f"  switched pulse: max|E| before t=L/c : {before:.2e}")
    print(f"                  max|E| in first 0.5 after front: {after:.2e}")
    print(f"                  overall max: {np.abs(out2).max():.2e}")


# ---------------------------------------------------------------- SIM 2
def bump(x, R=1.0):
    y = np.zeros_like(x)
    m = np.abs(x) < R
    y[m] = np.exp(1 - 1 / (1 - (x[m] / R) ** 2))
    return y


def sim2_tachyon():
    """phi_tt = phi_xx + mu^2 phi (m^2<0). Does anything leave the light cone?"""
    print("SIM 2  tachyonic Klein-Gordon field (m^2 = -mu^2)")
    for mu2, label in ((+1.0, "tachyon  mu^2=+1"), (-1.0, "ordinary m^2=+1")):
        for dx in (0.02, 0.01, 0.005):
            dt, T, R = 0.5 * dx, 10.0, 1.0       # CFL 0.5: numerical cone is 2c wide
            x = np.arange(-30, 30, dx)
            p0 = bump(x, R)
            lap = lambda p: (np.roll(p, 1) - 2 * p + np.roll(p, -1)) / dx**2
            p1 = p0 + 0.5 * dt**2 * (lap(p0) + mu2 * p0)   # zero initial velocity
            steps = int(round(T / dt))
            for _ in range(steps - 1):
                p0, p1 = p1, 2 * p1 - p0 + dt**2 * (lap(p1) + mu2 * p1)
            outside = np.abs(p1[np.abs(x) > R + T + 0.25]).max()
            print(f"  {label}  dx={dx:<6} max inside={np.abs(p1).max():.3e} "
                  f"max outside cone={outside:.3e} ratio={outside/np.abs(p1).max():.1e}")
    k = 1.2
    print(f"  (plane-wave group velocity at k=1.2mu: {k/np.sqrt(k*k-1):.2f} c - yet nothing leaves the cone)")


# ---------------------------------------------------------------- SIM 3
def sim3_superluminal_dispersion():
    """omega^2 = k^2 (1 + l^2 k^2): Lorentz-violating, preferred frame. Exact spectral evolution."""
    print("SIM 3  quartic (superluminal) dispersion  w^2 = k^2 + l^2 k^4")
    Lbox, N, R, T = 800.0, 2**16, 1.0, 10.0
    x = (np.arange(N) - N // 2) * (Lbox / N)
    k = 2 * np.pi * np.fft.fftfreq(N, Lbox / N)
    p0 = bump(x, R)
    for l in (0.0, 0.01, 0.05, 0.2):
        wk = np.abs(k) * np.sqrt(1 + (l * k) ** 2)
        p = np.fft.ifft(np.fft.fft(p0) * np.cos(wk * T)).real
        outside = np.abs(p[np.abs(x) > R + T + 0.25]).max()
        print(f"  l={l:<5} max|phi| outside light cone at t={T}: {outside:.3e}")
    # wave-packet group advance
    l, k0, sig, T = 0.05, 5.0, 4.0, 50.0
    wk = np.abs(k) * np.sqrt(1 + (l * k) ** 2)
    a0 = np.exp(-x**2 / (2 * sig**2)) * np.exp(1j * k0 * x)
    a = np.fft.ifft(np.fft.fft(a0) * np.exp(-1j * np.sign(k) * wk * T))
    cen = np.sum(x * np.abs(a) ** 2) / np.sum(np.abs(a) ** 2)
    vg = (1 + 2 * (l * k0) ** 2) / np.sqrt(1 + (l * k0) ** 2)
    print(f"  packet k0={k0}, l={l}: centroid at t={T} is x={cen:.3f}; "
          f"predicted v_g*t={vg*T:.3f}; light would be at {T:.1f}")


# ---------------------------------------------------------------- SIM 4
def sim4_numbers():
    print("SIM 4  magnitudes (SI)")
    alpha, lamC, c = 7.2973525693e-3, 3.8615926796e-13, 2.99792458e8
    hbarc_eVm, Epl_eV = 1.973269804e-7, 1.220890e28
    coef = 11 * np.pi**2 / 8100 * alpha**2
    print(f"  Scharnhorst coefficient 11 pi^2 alpha^2/8100 = {coef:.4e}")
    for a in (1e-5, 1e-6, 1e-7, 1e-8, 1e-9):
        d = coef * (lamC / a) ** 4
        print(f"   gap a={a:.0e} m: dc/c={d:.2e}  time gained across gap={a*d/c:.2e} s")
    for target in (1e-18, 1e-21):
        a = lamC * (coef / target) ** 0.25
        print(f"   gap needed for dc/c={target:.0e}: a={a:.2e} m")
    # general light-cone formula check: dv = -(11/45) alpha^2 T_kk / m^4, Casimir T_kk=-pi^2/(180 a^4)
    print(f"   check via T_kk formula: coefficient = {11/45*np.pi**2/180*alpha**2:.4e}")
    # Lorentz-violating dispersion, superluminal branch
    E1, E2 = 6.2 * Epl_eV, 4.6e-8 * Epl_eV      # LHAASO GRB 221009A time-of-flight limits
    print(f"  LIV scales: E_QG1 > {E1:.2e} eV, E_QG2 > {E2:.2e} eV "
          f"(length l2 < {hbarc_eVm/E2:.2e} m)")
    for E, name in ((1.0, "1 eV optical"), (1e4, "10 keV X-ray"), (1e12, "1 TeV"), (1e15, "1 PeV")):
        print(f"   {name:13s}: max dv/c linear={E/E1:.1e}  quadratic={1.5*(E/E2)**2:.1e}")
    D = 0.151 * c / 2.2e-18 / c                 # crude light-travel time z/H0 (s), H0=68 km/s/Mpc
    print(f"   GRB 221009A (z=0.151) travel time ~{D:.1e} s; 1 TeV linear-LIV lag at limit ~{1e12/E1*D:.2f} s")
    # experiment sensitivities
    for name, dt_res, base in (("optical vs X-ray ToF, 10 fs over 1 km", 1e-14, 1e3),
                               ("LSW early-arrival, 10 ps over 100 m", 1e-11, 1e2),
                               ("LSW early-arrival, 1 ns over 100 m", 1e-9, 1e2)):
        print(f"   {name}: dv/c sensitivity = {dt_res*c/base:.1e}")
    # coupling-constraint trade-off for a hidden superluminal species
    for bound in (1e-15, 1e-18):
        print(f"   hidden species: g^2 * (dc/c)_hidden < ~{bound*16*np.pi**2:.1e} if SM speeds fixed to {bound:.0e}")


if __name__ == "__main__":
    sim1_fast_light(); print()
    sim2_tachyon(); print()
    sim3_superluminal_dispersion(); print()
    sim4_numbers()