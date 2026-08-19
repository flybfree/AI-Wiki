---
title: Lipschitz Bandits with Arbitrary Feedback Delays
url: http://arxiv.org/abs/2608.15036v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-15_04-39-49Z_LipschitzBanditswithArbitraryFeedbackDelays.md
generated_at: 2026-08-18 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the Lipschitz bandit problem when rewards are delayed by an arbitrary amount of time, showing that standard regret bounds still hold with a modest extra term. The authors introduce two algorithms — one based on elimination and another using EXP3 — to achieve tight regret guarantees under both stochastic and adversarial reward settings.

## Key Takeaways
- The regret bound is $\tilde{O}\left(T^{\frac{d_z+1}{d_z+2}}+\sqrt{D}\right)$ where $T$ is the horizon, $D$ total delay, and $d_z$ a zooming dimension that differs between stochastic and adversarial cases. 
- Both algorithms retain the same high‑order term as delay‑free Lipschitz bandits but incur an additional $\tilde{O}(\sqrt{D})$ penalty proportional to the square root of the feedback delay. 
- The elimination algorithm works for stochastic rewards while EXP3 handles adversarial settings, demonstrating that the extra cost is unavoidable due to delayed information.

## Context
Lipschitz bandits are central to continuous‑action reinforcement learning where actions can be chosen from a bounded set and rewards depend smoothly on those choices. Feedback delays mimic real‑world scenarios such as sensor lag or network latency, making theoretical guarantees crucial for designing robust policies.

## Implications
For practitioners building online control systems that rely on delayed feedback, the $\sqrt{D}$ term signals that longer delays degrade performance but remain manageable with careful algorithm selection. This result guides engineers in balancing delay tolerance against regret, ensuring practical deployments do not suffer from unmanageable cumulative error.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15036v1)
