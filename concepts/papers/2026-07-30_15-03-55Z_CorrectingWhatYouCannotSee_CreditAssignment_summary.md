# Summary: 2026-07-30_15-03-55Z_CorrectingWhatYouCannotSee_CreditAssignmentforPerc.md
Saved: 2026-07-30 20:39
Source: 2026-07-30_15-03-55Z_CorrectingWhatYouCannotSee_CreditAssignmentforPerc.md
Model: None

---

## Summary  
The paper tackles a longstanding challenge in multimodal reasoning: how to distill teacher‑student knowledge when the student’s answer fails because of an incorrect perception rather than faulty reasoning. On‑policy distillation normally relies on trajectory‑level rewards, which cannot distinguish between perceptual errors and downstream logical mistakes, leading to ambiguous Perception Success Rates (PSR). The authors propose a label‑free correction mechanism that uses teacher–student disagreement and downstream failure signals as complementary witnesses to identify when perception is the appropriate target for correction. Their method, called Perception‑Correction Distillation (PCD), combines these witnesses with a normalized bilinear gate that only activates when both are present. This approach improves performance on large multimodal models without altering their reasoning objectives.

## Key Contributions  
- [Finding 1] PCD introduces a soft AND gate formed by the product of two witness signals—teacher‑student disagreement and downstream failure evidence—to create a correction signal that vanishes if either witness is absent.  
- [Finding 2] The method proves, via Bayesian evidence combination theory, that multiplication is the unique normalized bilinear operation that satisfies the “vanish‑when‑either‑absent” property required for label‑free distillation.  
- [Finding 3] Empirically, PCD raises macro averages on eight benchmarks: 8B‑2B from 44.50 to 47.28 and 32B‑8B from 56.94 to 61.22, with ablations showing that removing either the correction or separated rollouts reduces held‑out scores by 2.22 and 0.88 points respectively.

## Methodology  
PCD operates on separated perception‑reasoning rollouts where each modality is processed independently before being combined in a mean‑preserving manner, leaving the reasoning loss unchanged. The teacher’s prediction provides one witness; downstream failure (e.g., incorrect output) supplies another. Their product acts as a soft AND gate that only contributes to the distillation signal when both witnesses are strong, effectively correcting perception errors without requiring explicit labels. This label‑free design preserves the original training dynamics while allowing the model to self‑correct misperceptions.

## Results  
Across eight multimodal reasoning benchmarks—including image‑text and video‑language tasks—the PCD method achieves a 2.78‑point improvement in macro average scores compared with OPD (On‑Policy Distillation). Ablation studies confirm that the correction component is essential: dropping only the separated rollouts reduces performance by 0.88 points, while removing both the correction and the separation drops it further by 2.22 points. The gains are consistent across model sizes, indicating robustness.

## Significance  
By decoupling perception from reasoning in distillation, PCD enables more reliable knowledge transfer that respects the true source of errors. This is crucial for large‑scale multimodal systems where perceptual failures can dominate loss signals, leading to suboptimal or unsafe outputs. The work provides a principled, label‑free framework that can be applied beyond vision‑language tasks.

## Related Concepts  
- Perception Success Rate (PSR)  
- On‑policy distillation  
- Soft AND gate  
- Bayesian evidence combination  
- Normalized bilinear operation  
- Separated perception‑reasoning rollouts  
- Mean‑preserving weights  
- Teacher–student disagreement  
- Downstream failure signals
