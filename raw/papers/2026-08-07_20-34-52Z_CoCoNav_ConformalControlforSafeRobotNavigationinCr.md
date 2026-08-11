---
title: CoCoNav: Conformal Control for Safe Robot Navigation in Crowds
published: 2026-08-07T20:34:52Z
authors: Cheng Guo, Mingzhe Ni, Zheng Liang, Yihu Ling, Yuan Hu, Michele Caprio, Daniele Pucci, Wei Pan
url: http://arxiv.org/abs/2608.07751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoCoNav: Conformal Control for Safe Robot Navigation in Crowds

## Abstract
Safe and efficient robot navigation in crowds requires anticipating pedestrian motion despite uncertain and potentially shifting prediction errors. Existing reactive methods can produce oscillatory behavior, while predictive planners often treat forecasts as exact or rely on restrictive error models. Incorporating conservative uncertainty sets as hard constraints can also render model predictive control (MPC) infeasible. We propose \textit{CoCoNav}, a crowd-navigation framework that combines online conformal calibration with runtime-certified planning. A horizon-specific conformal proportional--integral controller adapts trajectory-error bounds to regulate long-run empirical coverage, enabling the framework to respond to changing prediction errors. A \textit{relax-then-verify} planner preserves solver feasibility by generating nominal trajectories with soft-constrained MPC and separately certifying them, together with contingency maneuvers, against the calibrated bounds before execution. Simulations and quadruped experiments show that CoCoNav achieves a favorable balance among collision avoidance, task success, and navigation efficiency relative to the evaluated baselines.

## Metadata
- **Published**: 2026-08-07T20:34:52Z
- **Authors**: Cheng Guo, Mingzhe Ni, Zheng Liang, Yihu Ling, Yuan Hu, Michele Caprio, Daniele Pucci, Wei Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07751v1)