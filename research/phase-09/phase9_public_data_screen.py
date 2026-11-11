#!/usr/bin/env python3
"""ANDROMEDA-5 Phase 9: conditional empirical-screen calculations.

USES REAL, PUBLISHED *SINGLE-YUKAWA FIT SUMMARIES* from Table 11.4 of
John G. Lee's 2020 dissertation. The two-pole inference is NOT an official
experimental limit: joint covariance, torque geometry and common-profile
likelihood are not available in this calculation.

No claimed new force or faster-than-light observation.
"""
from __future__ import annotations
import csv
import json
import math
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).resolve().parent
ROWS = [
    {"lambda_mm": 0.200, "alpha_hat": -0.00235, "sigma_alpha": 0.0157},
    {"lambda_mm": 0.220, "alpha_hat": -0.00351, "sigma_alpha": 0.0147},
    {"lambda_mm": 0.890, "alpha_hat": -0.00612, "sigma_alpha": 0.00845},
    {"lambda_mm": 1.000, "alpha_hat": -0.00569, "sigma_alpha": 0.00796},
]
ELL = 2e-4  # assumed benchmark, metres
MU = 1000.0  # assumed benchmark, inverse metres

def write_csv(filename, rows):
    rows = list(rows)
    with open(HERE / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def poles(ell=ELL, mu=MU):
    s = math.sqrt(1 - 4 * ell**2 * mu**2)
    a = math.sqrt((1 - s) / (2 * ell**2))
    b = math.sqrt((1 + s) / (2 * ell**2))
    return a, b, s

def interp_loglam(x, r0, r1):
    p = (math.log(x) - math.log(r0["lambda_mm"])) / (
        math.log(r1["lambda_mm"]) - math.log(r0["lambda_mm"])
    )
    return {
        "lambda_mm": x,
        "alpha_hat": (1 - p) * r0["alpha_hat"] + p * r1["alpha_hat"],
        "sigma_alpha": (1 - p) * r0["sigma_alpha"] + p * r1["sigma_alpha"],
    }

def conditional_combination(r1, r2, rho, s):
    """Sensitivity illustration under an ASSUMED shared Gaussian model."""
    a, sa = r1["alpha_hat"], r1["sigma_alpha"]
    b, sb = r2["alpha_hat"], r2["sigma_alpha"]
    dot = a / sa**2 - b / sb**2
    norm = 1 / sa**2 + 1 / sb**2 - 2 * rho / (sa * sb)
    if norm <= 0:
        raise ValueError("Degenerate assumed covariance")
    alpha = s * dot / norm
    sig = s / math.sqrt(norm)
    z = abs(dot) / math.sqrt(norm)
    return {
        "rho": rho,
        "alpha_hat_two_pole": alpha,
        "sigma_two_pole": sig,
        "normal_95_lower": alpha - 1.96 * sig,
        "normal_95_upper": alpha + 1.96 * sig,
        "abs_z_proxy": z,
    }

def main():
    a, b, s = poles()
    long = interp_loglam(1000 / a, ROWS[2], ROWS[3])
    short = interp_loglam(1000 / b, ROWS[0], ROWS[1])
    allrows = [
        conditional_combination(long, short, float(rho), s)
        for rho in np.linspace(-1, 1, 401)
    ]
    write_csv("source_table11_4_selected_rows.csv", ROWS)
    write_csv("conditional_correlation_sweep.csv", allrows)
    write_csv("interpolated_component_summaries.csv", [
        {"component": "long", **long}, {"component": "short", **short}
    ])
    neighbors = []
    for ra in ROWS[2:]:
        for rb in ROWS[:2]:
            z = conditional_combination(ra, rb, 1.0, s)["abs_z_proxy"]
            neighbors.append({
                "long_lambda_mm": ra["lambda_mm"],
                "short_lambda_mm": rb["lambda_mm"],
                "upper_abs_z_conditional": z
            })
    write_csv("neighbor_bracketing_robustness.csv", neighbors)
    v = np.asarray([
        [r["rho"], r["alpha_hat_two_pole"], r["normal_95_lower"],
         r["normal_95_upper"], r["abs_z_proxy"]]
        for r in allrows
    ])
    fig, axes = plt.subplots(2, 1, figsize=(9.1, 7.0), sharex=True)
    axes[0].fill_between(v[:, 0], v[:, 2], v[:, 3],
                         color="#cbd5e1", label="Assumed 95% interval")
    axes[0].plot(v[:, 0], v[:, 1], label="Conditional amplitude")
    axes[0].axhline(0, color="gray", ls="--")
    axes[0].legend()
    axes[1].plot(v[:, 0], v[:, 4], label="|z| sensitivity proxy")
    axes[1].axhline(1.96, color="gray", ls="--")
    axes[1].set(xlabel="Assumed correlation", ylabel="Proxy significance")
    axes[1].legend()
    fig.tight_layout()
    fig.savefig(HERE / "phase9_correlation_envelope.png", dpi=170)
    plt.close(fig)
    summary = {
        "source": "Lee 2020 dissertation, Table 11.4",
        "evidence_class": "Published marginal fit summaries + conditional model",
        "ell_m_assumed": ELL,
        "mu_inv_m_assumed": MU,
        "long_lambda_mm": 1000/a,
        "short_lambda_mm": 1000/b,
        "max_abs_z_conditional": float(v[:, 4].max()),
        "interpretation": "Not a measured joint likelihood or experimental exclusion",
    }
    (HERE / "phase9_validation.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
