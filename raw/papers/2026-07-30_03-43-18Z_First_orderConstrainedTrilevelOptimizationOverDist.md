---
title: First-order Constrained Trilevel Optimization Over Distributed Networks for Robust Coreset Selection
published: 2026-07-30T03:43:18Z
authors: Yang Jiao, Kaixuan Jiao, Kai Yang, Nadjib Aitsaadi, Ilhem Fajjari,  Renwei,  Li
url: http://arxiv.org/abs/2607.27632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# First-order Constrained Trilevel Optimization Over Distributed Networks for Robust Coreset Selection

## Abstract
With the rapid advancement of the Internet of Things (IoT), massive amounts of data are generated across distributed edge networks. Training models on full data incurs significant computational overhead and storage bottlenecks, rendering coreset selection a critical paradigm. Furthermore, given the privacy-sensitive nature of local data and the escalating demand for model robustness in real-world deployments, developing an effective distributed optimization framework for robust coreset selection is vital, yet remains largely unexplored. To this end, this work first characterizes the hierarchical dependencies among coreset selection, robust optimization, and distributed learning, and formulates the distributed robust coreset selection as a trilevel optimization problem with level-wise constraints. Furthermore, to effectively solve the trilevel problem in a distributed manner, the \underline{F}ederated \underline{F}irst-order \underline{C}onstrained \underline{T}rilevel \underline{O}ptimization (F$^2$CTO) is proposed, which synergistically integrates a hierarchical composite value-function reformulation and a distributed alternating projected gradient algorithm. To the best of our knowledge, F$^2$CTO is the first method developed for distributed robust coreset selection, as well as the first distributed optimization approach for trilevel optimization problems with level-wise constraints. Additionally, we prove that the proposed method achieves a non-asymptotic convergence rate of $\mathcal{O}(ε^{-3/2})$ for finding an $ε$-stationary point. Extensive empirical evaluations on reliable continual learning demonstrate the effectiveness and efficiency of the proposed F$^2$CTO.

## Metadata
- **Published**: 2026-07-30T03:43:18Z
- **Authors**: Yang Jiao, Kaixuan Jiao, Kai Yang, Nadjib Aitsaadi, Ilhem Fajjari,  Renwei,  Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27632v1)