---
title: EMS Coreset: An Efficient Expectation-Maximization Algorithm for Sinkhorn Coreset
published: 2026-08-17T04:46:34Z
authors: Haoyun Yin, Chuanhui Liu, Xiao Wang
url: http://arxiv.org/abs/2608.16101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EMS Coreset: An Efficient Expectation-Maximization Algorithm for Sinkhorn Coreset

## Abstract
Coresets distill large datasets into small, representative subsets for efficient downstream learning. Yet Optimal Transport (OT)-based selection typically requires intensive computation of transport plans, limiting scalability. We introduce a scalable Sinkhorn coreset method that permits closed-form updates of the entropically regularized OT coupling by allowing non-uniform coreset weights. This produces centroids that generalize k-means via soft assignments. We establish asymptotic consistency of the selected measure and Lipschitz stability to data perturbations, providing accuracy and robustness guarantees. Across synthetic and real-world benchmarks, the proposed method achieves competitive or improved approximation quality while substantially reducing runtime compared to Wasserstein- and standard Sinkhorn-based coreset selection, especially at large scale.

## Metadata
- **Published**: 2026-08-17T04:46:34Z
- **Authors**: Haoyun Yin, Chuanhui Liu, Xiao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16101v1)