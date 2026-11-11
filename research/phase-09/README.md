# ANDROMEDA-5 Phase 9 reproducibility pack

Status: secondary published-data study, not a discovery.

Run with Python 3, NumPy, SciPy and Matplotlib:

```bash
python phase9_public_data_screen.py
python phase9_integrated_evidence.py
python -m unittest -v test_phase9.py test_phase9_integrated.py
```

The 95-run dataset is provided directly in this repository. The standalone original transcription generator is not yet mirrored here. The dataset is a transcription of **corrected/calibrated published torques**, not primary raw time-series measurements. Check Appendix A.1 pages 147-150 of the cited Lee dissertation against the transcription before external re-publication. Published Table 11.4 single-Yukawa summaries are **marginal** fits; the conditional correlation sweep is **not** an experimental exclusion.

`PHASE9_EVIDENCE_REPORT.md` is the main technical report; PDF generated via Pandoc. `PUBLIC_RELEASE_STATEMENT.md` is the recommended cautious public wording. `REVIEWER_REQUEST.md` is an optional unsent message for experimental scientists.

Original scientific sources are linked in the report. This research pack's scripts and outputs are not peer-reviewed.