---
title: Designing Compact Neural Architectures via Neuron Gating and Mixed Activation
published: 2026-08-14T16:28:32Z
authors: Abhishek Shukla, Ankur Sinha, Faiz Hamid
url: http://arxiv.org/abs/2608.14443v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Designing Compact Neural Architectures via Neuron Gating and Mixed Activation

## Abstract
Neural Architecture Search (NAS) is naturally formulated as a bilevel optimization problem, where the upper-level optimizes the architecture using validation performance and the lower-level trains network parameters using training loss. However, NAS is computationally expensive due to discrete architectural decisions, exponentially growing search spaces, and the high cost of training candidate architectures. This work develops a general bilevel optimization framework for NAS across diverse architectures, including MLPs, CNNs, RNNs, and Transformers, to identify compact architectures with strong predictive performance. We propose three scalable formulations that replace discrete neuron- and activation-level decisions with continuous relaxations, enabling differentiable optimization over otherwise combinatorial architecture spaces. These formulations give rise to three NAS methods: NAS based on Neuron Gating (NAS-NG), NAS based on Mixed Activation (NAS-MA), and NAS based on Neuron Gating and Mixed Activation (NAS-NGMA). Experiments on MLPs and CNNs using MNIST and CIFAR-10 show that the proposed methods consistently identify compact architectures with competitive or improved predictive performance. On MNIST, NAS-NGMA achieves 98.68% test accuracy with 7.69M MLP parameters, while NAS-NG achieves 99.63% accuracy with only 0.26M CNN parameters. On CIFAR-10, the proposed methods consistently outperform vanilla DARTS. Further experiments demonstrate that NAS-NG can optimize substantially over-parameterized and literature-optimal architectures, improving accuracy while reducing parameters. These results establish relaxed bilevel optimization as a scalable alternative to discrete NAS and provide a general framework for efficient neuron- and activation-level architecture optimization.

## Metadata
- **Published**: 2026-08-14T16:28:32Z
- **Authors**: Abhishek Shukla, Ankur Sinha, Faiz Hamid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14443v1)