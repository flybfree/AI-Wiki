---
title: Benchmarking Deep Learning Approaches for AEC Engineering Drawing Layout Detection and Information Extraction
url: http://arxiv.org/abs/2607.18997v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_11-30-32Z_BenchmarkingDeepLearningApproachesforAECEngineerin.md
generated_at: 2026-07-23 23:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of extracting information from Architecture, Engineering, and Construction drawings by first detecting their layout structures. The study builds a dedicated AEC-specific dataset and evaluates five deep learning models, reporting that RF-DETR achieves an mAP50 of 0.949 while Qwen3-VL reaches an F1-score of 0.911, outperforming general document models.

## Key Takeaways
- RF-DETR attains state‑of‑the‑art layout detection with an $mAP_{50}$ of 0.949, demonstrating superior ability to map graphical and textual elements in AEC drawings.  
- Qwen3-VL reaches a leading F1-score of 0.911, showing that vision‑language models can effectively combine visual layout cues with textual content for extraction tasks.  
- Models trained on general document datasets suffer from domain interference, causing noticeable performance degradation when applied to engineering drawings.

## Context
The integration of deep learning into AEC workflows is gaining momentum as manual data processing becomes increasingly costly and error‑prone. Existing research often reuses models optimized for generic text or image tasks without considering the unique hierarchical nature of engineering drawings, leading to suboptimal results. This work fills that gap by creating a specialized benchmark.

## Implications
Automated layout detection can streamline information extraction across large AEC projects, reducing labor costs and accelerating design reviews. Practitioners can leverage these models to extract specifications directly from drawings, improving data consistency and enabling smarter decision‑making in construction planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18997v1)
