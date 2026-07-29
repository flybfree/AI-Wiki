---
title: Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control
url: http://arxiv.org/abs/2607.25337v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_06-38-16Z_Temporal_DistanceJEPA_Plan_AwareRepresentationLear.md
generated_at: 2026-07-28 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Temporal-Distance JEPA (TD-JEPA), a method that improves latent world model predictive control by mining temporal progress from offline logs. It replaces Euclidean distance with a directed cost derived from reward-free trajectories, boosting performance on Two-Room and OGB-Cube. The approach narrows the train-plan gap and matches or exceeds existing planners.

## Key Takeaways
- TD-JEPA retains the LeWM encoder-predictor backbone while replacing Euclidean ranking with a temporal-cost signal that uses same-trajectory step order as positive targets, cross‑trajectory pairs as negatives, and rollout consistency to match planner horizon. 
- The mined cost serves both as the deployment planning metric when progress is topological and as a representation signal that refines Euclidean geometry. 
- Under locked evaluation TD-JEPA achieves 100% success on Two‑Room versus LeWM’s 97.4%, improves OGB‑Cube by 14.2 points over LeWM, and matches or exceeds both LeWM and RC‑aux baselines across all environments.

## Context
Latent model predictive control relies on world models learned from demonstrations, but current planners often use Euclidean distance which does not reflect true progress. This gap limits performance in complex tasks where trajectory order matters more than spatial proximity. TD-JEPA addresses this by extracting a temporally informed cost directly from logs.

## Implications
For practitioners, TD-JEPA offers a practical way to align offline training with online planning without extra supervision. The method can be integrated into existing JEPA pipelines, reducing the need for costly human‑defined progress metrics and enabling more reliable control in real‑world robotics applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25337v1)
