---
title: Liquid Gated Attention
published: 2026-08-31T12:30:09Z
authors: Yiheng Jiang, Yuanbo Xu, Yongjian Yang
url: http://arxiv.org/abs/2608.30695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Liquid Gated Attention

## Abstract
Real-world time series often exhibit irregular sampling and extended temporal horizons, requiring models to capture continuous-time dynamics across arbitrary intervals without prohibitive scaling costs. Discrete-time methods collapse variable time intervals into static positional steps; solver-dependent continuous-time models preserve temporal structure but rely on sequential integration, precluding parallelization; and solver-free approximations avoid this cost yet none couples observed time intervals with input-driven state modulation. We propose Liquid Gated Attention (LGA), a solver-free parallel temporal operator. By parameterizing an input-driven gating mechanism with observed time intervals, LGA introduces a continuous-time inductive bias and formulates hidden state evolution as a fast-weight associative memory, enabling parallel computation across the temporal dimension. Using matrix associativity in non-causal encoding and a prefix scan in causal encoding, LGA attains linear temporal complexity in sequence length in both modes. A sequence-level normalization bounds cumulative temporal decay for stable long-horizon optimization. Building on LGA, we instantiate LFormer, a modular backbone for continuous-time representation learning. Across six tasks and sixteen datasets spanning up to 17,984 steps, LFormer demonstrates long-range dependency modeling, fine-grained state tracking, and trajectory reconstruction from sparse and noisy observations, while delivering competitive performance against state-of-the-art discrete-time and continuous-time baselines with linear scaling efficiency.

## Metadata
- **Published**: 2026-08-31T12:30:09Z
- **Authors**: Yiheng Jiang, Yuanbo Xu, Yongjian Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30695v1)