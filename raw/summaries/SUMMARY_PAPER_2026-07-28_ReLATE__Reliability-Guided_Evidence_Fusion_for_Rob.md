---
title: ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization
url: http://arxiv.org/abs/2607.25524v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_10-07-18Z_ReLATE_Reliability_GuidedEvidenceFusionforRobustUA.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces UAVSat-Deg, a large‑scale benchmark for degraded UAV‑satellite geo‑localization that tests 27 types of image corruption across three severity levels. The proposed ReLATE framework learns reliable evidence and adapts token integration to improve robustness while preserving clean‑image performance.

## Key Takeaways
- UAVSat-Deg provides a comprehensive dataset with over 11.7 million pre‑generated corrupted images, enabling systematic evaluation of degradation effects on geo‑localization tasks.
- ReLATE’s reliability‑adaptive fusion learns a structure‑smoothed reliability field per visual token, allowing it to prioritize trustworthy evidence and mitigate the impact of compound corruptions.
- The method achieves the highest average performance across both test sets and retrieval directions while maintaining competitive accuracy on clean images.

## Context
The integration of UAV and satellite imagery is crucial for large‑scale mapping and monitoring, yet real‑world conditions introduce severe visual degradations that degrade existing models. This work addresses the gap by creating a realistic benchmark and developing a reliability‑aware fusion strategy tailored to such challenges.

## Implications
For practitioners, ReLATE offers a practical solution to improve robustness in UAV‑satellite fusion pipelines without sacrificing overall accuracy. The released code and dataset will accelerate research and deployment of reliable geolocation systems in challenging environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25524v1)
