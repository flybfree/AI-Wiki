---
title: Analytic Planning under Uncertainty with Moment Closure
url: http://arxiv.org/abs/2608.02519v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-17-00Z_AnalyticPlanningunderUncertaintywithMomentClosure.md
generated_at: 2026-08-03 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a method for model‑based reinforcement learning that propagates predictive uncertainty analytically without imposing restrictive policies or reward functions. By using a quadratic action‑value parameterization and a compatibility principle between the transition distribution and the value function, it derives a closed‑form Bellman backup that is analytic in the moments of the state distribution. Experiments on continuous control tasks show reduced target variance and well‑calibrated uncertainty estimates.

## Key Takeaways
- The method replaces full state distributions with their moments, allowing an exact expectation over the value function without sampling.  
- A compatibility principle ensures that the transition model’s Gaussian form matches the radial‑basis value function, guaranteeing analytic backup computation.  
- Empirical results demonstrate lower variance in learned targets and calibrated uncertainty under stochastic observations.

## Context
Current deep reinforcement learning often relies on either deterministic point estimates or stochastic sampling, both of which suffer from high variance or ignore predictive covariance. This work bridges that gap by integrating learned distribution models into the planning loop, offering a principled alternative to existing approaches.

## Implications
Practitioners can now generate more reliable action policies with quantified uncertainty, improving safety and interpretability in autonomous systems. The framework may also inspire future research on uncertainty‑aware model‑based RL without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02519v1)
