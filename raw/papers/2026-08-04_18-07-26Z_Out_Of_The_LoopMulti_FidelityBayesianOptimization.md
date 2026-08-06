---
title: Out-Of-The-Loop Multi-Fidelity Bayesian Optimization
published: 2026-08-04T18:07:26Z
authors: Gustavo Sutter, Hao Wang, Luis Ricardez-Sandoval, Pascal Poupart, Agustinus Kristiadi
url: http://arxiv.org/abs/2608.04113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Out-Of-The-Loop Multi-Fidelity Bayesian Optimization

## Abstract
Black-box optimization is a ubiquitous problem in science and engineering, often dealing with expensive objective functions with cheaper lower-fidelity proxies available. Multi-fidelity Bayesian optimization (MF-BO) is a principled approach to this problem, leveraging correlations across different fidelities when querying the objective. However, for many important MF-BO tasks, the true highest-fidelity function is prohibitively expensive to be part of the optimization loop. Nevertheless, practitioners often have gold standard data (observations of the highest-fidelity function) obtained from previous experiments that might provide information for the current task. For instance, in molecular optimization, chemists often pick the top-$k$ candidate molecules using various computer simulations, and later reveal their true objective function values. In this work, we demonstrate the suboptimality of standard MF-BO algorithms in the real-world scenarios above, even under ideal assumptions. Next, we mitigate this problem by incorporating historical high-fidelity data accompanied by task descriptors---which can be explicitly given or extracted from unstructured metadata. We demonstrate the effectiveness of our methods on synthetic functions, as well as real-world problems in chemistry and hyperparameter optimization.

## Metadata
- **Published**: 2026-08-04T18:07:26Z
- **Authors**: Gustavo Sutter, Hao Wang, Luis Ricardez-Sandoval, Pascal Poupart, Agustinus Kristiadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04113v1)