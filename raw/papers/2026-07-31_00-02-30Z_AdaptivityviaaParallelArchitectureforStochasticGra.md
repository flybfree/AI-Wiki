---
title: Adaptivity via a Parallel Architecture for Stochastic Gradient Methods Adaptivity via a Parallel Architecture for Stochastic Gradient Methods Adaptivity via a Parallel Architecture for Stochastic Gradient Methods
published: 2026-07-31T00:02:30Z
authors: Bin Fu
url: http://arxiv.org/abs/2607.28902v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptivity via a Parallel Architecture for Stochastic Gradient Methods Adaptivity via a Parallel Architecture for Stochastic Gradient Methods Adaptivity via a Parallel Architecture for Stochastic Gradient Methods

## Abstract
We develop a parallel framework that assembles static gradient methods to achieve better adaptivity. A static gradient method, denoted by $\mathrm{GD}(x_0,T)$, takes as input an initial point $x_0\in\mathbb{R}^n$ and $T\in \mathbb{R}^+$ specifying the number $\floor{T}$ of iterations. The step size is chosen as $s=S(T)$, where $S(\cdot)$ is a predetermined function of $T$. The method then performs the iterations $ x_{i+1}=x_i-\fracη{s}\cdot g_i,$ where $g_i$ is a stochastic gradient evaluated at $x_i$, and $η$ is a scaling factor. For an integer $p\ge1$, the $p$ processors in the proposed parallel framework search for an appropriate value of $T$ according to a geometric sequence so that the resulting gradient descent satisfies the desired convergence conditions. Each processor executes an infinite sequence of stages indexed by $i=1,2,\ldots$. At stage $i$, processor $j$ is assigned $ T_{j,i}=h(j,i),$ where $h:\mathbb{N}\times\mathbb{N} \rightarrow\mathbb{R}^{+}$ is a prescribed function. Processor $j$ $(j=0,1,\ldots,p-1)$ executes $\mathrm{GD}(x_0, T_{j,i})$ at stage $i$.

## Metadata
- **Published**: 2026-07-31T00:02:30Z
- **Authors**: Bin Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28902v1)