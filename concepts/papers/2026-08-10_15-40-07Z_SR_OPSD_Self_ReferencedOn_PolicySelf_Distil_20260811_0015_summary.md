# Summary: 2026-08-10_15-40-07Z_SR_OPSD_Self_ReferencedOn_PolicySelf_Distillation.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-40-07Z_SR_OPSD_Self_ReferencedOn_PolicySelf_Distillation.md
Model: None

---

## Summary  
Self‑referenced on‑policy self‑distillation (SR‑OPSD) is introduced as a refinement of existing OPSD methods that suffer from instability when the self‑teacher policy co‑evolves with its context distribution. The paper proposes a token‑level variational characterization that treats the effective distillation target as a geometric interpolation between the self‑teacher and a reference policy, while using the Rényi divergence family to control how strongly the student is projected toward this target. This formulation separates *where* the adaptive target resides from *how* the projection is performed, enabling more stable optimization across diverse token‑level density ratios.

## Key Contributions  
- **Adaptive target placement**: The effective distillation target is defined as a geometric interpolation between the self‑teacher policy and a reference policy, with an interpolation coefficient that fixes the location of the target for a given student context.  
- **Rényi‑controlled projection geometry**: A Rényi order parameter governs the sensitivity of the projection to token‑level density ratios, allowing the method to adapt without retraining the projection mechanism.  
- **Variational characterization**: The paper derives a variational model for the distillation target that isolates the interpolation coefficient from the projection geometry, clarifying why OPSD can become unstable.

## Methodology  
The authors fix student‑generated contexts and treat token‑level supervision as a variational problem. For each context they compute an effective teacher policy \( \pi_{\text{eff}} = (1-\alpha)\pi_{\text{ref}} + \alpha\pi_{\text{self}} \), where the interpolation coefficient \(\alpha\) is determined by the Rényi order of the divergence used to compare token densities. The student policy is projected toward this effective teacher via a KL‑style loss that depends on the Rényi order, ensuring that changes in density ratios are handled smoothly.

## Results  
Extensive experiments across scientific evaluation, mathematical reasoning, and coding generation tasks with multiple large language models demonstrate that SR‑OPSD attains state‑of‑the‑art or competitive performance. The method consistently outperforms baseline OPSD variants on perplexity, accuracy, and code correctness metrics, showing robustness to varying token‑level densities without additional hyper‑parameter tuning.

## Significance  
By decoupling the placement of the adaptive target from the projection geometry, SR‑OPSD mitigates the instability inherent in traditional OPSD. This separation enables generalization across new contexts and improves robustness for large language models, making self‑distillation a more reliable training signal in reinforcement learning pipelines.

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Self‑teacher policy  
- Rényi divergence family  
- Variational inference  
- Geometric interpolation  
- Token‑level supervision
