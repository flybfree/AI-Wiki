---
title: GeoDistill-Refine: Silhouette-First Geometry Distillation for Annotation-Free Spacecraft Segmentation
url: http://arxiv.org/abs/2608.07405v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_16-53-05Z_GeoDistill_Refine_Silhouette_FirstGeometryDistilla.md
generated_at: 2026-08-09 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
GeoDistill-Refine is a two‑stage framework that transfers offline SAM 3 pseudo‑masks to a compact segmentation network while correcting geometric errors. On the SpaceSense‑Bench HJM lockbox set it improves Image IoU by 0.0456 and Boundary F1 by 0.1380 over a plain pseudo‑label student.

## Key Takeaways
- The framework fuses six fixed prompts via an unweighted vote to stabilize the teacher output, reducing variation from textual prompts.
- It employs a sample‑level gate that combines prompt agreement, valid‑prompt ratio, and pseudo‑mask area plausibility to filter unreliable geometry.
- A tiny TinyUNet with 0.263 M parameters achieves near‑SAM performance in inference time of about 1.1 ms on an RTX 4090.

## Context
Foundation segmentation models are valuable for annotation‑free spacecraft imagery but suffer from prompt sensitivity and geometric drift during distillation, limiting practical deployment.

## Implications
This work enables lightweight, accurate segmentation pipelines that can run locally on edge hardware without manual masks, supporting real‑time monitoring of satellite or drone imagery. It also shows how structured geometry objectives improve model robustness in AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07405v1)
