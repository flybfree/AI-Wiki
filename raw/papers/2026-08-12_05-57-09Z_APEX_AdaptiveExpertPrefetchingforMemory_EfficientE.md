---
title: APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference
published: 2026-08-12T05:57:09Z
authors: Alish Kanani, Layan Badawi, Umit Y. Ogras
url: http://arxiv.org/abs/2608.11688v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference

## Abstract
Mixture-of-Experts (MoE) models are attractive for edge deployment because they provide high model capacity while activating only a small subset of parameters per token, improving compute efficiency. However, MoE inference at the edge is fundamentally limited by memory. Expert parameters are large and often reside in off-chip memory due to capacity, cost, and power constraints, putting expert loading to the critical path. We present APEX: Adaptive Expert Prefetching, a predictive resource management framework that overlaps expert loading with useful computation. APEX introduces a lightweight prefetch router that predicts candidate experts before the attention block to dynamically fetch additional experts using a learned confidence model. This adaptive strategy achieves over 99% overlap accuracy, significantly outperforming fixed top-k prefetching techniques. APEX supports two execution modes: a correctness-preserving mode that guarantees exact routing semantics, and a stall-free mode that eliminates residual stalls by operating on available experts with negligible impact on application accuracy. Across multiple MoE models, the correctness-preserving mode reduces per-token latency by up to 26% and improves energy-delay product (EDP) by up to 41% over state-of-the-art baselines, while the stall-free mode provides additional efficiency gains with negligible impact on application accuracy. These results establish adaptive, confidence-driven expert prefetching as an effective approach for efficient MoE inference on edge systems.

## Metadata
- **Published**: 2026-08-12T05:57:09Z
- **Authors**: Alish Kanani, Layan Badawi, Umit Y. Ogras
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11688v1)