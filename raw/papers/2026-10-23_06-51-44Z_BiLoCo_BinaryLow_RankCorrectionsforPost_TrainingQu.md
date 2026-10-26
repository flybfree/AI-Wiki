---
title: BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization
published: 2026-10-23T06:51:44Z
authors: David Jin, Beshr IslamBouli, Tarushii Goel, Han Guo, Yoon Kim
url: http://arxiv.org/abs/2610.32243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization

## Abstract
Post-training quantization (PTQ) to FP4 has emerged as a key technique for reducing large language model inference cost, especially on Blackwell GPUs, which offer native FP4 tensor core support. Direct PTQ to FP4, however, still leaves a noticeable accuracy gap. Recent work on SVDQuant mitigates the errors introduced through FP4 quantization for diffusion models by adding high-precision low-rank corrections obtained via SVD. However, this high-precision low-rank correction requires many bits per rank, and it runs on the same tensor cores as the main FP4 GEMM. We introduce BiLoCo, a low-rank correction method whose left and right factors are stored as binary ${\{\pm 1\}}$ sign vectors rather than as BF16 numbers. The signed format uses $16{\times}$ less storage per rank-one component, and since the correction now consists of additions/subtractions, this can be run on CUDA cores concurrently with the FP4 tensor-core GEMM. On 4B--72B LLMs, BiLoCo matches or improves memory-matched SVDQuant for PTQ. We implement BiLoCo on B300 as a fused single kernel, where the FP4 GEMM runs on tensor cores, the bit-packed correction on the CUDA cores of the same launch, and the two are combined in the GEMM epilogue. With batch size $1$, the fused kernel is at most $11\%$ slower than the FP4-only GEMM for every rank up to $512$. At rank $128$, it is at most $20\%$ slower up to batch size $8$.

## Metadata
- **Published**: 2026-10-23T06:51:44Z
- **Authors**: David Jin, Beshr IslamBouli, Tarushii Goel, Han Guo, Yoon Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32243v1)