---
title: SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization
published: 2026-08-16T06:29:10Z
authors: Gunjun Lee, Sehwan Son, Younjoo Lee, Byungjun Kim, Jung Ho Ahn
url: http://arxiv.org/abs/2608.15567v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization

## Abstract
Weight-only post-training quantization (PTQ) enables the deployment of large language models under tight memory budgets, but accuracy often collapses at 2-3 bits. Existing backpropagation-free PTQ optimizers have two limitations: group decisions ignore the correction that the remaining continuous suffix can absorb, and discrete refinements typically keep the affine quantization grid fixed. We introduce SCHUROPT, which analytically eliminates the suffix's optimal continuous response, yielding an exact groupwise quadratic with Schur-complement curvature. It then alternates closed-form row-wise scale/zero-point refitting with coordinate descent over integer codes. With the GPTQ objective fixed, SCHUROPT improves mean zero-shot accuracy on 2-bit Qwen3-4B by 11.88 percentage points (pp). At higher precision, however, tighter reconstruction does not consistently improve end-model metrics. SCHURQUANT therefore combines SCHUROPT with quantized-prefix teacher reconstruction, reference-weight regularization, residual-add targets, and teacher-decision token weighting. Across eight Llama and Qwen models, SCHURQUANT achieves the highest mean zero-shot accuracy among the evaluated backpropagation free PTQ baselines, outperforming the strongest baseline by 9.65 pp at 2 bits.

## Metadata
- **Published**: 2026-08-16T06:29:10Z
- **Authors**: Gunjun Lee, Sehwan Son, Younjoo Lee, Byungjun Kim, Jung Ho Ahn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15567v1)