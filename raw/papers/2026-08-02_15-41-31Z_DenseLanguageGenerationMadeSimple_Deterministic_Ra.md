---
title: Dense Language Generation Made Simple: Deterministic, Randomized, and Multi-Order Algorithms
published: 2026-08-02T15:41:31Z
authors: Ziyi Cai, Shuangping Li, Yiheng Shen, Kangning Wang, Peng Zhang
url: http://arxiv.org/abs/2608.01320v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dense Language Generation Made Simple: Deterministic, Randomized, and Multi-Order Algorithms

## Abstract
Language generation in the limit is a theoretical framework for studying how a generator can learn to produce new valid strings from a stream of positive examples. In this model, an adversary chooses an unknown language from a countable family and enumerates its elements in an arbitrary order, while the generator must eventually output only elements of the language that have not yet appeared in the enumeration. Reliable generation is thus formalized through two eventual guarantees: validity and novelty relative to the observed data. To further quantify the breadth of the generator's outputs, Kleinberg and Wei (FOCS 2025, STOC 2026) introduced lower density as a measure of output coverage. Given an order representing the importance or relevance of possible outputs, lower density is the asymptotic lower bound, as $n$ grows, on the fraction of the first $n$ elements of the target language that the generator outputs before they appear in the data. Kleinberg and Wei showed that $1/2$ is the optimal lower-density guarantee for deterministic algorithms.   We develop a simple and unified framework for obtaining optimal lower-density guarantees. We first give a deterministic algorithm that recovers the optimal guarantee of $1/2$ with a significantly simpler analysis than prior work. We then demonstrate the flexibility of our framework through two extensions. First, against an oblivious adversary, randomization raises the optimal guarantee to $1-1/e$. Second, for any finite collection of orders, the optimal deterministic and randomized guarantees can be achieved simultaneously with respect to every order, so accommodating multiple notions of importance or relevance entails no loss in the optimal guarantee.

## Metadata
- **Published**: 2026-08-02T15:41:31Z
- **Authors**: Ziyi Cai, Shuangping Li, Yiheng Shen, Kangning Wang, Peng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01320v1)