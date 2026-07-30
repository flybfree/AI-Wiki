---
title: Reinforcement Learning on Cost-Constrained Quadrupedal Hardware
published: 2026-07-29T03:22:12Z
authors: Javier C. Weddington, Bence P. Ölveczky, Stephen A. Baccus
url: http://arxiv.org/abs/2607.26434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforcement Learning on Cost-Constrained Quadrupedal Hardware

## Abstract
Deploying learned control policies on low-cost robotic platforms introduces transport latencies and noisy motor feedback that systematically widens the sim-to-real gap. The chasm of simulation to deployment in hardware lies in the delay of the actuator reaching the commanded position. On platforms such as the Mini Pupper 2, a measured > $50 ms transport delay transforms the locomotion task from a standard Markov decision process into a partially observable one. In this paper, we take a biologically inspired approach of handling noisy and delayed feedback to close the sim-to-real gap, thereby expanding the capability of reinforcement learning on cost-constrained hardware. Using a low-cost quadrupedal hardware platform, we find that using a forward model of the average actuator delay, paired with a time-aware neural network results in robust locomotion. Additionally, our time-aware neural network learned a central pattern generator (CPG): a self-sustaining rhythmic gait that is robust to +320 ms latency perturbations, mirroring the CPGs found in the spinal cords of vertebrates. We posit that temporal self-organization may be a general strategy for cost-constrained locomotion.

## Metadata
- **Published**: 2026-07-29T03:22:12Z
- **Authors**: Javier C. Weddington, Bence P. Ölveczky, Stephen A. Baccus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26434v1)