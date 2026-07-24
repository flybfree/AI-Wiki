---
title: From Distances to Trajectories: Real-Time Signed Distance Function Mapping and Distance-Accelerated Motion Planning for UAVs
url: http://arxiv.org/abs/2607.19306v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_17-18-46Z_FromDistancestoTrajectories_Real_TimeSignedDistanc.md
generated_at: 2026-07-23 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an integrated system that combines a neural signed distance function estimator with a search‑based planner to enable real‑time UAV navigation in cluttered indoor environments. By jointly using OREN for SDF reconstruction and Bubble* for collision‑free bubble generation, the approach achieves both higher estimation accuracy and significantly faster trajectory computation.

## Key Takeaways
- OREN improves SDF estimation by 22% compared to baselines.
- Bubble* finds trajectories spanning approximately 90 m in 1–3 seconds, whereas baselines require up to 10 seconds for the same environment.
- The bubble graph reduces collision checks and provides formal guarantees of termination, completeness, and failure detection.

## Context
Real‑time perception and planning are essential challenges for autonomous aerial robots operating indoors where obstacles are dense and compute resources are limited. This work bridges the gap between neural SDF reconstruction and geometric search methods, offering a unified framework that balances accuracy with speed.

## Implications
The results demonstrate that compact UAVs can navigate complex spaces quickly without sacrificing safety, reducing both computational load and latency. For industry and researchers, this approach accelerates deployment of safe, real‑time flight systems in dynamic environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19306v1)
