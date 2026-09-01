---
title: SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference
published: 2026-08-28T22:19:47Z
authors: Daeha Lee, Do-Hyung Kim, Jae-Hong Kim
url: http://arxiv.org/abs/2608.28911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference

## Abstract
The key-value (KV) cache is the dominant memory bottleneck of long-context large language model (LLM) inference, growing linearly with context length. We show that uniform KV quantization on a fractional-bit grid does not degrade gracefully: under a prespecified multi-seed statistical protocol, Llama-3.1-8B-Instruct with an affine quantizer is statistically indistinguishable from FP16 KV down to 2.322 code bits/value and collapses at 2.0 bits - a quality cliff in (2.0, 2.322] that reappears in generation-time quantization and multi-turn dialogue and transfers to Mistral-7B. The cliff reframes importance-aware mixed precision: above it, eight model-internal importance indicators are statistically interchangeable, so the benefit of mixing is grid interpolation, reaching average precisions uniform quantization cannot realize. SemKV preserves every token, ranks tokens by a model-internal score, and assigns two adjacent above-cliff precisions, achieving a measured 6.0x storage reduction with no statistically detectable quality difference from full KV (n=900, three seeds), and outperforming FP16 token pruning granted a 1.5x larger memory budget. Replacing the affine base with a distortion-optimized quantizer (TurboQuant-MSE) lowers the cliff in every protocol tested, raising the no-detectable-loss operating point to 7.9x. The recipe: measure the cliff for the target deployment setting, then interpolate above it.

## Metadata
- **Published**: 2026-08-28T22:19:47Z
- **Authors**: Daeha Lee, Do-Hyung Kim, Jae-Hong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28911v1)