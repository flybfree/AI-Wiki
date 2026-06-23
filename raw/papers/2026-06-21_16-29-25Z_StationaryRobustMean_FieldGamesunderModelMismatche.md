---
title: Stationary Robust Mean-Field Games under Model Mismatches
published: 2026-06-21T16:29:25Z
authors: Yue Wang
url: http://arxiv.org/abs/2606.22579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stationary Robust Mean-Field Games under Model Mismatches

## Abstract
Deploying multi-agent reinforcement learning (MARL) in the real world is often limited by model mismatches between the training simulators and the true environment, which could be further amplified through strategic interactions and result in severe performance degradation upon deployment. Distributional robustness offers a principled response by optimizing policies against worst-case transition models drawn from an uncertainty set, but standard robust MARL frameworks become increasingly intractable as the number of agents grows. This paper develops an infinite-horizon, stationary mean-field game framework that incorporates distributional model uncertainty directly into the population-coupled dynamics. We establish a robust dynamic programming principle with a contractive Bellman operator and prove the existence of a stationary robust mean-field equilibrium via a fixed-point argument. We further develop the first concrete algorithm with convergence guarantees. We then connect the mean-field solution to a finite-population robust game whose ambiguity sets depend on the empirical distribution, showing that the mean-field equilibrium policy induces approximate equilibrium behavior as the population size increases. Under a contractive robust-dynamics regime, we further obtain explicit non-asymptotic error bounds. Numerical experiments further illustrate the qualitative and quantitative impact of robustness under multiple uncertainty models, validating our theoretical findings.

## Metadata
- **Published**: 2026-06-21T16:29:25Z
- **Authors**: Yue Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22579v1)