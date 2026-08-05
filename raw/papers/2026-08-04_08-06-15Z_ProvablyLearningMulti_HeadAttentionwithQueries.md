---
title: Provably Learning Multi-Head Attention with Queries
published: 2026-08-04T08:06:15Z
authors: Sunyeop Kim, Insung Kim, Jian Guo
url: http://arxiv.org/abs/2608.03294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Provably Learning Multi-Head Attention with Queries

## Abstract
We study the problem of learning multi-head softmax attention from black-box input-output access. The learner may query arbitrary real-valued token sequences and observe only the scalar output at the final token. Recent work gives an algorithm using $O(d^2)$ value queries to recover the single-head parameters $(W,v)$. For multiple heads, the same work establishes identifiability under the assumption that the heads occupy pairwise orthogonal subspaces. Applying the single-head recovery algorithm separately to the heads additionally requires bases for these subspaces to be known. We recover a canonical representation by merging heads with the same $W_h$, summing their corresponding $v_h$, and discarding a merged head when this sum is zero, without these subspace assumptions. By varying the number of copies of a token, our algorithm obtains samples of a rational function whose interpolation separates the canonical heads. Additional queries formed by adding selected token vectors then match the same head across different queries. When the oracle outputs and all subsequent computations are exact, the learner chooses its query vectors at random and recovers the canonical pairs $\{(W_h,v_h):h\in[H]\}$ up to permutation with probability one. When $H$ is known, it uses exactly $4Hd^2-2H+1$ value queries of maximum length $2H+1$. If only a known upper bound $H_0$ is available, the algorithm uses $4H_0d^2-2H_0+1$ value queries of maximum length $2H_0+1$. For approximate oracle outputs, we give conditions under which the parameter error is at most a model- and query-dependent constant multiple of the output error. Finally, we extend our result to a one-layer Transformer with multi-head attention followed by a bias-free ReLU feed-forward network. Under additional conditions, we recover a functionally equivalent Transformer without relying on a separate algorithm for learning the feed-forward network.

## Metadata
- **Published**: 2026-08-04T08:06:15Z
- **Authors**: Sunyeop Kim, Insung Kim, Jian Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03294v1)