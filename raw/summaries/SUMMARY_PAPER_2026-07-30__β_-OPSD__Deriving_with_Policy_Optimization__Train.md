---
title: $β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation
url: http://arxiv.org/abs/2607.28582v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-41-16Z_β__OPSD_DerivingwithPolicyOptimization_Trainingwit.md
generated_at: 2026-07-30 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces β‑OPSD, a generalization of on‑policy self‑distillation that uses a parameter β to blend the reference policy and a privileged teacher. By treating the optimal policy as a geometric interpolation between these two policies, the authors replace costly reinforcement‑learning optimization with cheap token‑level distillation. Experiments show that β‑OPSD improves stability and reasoning performance compared with vanilla OPSD.

## Key Takeaways
- The paper shows that vanilla OPSD corresponds to β=1 in a broader policy‑optimization family where β weights the KL penalty, turning it into a controllable regularization parameter.
- Optimizing the RL objective directly is expensive and high variance; instead they use the closed‑form solution as a distillation target by mixing token logits from the reference and teacher policies.
- Return‑to‑go credit assignment aligns token updates with the sequence‑level objective while preserving OPSD’s simplicity.

## Context
Self‑distillation methods aim to improve language models without retraining, but they often require handcrafted engineering. This work reframes OPSD as a principled interpolation between two policies, offering a systematic way to tune regularization and teacher influence. The approach highlights the gap between theoretical policy optimization and practical distillation pipelines.

## Implications
For practitioners, β‑OPSD provides an efficient alternative to full RL training for model refinement, reducing compute costs while boosting performance on reasoning tasks. The method could be adopted in large language model pipelines where iterative improvement is needed without sacrificing speed or stability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28582v1)
