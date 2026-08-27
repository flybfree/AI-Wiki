---
title: Group-Shared Low-Rank Approximation for Mobile-Efficient Pointwise Convolutions in Large-Kernel CNNs
url: http://arxiv.org/abs/2608.26069v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_17-36-35Z_Group_SharedLow_RankApproximationforMobile_Efficie.md
generated_at: 2026-08-26 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the storage bottleneck of large-kernel CNNs caused by pointwise convolutions. It introduces Channel Group‑Shared low‑rank approximation (CGS) that reduces parameters via structured sharing across channel groups. Experiments show CGS enables deployment on edge devices while preserving performance.

## Key Takeaways
- Pointwise convolutions dominate parameter volume (>87%) and cause storage and memory bandwidth issues on resource‑constrained devices.
- The CGS method uses SVD‑based group sharing to cut parameters without sacrificing accuracy, achieving a favorable balance between performance and cost.
- CGS reduces model loading latency and enables feasible deployment of large‑kernel CNNs such as RepLKNet‑31B on smartphones with limited RAM.

## Context
Large‑kernel CNNs provide deep receptive fields but suffer from quadratic parameter growth. Efficient architectures typically focus on depthwise separable convolutions, yet pointwise components remain a hidden cost driver for edge deployment. This work fills that gap by targeting the dominant bottleneck directly.

## Implications
For practitioners deploying vision models on smartphones and IoT devices, CGS offers a practical path to high‑performance inference without massive storage footprints. It may inspire similar group‑aware compressions in other large‑scale neural networks beyond CNNs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.26069v1)
