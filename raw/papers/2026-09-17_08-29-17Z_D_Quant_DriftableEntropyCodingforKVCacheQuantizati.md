---
title: D-Quant: Driftable Entropy Coding for KV Cache Quantization
published: 2026-09-17T08:29:17Z
authors: Yi Su, Hong Liu, Guanghua Yu, Jianchen Zhu
url: http://arxiv.org/abs/2609.19880v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D-Quant: Driftable Entropy Coding for KV Cache Quantization

## Abstract
The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bit width decreases, the number of available levels shrinks exponentially, leading to severe information loss and rapid performance degradation. We further observe that fixed-width quantization fails to exploit the highly non-uniform distribution of KV cache. After rotation and normalization, KV values approximately follow a normal distribution, with most values concentrated near the center and only a small fraction appearing in the tails. Nevertheless, fixed-width coding allocates the same number of bits to frequent and rare symbols. Entropy coding naturally exploits such non-uniformity by assigning shorter codewords to frequent symbols and longer ones to rare symbols, substantially reducing the average number of bits required for representation. However, its variable-length output is not suited to highly parallel attention kernels, where efficient dequantization and computation rely on regular memory layouts and fixed-stride accesses. To bridge this gap, we propose \textbf{D-Quant}, a flexible KV cache quantization framework that introduces a \textbf{drift} mechanism to convert entropy-coded representations of each token into fixed-size bitstreams, enabling regular memory access and parallel dequantization within attention kernels.

## Metadata
- **Published**: 2026-09-17T08:29:17Z
- **Authors**: Yi Su, Hong Liu, Guanghua Yu, Jianchen Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19880v1)