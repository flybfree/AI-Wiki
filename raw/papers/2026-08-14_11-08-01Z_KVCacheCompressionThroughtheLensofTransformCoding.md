---
title: KV Cache Compression Through the Lens of Transform Coding
published: 2026-08-14T11:08:01Z
authors: Hannah Laus, Claudio Mayrink Verdun, Hao Wang, Flavio du Pin Calmon, Felix Krahmer
url: http://arxiv.org/abs/2608.14191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KV Cache Compression Through the Lens of Transform Coding

## Abstract
The key-value (KV) cache stores information from past tokens and is a major memory bottleneck in long-context inference. Existing quantization methods address this bottleneck by representing the KV cache uniformly with lower-precision data types and designing quantization schemes to minimize reconstruction error in the cache itself, without accounting for how that error propagates through attention mechanisms. We prove that, under a white-noise quantization model, the expected attention-aware distortion decomposes into additive key and value contributions that factor across tokens and channels. Building on transform coding and reverse water-filling, which are classical tools from signal processing and rate-distortion theory, we introduce Attention-Aware Transform Coding (AATC), which allocates bits over a calibration set to minimize attention-aware distortion. On Llama-3.1-8B-Instruct and Qwen-2.5-7B-Instruct, evaluated across LongBench, RULER, GSM8K, MMLU-Pro, and MATH-500, our method achieves near-lossless accuracy at approximately $5.8\times$ compression, whereas each baseline degrades in at least some settings.

## Metadata
- **Published**: 2026-08-14T11:08:01Z
- **Authors**: Hannah Laus, Claudio Mayrink Verdun, Hao Wang, Flavio du Pin Calmon, Felix Krahmer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14191v1)