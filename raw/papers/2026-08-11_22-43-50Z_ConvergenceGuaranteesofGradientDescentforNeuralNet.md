---
title: Convergence Guarantees of Gradient Descent for Neural Networks via Generalized Lipschitz Smoothness
published: 2026-08-11T22:43:50Z
authors: Siqiao Mu, Diego Klabjan
url: http://arxiv.org/abs/2608.11479v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Convergence Guarantees of Gradient Descent for Neural Networks via Generalized Lipschitz Smoothness

## Abstract
We establish convergence guarantees of gradient descent for general feedforward neural networks of arbitrary width or depth, with no special requirements on the initialization or dataset. We only assume that the activation functions are Lipschitz smooth, Lipschitz continuous, and linearly bounded--- properties that hold for linear, tanh, softplus, and sigmoid activation functions. For the loss function, we require that it is Lipschitz smooth in the model outputs, which is true for mean-squared error. The key theoretical insight is that the Lipschitz properties of the activation functions are partially preserved even through repeated compositions, leading to a novel generalized Lipschitz smoothness condition where the change in gradient is upper bounded by the change in the parameter space, multiplied by polynomial terms of the parameter norms at both endpoints. This type of condition holds for both the model function and the loss function, enabling a descent lemma where the loss decreases as long as the learning rate is small enough with respect to the parameter norms. By ensuring that the parameter norms do not grow too quickly to infinity, we prove that the minimum squared gradient norm converges to zero in $T$ iterations at rate $O(1/T^{1/L})$ for an $L$-layer neural network.

## Metadata
- **Published**: 2026-08-11T22:43:50Z
- **Authors**: Siqiao Mu, Diego Klabjan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11479v1)