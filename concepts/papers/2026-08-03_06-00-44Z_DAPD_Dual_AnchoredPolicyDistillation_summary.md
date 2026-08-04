# Summary: 2026-08-03_06-00-44Z_DAPD_Dual_AnchoredPolicyDistillation.md
Saved: 2026-08-04 00:26
Source: 2026-08-03_06-00-44Z_DAPD_Dual_AnchoredPolicyDistillation.md
Model: None

---

## Summary  
On‑policy self distillation (OPSD) suffers from a “privilege illusion” where the student learns behavior tied to privileged teacher information that cannot be reproduced at inference time, harming performance. The authors identify an information asymmetry between the privileged teacher and the inference‑time student as the root cause. To resolve this, they introduce Dual‑Anchored Policy Distillation (DAPD), a unified framework with two levels of anchoring. DAPD aligns reference and rollout behavior along matched‑information paths while preserving correctness supervision.

## Key Contributions  
- Finding 1: The information asymmetry between the privileged teacher and the student at inference is identified as the root cause of privilege illusion in OPSD.  
- Finding 2: Dual‑Anchored Policy Distillation (DAPD) is proposed, introducing Dual‑Path Anchoring (DPA) and Dual‑Source Anchoring (DSA) to create two matched information paths that reduce reliance on privileged guidance.  
- Finding 3: Extensive experiments show DAPD significantly improves performance over OPSD across tasks, with gains of +2.00 points at Qwen3‑4B, persisting at +2.69 for 4B and +2.78 for 32B models.

## Methodology  
The authors address the asymmetry by constructing a dual‑anchored system: Dual‑Path Anchoring (DPA) creates a self‑conditioned bridge that aligns reference‑to‑rollout behavior along one matched path, while Dual‑Source Anchoring (DSA) applies these paths in both directions. This design ensures that privileged teacher guidance is mirrored without overfitting to it, and correctness supervision remains intact during rollout.

## Results  
On the Qwen3‑4B benchmark, DAPD outperforms OPSD by an average of +2.00 points across all tasks. The improvement scales: at 4B parameters the gain is +2.69 points, and at 32B parameters it reaches +2.78 points, demonstrating robustness to model size.

## Significance  
By mitigating privilege illusion, DAPD enables more reliable self‑distillation that does not overfit to privileged data, leading to higher-quality language models with fewer training resources. This is especially valuable for large‑scale models where preserving inference‑time generalization is critical.

## Related Concepts  
on‑policy self distillation (OPSD), privilege illusion, dual‑anchored policy distillation (DAPD), Dual‑Path Anchoring (DPA), Dual‑Source Anchoring (DSA), information asymmetry, reference‑to‑rollout alignment.
