---
title: EMASAM: a Computationally Efficient Sharpness-Aware Minimization via EMA-Guided Perturbations
published: 2026-08-15T08:10:31Z
authors: Tanapat Ratchatorn, Masayuki Tanaka
url: http://arxiv.org/abs/2608.15105v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EMASAM: a Computationally Efficient Sharpness-Aware Minimization via EMA-Guided Perturbations

## Abstract
Recent progress in optimization research has highlighted the sharpness of the loss landscape as a key factor in narrowing the generalization gap. Motivated by this insight, Sharpness-Aware Minimization (SAM) was proposed as a training strategy that enhances generalization. Despite the promising performance, SAM suffers from its twice computational cost due to its core algorithm requiring an extra gradient computation during the perturbation step. To overcome this limitation, we introduce Exponential Moving Average Sharpness-Aware Minimization (EMASAM), a computationally efficient variant of SAM. EMASAM does not require the loss gradient in the perturbation step. Instead, EMASAM defines the perturbation direction based on the discrepancy between the main model and the EMA shadow model. This perturbation travels away from the stable average position toward the less stable area, acting as a softer yet cheaper alternative to SAM's worst-case scenario perturbation. Moreover, since EMASAM's perturbation does not rely on noisy mini-batch gradients, it mitigates the gradient-induced instability inherent in SAM. Hence, EMASAM eliminates the need for an extra backpropagation while also preserving the generalization ability of the SAM-style training. Several experiments have been performed and confirm the efficiency and robustness of our method.

## Metadata
- **Published**: 2026-08-15T08:10:31Z
- **Authors**: Tanapat Ratchatorn, Masayuki Tanaka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15105v1)