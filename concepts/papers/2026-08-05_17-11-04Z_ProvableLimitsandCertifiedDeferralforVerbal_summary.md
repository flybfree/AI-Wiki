# Summary: 2026-08-05_17-11-04Z_ProvableLimitsandCertifiedDeferralforVerbalizedUnc.md
Saved: 2026-08-05 22:33
Source: 2026-08-05_17-11-04Z_ProvableLimitsandCertifiedDeferralforVerbalizedUnc.md
Model: None

---

## Summary  
The paper investigates whether the confidence scores that small language models (SLMs) verbalize can be used to certify when a model should defer to a human, thereby enabling safe and cost‑effective deployment. It provides theoretical limits on how different calibration techniques affect risk coverage and error detection, and it empirically evaluates eleven instruction‑tuned SLMs ranging from 0.5 B to 14 B parameters on ARC‑Challenge and TruthfulQA. The authors show that while certain methods like Platt scaling can achieve very low expected calibration error (ECE ≈ 0.02), others such as temperature scaling are often infeasible when confidence remains above one half despite accuracy dropping below it, and a Clopper‑Pearson procedure yields finite‑sample risk certificates under an i.i.d. deployment assumption. Overall, the work bridges provable uncertainty limits with practical certification for deferral decisions in small models.

## Key Contributions  
- **Finding 1:** Strictly monotone calibration preserves both the risk‑coverage frontier and the error‑detection AUROC, establishing a theoretical guarantee that calibrated confidence reflects true performance.  
- **Finding 2:** Temperature scaling cannot be used to calibrate models whose predicted confidence stays above one half while accuracy falls below it; eight of twenty‑two model‑task pairs empirically hit this infeasibility floor within one percentage point.  
- **Finding 3:** A Clopper‑Pearson procedure converts a calibration set into a finite‑sample risk certificate under the i.i.d. deployment assumption, providing a formal bound on uncertainty.

## Methodology  
The authors selected eleven instruction‑tuned SLMs (0.5 B–14 B parameters) and evaluated them locally with 25,168 predictions across ARC‑Challenge and TruthfulQA. They derived theoretical constraints on calibration methods: monotone scaling maintains risk coverage; temperature scaling is limited when confidence > ½ but accuracy < ½; and Clopper‑Pearson offers a finite‑sample certificate under i.i.d. assumptions. Empirically, they measured Expected Calibration Error (ECE) for Platt scaling, which achieved as low as 0.02, while temperature scaling was infeasible for many pairs. They also identified an answer‑ordering artifact in TruthfulQA’s multiple‑choice format and repaired it.

## Results  
Platt scaling reduced ECE to a minimum of 0.02 across the evaluated models. However, only three model‑task pairs met a certified autonomy threshold at a 20 % risk budget, and none succeeded at a stricter 10 % budget. Temperature scaling was infeasible for eight out of twenty‑two pairs within one percentage point of its theoretical bound. The Clopper‑Pearson certificate provided a formal risk bound that could be used to decide deferral.

## Significance  
These results establish provable limits on how small language models can safely verbalize uncertainty, turning confidence scores into actionable safety guarantees. By linking calibration theory with empirical performance, the work enables developers to certify when an SLM should hand off to a human, reducing costly errors and improving trust in private deployments.

## Related Concepts  
- Calibration (monotone, Platt scaling)  
- Expected Calibration Error (ECE)  
- Risk‑coverage frontier and AUROC  
- Temperature scaling constraints  
- Clopper‑Pearson finite‑sample risk certificates  
- i.i.d. deployment assumption  
- Confidence semantics for deferral decisions
