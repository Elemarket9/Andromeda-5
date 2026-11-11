import sys
import unittest
from pathlib import Path
import math, numpy as np
sys.path.insert(0,str(Path(__file__).parent))
from adversarial_recast import (S,A,B,LAM_LONG_MM,LAM_SHORT_MM,
 marginal_screen,force_ratio,design_from_csv,estimate_data_alpha,interpolate)

class TestRecast(unittest.TestCase):
 def test_poles(self):
  self.assertAlmostEqual(LAM_LONG_MM,0.9789063129307031,12)
  self.assertAlmostEqual(LAM_SHORT_MM,0.2043096436892199,12)
 def test_pole_inverse(self):
  ell = 1/math.sqrt(A*A+B*B)
  mu=A*B/math.sqrt(A*A+B*B)
  self.assertAlmostEqual(ell, 2e-4,12)
  self.assertAlmostEqual(mu,1000.,8)
 def test_positive_point_force(self):
  for mm in [.052,.1,.2,.5,1,2,3]: self.assertGreater(force_ratio(mm),0)
 def test_marginal_rho_independent_source(self):
  a=dict(alpha_hat=-.005768666566656741,sigma_alpha=.008049643296887914)
  b=dict(alpha_hat=-.0026094731414687505,sigma_alpha=.015476316257354525)
  self.assertAlmostEqual(marginal_screen(a,b,1)['sigma'],.015374095520882806,10)
  self.assertLess(marginal_screen(a,b,0)['sigma'],marginal_screen(a,b,1)['sigma'])
 def test_injection_present_and_identifiable_with_identical_noise(self):
  n,z,N,Y,sigma,X=design_from_csv()
  rng=np.random.default_rng(44)
  eps=rng.normal(size=len(n))*sigma
  nuisance=X@np.array([1.,0.,.25,-.15])+eps
  fit0=estimate_data_alpha(X,sigma,nuisance)
  fit05=estimate_data_alpha(X,sigma,nuisance+.5*Y)
  # Paired comparison verifies that alpha=0.5 is *actually* injected
  # and fitted; the original Phase10B random noises were not paired.
  self.assertAlmostEqual(fit05-fit0,.5,10)
 def test_source_rows(self):
  import csv
  
  with (Path(__file__).parent/'source_table11_4_selected_rows.csv').open() as f:
   rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),4)
  self.assertEqual({float(r['lambda_mm']) for r in rows},{.2,.22,.89,1.})

if __name__=='__main__':unittest.main()
