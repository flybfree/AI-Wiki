# Summary: 2026-07-23_09-43-46Z_Self_PoisoninginAdaptiveOut_of_DistributionDetecti.md
Saved: 2026-07-27 00:03
Source: 2026-07-23_09-43-46Z_Self_PoisoninginAdaptiveOut_of_DistributionDetecti.md
Model: None

---

## Summary  
The paper investigates test‑time adaptive out‑of‑distribution (OOD) detectors that maintain a memory bank of unlabelled samples and show how this adaptation can either remain benign or catastrophically poison the detector, depending on its evolution. By modelling the bank’s impurity as a generalized Pólya urn process, the authors derive an almost‑sure mean‑field limit whose slope acts as a reproduction number that determines whether poisoning occurs. They also introduce a certified label‑free admission gate that can halt adaptation and prevent collapse at any contamination rate while guaranteeing zero false positives.

## Semantic links
- [[concepts/papers/2026-07-13_21-13-46Z_Self_ImprovingAICodingAgentsThroughAccumula_summary.md|Summary: 2026-07-13_21-13-46Z_Self_ImprovingAICodingAgentsThroughAccumulatedBeha.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-08-04_12-26-58Z_Test_TimeAugmentationforTabular_to_ImageCla_summary.md|Summary: 2026-08-04_12-26-58Z_Test_TimeAugmentationforTabular_to_ImageClassifier.md]] — 3 title terms overlap; 14 summary/topic terms overlap; semantic match 0.09

## Key Contributions  
- [Finding 1] The adaptive memory bank follows an almost‑sure mean‑field limit governed by a reproduction number; below one it stays benign, above one it fully poisons the detector.  
- [Finding 2] A certified admission gate that reads only frozen reserve data can sever the feedback loop and eliminate the transition at every contamination rate, achieving label‑free zero false positives.  
- [Finding 3] The authors prove a two‑world impossibility theorem: drift and contamination are indistinguishable without labels, establishing a closed‑form power ceiling for any procedure.

## Methodology  
The authors treat the bank’s impurity as a generalized Pólya urn model, compute its mean‑field dynamics, and obtain the reproduction number that controls poisoning. They implement a static admission gate using only frozen reserve samples to cut off adaptation. Experimental evaluation is performed across 96 encoder families, with additional testing on drift‑affected cells using CDC (Certified Drift Correction) to restore nominal false‑positive rates.

## Results  
Empirical admission kernels exhibit R² ≥ 0.996 and a slope just below one for every encoder family, indicating the detector is near‑critical by design. Ungated dictionaries lose up to 0.163 AUROC. The certified gate preserves nominal label‑free FPR at all contamination rates, while CDC corrects static calibration failure under drift, restoring nominal FPR on all tested cells.

## Significance  
This work provides a complete possibility/impossibility characterization of label‑free adaptive OOD detection: it shows that the system is inherently near‑critical, that poisoning can be prevented with a simple certified gate, and that without labels one cannot distinguish drift from contamination. The results enable robust, label‑free detectors that are theoretically grounded and practically reliable.

## Related Concepts  
Adaptive out‑of‑distribution detection, Pólya urn model, mean‑field dynamics, reproduction number, certified calibration, admission gate, two‑world theorem, label‑free testing, drift correction (CDC).
