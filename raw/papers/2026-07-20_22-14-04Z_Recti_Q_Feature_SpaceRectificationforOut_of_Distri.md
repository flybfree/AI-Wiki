---
title: Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics
published: 2026-07-20T22:14:04Z
authors: Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin
url: http://arxiv.org/abs/2607.18540v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics

## Abstract
Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference. However, while PTQ often preserves clean in-distribution accuracy, we show that it can substantially degrade reliability under deployment-relevant distribution shifts (e.g., sensor noise, severe weather, and novel operating environments), creating a Quantization-Induced Robustness Gap. Across foundational vision benchmarks (ImageNet-C and PACS), 4-bit PTQ models exhibit pronounced robustness degradation despite negligible ID accuracy loss. To address this, we propose Recti-Q, a lightweight feature-space rectification framework that freezes the quantized backbone and trains a small classifier-head LoRA adapter using only source data. Recti-Q is architecture-agnostic across CNNs and Transformers, supports efficient teacher-free training, and recovers a significant portion of the lost robustness, in some cases matching or exceeding FP32 performance. At less than 1% parameter overhead (as small as 6 KB), Recti-Q preserves over 99% of PTQ memory savings, adds negligible compute, and enables low-bandwidth Over-The-Air (OTA) resilience patching for deployed robotic fleets operating in unpredictable physical environments.

## Metadata
- **Published**: 2026-07-20T22:14:04Z
- **Authors**: Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18540v1)