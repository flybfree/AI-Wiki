---
title: Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression
published: 2026-10-05T09:25:08Z
authors: Hankyul Kang, Jongbin Ryu
url: http://arxiv.org/abs/2610.06026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression

## Abstract
SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models. In these methods, compression is performed in two stages: components are first truncated, and the remaining ones are subsequently quantized. Although this decoupled pipeline benefits from both pruning and quantization, it requires separate optimization for each stage and fails to fully exploit their balance, which can lead to suboptimal performance under aggressive compression. To address this limitation, we propose a new LLM compression method that co-optimizes pruning and quantization in a unified framework. Our key idea is a differentiable method for learning component-wise bit-widths, allowing less important components to be assigned 0-bit precision and pruned away. Notably, our method performs favorably against two-stage baselines, even when subjected to extreme quantization settings ($1.61$ bits) designed for ultra-efficiency. Code: https://github.com/MMAI-Laboratory/DBW.

## Metadata
- **Published**: 2026-10-05T09:25:08Z
- **Authors**: Hankyul Kang, Jongbin Ryu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06026v1)