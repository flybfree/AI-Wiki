---
title: SSTG-Nav: Metric-Grounded Spatial-Semantic Topological Graphs for Reusable Object Navigation
url: http://arxiv.org/abs/2608.00527v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_08-40-04Z_SSTG_Nav_Metric_GroundedSpatial_SemanticTopologica.md
generated_at: 2026-08-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SSTG-Nav, a reusable metric-semantic memory that converts a one-time survey into actionable object goals and consolidates evidence across viewpoints while keeping spatially distinct recovery standoffs. On 1,000 HM3D-v2 episodes across 36 scenes the goal-independent topology reaches a 99.4% geometric success ceiling.

## Key Takeaways
- The goal-independent topology achieves a 99.4% geometric success ceiling on the test set.
- Metric grounding improves SR/SPL from 0.835/0.560 to 0.920/0.603 when semantic responses are held fixed.
- Fusion-aware Top-3 recovery yields Success@1/2/3 of 0.928/0.965/0.975 and SPL@3 of 0.601.

## Context
This work addresses a longstanding challenge in service robotics: the need for reliable navigation that does not require repeated one-shot exploration each time an object is requested. By integrating metric data with semantic knowledge, SSTG-Nav demonstrates how pre-exploration can produce reusable navigation plans.

## Implications
For industry and practitioners, the results show that building a memory that couples precise spatial metrics with robust semantics enables consistent performance across multiple sessions. This approach reduces hardware wear, operational costs, and deployment risk in long-term service environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00527v1)
