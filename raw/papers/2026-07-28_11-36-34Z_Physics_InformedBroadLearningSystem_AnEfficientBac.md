---
title: Physics-Informed Broad Learning System: An Efficient Backpropagation-Free Framework for Solving Partial Differential Equations
published: 2026-07-28T11:36:34Z
authors: Pinki Khatun, M. Sajid, Abhinav Jha, M. Tanveer
url: http://arxiv.org/abs/2607.25608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Informed Broad Learning System: An Efficient Backpropagation-Free Framework for Solving Partial Differential Equations

## Abstract
Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding governing physical laws into deep neural networks. However, their reliance on computationally expensive gradient-based optimization and deep architectures often results in slow training, high computational cost, and limited scalability. In this work, we propose a novel physics-informed broad learning system (PI-BLS), the first physics-informed learning framework based on broad RdNNs. The proposed formulation embeds the governing differential operator and the associated initial and boundary constraints directly into a linear output-layer optimization problem, thereby replacing nonlinear gradient-based training with a deterministic least-squares solution obtained via the pseudoinverse. Consequently, the entire learning process is reduced to a single linear optimization stage while preserving the underlying physical constraints. As a result, PI-BLS offers an efficient learning paradigm for a physics-informed learning framework for solving PDEs that eliminates iterative backpropagation while preserving the underlying physical constraints. Experimental results on representative forward PDE benchmarks demonstrate that PI-BLS achieves competitive and often superior performance with reduced training time and model parameters compared with conventional PINNs.

## Metadata
- **Published**: 2026-07-28T11:36:34Z
- **Authors**: Pinki Khatun, M. Sajid, Abhinav Jha, M. Tanveer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25608v1)