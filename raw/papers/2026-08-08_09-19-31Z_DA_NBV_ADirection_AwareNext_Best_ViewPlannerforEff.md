---
title: DA-NBV: A Direction-Aware Next-Best-View Planner for Efficient 3D Reconstruction of Ships at Sea
published: 2026-08-08T09:19:31Z
authors: Jiaming Chen, Juntao Yang, Zhentao Zou, Qi Ming, Yi Yu, Zhihang Zhong, Xue Yang, Xue Jiang, Yue Zhou
url: http://arxiv.org/abs/2608.08025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DA-NBV: A Direction-Aware Next-Best-View Planner for Efficient 3D Reconstruction of Ships at Sea

## Abstract
Accurate 3D reconstruction of ships at sea is important for maritime supervision, damage assessment, and autonomous maritime operations. Although 3D reconstruction has advanced considerably, high-quality data acquisition still largely relies on manually designed trajectories or skilled operators, resulting in high costs and limited scalability. Next-best-view (NBV) planning automates this process by selecting subsequent viewpoints based on the current state. However, existing NBV policies mainly model spatial occupancy while overlooking directional observation history. This limitation is particularly problematic for ships: their complex superstructures and severe self-occlusions require observations from multiple viewpoints, and insufficient directional coverage often yields incomplete reconstructions. These challenges are further amplified at sea, where wave-induced heave, roll, and pitch continuously alter the ship's pose and surface visibility. Meanwhile, wind disturbances and limited onboard power impose stricter requirements on scanning efficiency. To address these challenges, we propose DA-NBV, a direction-aware NBV policy that augments the conventional occupancy state with directional observation statistics. We introduce a learnable Position Advantage Field (PAF) that uses directional information to guide viewpoint selection. The policy further adopts a locally constrained action space and a nonlinear coverage-shaping reward to improve scanning efficiency. We also develop the ship-oriented SeaShip-3D dataset and a configurable sea-state simulation environment. Experiments under varying heave, roll, and pitch conditions show that DA-NBV improves reconstruction completeness by approximately 3 percentage points and reduces Chamfer distance by 43% while achieving higher path efficiency.

## Metadata
- **Published**: 2026-08-08T09:19:31Z
- **Authors**: Jiaming Chen, Juntao Yang, Zhentao Zou, Qi Ming, Yi Yu, Zhihang Zhong, Xue Yang, Xue Jiang, Yue Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08025v1)