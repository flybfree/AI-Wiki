---
title: Wasserstein Policy Gradient for Entropy-Regularized Linear-Quadratic Control
url: http://arxiv.org/abs/2608.07433v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-17-58Z_WassersteinPolicyGradientforEntropy_RegularizedLin.md
generated_at: 2026-08-09 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a Wasserstein policy gradient method for entropy‑regularized linear‑quadratic control and shows that the resulting update reduces to an ODE whose solution is globally well posed. It proves exponential convergence from any admissible initialization and demonstrates that the convergence exponent approaches a positive limit as the entropy temperature vanishes, without introducing exp(−c/τ) terms.

## Key Takeaways
- The Wasserstein policy gradient updates state‑conditional action laws via transport in the action space, yielding an ODE for feedback gain and action covariance.  
- Bellman verification confirms that the unrestricted problem has a linear‑Gaussian optimal policy, making WPG tangent to this class of policies.  
- Exponential convergence holds from every admissible initialization and the exponent converges to a positive limit as entropy temperature approaches zero.

## Context
This work advances reinforcement learning by providing a principled gradient framework that aligns with known optimal control theory for LQ problems. It bridges deep RL methods with classical optimal control, offering a more stable and interpretable optimization path.

## Implications
For practitioners, the method yields reliable policy updates without the need for perturbative temperature scaling, simplifying implementation. In industry, this could lead to faster convergence in safety‑critical control systems where stability guarantees are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07433v1)
