---
title: Second-Moment Memory in Coordinatewise Adam
published: 2026-08-16T15:56:36Z
authors: Jeonseong Kim
url: http://arxiv.org/abs/2608.15824v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Second-Moment Memory in Coordinatewise Adam

## Abstract
Adam retains a moving average of past squared gradients in its denominator, but the optimization cost of this memory is not well understood. We show that second-moment memory can itself suppress progress toward the optimum even under finite-variance stochastic gradients. For a simple two-point oracle, the expected positive normalized update is $O(M_2^{-1/2})$ after an initialization transient, where $M_2=(1-β_2)^{-1}$ is the second-moment memory length. We convert this directional bound, under the stated memory and stepsize scaling, into an average-stationarity lower bound of the same order on a smooth convex problem with normalized gap, smoothness, and variance. Long second-moment memory can slow optimization even when the gradient noise has finite variance.

## Metadata
- **Published**: 2026-08-16T15:56:36Z
- **Authors**: Jeonseong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15824v1)