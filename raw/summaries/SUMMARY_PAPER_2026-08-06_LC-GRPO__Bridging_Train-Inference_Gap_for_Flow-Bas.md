---
title: LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction
url: http://arxiv.org/abs/2608.05600v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_04-47-57Z_LC_GRPO_BridgingTrain_InferenceGapforFlow_BasedGRP.md
generated_at: 2026-08-06 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LC‑GRPO, a flow‑based GRPO method that aligns training rollouts with test‑time inference by adding a single Langevin correction step after an ODE Euler update. The authors demonstrate that this correction reduces the mismatch between stochastic training samples and deterministic ODE outputs, leading to higher reward optimization on text‑to‑image and text‑to‑video benchmarks while preserving generation quality.

## Key Takeaways
- LC‑GRPO combines a deterministic ODE step with an isotropic Gaussian Langevin correction to match the marginal distribution at each timestep.  
- The score function is derived directly from flow velocity, eliminating the need for an additional score model.  
- Under matched randomness levels, LC‑GRPO’s transition can be more accurate than the standard Euler–Maruyama discretization of the reverse SDE.

## Context
Flow models are prized for their exact sampling but suffer when used with online RL because training requires stochastic rollouts while inference remains deterministic. Existing work replaces ODEs with SDEs, yet discretization errors cause a gap between training and test behavior that hampers performance.

## Implications
LC‑GRPO offers a practical way to close this gap without sacrificing the exactness of flow models, which is crucial for high‑quality generative AI in creative applications. Practitioners can achieve more reliable RL training while maintaining state‑of‑the‑art generation quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05600v1)
