---
title: Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller
published: 2026-07-28T13:52:12Z
authors: Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf
url: http://arxiv.org/abs/2607.25728v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller

## Abstract
This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised continuous control. The policy combines BEV map features, near-field obstacle observations, and compact goal and peer-state information within a centralised-training, decentralised-execution framework. In simulation, the learned controller achieves a 90.3% success rate in corridor navigation, outperforming Astar planning, an artificial potential field controller, and a prior guidance method. To address residual sim-to-real mismatch, the simulation-trained policy is further adapted using offline imitation fine-tuning from real-world data. Real-world experiments in GNSS-denied indoor environments demonstrate stable two-UAV cooperative operation across increasingly chal- lenging obstacle layouts. The results show that shared voxel-map representations provide an effective and scalable spatial substrate for learned cooperative indoor UAV guidance.

## Metadata
- **Published**: 2026-07-28T13:52:12Z
- **Authors**: Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25728v1)