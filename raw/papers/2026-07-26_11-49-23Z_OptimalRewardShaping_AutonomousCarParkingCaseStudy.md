---
title: Optimal Reward Shaping: Autonomous Car Parking Case Study
published: 2026-07-26T11:49:23Z
authors: Emre Özkaya, Nicolas R. Gauger
url: http://arxiv.org/abs/2607.23617v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Reward Shaping: Autonomous Car Parking Case Study

## Abstract
Designing effective reward functions for model-free reinforcement learning under non-holonomic constraints remains a persistent challenge, often resulting in severe local minima such as policy paralysis or over-conservative hazard avoidance. In this work, we present a parameterized reward shaping framework featuring coverage-gated alignment feedback, drive-direction switch regularization, and an aligned episode termination mechanism evaluated on an autonomous parallel parking task. Crucially, we show that environmental reward parameters and algorithmic hyperparameters are deeply co-dependent, requiring joint meta-optimization to achieve stable convergence. By employing surrogate-based Bayesian optimization, our co-optimized Deep Q-Network (DQN) agent resolves characteristic control failure modes, significantly outperforming uncalibrated baselines across both success rate and trajectory smoothness.

## Metadata
- **Published**: 2026-07-26T11:49:23Z
- **Authors**: Emre Özkaya, Nicolas R. Gauger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23617v1)