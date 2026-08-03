---
title: DFSC: Error-Controlled Differentiable Mittag-Leffler Propagation for Fractional Scientific Machine Learning
published: 2026-07-31T05:29:25Z
authors: Ning Hu, Haitao Duan, Shuqun Li, Chuyang Hu
url: http://arxiv.org/abs/2607.29038v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DFSC: Error-Controlled Differentiable Mittag-Leffler Propagation for Fractional Scientific Machine Learning

## Abstract
Fractional scientific machine learning requires numerical operators that can be differentiated, batched, accelerated, and composed with neural networks. When the dominant linear fractional evolution is known through a Mittag-Leffler propagator, repeatedly reconstructing that response with a history solver or relearning it from data is unnecessary. We present DFSC, a PyTorch environment organized around the Mittag-Leffler Spectral Layer (MLSL). The layer separates known fractional propagation from data-driven corrections, so neural modules learn only unresolved dynamics while fractional orders and residual-network parameters are optimized jointly. Its adaptive algorithm increases special-function truncation depth or Lanczos dimension until successive differentiable evaluations satisfy a requested tolerance. In the negative-real alternating-series regime, DFSC additionally returns a certified first-omitted-term bound; outside that regime it explicitly labels estimates as empirical.   DFSC supports dense, sparse, matrix-free, self-adjoint, generalized, and controlled complex operator paths; trainable fractional orders; direct inverse problems; residual neural composition; and CPU/GPU execution. The certified series bound covers all 59 eligible reference cases, with median bound/error effectivity 1.246 for resolved errors. Reusing a prepared batched Lanczos basis gives identical fixed-path values and reduces repeated-query time by 4.61--7.11 times on CPU and 13.07--16.22 times on an RTX 5070, excluding one-time preparation. A 27-case inverse matrix finds full-rank local curvature throughout, while remaining explicitly model-conditional. External solver and mixed real-data results support DFSC as an error-aware optional primitive for matched fractional structure, rather than a general replacement for fractional solvers or neural models.

## Metadata
- **Published**: 2026-07-31T05:29:25Z
- **Authors**: Ning Hu, Haitao Duan, Shuqun Li, Chuyang Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29038v1)