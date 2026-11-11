#!/usr/bin/env python3
"""Phase 9: analyze published, calibrated Lee (2020) torque tables.

This is a descriptive secondary analysis, NOT a full two-pole exclusion,
NOT a detection of a new force, and NOT evidence of FTL signaling.
"""
from pathlib import Path
import csv
import json
import numpy as np
from scipy.stats import chi2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from phase9_public_data_screen import poles, ROWS, interp_loglam, conditional_combination

HERE = Path(__file__).resolve().parent

def load():
    with (HERE / "lee2020_dissertation_appendix_A1_transcribed.csv").open() as f:
        return list(csv.DictReader(f))

def wls(x, y, sigma, x0=69.0):
    xx = np.asarray(x) - x0
    X = np.column_stack([np.ones(len(xx)), xx])
    w = 1 / np.asarray(sigma)**2
    inv = np.linalg.inv((X.T * w) @ X)
    beta = inv @ ((X.T * w) @ np.asarray(y))
    residual = np.asarray(y) - X @ beta
    value = float(np.sum(w * residual**2))
    dof = len(xx) - 2
    return {
        "n": len(xx),
        "intercept_at_69_fNm": float(beta[0]),
        "intercept_stat_error_fNm": float(np.sqrt(inv[0, 0])),
        "slope_fNm_per_um": float(beta[1]),
        "chi2": value,
        "dof": dof,
        "chi2_dof": value / dof,
        "p_naive_independent": float(chi2.sf(value, dof)),
    }

def main():
    data = load()
    assert len(data) == 95
    runs = [r["run"] for r in data]
    assert len(set(runs)) == len(runs)
    sep = np.asarray([float(r["separation_um"]) for r in data])
    assert all(float(r["sigma_120_fNm"]) > 0 for r in data)
    pages = {p: sum(int(r["printed_page"]) == p for r in data)
             for p in (147, 148, 149, 150)}
    near = [r for r in data if 68 <= float(r["separation_um"]) <= 70.2]
    checks = {}
    for h in (120, 18, 54):
        y = [float(r[f"torque_{h}_fNm"]) for r in near]
        dy = [float(r[f"sigma_{h}_fNm"]) for r in near]
        checks[str(h)] = wls(
            [float(r["separation_um"]) for r in near], y, dy
        )
    a, b, delta = poles()
    long = interp_loglam(1000/a, ROWS[2], ROWS[3])
    short = interp_loglam(1000/b, ROWS[0], ROWS[1])
    rhogrid = np.linspace(-0.95, 0.95, 191)
    cond = [conditional_combination(long, short, float(rho), delta)
            for rho in rhogrid]
    summary = {
        "sample_count": len(data),
        "source": "Lee 2020 dissertation Appendix A.1, published corrected torques",
        "harmonics": [120, 18, 54],
        "torque_values_count": len(data) * 3,
        "page_row_counts": pages,
        "min_reported_separation_um": float(sep.min()),
        "max_reported_separation_um": float(sep.max()),
        "below_52um_runs": [r["run"] for r in data if float(r["separation_um"]) < 52],
        "local_repeatability": checks,
        "published_newtonian_chi2": 274.99,
        "published_newtonian_dof": 285,
        "published_newtonian_p": float(chi2.sf(274.99, 285)),
        "model_assumed_ell_m": 0.0002,
        "model_assumed_mu_per_m": 1000.0,
        "model_pole_long_mm": 1000/a,
        "model_pole_short_mm": 1000/b,
        "conditional_rho_sweep_min_abs_z": min(r["abs_z_proxy"] for r in cond),
        "conditional_rho_sweep_max_abs_z": max(r["abs_z_proxy"] for r in cond),
        "actual_two_pole_exclusion_computed": False,
        "raw_uncorrected_data_available": False,
        "source_table_needs_visual_row_verification": True,
        "claim": "No measured additional force or FTL signal",
    }
    (HERE / "phase9_integrated_validation.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    for ax, h in zip(axes, (120, 18, 54)):
        y = np.asarray([float(r[f"torque_{h}_fNm"]) for r in data])
        dy = np.asarray([float(r[f"sigma_{h}_fNm"]) for r in data])
        ax.errorbar(sep, y, yerr=dy, fmt="o", ms=3.2, lw=0.5, alpha=0.8)
        ax.set_ylabel(f"{h} omega torque (fN m)")
        ax.grid(alpha=0.2)
    axes[-1].set_xscale("log")
    axes[-1].set_xlabel("Separation (micrometres, log scale)")
    fig.suptitle("Lee 2020 published corrected Eot-Wash torque data")
    fig.tight_layout()
    fig.savefig(HERE / "phase9_published_torque_data.png", dpi=180)
    plt.close(fig)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
