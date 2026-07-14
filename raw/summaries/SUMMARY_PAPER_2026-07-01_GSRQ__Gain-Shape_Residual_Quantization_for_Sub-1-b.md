---
title: "Summary: GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache"
url: http://arxiv.org/abs/2607.01065v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_15-25-21Z_GSRQ_Gain_ShapeResidualQuantizationforSub_1_bitKVC.md
generated_at: 2026-07-01 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Gain‑Shape Residual Quantization (GSRQ), a method that reduces the memory footprint of key‑value caches in large language models to sub‑1‑bit levels. By replacing standard K‑means with a directional‑aware variant called Gain‑Shape K‑means, GSRQ improves quantization accuracy on LLaMA‑3‑8B across various bit rates, achieving a 22.20 percentage point gain at 1‑bit compared to VQLLM.

## Key Takeaways
- The Euclidean centroid averaging used in standard K‑means can cause centroid shrinkage, weakening the angular alignment term and harming directional preservation.
- Gain‑Shape K‑means mitigates this issue by preserving directionality while matching or improving ℓ₂ distortion.
- GSRQ integrates this improved codebook learning into a residual quantization pipeline, delivering substantial accuracy improvements on LongBench tasks.

## Context
The linear growth of key‑value cache memory limits the practical use of extended context windows in large language models. Vector quantization techniques aim to compress these caches toward sub‑1‑bit storage, but most existing approaches suffer from high distortion due to centroid shrinkage. This paper tackles a fundamental limitation by rethinking the core K‑means learning process.

## Implications
For practitioners developing long‑context LLMs, GSRQ offers a practical path to lower memory usage without sacrificing performance, enabling more scalable deployment. The industry can leverage this approach to reduce hardware costs and improve latency in real‑time applications that rely on extended context processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01065v1)
