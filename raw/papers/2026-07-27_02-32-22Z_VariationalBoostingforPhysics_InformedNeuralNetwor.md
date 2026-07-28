---
title: Variational Boosting for Physics-Informed Neural Networks
published: 2026-07-27T02:32:22Z
authors: Pavlos Protopapas, Kaylee Vo
url: http://arxiv.org/abs/2607.23940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Variational Boosting for Physics-Informed Neural Networks

## Abstract
Physics-Informed Neural Networks (PINNs) solve differential equations by minimizing the residual of a nonlinear operator over a neural parameterization of the solution. However, monolithic PINNs often suffer from ill-conditioning, spectral bias, and optimization instability.   We introduce a variational boosting framework in which solutions are constructed additively in function space. Each stage trains a weak learner whose converged correction satisfies a local orthogonality condition, equivalent to a projected functional gradient descent step onto the tangent space of the network's function manifold. Because each correction network is deliberately small, the restricted minimization admits full Newton or conjugate gradient updates, which are typically infeasible in large PINNs. The resulting method separates global nonlinear refinement into a sequence of well-conditioned subproblems while preserving the full variational structure of the operator.   This framework provides a geometric interpretation of multi-stage PINNs as projected functional gradient descent and enables stable second-order optimization for nonlinear differential equations.

## Metadata
- **Published**: 2026-07-27T02:32:22Z
- **Authors**: Pavlos Protopapas, Kaylee Vo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23940v1)