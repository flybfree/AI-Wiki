title: "Summary: 2026-06-26_17-31-34Z_BridgingAbInitioSymmetriesandGlobalNuclearMasseswi.md"
# Summary: 2026-06-26_17-31-34Z_BridgingAbInitioSymmetriesandGlobalNuclearMasseswi.md
Saved: 2026-06-28 21:01
Source: 2026-06-26_17-31-34Z_BridgingAbInitioSymmetriesandGlobalNuclearMasseswi.md
Model: None

---


## Summary  
The paper investigates whether the SU(4) and SU(3) symmetries of nuclear forces extend beyond individual nuclei to govern binding across the entire nuclear chart using interpretable neural networks. It constructs three symmetry‑based NN mass models—FINN, GINN, and WINN—that are trained on AME2016 data and validated on newer nuclei. The study demonstrates that Wigner’s SU(4) Casimir operators provide predictive power beyond bulk properties.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The SU(4) Casimir operator reduces RMSE by ~50 % compared to the liquid‑drop baseline, indicating its predictive relevance.  
- [Finding 2] WINN achieves the lowest validation RMSE (0.430 MeV), comparable to state‑of‑the‑art mass models.  
- [Finding 3] The quadratic SU(4) Casimir shows enhancement near the neutron dripline and a quartic operator appears in superheavy regions, suggesting emergent symmetry restoration.

## Methodology  
The authors employ feature‑informed neural networks that directly incorporate the Casimir operators of SU(4) and SU(3), using them as an interpretable basis for mass predictions. Models are trained on AME2016 dataset (ground‑state masses) and tested on AME2020 nuclei not previously modeled, with uncertainty quantified via GINN.

## Results  
The SU(4) operators alone cut RMSE by ~50 % on training data and ~20 % on test data relative to the liquid‑drop model. WINN reaches a validation RMSE of 0.430 MeV, the best among the three models. The quadratic Casimir exhibits a pronounced rise near the neutron dripline, while a quartic term dominates in superheavy nuclei.

## Significance  
These findings demonstrate that symmetry‑based neural networks can capture physics beyond empirical bulk parameters, offering interpretable insights into nuclear structure and the validity of Wigner’s SU(4) hypothesis across the entire chart. The results suggest that emergent symmetries may govern collective behavior rather than being isolated to individual nuclei.

## Related Concepts  
- Wigner’s SU(4) symmetry  
- Elliott’s SU(3) symmetry  
- Casimir operators (quadratic, quartic)  
- Neural network mass models (FINN, GINN, WINN)  
- AME2016 and AME2020 nuclear data sets
