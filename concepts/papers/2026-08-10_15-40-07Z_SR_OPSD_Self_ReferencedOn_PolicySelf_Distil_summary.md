# Summary: 2026-08-10_15-40-07Z_SR_OPSD_Self_ReferencedOn_PolicySelf_Distillation.md
Saved: 2026-08-10 23:53
Source: 2026-08-10_15-40-07Z_SR_OPSD_Self_ReferencedOn_PolicySelf_Distillation.md
Model: None

---

## Summary  
The paper proposes SR‑OPSD, a self‑referenced on‑policy self‑distillation method that improves the original OPSD by using a geometric interpolation between the student policy and a reference policy conditioned on fixed token contexts. It separates where the adaptive target is placed from how the student is projected toward it, enabling stable token‑level supervision for reinforcement learning with sparse rewards. The approach is applied across scientific evaluation, mathematical reasoning, and coding generation tasks.

## Key Contributions  
- [Finding 1] Introduces self‑referenced OPSD where the distillation target is a geometric interpolation between the student policy and a reference policy at fixed contexts.  
- [Finding 2] Uses the Rényi divergence family to parameterize projection geometry, allowing flexible sensitivity to token‑level density ratios.  
- [Finding 3] Demonstrates state‑of‑the‑art or competitive performance across multiple large language models in diverse tasks.

## Methodology  
The authors model the effective distillation target as a point on the line segment connecting the self‑teacher policy and the reference policy for each fixed student context. By variational analysis they derive that this interpolation is a convex combination whose coefficient α reflects token density. The Rényi divergence of order λ > 1 defines the projection geometry, making the sensitivity to density ratios adjustable while keeping the target location fixed.

## Results  
Experiments show SR‑OPSD outperforms baseline OPSD and other distillation methods in scientific evaluation (e.g., PubMed QA), mathematical reasoning (e.g., theorem proving), and coding generation (e.g., Python code). Performance gains are consistent across models, with up to 12 % improvement in accuracy compared to prior work.

## Significance  
By decoupling target placement from projection sensitivity, SR‑OPSD offers a more stable and generalizable self‑distillation framework that can be applied broadly without fine‑tuning per task. It mitigates distributional concentration and provides dense supervision where reward signals are sparse, thereby enhancing learning efficiency.

## Related Concepts  
On‑policy self‑distillation (OPSD), reference policies, geometric interpolation, Rényi divergence, token‑level supervision, variational analysis, KL minimization.
