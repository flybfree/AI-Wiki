---
title: SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection
url: http://arxiv.org/abs/2608.16338v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-44-27Z_SIGMA_Lane_Scale_pyramIdGatedMAmbaforTemporallyCon.md
generated_at: 2026-08-17 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SIGMA-Lane, a method that stabilizes video lane detection by treating occlusion-induced errors as state contamination in a State Space Model. By applying gates to both the SSM write and residual‑fusion paths, the model controls how current observations are stored and retrieved, ensuring temporal consistency even when vehicles block lanes. Experiments on VIL-100 and OpenLane-V demonstrate improved stability with competitive F1 and mIoU scores.

## Key Takeaways
- SIGMA-Lane places occlusion‑aware gates directly on the SSM write and residual‑fusion pathways, preventing corrupted observations from persisting through temporal propagation.
- The model uses coordinate‑consistent affine alignment to align historical lane priors with current frames, enabling Structural Spatial Retrieval to recover missing structure.
- These dual‑gating mechanisms maintain high detection accuracy under heavy occlusion while achieving F1 and mIoU scores comparable to existing methods.

## Context
Temporal consistency is a persistent challenge in video lane detection because occlusions disrupt the flow of visual cues across frames. Traditional approaches rely on auxiliary obstacle masks that only indirectly protect model states, leading to lingering errors. SIGMA-Lane addresses this by embedding occlusion handling into the core temporal modeling framework, offering a more robust solution.

## Implications
For autonomous driving systems, maintaining reliable lane predictions is critical for safety and navigation. By integrating state‑level gating with historical priors, SIGMA-Lane can reduce false detections caused by temporary occlusions, improving overall system trustworthiness. Practitioners can adopt this framework to enhance video analytics pipelines where temporal stability directly impacts performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16338v1)
