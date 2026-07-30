---
title: Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning
published: 2026-07-29T00:19:09Z
authors: Keegan Harris, Brian W. Lee, Ian Waudby-Smith, Philip Amortila, Nika Haghtalab, Michael I. Jordan
url: http://arxiv.org/abs/2607.26358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning

## Abstract
Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy. A standard way to balance this trade-off is via a KL-regularized RL objective, although this formulation does not by itself provide a principled way to set the regularization coefficient. In practice, the coefficient is typically chosen heuristically or via hyperparameter search, which can lead to unnecessary overhead in training cost or undesirable reward-retention trade-offs. We instead propose a game-theoretic framework that gives this trade-off an explicit statistical interpretation. Specifically, we study a sequential game in which an agent chooses a policy to maximize cumulative reward while a monitor observes policy outputs over time and tests for deviations from the reference policy. Although not originating from the same perspective, we show that the resulting equilibrium policy can nonetheless be expressed as the solution to a KL-regularized RL problem for an optimal regularization parameter that can be viewed as maximizing reward per unit of statistical distinguishability. Drawing on classical results from concave-convex fractional programming, we provide a principled method for learning this equilibrium coefficient via reduction to the KL-regularized RL objective, thus allowing for flexible integration into standard fine-tuning pipelines. In experiments with Qwen3-8B and Llama-3.2-1B, we demonstrate that our methods result in competitive reward-retention trade-offs in a continual learning setting, and illustrate how our framework may be used to audit API providers serving open-source models.

## Metadata
- **Published**: 2026-07-29T00:19:09Z
- **Authors**: Keegan Harris, Brian W. Lee, Ian Waudby-Smith, Philip Amortila, Nika Haghtalab, Michael I. Jordan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26358v1)