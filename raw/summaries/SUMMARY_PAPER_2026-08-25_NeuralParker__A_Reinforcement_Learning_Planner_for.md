---
title: NeuralParker: A Reinforcement Learning Planner for Irregular Parking Environments
url: http://arxiv.org/abs/2608.24485v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_12-33-14Z_NeuralParker_AReinforcementLearningPlannerforIrreg.md
generated_at: 2026-08-25 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
NeuralParker is a reinforcement learning planner that tackles irregular parking by encoding full environment geometry in a target-relative vertex representation. The method combines a curvature-length arc policy with an ensemble of cubic Hermite connections to generate diverse trajectories. Experiments on benchmark tasks show higher success rates and better trajectory quality than baselines, confirming the approach's effectiveness.

## Key Takeaways
- NeuralParker encodes full obstacle and boundary geometry in a target‑relative vertex representation, preserving long‑range route context throughout the approach.
- It couples a learned curvature–length arc policy with an in‑loop terminal ensemble that selects diverse cubic Hermite connections using a curvature‑regularized cost.
- Ablation studies demonstrate that both the global representation and the terminal ensemble are essential for achieving high planning success and trajectory quality.

## Context
Automated parking systems traditionally assume uniform slots and short approaches, limiting applicability to delivery vehicles with irregular poses. Learning‑based planners often rely on local observations, which hinder long‑range reasoning needed in complex bounded environments. This work addresses those limitations by introducing a global representation that maintains route context across the entire maneuver.

## Implications
The results suggest that hybrid reinforcement learning can deliver robust, low‑cost planning for real delivery vehicles at working sites. Practitioners can adopt NeuralParker’s target‑relative encoding and terminal ensemble to improve success rates without sacrificing computational efficiency, opening new possibilities for autonomous service operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24485v1)
