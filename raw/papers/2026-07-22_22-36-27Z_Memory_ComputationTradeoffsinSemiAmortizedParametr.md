---
title: Memory-Computation Tradeoffs in Semi Amortized Parametric Optimization
published: 2026-07-22T22:36:27Z
authors: Shijie Pan, Agustin Castellano, Zeyu Shen, Enrique Mallada
url: http://arxiv.org/abs/2607.20769v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory-Computation Tradeoffs in Semi Amortized Parametric Optimization

## Abstract
Learning-enabled decision systems often use offline data or computation to reduce online compute cost. Despite the empirical success of such approaches, there is limited general understanding of how much offline information is needed to achieve a desired accuracy under a fixed online computation budget. We study this question through the lens of amortized parametric optimization: an offline phase stores a finite memory of solved problem instances, and an online phase produces a solution to a new instance by retrieving a warm start and applying $K$ steps of projected gradient descent. We analyze this setup for smooth convex parametric optimization over a compact domain, using a nonparametric predictor built from the stored offline solutions. For $μ$-strongly convex objectives, we establish matching upper and lower bounds on the memory required to guarantee $\varepsilon$-accuracy under a fixed online iteration budget $K$. For convex objectives satisfying a $β$-growth condition ($β>2$), we obtain near-matching bounds and identify a phase transition in $K$ beyond which additional memory provides no benefit. We further provide a general proof framework that (i) explicitly quantifies the memory cost of acceleration---how much offline memory is required to achieve a prescribed speedup over the unaided online optimizer---and (ii) identifies two key quantities driving this cost: the convergence rate of the online optimizer and the Lipschitz sensitivity of the solution map to the problem parameter. Experiments on parameterized ridge regression confirm the predicted memory--computation--accuracy tradeoffs.

## Metadata
- **Published**: 2026-07-22T22:36:27Z
- **Authors**: Shijie Pan, Agustin Castellano, Zeyu Shen, Enrique Mallada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20769v1)