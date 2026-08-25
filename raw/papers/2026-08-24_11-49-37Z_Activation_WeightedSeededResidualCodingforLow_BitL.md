---
title: Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair
published: 2026-08-24T11:49:37Z
authors: Zehao Liu, Chuangchuang Fang, Yang Ren
url: http://arxiv.org/abs/2608.23144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair

## Abstract
Low-bit weight quantization saves storage but leaves errors that degrade language-model quality. We introduce Activation-Weighted Seeded Residual Coding (AWSRC), a compact repair codec for an existing quantization backbone. Given a reconstructed weight $W_0$, AWSRC encodes the residual $W-W_0$ using deterministic seed-generated bases. The sidecar stores seed selectors, low-bit coefficients, and scales rather than an explicit codebook. Activation statistics prioritize errors that affect layer outputs. On Qwen2.5-3B-Instruct, adding 0.162 scope-bits/weight to an INT4 RTN backbone closes 88.2%, 78.9%, and 71.3% of the matched PPL, KL, and accuracy gaps to BF16. Repairing a matched strong low-bit backbone also improves all measured quality metrics. With a matched 49.25 MB sidecar, about 0.8% of the BF16 model-weight payload, AWSRC gives the best perplexity and mean task accuracy among sparse, low-rank, and vector-quantized codecs.

## Metadata
- **Published**: 2026-08-24T11:49:37Z
- **Authors**: Zehao Liu, Chuangchuang Fang, Yang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23144v1)