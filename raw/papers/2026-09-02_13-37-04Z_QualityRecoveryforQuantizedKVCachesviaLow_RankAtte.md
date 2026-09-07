---
title: Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation
published: 2026-09-02T13:37:04Z
authors: Seifeldin Abdellatif
url: http://arxiv.org/abs/2609.04263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quality Recovery for Quantized KV Caches via Low-Rank Attention Adaptation

## Abstract
Low-bit key--value (KV) caches reduce the memory required for autoregressive decoding, but the resulting quality loss depends on the model and quantizer. We keep the quantizer fixed and distill the floating-cache model's behavior into low-rank Q/K/V projection updates while the student executes a physically packed incremental cache. Across three seeds, 4-bit affine-cache adapters recover $54.24\%\pm2.47\%$ of the held-out perplexity gap on TinyLlama-1.1B and $75.96\%\pm4.04\%$ on Gemma-4-12B. On the same frozen NF4 Llama-3.1-8B base, one validation-selected run per quantizer recovers $60.42\%$ under KIVI K2V2 and $37.61\%$ under KVarN K4V2, while preserving 180-case associative retrieval. Gemma's score on an official 4K/8K RULER subset rises from 42.80 with the unadapted 4-bit cache to 48.33 after adaptation (46.15 floating), with substantial task heterogeneity. Finally, a 2-bit rank--token sweep reduces TinyLlama's 2-bit PPL from 576.10 to $11.4000\pm0.0059$ across three seeds, versus 10.3988 floating, but restores only 11--12 of 180 retrieval cases. These results show that low-rank projection adaptation can recover held-out quality across fixed cache formats, while perplexity recovery need not restore long-context retrieval.

## Metadata
- **Published**: 2026-09-02T13:37:04Z
- **Authors**: Seifeldin Abdellatif
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04263v1)