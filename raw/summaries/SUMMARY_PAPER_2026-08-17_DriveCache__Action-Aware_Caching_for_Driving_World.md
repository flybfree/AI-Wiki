---
title: DriveCache: Action-Aware Caching for Driving World Model Inference
url: http://arxiv.org/abs/2608.16354v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_10-04-49Z_DriveCache_Action_AwareCachingforDrivingWorldModel.md
generated_at: 2026-08-17 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
DriveCache is a training-free action‑aware controller that improves diffusion‑based driving video generation by reusing scene features based on planned motion and denoising progress. It allocates cache slots across scenes using dynamic programming within a response budget and refreshes when the generated scene deviates from calibration, preserving fidelity while boosting efficiency.

## Key Takeaways
- DriveCache uses planned ego speed and trajectory to decide which cached features can be reused, reducing redundant backbone evaluations.
- The controller employs dynamic programming to schedule cache placement across denoising steps under a calibrated budget, balancing reuse length with motion changes.
- A causal drift check detects when the generated scene diverges from expected motion, triggering feature refresh and replanning of remaining cache usage.

## Context
Diffusion models for autonomous driving generate high‑fidelity video but are computationally expensive due to repeated backbone passes. Existing acceleration techniques treat each step independently, ignoring the rich temporal information available before generation. This paper introduces a method that leverages action data to make better use of cached features, aligning with trends toward efficient multimodal AI.

## Implications
For developers building driving simulators, DriveCache offers a plug‑in solution that can be deployed without retraining models, lowering latency for real‑time planning. In industry, it may reduce GPU costs and enable faster offline data generation, supporting broader adoption of autonomous‑driving research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16354v1)
