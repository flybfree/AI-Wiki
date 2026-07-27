---
title: Convergence analysis of a family of Zermelo-type iterations for the Bradley--Terry model
published: 2026-07-24T11:39:24Z
authors: Ruijian Han, Ding Lu, Yiming Xu
url: http://arxiv.org/abs/2607.22221v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Convergence analysis of a family of Zermelo-type iterations for the Bradley--Terry model

## Abstract
Zermelo's algorithm is a classical method for computing the maximum likelihood estimator in the Bradley--Terry (BT) model, but its convergence can be slow in practice. To accelerate computation, Newman introduced a family of Zermelo-type fixed-point iterations parameterized by $α$, with Zermelo's algorithm recovered at $α=1$. Empirical evidence suggests that the choice $α=0$ often converges substantially faster, making it a promising alternative, yet the mechanism underlying this acceleration remains elusive. This paper provides theoretical insight into this phenomenon through a systematic local convergence analysis. We derive closed-form expressions for local convergence factors under synchronous and asynchronous updates and analyze their dependence on $α$ via spectral analysis of the associated Jacobian matrices. For synchronous updates, we show that the algorithm may fail to converge when $α<1$, and its local convergence factor is quasi-convex in $α$ under the population BT model. In contrast, asynchronous updates are always locally convergent, and their local convergence factor is provably monotonically increasing in $α$ under the population BT model of consistently ordered bipartite comparison graphs, establishing the optimality of $α=0$ in this setting. We further establish asymptotic approximation results for the population convergence factors under the BT model, justifying their practical relevance. Numerical experiments on synthetic and real-world datasets confirm the theory. Our analysis complements existing convergence results and shows that the acceleration of $α=0$ arises not only from the parameter choice but, more importantly, from the use of asynchronous updates.

## Metadata
- **Published**: 2026-07-24T11:39:24Z
- **Authors**: Ruijian Han, Ding Lu, Yiming Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22221v1)