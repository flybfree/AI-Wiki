---
title: Depth Enables Local Entropy: Quadratic Depth Dependence in Deep Variation-Norm ReLU Regression
published: 2026-08-18T07:03:14Z
authors: Tao Jiang, Minbo Gao, Shaowei Cai
url: http://arxiv.org/abs/2608.17434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Depth Enables Local Entropy: Quadratic Depth Dependence in Deep Variation-Norm ReLU Regression

## Abstract
We study Gaussian regression over the explicit vector-valued Parhi--Nowak deep-RBV^2 architecture with depth L, width w, layer-sum variation budget A, and output bound B. For this O(L w^2)-parameterized architecture, the known lower and upper bounds differ by one factor of depth. We construct a local packing showing that the quadratic depth dependence is intrinsic under an explicit sample-size-dependent radius condition. The packing has log-cardinality Omega(L^2 w^2 log w); its codewords lie in an O(lambda) L^2 ball and are pairwise Omega(lambda)-separated. The main ingredients are a bias-corrected bounded-coefficient approximation theorem and balanced amplification: multiplying a depth-D ReLU network by q can be implemented using one constant channel so that every coefficient grows by only q^(1/D). Translation to vector-valued RBV^2 blocks then has layer-sum cost O(D w^2 q^(1/D)). Gaussian Fano yields a radius-explicit lower bound governed by the output, testing, and representation scales. Under A=B=R, sigma proportional to R, and the stated radius condition, this gives minimax risk at least of order L^2 w^2 log(w) R^2/n. A pseudodimension-based finite-net upper bound gives O-tilde(L^2 w^2 R^2/n) for unbounded Gaussian responses. Thus the minimax risk has quadratic polynomial dependence on depth, up to logarithmic factors, and exhibits a transition to representation-limited behavior at smaller radius.

## Metadata
- **Published**: 2026-08-18T07:03:14Z
- **Authors**: Tao Jiang, Minbo Gao, Shaowei Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17434v1)