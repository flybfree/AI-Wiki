---
title: A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference
published: 2026-07-27T08:29:05Z
authors: Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan
url: http://arxiv.org/abs/2607.24148v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference

## Abstract
Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited.   In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution dynamics. We first introduce MotionVQ, a motion-aware vector quantization scheme that dynamically adjusts quantization precision based on the robot's execution state, reducing memory access while preserving task success rate. We then propose a merged-centroid vectorized GEMM paradigm that operates on the codebook-index representation, eliminating redundant multiplications through spatial aggregation and temporal reuse of centroids. To realize these optimizations, we design an accelerator that efficiently supports dynamic precision selection and centroid-reuse computation. Experimental results show that VQVLA achieves 6.5x, 2.8x, 1.9x, 3.3x, and 4.3x speedup over the A100 GPU, Dadu-Corki, LUT-DLA, CodeGEMM, and ShiftAddLLM, respectively, with negligible accuracy degradation.

## Metadata
- **Published**: 2026-07-27T08:29:05Z
- **Authors**: Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24148v1)