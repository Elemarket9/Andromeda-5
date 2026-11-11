import unittest
import math
import numpy as np
from phase9_public_data_screen import poles, interp_loglam, ROWS, conditional_combination

class Phase9Tests(unittest.TestCase):
    def test_poles(self):
        a, b, s = poles()
        self.assertAlmostEqual(1000/a, .978906, places=5)
        self.assertAlmostEqual(1000/b, .204310, places=5)
        self.assertAlmostEqual(s, math.sqrt(.84), places=12)

    def test_source_interpolation(self):
        x = interp_loglam(.2, ROWS[0], ROWS[1])
        self.assertAlmostEqual(x["alpha_hat"], -.00235, places=12)
        x = interp_loglam(1.0, ROWS[2], ROWS[3])
        self.assertAlmostEqual(x["sigma_alpha"], .00796, places=12)

    def test_max_z_under_unknown_rho(self):
        a, b, s = poles()
        lon = interp_loglam(1000/a, ROWS[2], ROWS[3])
        short = interp_loglam(1000/b, ROWS[0], ROWS[1])
        zmax = conditional_combination(lon, short, 1.0, s)["abs_z_proxy"]
        self.assertLess(zmax, 1.5)
        for rho in np.linspace(-1, 1, 41):
            r = conditional_combination(lon, short, float(rho), s)
            self.assertTrue(r["normal_95_lower"] < 0 < r["normal_95_upper"])
            self.assertLessEqual(r["abs_z_proxy"], zmax + 1e-12)

    def test_linear_model_identity(self):
        rng = np.random.default_rng(2026)
        for rho in (-.7, 0, .6, .95):
            s1, s2 = .008, .015
            n = 1000
            u = rng.normal(size=n); u = u / np.linalg.norm(u)
            v = rng.normal(size=n); v = v-u*np.dot(u, v); v = v/np.linalg.norm(v)
            t1 = u/s1
            t2 = (rho*u + math.sqrt(1-rho**2)*v)/s2
            ah1, ah2 = -.005, -.002
            A = np.array([[np.dot(t1, t1), np.dot(t1, t2)],
                          [np.dot(t1, t2), np.dot(t2, t2)]])
            vec = np.linalg.solve(A, np.array([ah1/s1**2, ah2/s2**2]))
            residual = vec[0]*t1 + vec[1]*t2
            factor = .916515138991168
            template = (t1-t2)/factor
            manual = np.dot(template, residual)/np.dot(template, template)
            calc = conditional_combination(
                {"alpha_hat": ah1, "sigma_alpha": s1},
                {"alpha_hat": ah2, "sigma_alpha": s2}, rho, factor
            )
            self.assertAlmostEqual(manual, calc["alpha_hat_two_pole"], places=9)

if __name__ == "__main__":
    unittest.main(verbosity=2)
