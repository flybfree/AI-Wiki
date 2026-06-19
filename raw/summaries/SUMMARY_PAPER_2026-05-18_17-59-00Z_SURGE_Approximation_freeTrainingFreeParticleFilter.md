---

title: "Summary: SURGE: Approximation-free Training Free Particle Filter for Diffusion Surrogate"
url: http://arxiv.org/abs/2605.18745v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-18_17-59-00Z_SURGE_Approximation_freeTrainingFreeParticleFilter.md
generated_at: "2026-06-11 10:43"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces URGE, a derivative‑free inference‑time scaling algorithm for diffusion surrogates that improves sample quality without requiring score or gradient evaluations. By attaching simple multiplicative weights to simulated trajectories and periodically resampling, URGE achieves unbiased terminal distributions comparable to more complex methods. The approach is both simpler to implement and significantly outperforms existing guidance baselines on synthetic and real‑world tests.

## Key Takeaways
- URGE performs path‑wise importance reweighting via a Girsanov change of measure, avoiding the need for score or Hessian calculations.
- The algorithm establishes an equivalence between path‑wise and particle‑wise stochastic marginalization, ensuring that both schemes yield identical unbiased terminal laws.
- Empirically, URGE delivers higher generation quality while being fully gradient‑free and computationally lightweight.

## Context
Inference‑time guidance is a key technique to steer diffusion models toward task objectives, yet most implementations rely on repeated score or gradient evaluations that introduce bias and high cost. This work offers a clean alternative that relies only on resampling, aligning with the trend toward simpler, scalable inference methods in generative AI.

## Implications
Practitioners can adopt URGE to enhance diffusion model outputs without adding complex evaluation pipelines, reducing both development time and resource consumption. The method’s gradient‑free nature makes it suitable for deployment in production settings where computational constraints are tight.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.18745v1)
