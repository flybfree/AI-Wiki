---
title: DeltaFlow: Noise-Adaptive Bidirectional Gated Delta Networks for Embedded Language Flows
published: 2026-08-02T13:48:40Z
authors: Guangfu Guo, Xiaoqian Lu, Linsey Pang, Weiran Yao, Haolin Chen, Kunpeng Liu, Long Cheng
url: http://arxiv.org/abs/2608.01240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeltaFlow: Noise-Adaptive Bidirectional Gated Delta Networks for Embedded Language Flows

## Abstract
Embedded Language Flows (ELF) rely primarily on full non-causal attention for iterative denoising, repeatedly incurring quadratic sequence-mixing cost at each sampling step. Gated Delta Networks (GDNs) provide an efficient recurrent alternative, but their standard causal formulation cannot directly capture the bidirectional context required by ELF. We introduce DeltaFlow, a noise-adaptive bidirectional GDN backbone for continuous language denoising. We study two variants: DeltaFlow-A, which alternates scan directions across layers, and DeltaFlow-P, which performs parallel forward and backward scans within each layer. We further introduce noise-adaptive memory control and scheduled Temporal State Consistency (TSC) to stabilize hidden representations across nearby noise levels. On OpenWebText, using a 32-step stochastic differential equation sampler, DeltaFlow-P reduces generated perplexity from 24.218 for the full-attention ELF baseline to 21.228 while maintaining comparable unigram entropy, with 36B training-token exposure compared with 45B for the baseline. In a denoiser-only benchmark, DeltaFlow-P achieves a 2.72x throughput speedup over the full-attention baseline at a sequence length of 16k. These results show that DeltaFlow is a promising alternative to dense attention for efficient continuous language denoising.

## Metadata
- **Published**: 2026-08-02T13:48:40Z
- **Authors**: Guangfu Guo, Xiaoqian Lu, Linsey Pang, Weiran Yao, Haolin Chen, Kunpeng Liu, Long Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01240v1)