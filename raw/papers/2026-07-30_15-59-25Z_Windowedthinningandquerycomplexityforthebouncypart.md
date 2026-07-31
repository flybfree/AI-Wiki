---
title: Windowed thinning and query complexity for the bouncy particle and Zigzag samplers
published: 2026-07-30T15:59:25Z
authors: Jianfeng Lu, Yinchen Luo
url: http://arxiv.org/abs/2607.28413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Windowed thinning and query complexity for the bouncy particle and Zigzag samplers

## Abstract
Let $μ(d x)\propto e^{-U(x)} d x$ on $\R^d$, where $U$ is $m$-strongly convex and $L$-smooth, and denote by $κ=L/m$ the condition number. We consider windowed thinning, an exact simulation method for the bouncy particle sampler and the coordinate Zigzag process. The method divides a trajectory into deterministic windows and uses a gradient evaluation at the beginning of each window to construct a tractable local envelope for the event rate. Combining this construction with quantitative mixing estimates and finite-time bounds on the expected numbers of bounces and flips yields query complexity guarantees from a Gaussian cold start. For total-variation error $\varepsilon$, the expected query counts are $O(κ^{1/2}d\,(d\logκ+\log\frac1\varepsilon))$ gradient queries for the bouncy particle sampler and $O(κd^{1/4}(d\logκ+\log\frac1\varepsilon))$ full-gradient equivalents for Zigzag, where $d$ coordinate-partial queries count as one equivalent.

## Metadata
- **Published**: 2026-07-30T15:59:25Z
- **Authors**: Jianfeng Lu, Yinchen Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28413v1)