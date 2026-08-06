---
title: Attention-based representations for multi-task computation
published: 2026-08-04T21:52:04Z
authors: Daniel Hsu, Mingyue Xu
url: http://arxiv.org/abs/2608.04243v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Attention-based representations for multi-task computation

## Abstract
Multi-head attention layers produce vector representations that support multiple downstream tasks. We establish bounds on the number of heads required in two simple and concrete multi-task scenarios. In the first scenario, a vector representation is sought so that linear predictors can compute both the smallest and largest numbers in a given list. In this case, it is known two attention heads with small embedding dimension and bit precision level suffice. We prove that a single attention head requires exponentially higher embedding dimension or precision level. In the second scenario, a vector representation is sought so that a polynomial threshold function can compute the XOR of a given string of $n$ bits. This scenario is analogous to the first one for $n=2$, since XOR is readily computed by a linear function using a vector representation that encodes both the AND and the OR of the two bits. We observe that $n$-bit XOR requires the product of the number of heads and the polynomial degree to be at least $n$, and we construct multi-head attention layers that match this lower bound. These results generalize to arbitrary (symmetric) Boolean functions, where the bound is given in terms of the threshold degree.

## Metadata
- **Published**: 2026-08-04T21:52:04Z
- **Authors**: Daniel Hsu, Mingyue Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04243v1)