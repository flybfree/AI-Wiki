---
title: Data-Dependent Regret and Polyak Corrections for Constrained Online Convex Optimization
published: 2026-07-28T09:13:00Z
authors: Wentao Zhang
url: http://arxiv.org/abs/2607.25480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Data-Dependent Regret and Polyak Corrections for Constrained Online Convex Optimization

## Abstract
Constrained online convex optimization requires minimizing regret against adversarial convex costs while satisfying a convex constraint at every round, as needed in safety-critical applications. A computationally efficient method combines online gradient descent with a Polyak feasibility step, using one constraint evaluation and one subgradient per round. Although this method achieves O(sqrt(T)) regret with per-round feasibility, we derive a tighter, data-dependent analysis by retaining two quantities omitted by the standard worst-case argument. First, we replace the gradient envelope G_f^2 T with the observed accumulation G_T = sum_t ||grad f_t(x_t)||^2. Second, we identify a nonnegative Polyak correction P_T that measures the cumulative squared displacement caused by feasibility projections and enters the regret bound with a negative sign. The resulting improvement, Delta_T = (eta/2)(G_f^2 T - G_T) + P_T/(2 eta), is always nonnegative. We further propose AdaOGD-PFS, an adaptive-step-size method that achieves O(sqrt(G_T)) regret while preserving per-round feasibility. Experiments on ball- and halfspace-constrained problems improve the regret bound by 38 to 43 percent, with both data-dependent gradients and Polyak corrections contributing substantially.

## Metadata
- **Published**: 2026-07-28T09:13:00Z
- **Authors**: Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25480v1)