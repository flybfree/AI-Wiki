---
title: Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models
url: http://arxiv.org/abs/2607.23602v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_11-11-23Z_ActionfromAdjacentSetinPhysicalSpaceOutperformsthe.md
generated_at: 2026-07-27 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why sampling‑based controllers can select infeasible actions despite accurate terminal‑cost predictions. It identifies a phenomenon called conditional failure proposal overgeneration and proposes Adjacent Set Action Reconstruction (ASAR) to improve selection. Experiments show ASAR outperforms the best world model on Carry and Release tasks.

## Key Takeaways
- Increasing the total proposal budget from 72 to 288 reduces feasibility of selection for position targets from .375 to .062, showing that larger pools increase chance of picking infeasible sequences. - The residual prediction error can give an infeasible sequence an anomalously low cost, leading to overgeneration. - ASAR reconstructs a full sequence using an adjacent set and a light anchor from the minimum‑cost sequence, improving event completion success by up to 28.0 percentage points.

## Context
Sampling‑based planners rely on terminal‑cost predictions to guide action selection in robotics, but they often ignore local feasibility constraints. This work highlights that even perfect cost estimates can be misleading when proposal pools are large enough for rare errors to dominate feasible options, a risk that is not captured by standard evaluation metrics.

## Implications
Practitioners must consider both global optimality and local feasibility when designing planner policies. The ASAR framework offers a lightweight alternative to exhaustive sampling, reducing computational cost while maintaining high success rates in real‑world tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23602v1)
