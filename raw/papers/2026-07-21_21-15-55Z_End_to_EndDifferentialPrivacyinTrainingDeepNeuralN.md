---
title: End-to-End Differential Privacy in Training Deep Neural Network Classifiers
published: 2026-07-21T21:15:55Z
authors: Huaiyuan Rao, Calvin Hawkins, Alexander Benvenuti, Matthew Hale
url: http://arxiv.org/abs/2607.19580v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# End-to-End Differential Privacy in Training Deep Neural Network Classifiers

## Abstract
Differentially private machine learning enables model training on sensitive data while ensuring that individual data is unlikely to be recoverable from the parameters of the resulting model. However, existing work often privatizes both training inputs and their labels, and these protections may be conservative when labels are public or can be safely made public. Therefore, in this work we propose a novel private training framework that instead privatizes training inputs while keeping labels public. We consider neural networks with softmax output layers, and thus the mapping from training inputs to the output of the softmax layer is a mapping onto the unit simplex. We randomize softmax outputs during training by applying the Dirichlet mechanism to enforce differential privacy for the training inputs, hence the ``end-to-end'' label. Because training data is reused across multiple training epochs, we use the notion of \Renyi differential privacy to formulate tight bounds on the strength of privacy provided by the Dirichlet mechanism across repeated uses. We show empirically that we attain new state-of-the-art accuracy when training from scratch on CIFAR10, MNIST, MedMNIST, FashionMNIST, and SVHN across all privacy budgets evaluated. Notably, when implementing $(ε, δ)$-differential privacy with $δ=10^{-5}$, we improve the prior state-of-the-art accuracy from $78.37\%$ to $88.17\%$ at $ε=4$ on CIFAR10, and our approach has $82.96\%$ accuracy even for $ε=1$, which significantly outperforms prior work.

## Metadata
- **Published**: 2026-07-21T21:15:55Z
- **Authors**: Huaiyuan Rao, Calvin Hawkins, Alexander Benvenuti, Matthew Hale
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19580v1)