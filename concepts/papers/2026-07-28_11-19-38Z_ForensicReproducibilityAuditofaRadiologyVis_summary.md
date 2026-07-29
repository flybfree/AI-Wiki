# Summary: 2026-07-28_11-19-38Z_ForensicReproducibilityAuditofaRadiologyVision_Lan.md
Saved: 2026-07-28 22:43
Source: 2026-07-28_11-19-38Z_ForensicReproducibilityAuditofaRadiologyVision_Lan.md
Model: None

---

## Summary  
The paper conducts a forensic reproducibility audit of a radiology vision‑language model benchmark, tracing the journey from an intended protocol to the released artifacts without invoking the model or generating new data. It reveals systematic deviations—such as missing polarity inversion, truncated reports, and lost dataset metadata—that compromise the integrity of reported performance metrics and clinical claims. By reconstructing a cohort of 369 case‑finding blocks and comparing archived outputs with original specifications, the authors expose gaps that invalidate many statistical tests and ranking statements.

## Key Contributions  
- The audit identifies 27 McNemar comparisons with unadjusted p < 0.05, showing that many significance claims are misleading when not corrected.  
- Reconstruction of a cohort of 369 case‑finding blocks changes Cochran’s Q from 154.73 to 182.29, demonstrating that reported statistical tests lose validity due to truncated or altered artifacts.  
- The study withdraws all original performance rankings, prompt‑effect claims, and clinical assertions, advocating for machine‑verifiable controls instead.

## Methodology  
The authors performed a retrospective audit without calling the model or creating new data. They examined 300 planned model‑prompt calls, recorded 297 nonempty reports, and traced prompt bindings, DICOM metadata, rendering steps, label extraction, annotation provenance, and release propagation to pinpoint procedural deviations.

## Results  
Of the 45 McNemar comparisons, 27 had unadjusted p < 0.05; after Holm adjustment only 20 remained significant. The Cochran’s Q statistic altered upon reconstruction (154.73 → 182.29). Four MONOCHROME1 images were rendered without required polarity inversion, and dataset split membership was lost. Five reports were truncated to 4000 characters.

## Significance  
This work underscores the fragility of AI benchmark reproducibility in medical imaging, where small procedural errors cascade into invalid performance claims. It calls for standardized verification protocols and machine‑checked pipelines to ensure trustworthy results.

## Related Concepts  
Forensic audit, reproducibility, Cochran’s Q, McNemar test, DICOM rendering, vision‑language models, benchmark integrity, automated labeling, statistical significance adjustment.
