# Summary: 2026-07-27_06-51-29Z_SuccessIsNotSelf_Explanatory_AuditingSuccessProven.md
Saved: 2026-07-27 22:54
Source: 2026-07-27_06-51-29Z_SuccessIsNotSelf_Explanatory_AuditingSuccessProven.md
Model: None

---

## Summary
The paper argues that a correct answer does not always reflect the reasoning behind an agent’s success; it may have been obtained simply by accessing the target value after evaluation changes. To uncover this hidden provenance, the authors introduce “missing evaluation object success” and audit it using three benchmark‑derived variants: CLEAN (retains original information), GOLD (makes the correct target available), and SHAM (preserves source structure but substitutes a matched incorrect value). Their joint QID‑clustered analysis on four surfaces reveals how score responses shift when target availability is altered, exposing behavioral dependencies that go beyond simple exposure cues. The study shows that success can persist even after the intended observation window has passed.

## Key Contributions
- Finding 1: A correct answer may conceal whether it resulted from reasoning or mere access to a value, introducing “missing evaluation object success.”  
- Finding 2: GOLD minus CLEAN and GOLD minus SHAM experiments quantify how score changes reflect target correctness versus source exposure.  
- Finding 3: Behavioral dependence can remain evident even when the observation unit no longer transfers high scores as a marker.

## Methodology
The authors construct four standardized evaluation surfaces (D0, D1, D2, D3) and apply three modified benchmark versions of CLEAN, GOLD, and SHAM. CLEAN preserves the original question‑answer pairs; GOLD replaces the target with the correct value; SHAM keeps the source structure but substitutes a matched incorrect value while preserving exposure opportunities. They then compare raw score differences between these variants (GOLD − CLEAN, GOLD − SHAM) and compute AUROC scores on QID‑clustered data to assess how much of the response variance is driven by target correctness versus source exposure.

## Results
In D0, GOLD exceeds SHAM by 19.1–25.9 percentage points, indicating that success follows the correct value when it is available. In D2, under distributed sufficiency and without coloc‑transfer as a high‑score marker, AUROC drops to 0.376 for GOLD − CLEAN and 0.142 for GOLD − SHAM, showing residual behavioral dependence beyond the probe’s intended observation window. A supported 5.0‑point CLEAN score gap compresses to a raw GOLD difference of –0.6 points without causing rank inversion.

## Significance
Understanding success provenance is crucial for trustworthy agent evaluation; it prevents over‑reliance on correctness alone and guides benchmark design that reports both outcome and the information state supporting it, thereby improving model comparison fairness.

## Related Concepts
- Success provenance  
- Evaluation object  
- CLEAN, GOLD, SHAM benchmarks  
- QID clustering  
- AUROC (Area Under ROC Curve)
