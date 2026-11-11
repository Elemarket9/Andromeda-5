# ANDROMEDA-5 Phase 5 reproducible research pack

The simulations continue the **user-supplied** `phase3_sims.py` and the Phase 4 source–receiver calculation. They **postulate**, rather than discover, a field with higher spatial derivatives. Nothing here is a real FTL transmission experiment.

Run:

```sh
python -m pip install -r requirements.txt
python phase5_coupled_field.py
python phase5_adversarial.py
```

Main files:
- `PHASE5_RESEARCH_REPORT.md`: derivation, tests, constraints, novelty and next research gates.
- `phase5_coupled_field.py`: fully coupled Hamiltonian field + detector; exact free spectral step and symmetric coupling kicks.
- `phase5_adversarial.py`: UV sensitivity, weak-coupling scaling, time refinement, fifth-force static shape and causality toy example.
- `coupled_detector_results.csv`, `uv_sensitivity.csv`, `time_convergence.csv`, `coupling_sensitivity.csv`, `static_fifth_force_kernel.csv`, `causality_example.csv`: numerical outputs.
- `phase5_detector_response.png`, `phase5_uv_sensitivity.png`: plots.
- `INITIAL_FAILED_CONVERGENCE_LOG.txt`: first method's *failed* spatial convergence check, retained rather than hidden.
- `run_log.txt`, `adversarial_log.txt`: executed stdout.

## Reproducibility statement

The output is deterministic and uses normalized artificial units. Values of `ell`, mass gap, detector coupling and UV scale are research inputs. No physical scalar, transmitter or detector has been observed. The code does not validate quantum or relativistic consistency beyond the checks explicitly stated.