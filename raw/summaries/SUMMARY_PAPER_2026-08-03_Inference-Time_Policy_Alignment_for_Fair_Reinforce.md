---
title: Inference-Time Policy Alignment for Fair Reinforcement Learning
url: http://arxiv.org/abs/2608.00175v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_18-00-50Z_Inference_TimePolicyAlignmentforFairReinforcementL.md
generated_at: 2026-08-03 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes inference-time policy alignment for fairness in reinforcement learning, showing that a pretrained RL agent can be steered toward welfare-based fairness without retraining by using action-dependent welfare scores to shape its actions multiplicatively. Experiments across multiple domains demonstrate improved fairness while maintaining task performance. The framework is general and requires no modification of the base policy.

## Key Takeaways
- The method uses inference-time alignment similar to large language models, applying a multiplicative shaping that multiplies action probabilities by action-dependent welfare scores, enabling real‑time adjustment without updating model weights.
- Welfare-based fairness objectives are substantially improved while core task performance remains largely unchanged, indicating trade‑off mitigation through careful shaping design.
- The approach is fully compatible with any deep RL agent, making it a universal tool for deploying existing policies under new stakeholder preferences.

## Context
In reinforcement learning the primary challenge is that agents optimize only scalar rewards, which can conflict with diverse fairness or welfare goals. Traditional solutions require full retraining or redesign of reward functions, limiting deployment flexibility and scalability. This work addresses those limitations by decoupling policy adaptation from training, aligning actions to fairness metrics at inference time.

## Implications
For industry practitioners this means existing RL systems can be repurposed for compliance or ethical constraints without costly retraining pipelines. For researchers it opens a path toward continual improvement of deployed AI agents, supporting responsible deployment across sectors such as finance and healthcare where fairness is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00175v1)
