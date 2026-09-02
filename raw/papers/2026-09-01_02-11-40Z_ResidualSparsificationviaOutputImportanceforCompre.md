---
title: Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs
published: 2026-09-01T02:11:40Z
authors: Seungwoo Jung, Dohyeok Kwon, Seungmin Cha, Junseok Lee, Yeonho Yoo, Chuck Yoo, Gyeongsik Yang
url: http://arxiv.org/abs/2609.00575v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs

## Abstract
Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by minimizing its compression error, thereby minimizing the error of each projection matrix. However, our analysis shows that this objective is misaligned with preserving model accuracy after compression. In an expert, the final output is produced through computations coupled across multiple projections and hidden representations. Therefore, even small errors in individual matrices can propagate through hidden representations and projection interactions, leading to large expert output errors and accuracy degradation. To address this misalignment, we propose PARSER, a new residual sparsification method that shifts the compression objective from minimizing isolated matrix errors to preserving the expert output error. PARSER achieves this by introducing output importance, which measures the actual contribution to the expert output error. Our experiments show that, compared with existing methods, PARSER narrows the accuracy gap to the uncompressed model by 1.41$\times$ on Qwen and 1.44$\times$ on DeepSeek, while achieving the same peak memory reduction.

## Metadata
- **Published**: 2026-09-01T02:11:40Z
- **Authors**: Seungwoo Jung, Dohyeok Kwon, Seungmin Cha, Junseok Lee, Yeonho Yoo, Chuck Yoo, Gyeongsik Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00575v1)