---
title: Linear Proposal Operators and Stochastic Search Geometry in SOMA and Differential Evolution
published: 2026-07-31T09:58:58Z
authors: Vojtěch Novák, Ivan Zelinka
url: http://arxiv.org/abs/2607.29228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Linear Proposal Operators and Stochastic Search Geometry in SOMA and Differential Evolution

## Abstract
Swarm and evolutionary algorithms are usually analyzed as complete procedural systems in which nonlinear selection, replacement, and adaptation obscure simpler structure within candidate generation. This paper introduces an operator--selection factorization that separates objective-independent variation from boundary repair and fitness-dependent selection, and uses it to study the proposal geometry of the Self-Organizing Migrating Algorithm (SOMA) and Differential Evolution (DE). The canonical SOMA proposal is shown to be affine in the search space and exactly linear in an augmented migrant--leader state. In leader-relative coordinates, the resulting operator provides a direct interpretation of interpolation, projection, overshooting, and coordinate masking. Under Bernoulli perturbation masks, we derive closed-form expressions for the proposal mean, covariance, expected squared step length, expected squared distance from the leader, active dimensionality, and coordinate coverage. For canonical DE/rand/1/bin, we derive the finite-population moments of differential mutation and characterize the additional covariance and coordinate dependence induced by forced-coordinate binomial crossover. Exact enumeration and Monte Carlo experiments verify the analytical identities and quantify the effects of mask conditioning, boundary repair, and fitness-based selection. The analysis further motivates geometry-controlled and rotation-aware SOMA variants, together with an adaptive population-reducing extension of iSOMA. Experiments on the complete noiseless BBOB benchmark show that these operator-guided variants substantially improve upon canonical SOMA and are competitive with established DE methods in several dimension--budget regimes. The results demonstrate how proposal-level operator analysis can support both the interpretation and design of population-based optimizers.

## Metadata
- **Published**: 2026-07-31T09:58:58Z
- **Authors**: Vojtěch Novák, Ivan Zelinka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29228v1)