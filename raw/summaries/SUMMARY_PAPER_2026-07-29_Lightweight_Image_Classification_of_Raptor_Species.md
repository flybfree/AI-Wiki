---
title: Lightweight Image Classification of Raptor Species for Edge Devices: Rare-Species Dataset Expansion via Video Frame Extraction, Knowledge Distillation, and TensorRT Deployment
url: http://arxiv.org/abs/2607.26238v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_20-19-25Z_LightweightImageClassificationofRaptorSpeciesforEd.md
generated_at: 2026-07-29 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a lightweight raptor species classifier for edge devices using knowledge distillation, dataset expansion via video frame extraction, and TensorRT deployment. It achieves high macro recall while reducing parameters to one‑eighth of the teacher model.

## Key Takeaways
- Dataset expanded to 12,519 images with increased Steller's Sea Eagle count from 463 to 2050 using video-frame extraction.
- Ensemble of MobileNetV4, ViT-Small, EfficientNet-B0 yields macro recall 0.935 +/- 0.004 over five distillation seeds, outperforming conventional split with 97.5% teacher recall.
- TensorRT FP16 deployment on Jetson Orin Nano delivers 3.19 ms/image with 99.95% argmax agreement.

## Context
This work addresses the need for real-time wildlife classification in wind‑turbine collision mitigation, where edge constraints limit model size and latency. The integration of video‑derived data improves rare‑species representation beyond static images.

## Implications
The approach demonstrates that dataset curation and teacher re‑fine‑tuning can yield substantial performance gains with minimal parameter overhead, offering a scalable template for deploying specialized AI on resource‑constrained hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26238v1)
