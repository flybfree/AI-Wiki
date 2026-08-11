---
title: Beyond Binary: Continuous State Optimization with Graph-Structured Objectives
published: 2026-08-10T09:46:28Z
authors: Corinna Cortes, Yishay Mansour, Mehryar Mohri
url: http://arxiv.org/abs/2608.09366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Binary: Continuous State Optimization with Graph-Structured Objectives

## Abstract
Large-scale learning systems often face the challenge of balancing multiple,   potentially competing objectives, such as fairness, accuracy, and   latency. While recent work has formalized this as an optimization problem over   binary states, many real-world control parameters, such as fairness   thresholds, diversity mixing rates, or resource budgets, are continuous. In   this work, we extend the framework to \emph{continuous state spaces}. We model   the problem as minimizing a sum of linear objectives subject to \emph{movement   costs} that penalize system instability. We capture the local structure of   the objectives using a \emph{dependency graph} (or factor graph), where each   objective is determined by a subset of the state attributes. To address the   tension between exploration and stability, we propose \emph{Lazy   Graph-LinUCB}, an algorithm that performs lazy updates to minimize switching   costs while maintaining near-optimal regret. Beyond stability, we introduce   three advanced mechanisms to exploit the underlying graph structure: (1) an   \emph{asynchronous} update schedule that eliminates synchronization overhead   in sparse graphs; (2) an \emph{adaptive} algorithm that learns the graph   structure from data; and (3) a \emph{joint estimator} that leverages data   sharing among correlated objectives to significantly tighten regret   bounds. Empirically, we demonstrate that these structural exploitations reduce   movement costs by more than a factor of three in heterogeneous systems while   maintaining similar cumulative losses.

## Metadata
- **Published**: 2026-08-10T09:46:28Z
- **Authors**: Corinna Cortes, Yishay Mansour, Mehryar Mohri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09366v1)