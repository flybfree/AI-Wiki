---
title: Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs
published: 2026-08-31T10:39:01Z
authors: Deokjae Lee, Sihun Chu, Hyun Oh Song
url: http://arxiv.org/abs/2608.30564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs

## Abstract
Mixed-precision quantization (MPQ) assigns a different bitwidth to each linear layer of a large language model (LLM) to minimize the quantization-induced quality loss under a fixed budget, but Mixture-of-Experts (MoE) models contain these layers in every expert of every MoE block, so the allocation space grows far larger than in a dense model. Existing methods either allocate within each block under a uniform per-block budget, or allocate across blocks through an additive proxy, and neither directly optimizes a model-level objective over the choices that couple the blocks. We propose Q-Strata, a bi-level allocator that ranks within-block assignments with a cheap proxy and allocates across blocks with a model-level objective evaluated on the assembled quantized model. Its inner stage caches a Pareto frontier of candidates per block over finely spaced budgets, leaving the outer stage to set one budget per block instead of a bitwidth for every linear layer. With the search reduced to one budget per block, the outer stage optimizes this model-level objective directly, capturing the inter-block coupling that additive proxies miss. On Mixtral-8x7B-Instruct, Qwen1.5-MoE-A2.7B, and DeepSeek-V2-Lite, Q-Strata consistently achieves lower WikiText2 perplexity than uniform-bitwidth GPTQ and the state-of-the-art MoE MPQ methods MxMoE and GEMQ in the low-bit regime. The code is available at https://github.com/snu-mllab/Q-Strata/tree/main.

## Metadata
- **Published**: 2026-08-31T10:39:01Z
- **Authors**: Deokjae Lee, Sihun Chu, Hyun Oh Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30564v1)