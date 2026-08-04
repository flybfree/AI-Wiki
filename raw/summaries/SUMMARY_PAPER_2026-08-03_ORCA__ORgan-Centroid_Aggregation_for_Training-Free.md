---
title: ORCA: ORgan-Centroid Aggregation for Training-Free 3D CT Visual Token Compression
url: http://arxiv.org/abs/2608.00345v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_23-27-39Z_ORCA_ORgan_CentroidAggregationforTraining_Free3DCT.md
generated_at: 2026-08-03 23:45
model: nvidia/nemotron-3-nano-4b
---

## Summary
ORCA introduces a training‑free token compression method for 3D CT scans that merges adjacent tokens guided by organ boundaries while preserving spatial centroid information. The approach reduces visual context size by a factor of sixty‑four and key‑value cache size by fifty, delivering faster downstream processing.

## Key Takeaways
- ORCA merges adjacent tokens using organ guidance to avoid blurring distinct anatomy, lesion, or air into single tokens.
- It adds sinusoidal encoding of each region’s centroid to retain spatial layout across the compressed token set.
- The method is fully training‑free and plug‑and‑play, producing an adjustable token set without changing any encoder or text query.

## Context
In vision‑language models, long 3D CT sequences are a bottleneck for efficient multimodal learning. Existing compression techniques often sacrifice anatomical fidelity, limiting model performance.

## Implications
This work enables faster inference and lower memory usage in medical imaging applications that rely on vision‑language pipelines. Practitioners can adopt ORCA without retraining existing models, accelerating deployment of AI diagnostics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00345v1)
