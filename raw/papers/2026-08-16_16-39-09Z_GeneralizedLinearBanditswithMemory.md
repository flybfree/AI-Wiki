---
title: Generalized Linear Bandits with Memory
published: 2026-08-16T16:39:09Z
authors: Heesang Ann, Hyunjun Choi, Taehyun Hwang, Younghoon Shin, Haeju Cheong, Min-hwan Oh
url: http://arxiv.org/abs/2608.15848v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generalized Linear Bandits with Memory

## Abstract
We study generalized linear bandits with memory, an endogenous non-stationary setting in which rewards depend on past actions through a finite memory matrix. Building on prior work for linear models (Clerici et al., 2024), we show that the previously known $\tilde{O}(T^{3/4})$ regret bound stems from a loose analysis, and we provide a sharpened analysis that recovers a $\tilde{O}(\sqrt{T})$ regret rate in the linear case. We then extend this improvement to generalized linear models and propose a block-wise algorithm based on shrunken confidence bounds. Our algorithm achieves a regret bound of $\tilde{O}\left(\sqrt{mT} + d\sqrt{T} + \sqrtκ\, d^{2} m^{1/4} T^{1/4} + κd^{2} \right)$, where $d$ denotes the feature dimension, $m$ the memory length, and $κ$ a curvature parameter of the link function. This attains a $\sqrt{T}$-type rate despite nonlinear rewards and memory effects. To the best of our knowledge, this analysis provides a unified treatment of memory-induced non-stationarity and nonlinear link functions, while ensuring that the leading regret term is independent of the curvature of the link function. We conduct numerical experiments that are consistent with our theoretical findings.

## Metadata
- **Published**: 2026-08-16T16:39:09Z
- **Authors**: Heesang Ann, Hyunjun Choi, Taehyun Hwang, Younghoon Shin, Haeju Cheong, Min-hwan Oh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15848v1)