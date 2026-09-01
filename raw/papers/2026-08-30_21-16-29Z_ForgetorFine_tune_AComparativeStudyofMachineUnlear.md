---
title: Forget or Fine-tune? A Comparative Study of Machine Unlearning Strategies for Noisy Label Correction
published: 2026-08-30T21:16:29Z
authors: João L. P. Santana, Filipe R. Cordeiro
url: http://arxiv.org/abs/2608.30046v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forget or Fine-tune? A Comparative Study of Machine Unlearning Strategies for Noisy Label Correction

## Abstract
Noisy labels remain a critical challenge for training deep neural networks, since memorizing incorrect labels degrades generalization. Once noisy samples are identified after training, the standard solution is to retrain the model from scratch on the cleaned dataset, which is increasingly expensive as datasets and models grow. Machine Unlearning (MU) has recently emerged as a computationally efficient alternative, but the relative effectiveness of different MU strategies for noisy-label correction remains poorly understood. In this work, we conduct a comparative empirical study of five MU methods (NegGrad, Fine-Tuning (FT), Random Labeling (RL), SalUn, and MUNBa) across symmetric, asymmetric, instance-dependent, and open-set noise on CIFAR-10, CIFAR-100, and the real-world noisy dataset Food-101N. Our central finding is that the appropriate unlearning strategy is conditioned on the noise structure. Simple FT is a strong baseline across most closed-set scenarios; RL and SalUn are the most consistently robust methods and, under instance-dependent noise, approach retraining accuracy at a fraction of the computational cost; MUNBa shows advantages mainly under extreme symmetric noise. Under open-set noise, in contrast, we show that retraining on the cleaned subset degrades accuracy relative to the noisy baseline, so approximating the retrained model is not an adequate objective in this regime. On Food-101N, all MU methods remain competitive and achieve accuracies close to retraining despite reducing runtime by an order of magnitude. These findings provide practical guidelines for selecting MU strategies for post-training noisy-label correction.

## Metadata
- **Published**: 2026-08-30T21:16:29Z
- **Authors**: João L. P. Santana, Filipe R. Cordeiro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30046v1)