---
title: Stable FP4 Training via Transposition-Invariant Block Quantization
url: http://arxiv.org/abs/2607.24953v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_18-03-34Z_StableFP4TrainingviaTransposition_InvariantBlockQu.md
generated_at: 2026-07-28 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles the instability of training large language models at four-bit precision (FP4) by identifying scale inconsistency caused by tensor transposition in block quantization. The authors introduce a 2D block FP4 scheme with transposition‑invariant scaling, truncation‑free scaling, and stochastic rounding to keep gradients unbiased. Experiments on dense LLMs up to 7B parameters and a 30B MoE model show stable training with less than 1.3% perplexity loss compared to BF16.

## Key Takeaways
- Scale inconsistency from transposition is eliminated by using 2D block quantization that enforces identical scaling for forward and backward passes.
- Truncation‑free scaling combined with stochastic rounding reduces quantization error while preserving unbiased gradients.
- Mixed MXFP8 quantization applied only to attention projections allows efficient mixed‑precision training at scale.

## Context
Training LLMs at lower bit depths is essential for reducing memory and compute costs, yet most prior methods fail beyond FP8 due to gradient instability. This work provides a principled solution that aligns scaling across computation directions, enabling practical low‑bit optimization without sacrificing model quality.

## Implications
The approach offers a straightforward path to deploy 4-bit training in industry pipelines, lowering hardware requirements and energy consumption for large models. Practitioners can adopt the 2D block quantization framework to achieve near‑BF16 performance with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24953v1)
