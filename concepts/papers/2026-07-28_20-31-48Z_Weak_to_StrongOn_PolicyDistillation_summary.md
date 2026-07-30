# Summary: 2026-07-28_20-31-48Z_Weak_to_StrongOn_PolicyDistillation.md
Saved: 2026-07-29 20:21
Source: 2026-07-28_20-31-48Z_Weak_to_StrongOn_PolicyDistillation.md
Model: None

---

## Summary  
On‑policy distillation (OPD) aims to align a student model’s token‑level distribution with that of a teacher, but existing methods require either a larger teacher model—unavailable at the frontier—or costly consolidation of multiple domain experts. Weak‑to‑Strong On‑Policy Distillation (W2S‑OPD) solves this by creating a proxy teacher from two weaker models whose logit difference isolates a specific capability direction. The student then distills this proxy, achieving improvements even when every supervision source is weaker than the original teacher. This approach enables strong students to surpass domain teachers across benchmarks without relying on expensive training.

## Key Contributions  
- [Finding 1] The logit‑space contrast between a positive and negative model isolates a capability direction, forming a proxy teacher that remains distributionally adjacent to the student.  
- [Finding 2] W2S‑OPD improves the strong student by distilling from multiple weak models, allowing it to surpass domain teachers on diverse tasks.  
- [Finding 3] Different contrast pairs (post‑RL vs pre‑RL, scale, hint) generate distinct signals: reasoning frameworks, solving procedures, and instance‑level direction.

## Methodology  
The authors construct a proxy teacher by computing the logit difference between two smaller models that are paired as positive and negative. This difference is added to the student’s base model, producing a teacher that captures the isolated capability while preserving distributional similarity. The student then performs on‑policy distillation by minimizing per‑token reverse KL divergence over its own rollouts, thereby aligning with the proxy teacher’s token distribution.

## Results  
Across four math and three code benchmarks, W2S‑OPD outperforms conventional OPD and enables the student to exceed the domain teacher’s performance. Moreover, the method continues to improve the student even when all supervision sources are weaker than the original teacher, demonstrating robustness across multiple contrast configurations.

## Significance  
This work decouples teacher strength from model size, allowing efficient capability transfer without training expensive large models or consolidating costly experts. By leveraging cheap weak proxies, it opens a pathway to stronger students that can surpass domain teachers, reducing reliance on high‑cost supervision and expanding the practicality of on‑policy distillation.

## Related Concepts  
- On‑policy distillation (OPD)  
- Proxy teacher  
- Logit‑space contrast  
- Reverse KL minimization  
- Multi‑contrast OPD  
- Domain teacher  
- Student model
