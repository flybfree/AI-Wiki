---
title: "Summary: Staleness-Learning Rate Scaling Laws for Asynchronous RLHF"
url: http://arxiv.org/abs/2607.01083v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_15-40-12Z_Staleness_LearningRateScalingLawsforAsynchronousRL.md
generated_at: 2026-07-01 21:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-07-01 Staleness-Learning Rate Scaling Laws For Asynchron

## Summary
The paper investigates how stale rollouts affect stability in asynchronous gradient policy optimization within reinforcement learning with human feedback. It shows that the bias introduced by a lag S and learning rate η scales as O(S·η) and derives a scaling law linking collapse time to either cumulative drift T·η or stale‑rollout constraint S·η.

## Key Takeaways
- The per-step surrogate‑gradient bias grows linearly with both rollout lag S and learning rate η, meaning longer delays amplify instability.  
- When within‑cycle drift stays below a batch clipping radius, collapse is driven mainly by cumulative learner drift proportional to T·η rather than stale‑rollout effects.  
- Stability requires η to be much smaller than the minimum of R_batch/(S·G_upd) and R_crit/(T·G_upd), revealing that maximum stable η can appear weakly dependent on staleness in horizon‑limited settings.

## Context
Asynchronous reinforcement learning with human feedback (RLHF) often runs rollout generation independently from policy updates, creating a lag between data collection and optimization. This decoupling is common but rarely quantified, leading to empirical tuning of learning rates that may be suboptimal or cause collapse.

## Implications
Practitioners can now set learning rates based on both the expected rollout delay and the batch‑level clipping radius, improving stability without sacrificing performance. The derived scaling law offers a principled guide for scheduling η in large‑scale RLHF pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01083v1)
