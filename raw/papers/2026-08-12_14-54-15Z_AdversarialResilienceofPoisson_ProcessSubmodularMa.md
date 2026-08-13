---
title: Adversarial Resilience of Poisson-Process Submodular Maximization over Matroids: From Robust Offline Optimization to Full-Bandit Learning
published: 2026-08-12T14:54:15Z
authors: Vaneet Aggarwal
url: http://arxiv.org/abs/2608.12134v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Resilience of Poisson-Process Submodular Maximization over Matroids: From Robust Offline Optimization to Full-Bandit Learning

## Abstract
We study nonnegative submodular maximization subject to a general matroid when the offline algorithm is given an arbitrary controlled value oracle. Our main result is an adversarial resilience theorem for the Spiteful Greedy Swap Poisson Process (SGS-Poisson): without modifying its Poisson intensity, single-element exchange rule, or spiteful drop step, the algorithm retains limiting approximation factors $1/e$ for non-monotone objectives and $1-1/e$ for monotone objectives. More precisely, under every controlled oracle $\widehat f$ satisfying $|\widehat f(S)-f(S)|\le ξ$ for every set $S$, our implementation returns a feasible set with expected value at least $(1/e-\varepsilon)\OPT-O(kξ)$ and $(1-1/e-\varepsilon)\OPT-O(kξ)$, respectively, using $\widetilde O(nk^2\varepsilon^{-2})$ oracle calls. As a consequence, the offline-to-online reduction yields full-bandit CMAB algorithms for general matroid-constrained submodular rewards with exact limiting approximation-regret factors $1/e$ and $1-1/e$ and $\widetilde O(n^{1/5}k^{4/5}T^{4/5})$ regret.

## Metadata
- **Published**: 2026-08-12T14:54:15Z
- **Authors**: Vaneet Aggarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12134v1)