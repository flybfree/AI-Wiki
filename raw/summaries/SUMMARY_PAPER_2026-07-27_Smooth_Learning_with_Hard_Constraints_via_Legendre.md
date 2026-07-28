---
title: Smooth Learning with Hard Constraints via Legendre-Regularized Policies
url: http://arxiv.org/abs/2607.24007v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_05-09-41Z_SmoothLearningwithHardConstraintsviaLegendre_Regul.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Legendre‑regularized policies that combine expressiveness, hard feasibility enforcement, and smoothness for gradient‑based training. By reformulating decisions as solutions of regularized optimization problems over the original feasible region, the authors obtain a policy class that is differentiable with respect to latent parameters and can be made arbitrarily smooth.

## Key Takeaways
- The proposed Legendre‑regularized policies guarantee feasibility by construction because they solve constrained optimization problems whose feasible set is the relative interior of the original constraints.  
- Their optimizer map is single‑valued, has an explicit Jacobian, is Lipschitz continuous, and can be made arbitrarily smooth, enabling reliable gradient computation for downstream loss functions.  
- A universal approximation result shows that any continuous feasible policy on a compact context set can be approximated by this class of policies.

## Context
In AI research, designing policy classes that balance expressiveness with training stability remains a challenge. Traditional methods often rely on soft penalties or implicit perturbations that may introduce non‑differentiability or loss of feasibility. This work addresses these issues by providing a principled construction that unifies regularized optimizers and perturbation‑based smoothness.

## Implications
The framework offers practitioners a reliable tool for training policies in constrained decision problems such as contextual newsvendor allocation, where hard constraints are essential. By ensuring both feasibility and smooth optimization, it can lead to more robust and accurate prescriptive models compared with benchmark approaches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24007v1)
