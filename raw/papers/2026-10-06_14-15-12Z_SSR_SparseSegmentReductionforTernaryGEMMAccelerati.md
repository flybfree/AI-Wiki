---
title: SSR: Sparse Segment Reduction for Ternary GEMM Acceleration
published: 2026-10-06T14:15:12Z
authors: Adeline Pittet, Shien Zhu, Valérie Verdan, Gustavo Alonso
url: http://arxiv.org/abs/2610.08403v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SSR: Sparse Segment Reduction for Ternary GEMM Acceleration

## Abstract
Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware. Ternary LLMs mitigate these demands through weight quantization via ternary values, achieving significant compression often with 50-90% sparsity. However, existing approaches have limitations: methods optimized for ternary weights, such as BitNet, redundant segment reduction (RSR), and its improved version RSR++, do not exploit sparsity structures, while conventional sparse formats neglect ternary characteristics, foregoing dual optimization opportunities.   In this paper, we introduce Sparse Segment Reduction (SSR), a ternary matrix multiplication method designed to accelerate the inference of ternary LLMs and general Ternary Weight Networks (TWNs). SSR has a dedicated optimized ternary data format and an algorithm that systematically exploits sparsity patterns through computation trees that scale with the sparsity. SSR provides theoretical gains with asymptotically faster inference than RSR++ for sparsity above 50%, while practical evaluations reveal performance improvements across all sparsity levels. Evaluation results show that SSR achieves 2.1-11.3x speedup over RSR++ on ternary GEMM with 45-95% sparsity. Furthermore, SSR achieves 3.5-6.3x end-to-end speedup and 4.9% of memory saving over RSR++ on the Llama-3 1B model inference.

## Metadata
- **Published**: 2026-10-06T14:15:12Z
- **Authors**: Adeline Pittet, Shien Zhu, Valérie Verdan, Gustavo Alonso
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08403v1)