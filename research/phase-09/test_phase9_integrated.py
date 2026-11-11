import csv
import unittest
from pathlib import Path
from scipy.stats import chi2
from phase9_public_data_screen import poles, conditional_combination, ROWS, interp_loglam

ROOT = Path(__file__).resolve().parent

class TestPhase9(unittest.TestCase):
    def setUp(self):
        with (ROOT / "lee2020_dissertation_appendix_A1_transcribed.csv").open() as f:
            self.rows = list(csv.DictReader(f))

    def test_count_95(self):
        self.assertEqual(len(self.rows), 95)
        self.assertEqual(len({r["run"] for r in self.rows}), 95)

    def test_anchor_rows(self):
        d = {r["run"]: r for r in self.rows}
        self.assertAlmostEqual(float(d["run6276"]["torque_120_fNm"]), .808)
        self.assertAlmostEqual(float(d["run6991"]["torque_120_fNm"]), 1.4653)
        self.assertAlmostEqual(float(d["run6725"]["separation_um"]), 1521.5)

    def test_positive_uncertainties(self):
        for row in self.rows:
            for col in ("separation_sigma_um", "sigma_120_fNm", "sigma_18_fNm", "sigma_54_fNm"):
                self.assertGreater(float(row[col]), 0)

    def test_published_newtonian_p(self):
        self.assertAlmostEqual(chi2.sf(274.99, 285), .65404842445, places=8)

    def test_interpolated_poles(self):
        a, b, s = poles()
        self.assertAlmostEqual(1000/a, .9789063129307, places=8)
        self.assertAlmostEqual(1000/b, .2043096436892, places=8)

    def test_all_conditional_z_below_1p96(self):
        a, b, s = poles()
        lon = interp_loglam(1000/a, ROWS[2], ROWS[3])
        short = interp_loglam(1000/b, ROWS[0], ROWS[1])
        for rho in (-.95, -.5, 0, .5, .9, .95):
            self.assertLess(conditional_combination(lon, short, rho, s)["abs_z_proxy"], 1.96)

if __name__ == "__main__":
    unittest.main(verbosity=2)
