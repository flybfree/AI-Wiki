---
title: Smooth Learning with Hard Constraints via Legendre-Regularized Policies
published: 2026-07-27T05:09:41Z
authors: Zikun Lin, Rui Chen, Yijie Wang
url: http://arxiv.org/abs/2607.24007v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Smooth Learning with Hard Constraints via Legendre-Regularized Policies

## Abstract
We revisit contextual optimization from the perspective of policy class design. A desirable policy class should be expressive enough to learn rich context-decision relationships, should enforce hard feasibility constraints rather than soft penalty terms, and should remain smooth enough for gradient-based training on downstream decision losses. Existing approaches usually emphasize only part of these requirements. We propose Legendre-regularized policies, which parameterize decisions as solutions of regularized optimization problems over the original feasible region. This construction yields policies that are feasible by construction and differentiable with respect to learned latent parameters. We prove that the associated optimizer map is single-valued, maps onto the relative interior of the feasible set, admits an explicit Jacobian, is Lipschitz continuous, and can be made arbitrarily smooth. We also establish a universal approximation result showing that the proposed class can approximate any continuous feasible policy on compact context sets. The framework unifies explicitly regularized optimizers and implicit perturbation-based smooth optimizers. Experiments on contextual newsvendor and resource allocation problems show that our approach improves prescriptive performance relative to the benchmark methods.

## Metadata
- **Published**: 2026-07-27T05:09:41Z
- **Authors**: Zikun Lin, Rui Chen, Yijie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24007v1)