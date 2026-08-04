---
title: Open-DiffLoco: Open-Source Differentiable Learning for Deployable Blind Quadruped Locomotion
published: 2026-08-03T11:11:13Z
authors: Martin Opat
url: http://arxiv.org/abs/2608.02069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Open-DiffLoco: Open-Source Differentiable Learning for Deployable Blind Quadruped Locomotion

## Abstract
Developing deployable locomotion policies through conventional reinforcement learning often requires complex reward engineering and expensive training times. While differentiable simulation offers a highly efficient alternative, open-source tools capable of end-to-end transfer of these policies to physical hardware remain limited. This paper introduces Open-DiffLoco, an open-source framework for training deployable blind quadruped locomotion policies with differentiable simulation. The framework implements the Short-Horizon Actor-Critic (SHAC) algorithm in MuJoCo XLA (MJX) and trains a proprioceptive policy that transfers to real-world hardware. The deployed policy removes privileged actor observations, including base linear velocity, and does not rely on reference trajectories. It also uses a substantially simplified reward function, enabling the robot to discover walking patterns without the complex auxiliary rewards typically used in conventional reinforcement learning pipelines. When deployed on physical hardware (a Unitree Go2 quadruped), the trained policy tracks omnidirectional velocity commands with root-mean-square error below 0.2 m/s, reaches speeds above 1 m/s, and remains robust to uneven terrain and external physical disturbances, such as lateral pushes. Across the reported configurations, training uses under 6 GB of VRAM on a single NVIDIA GeForce RTX 5080 GPU and completes in approximately 20-60 minutes. As an algorithmic extension to SHAC, we propose Jacobian-Augmented Value Estimation (JAVE), which supervises the critic Jacobians to improve early first-order policy-gradient training. To our knowledge, Open-DiffLoco is the first open-source framework for training deployable locomotion policies using differentiable simulation. Deployment videos and source code are available at: https://diffloco.martin-opat.com/

## Metadata
- **Published**: 2026-08-03T11:11:13Z
- **Authors**: Martin Opat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02069v1)