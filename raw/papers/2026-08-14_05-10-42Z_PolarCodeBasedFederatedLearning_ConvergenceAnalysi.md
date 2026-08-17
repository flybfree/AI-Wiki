---
title: Polar Code Based Federated Learning: Convergence Analysis and Resource Allocation
published: 2026-08-14T05:10:42Z
authors: Han Xiao, Wei Kang, Nan Liu
url: http://arxiv.org/abs/2608.13961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Polar Code Based Federated Learning: Convergence Analysis and Resource Allocation

## Abstract
Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data; however, it faces significant communication bottlenecks and channel impairments in practice. Conventional network layer treatments either idealize the channel as error free or apply equal error protection (EEP) to transmitted model updates, failing to account for the inherently unequal importance of quantization bits within a single local model. To address this limitation, we propose a cross layer polar code based FL scheme that leverages the unequal error protection (UEP) property of polar codes under finite block lengths. Specifically, the proposed design selectively protects more significant quantization bits, thereby mitigating the detrimental effects of channel noise. We further provide a rigorous convergence analysis of the proposed scheme, deriving an upper bound on the convergence gap, which we then jointly optimize over the number of quantization bits and the polar code block length across all training iterations. Experimental results demonstrate that both constant and variable block length configurations of our polar code based scheme consistently achieve substantial performance gains over uncoded and LDPC-based EEP benchmarks, with the advantage becoming increasingly pronounced as the channel quality deteriorating. These findings confirm the efficacy of our cross-layer design in enhancing FL robustness and efficiency under realistic channel conditions.

## Metadata
- **Published**: 2026-08-14T05:10:42Z
- **Authors**: Han Xiao, Wei Kang, Nan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13961v1)