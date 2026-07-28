---
title: Training with (Swap) Regret Loss in a Single-Layer Self-Attention Model: A Case Study on the Probability Simplex
published: 2026-07-25T19:11:15Z
authors: Chanwoo Park, Asuman Ozdaglar
url: http://arxiv.org/abs/2607.23333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training with (Swap) Regret Loss in a Single-Layer Self-Attention Model: A Case Study on the Probability Simplex

## Abstract
We revisit the regret loss framework introduced in Park et al. (2025), which uses decision-theoretic regret as a direct loss function for training models to make better decisions, through the lens of probability-simplex policies. Our first result shows that a single-layer self-attention model trained with regret loss admits a stationary point whose forward-pass exactly matches smoothed fictitious play with the appropriate stepsize that ensures no-regret behavior-i.e., for any given policy input, the model outputs the same update that smoothed fictitious play would produce. In parallel, we also newly introduce a swap-regret loss function, which extends the regret-loss framework beyond external regret and enables models to directly optimize for swap-deviation robustness. We further show that this swap-regret loss admits a stationary point whose forward pass implements the corresponding swap-regret update induced by classical Blum-Mansour no-pass implementation algorithm, with each head implementing an external-regret update via smoothed fictitious play. Together, these results show that regret-trained attention can realize differentiable mechanisms whose deployment induces equilibrium behavior in games: external-regret dynamics lead to coarse correlated equilibrium, while swap-regret dynamics lead to correlated equilibrium. Thus, regret-based objectives steer minimal attention architectures toward online-learning dynamics with game-theoretic guarantees, without supervised traces of those algorithms.

## Metadata
- **Published**: 2026-07-25T19:11:15Z
- **Authors**: Chanwoo Park, Asuman Ozdaglar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23333v1)