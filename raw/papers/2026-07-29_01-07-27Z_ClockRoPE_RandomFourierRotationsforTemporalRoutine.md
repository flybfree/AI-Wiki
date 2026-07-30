---
title: ClockRoPE: Random Fourier Rotations for Temporal Routine Modeling
published: 2026-07-29T01:07:27Z
authors: Yiwen Chen, Joshua Ainslie, Krzysztof Choromanski, Xiang Gao, Su-Lin Wu, Yiping Yuan, Qian Sun
url: http://arxiv.org/abs/2607.26369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClockRoPE: Random Fourier Rotations for Temporal Routine Modeling

## Abstract
Rotary Position Embedding (RoPE) has been widely adopted in transformer-based large language models. However, its log-linear frequency schedule, originally designed to produce long-term attention decay, limits its adoption in domains with more complex distance-correlation patterns, such as temporal periodicity in sequential recommendation. We investigate the expressiveness of general query/key rotations and find that any normalized continuous positive-definite attention modulation function can be approximated by random rotations induced by its own Fourier transform, which we term Random Fourier Rotations. Building on this theory, we propose ClockRoPE for routine modeling in sequential recommendation, where rotation frequencies are derived from periodic attention modulation functions. In online A/B tests, ClockRoPE demonstrates consistent improvements in valued engagement metrics, and has been successfully deployed in production-scale generative retrieval system at a major video-sharing platform.

## Metadata
- **Published**: 2026-07-29T01:07:27Z
- **Authors**: Yiwen Chen, Joshua Ainslie, Krzysztof Choromanski, Xiang Gao, Su-Lin Wu, Yiping Yuan, Qian Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26369v1)