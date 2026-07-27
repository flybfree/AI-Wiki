---
title: Graph-Based Correlation Matrix Generation: A Convex Optimization Approach
published: 2026-07-24T15:54:23Z
authors: Ali Fakhar, K{é}vin Polisano, Ir{è}ne Gannaz, Sophie Achard
url: http://arxiv.org/abs/2607.22436v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph-Based Correlation Matrix Generation: A Convex Optimization Approach

## Abstract
This work addresses the generation of theoretical correlation matrices with prescribed sparsity patterns associated to graph structures. We propose a novel convex optimization framework in which an initial matrix is projected onto an elliptope under a positive semidefiniteness constraint. Several numerical schemes are implemented and compared. The problem falls within the broader class of matrix completion, where off-diagonal entries corresponding to absent edges are fixed to zero and diagonal entries are fixed to one. Beyond this structural constraint, the approach offers greater flexibility than existing methods by allowing control over the mean of the off-diagonal entry distribution, enabling the generation of correlation matrices that better reflect realistic data. This procedure is not designed to yield a uniform distribution over the feasible set; rather, it provides a principled and tunable way to construct correlation matrices suitable for benchmarking statistical methods for graphical model inference. Theoretical guarantees on the existence of solutions are established, both in the general setting and under the additional mean constraint. Simulation studies illustrate the properties of the generated matrices with respect to graph structure. The methodology is applied to two real-world datasets from neuroscience and finance, and a comparison with GAN-based correlation matrix generation is provided.

## Metadata
- **Published**: 2026-07-24T15:54:23Z
- **Authors**: Ali Fakhar, K{é}vin Polisano, Ir{è}ne Gannaz, Sophie Achard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22436v1)