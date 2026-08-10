---
title: Learning Fault-Tolerant Locomotion with Adaptive Gait Timing
published: 2026-08-07T15:27:03Z
authors: Giovanbattista Gravina, Luca Rossini, Carlo Rizzardo, Arturo Laurenzi, Nikos Tsagarakis
url: http://arxiv.org/abs/2608.07328v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Fault-Tolerant Locomotion with Adaptive Gait Timing

## Abstract
Hardware failures require legged robots to rapidly reorganize coordination and gait timing to maintain stability and mobility. This is particularly challenging for larger quadrupeds, where increased mass and tighter actuation limits reduce the feasibility of aggressive, high-frequency compensation strategies often observed on smaller platforms. In this work, we propose a deep reinforcement learning approach for fault-tolerant locomotion under actuator power loss. The method employs an asymmetric actor-critic architecture in which the critic has access to privileged information during training, while the actor learns to reconstruct a corresponding latent representation from proprioceptive observations. We introduce a latent-alignment loss that encourages consistency between actor and critic representations. Additionally, we augment the action space with a learnable gait frequency parameter, enabling adaptive gait timing in response to terrain variations and actuator degradation without predefined faulty-leg strategies. The approach is validated in high-fidelity simulation on uneven terrain and real-world experiments on flat ground using a 68 kg quadruped robot.

## Metadata
- **Published**: 2026-08-07T15:27:03Z
- **Authors**: Giovanbattista Gravina, Luca Rossini, Carlo Rizzardo, Arturo Laurenzi, Nikos Tsagarakis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07328v1)