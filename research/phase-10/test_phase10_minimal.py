#!/usr/bin/env python3
"""Phase 10 numerical smoke tests; not experimental validation."""
import unittest
import numpy as np
from phase10_minimal_repro import poles, potential, torque, synthetic_fit

class NumericalSmokeTests(unittest.TestCase):
    def test_pole_scales(self):
        a,b,s=poles()
        self.assertAlmostEqual(1000/a,0.9789063129307032,places=10)
        self.assertAlmostEqual(1000/b,0.20430964368921992,places=10)
    def test_potential_torque_derivative(self):
        rd=np.array([.002,.001,0.]);rs=np.array([-.001,.003,.00012])
        h=1e-5
        def rotate(t):
            return np.array([rd[0]*np.cos(t)-rd[1]*np.sin(t),
                             rd[0]*np.sin(t)+rd[1]*np.cos(t),rd[2]])
        check=-(potential(rotate(h),rs,.002,.003,.09)-potential(rotate(-h),rs,.002,.003,.09))/(2*h)
        result=torque(rd,rs,.002,.003,.09)
        self.assertLess(abs(check-result)/abs(result),1e-7)
    def test_toy_detection_null(self):
        sd,condition,mc=synthetic_fit(ntrials=2000)
        self.assertAlmostEqual(sd,0.2914216258057534,places=10)
        self.assertLess(condition,150)
        self.assertLess(abs(mc['0.0']['detection_rate_abs_z_gt_1p96']-.05),.02)
        self.assertGreater(mc['1.0']['detection_rate_abs_z_gt_1p96'],.85)

if __name__=='__main__':
    unittest.main()
