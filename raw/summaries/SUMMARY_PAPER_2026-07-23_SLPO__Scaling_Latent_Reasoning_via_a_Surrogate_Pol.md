---
title: SLPO: Scaling Latent Reasoning via a Surrogate Policy
url: http://arxiv.org/abs/2607.19691v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_02-45-08Z_SLPO_ScalingLatentReasoningviaaSurrogatePolicy.md
generated_at: 2026-07-23 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Surrogate Latent Policy Optimization (SLPO) to enable outcome-reward reinforcement learning on autoregressive latent reasoners. It achieves improved Pass@k scores by using a surrogate policy density for trajectory credit assignment and a stopping head that refines variable-horizon policies, showing gains across both continuous and soft thinking settings.

## Key Takeaways
- Latent reasoning lacks per-step likelihood, preventing outcome-reward RL from directly optimizing latent trajectories.  
- The surrogate policy acts as a probability model mapping latent transitions to credit assignments, enabling scalable evaluation without token decoding.  
- A correctness-supervised stopping head adapts horizon length based on deterministic accuracy, allowing longer computation for harder instances.

## Context
In AI research, chain-of-thought prompting seeks to scale reasoning by rewarding correct intermediate steps. Yet this approach is limited by token-by-token decoding and fixed budget constraints. Latent methods circumvent these limits but have not yet integrated RL-driven scaling mechanisms.

## Implications
SLPO provides a practical path for deploying latent reasoners in production where compute efficiency and dynamic allocation are critical. It suggests that future agents can combine implicit representations with reward shaping to achieve both speed and accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19691v1)
