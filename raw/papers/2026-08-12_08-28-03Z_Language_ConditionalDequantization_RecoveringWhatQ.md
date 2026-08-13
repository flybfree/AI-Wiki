---
title: Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages
published: 2026-08-12T08:28:03Z
authors: Nirmal Thomas
url: http://arxiv.org/abs/2608.11786v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages

## Abstract
Aggressive quantization disproportionately harms multilingual capability: in the sub-4B INT3 GPTQ regime, we measure 2-4x larger perplexity degradation on non-English languages than on English. We propose Language-Conditional Dequantization (LCD), a post-hoc method that attaches per-language rank-2 LoRA corrections to the linear layers of an already-quantized model, adding 0.12% parameters per language and training in under 20 minutes on a single GPU. Across Qwen2.5-3B and Llama-3.2-3B, LCD recovers 70-83% of the perplexity gap for non-Latin script languages and 17-28% of the GlobalMMLU accuracy gap, outperforming a language-agnostic correction of equal capacity by 3-9 points on typologically distant languages and a data-free low-rank baseline (LQER) by an order of magnitude. We further identify a perplexity-accuracy disconnect and trace it to where quantization concentrates damage: early-depth errors (Llama) propagate downstream and resist local correction, while late-depth errors (Qwen) do not. A layer-restricted variant of LCD validates this mechanism directly.

## Metadata
- **Published**: 2026-08-12T08:28:03Z
- **Authors**: Nirmal Thomas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11786v1)