---
title: Trust Is Not Enough: Influence Calibration for On-Policy Self-Distillation in Agentic RL
url: http://arxiv.org/abs/2608.14945v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_23-56-38Z_TrustIsNotEnough_InfluenceCalibrationforOn_PolicyS.md
generated_at: 2026-08-17 21:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles the trust-utility mismatch in on-policy self-distillation where teacher‑assigned importance does not reflect token usefulness for the policy objective. It introduces Influence Calibration for Self-Distillation (ICSD) that measures surrogate response to perturbations and adapts allocation weights, achieving higher performance across multiple benchmarks.

## Key Takeaways
- ICSD quantifies the first-order response of each token’s importance‑weighted RL contribution to a teacher‑directed output perturbation, revealing which tokens actually support the policy objective.  
- The batch‑adaptive calibration converts this non‑stationary signal into bounded weights that keep auxiliary loss mass within an action turn while discarding mass on objective‑opposed tokens.  
- Experiments show ICSD raises cosine compatibility with RL gradients by 0.192 and cuts teacher‑supported mass from 60.1% to 37.8%, delivering higher aggregate scores on ALFWorld, WebShop, and Search‑QA.

## Context
Self‑distillation leverages a model’s own output as supervision, reducing reliance on external data; however, naïve trust allocation can misdirect learning toward irrelevant tokens. This work provides a principled calibration that aligns teacher feedback with policy gradients, offering a more effective way to use dense token supervision in RL.

## Implications
By decoupling the distillation loss from auxiliary mass, practitioners can fine‑tune agents without extra model passes, enabling scalable deployment of large language models in RL pipelines where efficiency and alignment are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14945v1)
