---
title: Self-Adaptive Learning and Model Predictive Control for Tracking Unknown Dynamics with No Regret
published: 2026-07-29T01:07:28Z
authors: Atharva Navsalkar, Hongyu Zhou, Vasileios Tzoumas
url: http://arxiv.org/abs/2607.26370v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Adaptive Learning and Model Predictive Control for Tracking Unknown Dynamics with No Regret

## Abstract
We propose a self-adaptive online learning for control method for tracking unknown target dynamics. The target dynamics can exhibit switching behavior, particularly, a mixture of structured, random, and/or adversarial motion. Such challenging target tracking scenarios arise in applications of dynamic mapping, traffic control, and pursuit evasion, where robots need to track, pursue, or avoid collision with moving landmarks, objects, humans, etc., whose dynamics are unknown. Our method simultaneously learns multiple predictors from scratch, via self-supervised, one-shot, and computationally efficient learning, and adaptively selects the best one to match the observed target behavior. The method enjoys finite-time near-optimality guarantees in expectation, characterized as a function of the learning error of the target dynamics and the frequency that the target dynamics switch. In the absence of both error and switching, the method asymptotically matches the optimal non-causal control policy that knows a priori the target dynamics, i.e., the method enjoys no regret in expectation. In the presence of learning errors and switching, the method degrades gracefully, \eg when there are errors and no switching, the average regret is proportional to the average learning error and switching times. To prove these guarantees, a novel technical approach is required compared to the existing works that employ RFF-based online learning. We validate our method in Crazyflie simulations and hardware experiments, across target trajectories that vary from structured to random to adversarial, in comparison to non-stochastic, kernel-based, and neural-network-based methods for online learning.

## Metadata
- **Published**: 2026-07-29T01:07:28Z
- **Authors**: Atharva Navsalkar, Hongyu Zhou, Vasileios Tzoumas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26370v1)