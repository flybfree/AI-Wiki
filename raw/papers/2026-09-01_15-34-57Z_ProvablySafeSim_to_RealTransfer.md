---
title: Provably Safe Sim-to-Real Transfer
published: 2026-09-01T15:34:57Z
authors: Tingting Ni, Maryam Kamgarpour
url: http://arxiv.org/abs/2609.01418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Provably Safe Sim-to-Real Transfer

## Abstract
To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in many applications, such as robotics and healthcare, this data-collection process is itself subject to safety constraints. This gives rise to the problem of safe sim-to-real transfer: how can an agent exploit an imperfect simulator while ensuring safe real-world data collection and learning a near-optimal feasible policy for the target system? We address this problem by formulating safe sim-to-real transfer within the framework of reward-free safe RL. We design a computationally efficient algorithm that exploits simulator information to provably reduce real-world interaction while ensuring safe exploration and enabling the computation of a near-optimal feasible policy for any potential reward function. Our real-world sample complexity bound characterizes the benefit of using the simulator in terms of the sim-to-real mismatch.

## Metadata
- **Published**: 2026-09-01T15:34:57Z
- **Authors**: Tingting Ni, Maryam Kamgarpour
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01418v1)