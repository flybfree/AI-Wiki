---
title: SSTG-Nav: Metric-Grounded Spatial-Semantic Topological Graphs for Reusable Object Navigation
published: 2026-08-01T08:40:04Z
authors: Daojie Peng, Bingtao Wang, Jun Ma
url: http://arxiv.org/abs/2608.00527v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SSTG-Nav: Metric-Grounded Spatial-Semantic Topological Graphs for Reusable Object Navigation

## Abstract
Service robots operating for months in the same homes, offices, and facilities should become more reliable with experience instead of searching familiar space from scratch for every request. Yet ObjectNav is predominantly formulated as one-shot exploration, leaving a central deployment challenge unresolved: recognizing an object does not identify a reachable place to stop, and one confident map error can terminate the task. We introduce SSTG-Nav, a reusable metric-semantic memory that turns a one-time survey into actionable object goals, consolidates evidence across viewpoints, and retains spatially distinct recovery standoffs. On 1,000 HM3D-v2 episodes across 36 scenes, our goal-independent topology achieves a 99.4% geometric success ceiling. Holding semantic responses fixed, metric grounding raises SR/SPL from 0.835/0.560 to 0.920/0.603, and source-aware fusion reaches 0.926/0.586. Fusion-aware Top-3 recovery raises Success@1/2/3 to 0.928/0.965/0.975 and reaches 0.601 SPL@3. Model, field-of-view, density, and corruption controls identify where these gains originate, and a ROS2/Nav2 realization demonstrates the complete reusable query-to-execution pipeline. Together, the results establish pre-exploration as a powerful practical regime for dependable, repeated semantic navigation.

## Metadata
- **Published**: 2026-08-01T08:40:04Z
- **Authors**: Daojie Peng, Bingtao Wang, Jun Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00527v1)