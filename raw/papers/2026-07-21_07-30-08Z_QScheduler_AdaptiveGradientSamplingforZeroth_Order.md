---
title: QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs
published: 2026-07-21T07:30:08Z
authors: Victor Felipe Domingues Do Amaral, Pierre Demaj, Erwan Libessart, Laurent Folliot, Anthony Kolar, Philippe Bénabès
url: http://arxiv.org/abs/2607.18802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs

## Abstract
Zeroth-Order (ZO) optimization enables On-Device Learning (ODL) on NPU-equipped microcontrollers by estimating gradients through forward passes alone, bypassing the need for backpropagation primitives and reducing memory requirements. The number of gradient samples q critically affects training: insufficient samples produce noisy gradients that plateau early, while excessive samples consume more computational resources. However, finding an optimal q typically requires costly hyperparameter searches. This work introduces QScheduler, an adaptive algorithm that adjusts q based on training progress, and provides the first proof-of-concept of INT8 quantized on-device training on the STM32N6's Neural-ART NPU. Experiments on EuroSAT and STL-10 show that QScheduler matches well-tuned fixed-q configurations for both ResNet18 and MobileNetV2, without requiring prior q hyperparameter optimization.

## Metadata
- **Published**: 2026-07-21T07:30:08Z
- **Authors**: Victor Felipe Domingues Do Amaral, Pierre Demaj, Erwan Libessart, Laurent Folliot, Anthony Kolar, Philippe Bénabès
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18802v1)