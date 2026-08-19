---
title: Online Generalized Sparse Regression: How Does Overparametrization Help?
published: 2026-08-18T07:46:32Z
authors: Shuoguang Yang, Qiang Sun
url: http://arxiv.org/abs/2608.17466v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Generalized Sparse Regression: How Does Overparametrization Help?

## Abstract
Regularized sparse regression has been extensively studied in the offline setting, but online formulation remains relatively under-explored. This gap stems from four key challenges: (i) the infeasibility of dynamically updating the regularization parameter in every online round, (ii) managing storage and memory complexity, (iii) enabling real-time computation via closed-form updates rather than solving full optimization problems at each round, and (iv) achieving optimal statistical guarantees under realistic assumptions. In this paper, we propose an online generalized-sparsity-constrained regression framework, focusing on online cardinality-constrained linear regression and low-rank matrix sensing. Unlike online regularized regression, our constrained formulation eliminates the need for dynamic parameter tuning. We introduce an efficient online hard-thresholding algorithm that performs closed-form updates and requires storing only summary statistics, making it computationally, memory, and storage efficient. Despite the inherent nonconvexity and combinatorial nature of the formulation, our algorithm achieves global convergence at the optimal statistical rate under realistic assumptions, provided that the projection set is properly overparameterized. Numerical experiments demonstrate that our method consistently outperforms state-of-the-art alternatives.

## Metadata
- **Published**: 2026-08-18T07:46:32Z
- **Authors**: Shuoguang Yang, Qiang Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17466v1)