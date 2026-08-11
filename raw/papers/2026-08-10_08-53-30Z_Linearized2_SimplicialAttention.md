---
title: Linearized 2-Simplicial Attention
published: 2026-08-10T08:53:30Z
authors: Aritra Das, Dhruman Gupta, Debayan Gupta
url: http://arxiv.org/abs/2608.09307v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Linearized 2-Simplicial Attention

## Abstract
We present a linearized form of 2-simplicial attention by rewriting the trilinear score as an inner product between a composite query and a key, so that the sum over one token axis takes the same form as ordinary softmax attention. We then approximate this sum with positive random features and store the entire past in a fixed-size state, while the second axis stays explicit over a short window of recent tokens. This enables us to achieve linear cost in sequence length combined with a global reach that windowed 2-simplicial attention lacks. We implement it with custom Triton kernels and combine it with Kimi Delta Attention to build a model with no softmax attention at all. Under matched compute, this model achieves the highest mean downstream accuracy among the compared architectures, and at 16k context it improves mean accuracy over a KDA hybrid while lowering LAMBADA perplexity from 715.6 to 602.6.

## Metadata
- **Published**: 2026-08-10T08:53:30Z
- **Authors**: Aritra Das, Dhruman Gupta, Debayan Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09307v1)