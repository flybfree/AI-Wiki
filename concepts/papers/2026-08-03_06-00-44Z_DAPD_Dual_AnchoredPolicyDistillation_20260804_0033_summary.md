# Summary: 2026-08-03_06-00-44Z_DAPD_Dual_AnchoredPolicyDistillation.md
Saved: 2026-08-04 00:33
Source: 2026-08-03_06-00-44Z_DAPD_Dual_AnchoredPolicyDistillation.md
Model: None

---

## Summary  
The paper tackles the “privilege illusion” that arises in on‑policy policy distillation (OPSD), where a student model learns to mimic a teacher using privileged training information but cannot generalize to inference‑time contexts, ultimately harming performance. To resolve this, DAPD introduces Dual‑Anchored Policy Distillation—a unified framework with two complementary anchoring mechanisms—so the student can be trained without relying on that privileged data at inference time.  

## Key Contributions  
- Identifies an information asymmetry between the teacher and the student at inference as the root cause of privilege illusion in OPSD.  
- Proposes Dual‑Anchored Policy Distillation (DAPD) comprising Dual‑Path Anchoring (DPA) that creates a self‑conditioned bridge aligning reference and rollout behavior, and Dual‑Source Anchoring (DSA) that applies these paths bidirectionally to reduce privileged guidance while preserving supervision.  
- Demonstrates consistent performance gains across model scales, outperforming OPSD on Qwen3‑4B by +2.00 points, reaching +2.69 at 4 B and +2.78 at 32 B.  

## Methodology  
The authors address the asymmetry by constructing two matched‑information paths: DPA generates a self‑conditioned bridge that forces the reference policy’s output to match the rollout policy’s behavior, thereby preventing privileged knowledge from leaking into the student’s inference model; DSA mirrors this alignment in the opposite direction (rollout‑to‑reference) so the supervision remains useful without explicit privileged references. The dual‑anchored scheme is then applied during distillation, producing a student that learns from both paths while being conditioned on its own rollout outputs, thus decoupling performance from privileged data.  

## Results  
Across a suite of downstream tasks, DAPD consistently improves Qwen3‑4B by an average of +2.00 points compared with the baseline OPSD method. The gains scale predictably: on 4 B parameters the improvement reaches +2.69 points, and at 32 B it reaches +2.78 points, indicating that DAPD’s architecture benefits from larger model capacity without sacrificing generalization.  

## Significance  
By eliminating reliance on privileged teacher information during inference, DAPD mitigates the privilege illusion that plagues OPSD, leading to more robust and generalizable policy distillation. The method is scalable across model sizes, offering a practical path toward higher‑quality language models without sacrificing privacy or data efficiency.  

## Related Concepts  
- On‑policy policy distillation (OPSD)  
- Privilege illusion  
- Dual‑anchored training  
- Self‑conditioned bridging (DPA)  
- Reference‑rollout alignment  
- Inference‑time generalization
