---
title: LowRankArena: A Standardized Evaluation Platform for SVD-Based LLM Compression
published: 2026-08-26T20:27:21Z
authors: Zishan Shao, Lixun Zhang, Kangning Cui, Wenhao Wu, Jinhee Kim, Yixiao Wang, Ting Jiang, Hancheng Ye, Qinsi Wang, Fan Yang, Danyang Zhuo, Yiran Chen, Hai Li
url: http://arxiv.org/abs/2608.26389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LowRankArena: A Standardized Evaluation Platform for SVD-Based LLM Compression

## Abstract
SVD-based low-rank compression has become a fast-growing direction for reducing the memory and computational cost of large language models (LLMs). However, meaningful comparison across existing studies remains difficult as prior evaluations use varied benchmarks, inconsistent ratios, and diverse setups, often failing to isolate low-rank effects from auxiliary techniques. As a result, it remains unclear whether reported gains reflect method-level improvements or differences in evaluation protocol. This lack of comparability highlights the need for a unified, reproducible evaluation platform. To address this problem, we present LowRankArena, a standardized evaluation platform for SVD-based LLM compression. LowRankArena unifies task versions, uniform-precision compression budgets, comparison regimes, and inference measurements, and provides a reproducible pipeline with over 3 TiB released compressed checkpoints. Using LowRankArena, our aligned audit of five representative SVD methods reveals that prior findings are highly conditional under standardized protocols: clear leaders and performance tiers shift across backbones and keep ratios, multiple-choice accuracy can hide large perplexity degradation, and nominal low-rank savings yield workload-dependent and often limited end-to-end speedups. Our code is available at: https://github.com/Zishan-Shao/lowrankarena.git.

## Metadata
- **Published**: 2026-08-26T20:27:21Z
- **Authors**: Zishan Shao, Lixun Zhang, Kangning Cui, Wenhao Wu, Jinhee Kim, Yixiao Wang, Ting Jiang, Hancheng Ye, Qinsi Wang, Fan Yang, Danyang Zhuo, Yiran Chen, Hai Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26389v1)