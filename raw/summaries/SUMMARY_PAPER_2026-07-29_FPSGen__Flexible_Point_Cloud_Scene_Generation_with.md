---
title: FPSGen: Flexible Point Cloud Scene Generation with BEV-Supported Transport Flows
url: http://arxiv.org/abs/2607.26645v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_09-06-01Z_FPSGen_FlexiblePointCloudSceneGenerationwithBEV_Su.md
generated_at: 2026-07-29 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
FPSGen introduces a flexible point‑cloud generation framework that creates scene sources independently of partial LiDAR scans. By generating a bird’s‑eye‑view (BEV) prior and using an approximate optimal transport scheme, the method achieves high-quality unconditional and cue‑conditioned outdoor scene synthesis.

## Key Takeaways
- The BEV‑supported point source construction removes the train‑inference mismatch that causes sparse distant regions.  
- Teacher‑student approximate optimal transport learns a velocity field to produce straighter transport paths, improving geometric consistency.  
- FPSGen outperforms existing methods on SemanticKITTI and KITTI‑360 unconditional generation with superior JSD, voxel IoU, and coverage scores.

## Context
Current point‑cloud generators rely heavily on noisy partial scans, limiting their flexibility when LiDAR data is unavailable. This reliance creates visibility bias and incomplete geometry, hindering real‑world deployment where alternative cues are used instead of raw scans.

## Implications
FPSGen’s BEV‑based approach enables reliable scene generation without full point clouds, opening doors for autonomous navigation systems that must operate with sparse or structured input data. Practitioners can adopt this framework to improve robustness and reduce computational load in outdoor perception pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26645v1)
