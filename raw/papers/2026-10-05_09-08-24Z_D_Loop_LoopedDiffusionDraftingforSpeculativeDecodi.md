---
title: D-Loop: Looped Diffusion Drafting for Speculative Decoding
published: 2026-10-05T09:08:24Z
authors: Kecheng Chen, Yuyang He, Cheng Gong, Hui Liu, Guoping Long, Jiajun Li, Shi Wu, Suiyun Zhang, Haoliang Li, Ziru Liu, Rui Liu
url: http://arxiv.org/abs/2610.06011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D-Loop: Looped Diffusion Drafting for Speculative Decoding

## Abstract
Block diffusion accelerates speculative decoding by drafting multiple tokens in one forward pass. However, each position predicts a marginal distribution without observing earlier proposed tokens, limiting draft quality and acceptance length. We identify a concrete failure, the \emph{repetition trap}, in which neighboring positions produce redundant copies of the same token. We explain this tendency theoretically and empirically examine its association with shorter accepted drafts. Recent methods refine marginal predictions with an additional causal head or a separately trained drafter, increasing parameter storage and introducing separate training objectives. We instead propose D-Loop, which introduces \emph{intra-block causal conditioning} within the original diffusion drafter without additional model components. Inspired by semi-autoregressive generation and parameter sharing, D-Loop reuses the same backbone across looped passes. The first pass proposes a block, and the second conditions on a selected prefix to regenerate the suffix in parallel. A complementary prefix--suffix objective trains the shared drafter for both anchor-only prefix prediction and prefix-conditioned suffix prediction. Across eight math, code, and chat benchmarks, D-Loop can beat DFlash and DSpark on Qwen3-4B and Qwen3-8B with obvious gains.

## Metadata
- **Published**: 2026-10-05T09:08:24Z
- **Authors**: Kecheng Chen, Yuyang He, Cheng Gong, Hui Liu, Guoping Long, Jiajun Li, Shi Wu, Suiyun Zhang, Haoliang Li, Ziru Liu, Rui Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06011v1)