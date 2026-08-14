---
title: Difference-of-Convex Regularization for Graph Learning by Differentiable Programming
published: 2026-08-13T03:10:05Z
authors: Liping Tao, Chee Wei Tan
url: http://arxiv.org/abs/2608.12757v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Difference-of-Convex Regularization for Graph Learning by Differentiable Programming

## Abstract
Laplacian-regularized minimization is fundamental in signal processing and machine learning, but is limited by the dense and ill-conditioned nature of the graph Laplacian pseudoinverse. While the Laplacian itself is sparse, its pseudoinverse is dense and often ill-conditioned, rendering direct computation impractical at scale. Moreover, pseudoinverse learning is more challenging than Laplacian learning. To address this challenge, this paper considers the setting where the graph Laplacian is given and proposes a Difference-of-Convex Regularizer (DCR) graph learning framework that approximates the spectral action of the Laplacian pseudoinverse without direct inversion via regularized Maximum Likelihood Estimation (MLE). By reformulating Laplacian-Regularized Nonnegative Least Squares (LR-NNLS) through a dual representation, DCR decouples pseudoinverse learning from instance-specific inference and enables efficient primal solution reconstruction via a differentiable dual-guided learning scheme. We establish theoretical guarantees on stability and the existence of a unique fixed point for DCR algorithm. Numerical experiments demonstrate improved performance over convex solvers and graph filtering baselines and robust performance across diverse graph topologies.

## Metadata
- **Published**: 2026-08-13T03:10:05Z
- **Authors**: Liping Tao, Chee Wei Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12757v1)