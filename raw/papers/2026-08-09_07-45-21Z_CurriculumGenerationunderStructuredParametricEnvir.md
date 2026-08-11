---
title: Curriculum Generation under Structured Parametric Environments for Robust Navigation Policies
published: 2026-08-09T07:45:21Z
authors: Prishita Ray
url: http://arxiv.org/abs/2608.08545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Curriculum Generation under Structured Parametric Environments for Robust Navigation Policies

## Abstract
Robust navigation policies for autonomous agents must generalize across continuously varying environmental conditions such as turn rates, obstacles, friction, pits, and slopes. Curriculum generation provides a principled mechanism for improving generalization by progressively adapting training environments, but designing such curricula in a sample-efficient and automated manner remains challenging. This paper proposes a reparameterized curriculum generation framework for structured continuous environment parameters using unidirectional gradient-based optimization. To improve robustness in multimodal observation spaces consisting of image-based and scalar inputs, a distribution-shift regularization objective is incorporated to encourage the learning of finer-grained latent representations. The proposed method is evaluated across two continuous-control OpenAI Gym environments: a 2D obstacle-based Car Racing variant and Bipedal Walker variant, where coupled environment parameters jointly influence policy performance. Across five random seeds, our method consistently outperforms vanilla policy training, random parameter sampling, manual curricula, frontier-based methods, Self-Paced Reinforcement Learning (SPRL), Absolute Learning Progress with Gaussian Mixture Models (ALP-GMM), and reverse curriculum learning baselines. Ablation studies further demonstrate the effectiveness of the reparameterized curriculum mechanism across both environments, while highlighting environment-dependent benefits of the auxiliary regularization objective.

## Metadata
- **Published**: 2026-08-09T07:45:21Z
- **Authors**: Prishita Ray
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08545v1)