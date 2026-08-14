---
title: HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark
url: http://arxiv.org/abs/2608.13555v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-59-40Z_HumanTracker_TowardsComprehensiveandHuman_AlignedM.md
generated_at: 2026-08-13 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
HumanTracker introduces a comprehensive benchmark for humanoid motion tracking that aligns evaluation with human perception and addresses the limitations of existing datasets. The system provides 153 hours of optical trajectories across four motion families and introduces HumanScore, a preference‑aligned metric trained on thousands of motion pairs.

## Key Takeaways
- Kinematic errors are often hidden because they focus on average per‑frame pose differences while ignoring critical physical artifacts such as foot skating or mistimed touch‑downs.  
- The benchmark’s four motion families and detailed text labels enable fine‑grained diagnosis of contact and stability failures that traditional metrics overlook.  
- HumanScore, trained on 12 K motion pairs with 24 K motions, better predicts human preferences than conventional kinematic scores.

## Context
Current humanoid tracking evaluation relies heavily on small, limited test suites that do not capture the diversity of real‑world contact behaviors. This gap hampers reliable assessment and progress measurement in teleoperation and whole‑body imitation tasks.

## Implications
For researchers, HumanTracker offers a scalable resource to benchmark trackers under realistic conditions, improving alignment between algorithmic performance and human perception. Practitioners can leverage the detailed labels and HumanScore metric to diagnose contact issues early, leading to more robust humanoid systems in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13555v1)
