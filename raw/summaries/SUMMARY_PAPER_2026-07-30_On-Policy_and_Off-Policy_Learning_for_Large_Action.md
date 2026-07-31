---
title: On-Policy and Off-Policy Learning for Large Action Spaces
url: http://arxiv.org/abs/2607.28408v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-56-11Z_On_PolicyandOff_PolicyLearningforLargeActionSpaces.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates learning in large action spaces for contextual bandits, comparing on-policy and off-policy approaches. It introduces Bayesian methods that share information across actions to reduce regret. The work also proposes efficient off-policy estimators with low variance. These methods adaptively allocate exploration effort, making them suitable for real‑time decision making.

## Key Takeaways
- mixed-effect Thompson sampling (meTS) and diffusion-inspired priors (dTS) provide regret guarantees that depend on an effective number of actions, improving exploration efficiency.
- structured direct method sDM shows optimization error can dominate estimation error in large action spaces, highlighting the need for concave objectives.
- exponential smoothing and PAC-Bayesian bounds enable differentiable pessimistic methods that control bias-variance trade‑off in importance‑sampling estimators.

## Context
In interactive AI systems where agents must choose among millions of possible actions with limited feedback, efficient learning is crucial. This research addresses the scalability challenges that plague standard bandit algorithms.

## Implications
The methods enable practical deployment in recommendation and control systems where action spaces are huge and data are sparse. Practitioners can reduce regret and variance, leading to more reliable policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28408v1)
