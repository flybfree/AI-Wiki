---
title: On the Implicit Flatness Bias of Sharpness-Aware Minimization: A Linear Stability Analysis with Quantitative Hyperparameter Bounds
published: 2026-08-04T06:37:44Z
authors: Jiaxin Deng, Junbiao Pang
url: http://arxiv.org/abs/2608.03197v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Implicit Flatness Bias of Sharpness-Aware Minimization: A Linear Stability Analysis with Quantitative Hyperparameter Bounds

## Abstract
Sharpness-Aware Minimization (SAM) improves generalization by seeking parameters whose loss is robust to local adversarial perturbations, but the quantitative mechanism underlying its implicit bias toward flat minima remains unclear. In particular, the perturbation radius $ρ$ is typically treated as an isolated tuning parameter, despite defining the neighborhood in which SAM measures sharpness. We analyze mini-batch SAM near an interpolating minimum through linear stability. Under local linearization and gradient-noise alignment assumptions, we prove that every linearly stable minimum satisfies $λ_{\max}\leq\sqrt[3]{bΓ/(2ρη^2)}$, where $λ_{\max}$ is the largest Hessian eigenvalue, $b$ is the batch size, $η$ is the learning rate, and $Γ$ bounds the gradient norm. The bound quantitatively characterizes SAM's implicit flatness bias: holding the other quantities fixed, a smaller batch size, a larger learning rate, or a larger radius restricts linearly stable SAM to flatter minima. It also exposes a necessary trade-off: $ρ$ should be large enough to promote flatness, yet remain local enough to preserve the approximation and stable training. We validate this prediction in a controlled study of 900 models on CIFAR-100 with ResNet-18 and VGG-19, where increasing $ρ$ is consistently associated with a smaller largest Hessian eigenvalue across batch-size and learning-rate settings. Finally, we instantiate the analysis in Taylor-Locality Controlled SAM (TLC-SAM), which adjusts $ρ$ using the observed Taylor-approximation error and further reduces the top Hessian eigenvalue relative to fixed-radius SAM. Our results provide quantitative hyperparameter bounds and a stability--locality perspective for analyzing and designing SAM variants.

## Metadata
- **Published**: 2026-08-04T06:37:44Z
- **Authors**: Jiaxin Deng, Junbiao Pang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03197v1)