---
title: BVR Sim: An Open and High-Throughput Environment for Heterogeneous Air-Combat Reinforcement Learning
published: 2026-08-26T06:21:24Z
authors: Haocheng Sun, Mulai Tan
url: http://arxiv.org/abs/2608.25419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BVR Sim: An Open and High-Throughput Environment for Heterogeneous Air-Combat Reinforcement Learning

## Abstract
Beyond-visual-range (BVR) air combat is a challenging reinforcement-learning domain characterized by partial observability, long-horizon decision making, energy management, and limited weapons. We present BVR Sim, an open-source Gymnasium-style environment designed for heterogeneous air-combat reinforcement learning. BVR Sim supports multiple JSBSim aircraft models, including the F-15, F-16, F/A-18, and F-22, with configurable weapons, sensors, controllers, and opponents. A unified tactical action interface specifies desired heading, altitude, speed, and weapon release above aircraft-specific inner-loop controllers, enabling policies to operate across heterogeneous platforms. The environment provides interchangeable Python and accelerated C++ backends, entity-oriented observations, compositional rewards, scripted opponents, replay and visualization, and adapters for multi-agent learning frameworks. At a 0.4-s decision interval, the C++ backend achieves 104 simulated seconds per wall-clock second in 1-vs-1 and remains practical through 10-vs-10 scenarios. A policy trained only on the F-16 transfers without retraining to four unseen aircraft, reaching a 45.5% mean win rate with aircraft-specific controller adaptation. MAPPO and HAPPO experiments further verify end-to-end compatibility with standard multi-agent reinforcement-learning pipelines.

## Metadata
- **Published**: 2026-08-26T06:21:24Z
- **Authors**: Haocheng Sun, Mulai Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25419v1)