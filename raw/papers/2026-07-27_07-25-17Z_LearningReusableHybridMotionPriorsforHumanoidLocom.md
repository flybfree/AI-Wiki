---
title: Learning Reusable Hybrid Motion Priors for Humanoid Locomotion from Motion Imitation
published: 2026-07-27T07:25:17Z
authors: Valerio Belli, Valerio Modugno, Enrico Mingo Hoffman, Fabio Amadio
url: http://arxiv.org/abs/2607.24083v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Reusable Hybrid Motion Priors for Humanoid Locomotion from Motion Imitation

## Abstract
Reinforcement learning can produce robust humanoid controllers, but each new task is typically trained as a separate policy with its own reward design and training process. Motion imitation provides an alternative source of motor competence by training policies to track retargeted human motions, yet the resulting controllers remain reference trackers and are not directly usable as task policies. We propose a three-stage pipeline that turns motion-imitation skills into a reusable hybrid motion prior (HMP) for humanoid locomotion. First, an expert policy is trained to imitate retargeted human motion-capture clips. Second, the expert is distilled into a frozen architecture composed of a proprioceptive encoder, a residual vector-quantized (RVQ) codebook, and an action decoder. Third, task-level policies are trained to solve locomotion tasks by selecting discrete codebook entries while the HMP remains frozen. We evaluate the method on velocity tracking, point-goal navigation, and fall-recovery velocity tracking in simulation, and deploy the velocity-tracking policy on a real Unitree G1 robot. The distillation process preserves the tracking behavior of the expert, while the resulting HMP can be reused without retraining as the action interface for different downstream locomotion policies. The learned HMP reveals an interpretable codebook structure in which the number of active RVQ stages modulates the available gait patterns. We further show that training the codebook with the rotation trick improves latent organization and reduces downstream falls compared with a standard straight-through estimator.

## Metadata
- **Published**: 2026-07-27T07:25:17Z
- **Authors**: Valerio Belli, Valerio Modugno, Enrico Mingo Hoffman, Fabio Amadio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24083v1)