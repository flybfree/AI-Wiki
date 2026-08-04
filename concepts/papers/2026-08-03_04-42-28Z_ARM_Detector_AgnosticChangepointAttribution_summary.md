# Summary: 2026-08-03_04-42-28Z_ARM_Detector_AgnosticChangepointAttributionwithFin.md
Saved: 2026-08-04 00:26
Source: 2026-08-03_04-42-28Z_ARM_Detector_AgnosticChangepointAttributionwithFin.md
Model: None

---

## Summary  
The paper addresses the limitation of changepoint detection that only identifies when a change occurs but not which variables changed. ARM provides a detector‑agnostic attribution framework that certifies each coordinate’s label (location or scale) with finite‑sample error control. It yields valid per‑coordinate certificates, exact family‑wise error bounds via permutation, and false discovery rate guarantees even under high‑dimensional dependence. Simulations show ARM maintains nominal error while naive methods blow up.

## Key Contributions  
- [Finding 1] The introduction of ARM, a wrapper that accepts any changepoint detector and outputs per‑coordinate attribution with location or scale labels.  
- [Finding 2] Three finite‑sample guarantees: per‑coordinate validity under any detector; exact family‑wise error control via Westfall–Young joint permutation with Holm fallback; false discovery rate control via Benjamini–Yekutieli and e‑BH.  
- [Finding 3] Empirical demonstration that ARM preserves nominal error across dimensions, whereas naive per‑coordinate testing inflates error beyond 0.66.

## Methodology  
The authors treat each coordinate independently by ranking its split statistics using a max‑over‑splits statistic; this rank dominates the corresponding statistic at the estimated changepoint, making the certificate invariant to estimator accuracy. The wrapper then applies permutation and false discovery rate procedures that respect cross‑coordinate dependence.

## Results  
Theoretical guarantees are derived: per‑coordinate validity holds for any detector, joint permutation yields exact family‑wise error ≤ α with Holm fallback, and e‑BH controls FDR under arbitrary dependence. Simulations on five financial series around the 2008 crisis show ARM attributes a scale change to every asset class while excluding control variables; naive per‑coordinate testing would exceed 0.66 FWE as dimension grows.

## Significance  
ARM bridges the gap between detection and attribution, delivering interpretable, statistically sound certificates that are robust to heavy tails and high dimensions. This is crucial for finance, where precise variable identification matters, and for any field requiring reliable change‑point analysis with error control.

## Related Concepts  
- Changepoint detection  
- Attribution of coordinate changes  
- Max‑over‑splits rank statistics  
- Westfall–Young joint permutation  
- Holm sequential testing  
- Benjamini–Yekutieli FDR bound  
- e‑BH false discovery rate control
