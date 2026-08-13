---
title: Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention
published: 2026-08-11T20:49:34Z
authors: Vicente Opazo
url: http://arxiv.org/abs/2608.11427v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention

## Abstract
Full attention exposes every token pair, whereas kernel attention compresses a sequence into a fixed-dimensional sketch. We show that this distinction becomes exponential at the first context length containing two competing candidates. On Min-IP over Boolean inputs, rank-one normalized kernel attention solves every sequence of length at most two exactly. In contrast, any single normalized nonnegative kernel-attention head that succeeds on all three-token sequences with error strictly below $1/2$ requires $2^{Ω(m)}$ features, even with arbitrary finite-dimensional tokenwise values and an arbitrary query-dependent affine readout. Dense softmax solves the same task with $m$-dimensional scores and constant temperature. The conclusion survives position-dependent token maps and a causal final query. As context length grows, the lower bound approaches the exact $2^m$-feature realization. Separately, for deterministic multihead, multilayer sketch models whose cross-token channels have finite alphabets, we prove a transcript lower bound linear in the number of independent answers and logarithmic in their alphabet size.

## Metadata
- **Published**: 2026-08-11T20:49:34Z
- **Authors**: Vicente Opazo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11427v1)