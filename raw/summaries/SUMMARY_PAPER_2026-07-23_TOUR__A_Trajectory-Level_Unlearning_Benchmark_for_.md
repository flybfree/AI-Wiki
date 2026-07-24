---
title: TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning
url: http://arxiv.org/abs/2607.21111v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-40-40Z_TOUR_ATrajectory_LevelUnlearningBenchmarkforOfflin.md
generated_at: 2026-07-23 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TOUR, a benchmark for trajectory-level unlearning in offline reinforcement learning that evaluates how well data can be removed while preserving utility and privacy. Experiments across D4RL locomotion tasks and an AntMaze extension reveal that common deletion methods often fail to reflect true privacy-utility trade‑offs because they rely on single likelihood scores.

## Key Takeaways
- A lower membership score may indicate trajectory removal, residual memorization visible to another attack, or policy collapse that destroys useful behavior.  
- Retraining and fine‑tuning provide stronger retained‑utility references than uniform GA+Refit, while TrajDeleter is only a useful comparator under specific audit conditions.  
- A single likelihood‑based membership score can overstate deletion quality; the results depend on matched non‑member construction, retraining‑relative calibration, attack family, retained utility, and explicit diagnostic scope.

## Context
Offline RL agents must be trained on fixed trajectories, making selective data deletion a practical concern. Existing evaluation methods often lack nuanced metrics, leading to misleading conclusions about privacy preservation and behavior retention.

## Implications
For practitioners, TOUR highlights the need for multi‑metric auditing rather than relying on one score. The field should adopt calibrated retraining references and consider attack families when assessing offline RL unlearning effectiveness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21111v1)
