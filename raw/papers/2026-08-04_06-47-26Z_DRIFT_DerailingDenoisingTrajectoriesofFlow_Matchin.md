---
title: DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack
published: 2026-08-04T06:47:26Z
authors: Hoseong Tae, Jong-Seok Lee
url: http://arxiv.org/abs/2608.03207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack

## Abstract
Flow-matching vision-language-action (VLA) models such as pi0 generate robot actions by integrating a learned denoising velocity field, and have been reported to resist adversarial perturbations that readily fool autoregressive VLAs. We show that this robustness is largely illusory: it stems from prior attacks ignoring the multi-step denoising ODE. We introduce DRIFT (Denoising Redirection via Input perturbation of the Flow-matching Trajectory), a test-time universal adversarial patch placed on the robot's gripper that attacks the denoising velocity field of an off-the-shelf policy. Our central finding is counterintuitive: attacking only the first denoising step is both stronger and cheaper than attacking a wider window of steps, which we explain through a gradient conflict unique to input-space optimization and which is exactly opposite to the training-time backdoor regime. On pi0 and pi0.5 across four LIBERO suites, DRIFT breaks essentially all originally-solvable tasks with a small single patch, far exceeding action- and embedding-space attack baselines.

## Metadata
- **Published**: 2026-08-04T06:47:26Z
- **Authors**: Hoseong Tae, Jong-Seok Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03207v1)