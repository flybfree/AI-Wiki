---
title: Quality Control Algorithms for Pattern Counting
published: 2026-08-04T10:35:00Z
authors: Cassandra Marcussen, Ronitt Rubinfeld, Madhu Sudan
url: http://arxiv.org/abs/2608.03439v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quality Control Algorithms for Pattern Counting

## Abstract
In recent work, Marcussen, Rubinfeld, and Sudan introduced the notion of quality control problems, which aim to capture the task of determining if a given input is truly random. Formally, their goal is to accept typical inputs from the specified distribution while rejecting every input whose value of a specified statistic is far from the distributional baseline. This captures the empirical practice of using specified statistics as a proxy for the quality of randomness. Empirical algorithms, however, have not exploited the asymmetry in the definition of quality control problems, which require soundness guarantees in the worst-case while only seeking average-case completeness. Their work abstracted a problem definition emphasizing this asymmetry and used it to give efficient quality control algorithms for assessing the randomness of graphs.   In this work, we introduce and study quality control problems over sequences, where the goal is to distinguish a sequence of i.i.d. characters from sequences where some specified pattern appears too often (or too infrequently) as a subsequence. We consider this problem in both the finite-alphabet setting and for real-valued sequences. We refer to the former setting as the pattern counting problem. In the latter case, the natural notion of a pattern is to consider the relative ordering of the characters in the subsequence, and we refer to this as the permutation pattern counting problem. Algorithms to approximately count (permutation) patterns of length $k$ in a worst-case sequence of length $n$ can provably require exponential in $k$ queries into the sequence. In contrast, we show that by taking advantage of the asymmetry in the definition of quality control, we give algorithms that run in poly$(k)$ time to solve these problems. We also prove that any quality control algorithm (over some natural distributions) requires superlinear queries in $k$.

## Metadata
- **Published**: 2026-08-04T10:35:00Z
- **Authors**: Cassandra Marcussen, Ronitt Rubinfeld, Madhu Sudan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03439v1)