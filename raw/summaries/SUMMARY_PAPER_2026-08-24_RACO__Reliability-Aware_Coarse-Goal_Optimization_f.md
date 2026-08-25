---
title: RACO: Reliability-Aware Coarse-Goal Optimization for Inspection-Oriented UAV Vision-Language Navigation
url: http://arxiv.org/abs/2608.22678v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_00-32-51Z_RACO_Reliability_AwareCoarse_GoalOptimizationforIn.md
generated_at: 2026-08-24 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RACO, a reliability‑aware coarse‑to‑fine navigation framework for UAV vision‑language navigation that targets inspection‑oriented tasks. It improves SR by 9.53 and 7.98 percentage points on validation‑unseen and test‑unseen datasets while reducing the risk of false verification.

## Key Takeaways
- The coarse goal is treated as a runtime hypothesis rather than a fixed waypoint, allowing it to be corrected using object‑level candidate anchors.
- RACO applies these anchor checks both before Stage 1 and at the boundary between Stage 1 and Stage 2 to refine localization dynamically.
- Scale‑adaptive terminal refinement leverages geometric and anchor evidence to handle near‑miss cases during final approach.

## Context
UAV vision‑language navigation is a rapidly advancing field aimed at enabling autonomous inspection robots to locate and verify objects with high reliability. Existing coarse‑to‑fine policies often assume the predicted goal is trustworthy, which can lead to missed inspections or unnecessary confirmations of incorrect regions.

## Implications
For industry practitioners, RACO demonstrates that optimizing the reliability of coarse goals directly improves inspection outcomes without sacrificing speed. This insight encourages a shift toward hypothesis‑driven planning in autonomous systems, offering a practical path to safer and more accurate inspection operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22678v1)
