---
title: Reward-guided Fine-Tuning of One-Step Generative Models via Wasserstein Gradient Flow
published: 2026-08-30T08:18:30Z
authors: Hoseong Hwang, Woorim Han, Joungin Chun, Jinseong Park, Jaewoong Choi
url: http://arxiv.org/abs/2608.29647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reward-guided Fine-Tuning of One-Step Generative Models via Wasserstein Gradient Flow

## Abstract
To mitigate the time complexity of generative models, one-step generative models have recently emerged through direct mapping from noise to data in a single forward pass. However, the reward-guided fine-tuning method of one-step generative models remains largely unexplored. To address this, we consider one-step generators from an optimal transport view, investigating Wasserstein Gradient Flow (WGF) for modeling smooth and controlled distributional evolution in probability space. We then propose a novel reward-guided fine-tuning of a one-step generative model via WGF. We derive a practical training method that requires no reward gradients, thereby handling both non-differentiable and differentiable rewards. Moreover, our method provides smooth and stable reward-guided distributional updates while mitigating reward hacking and mode collapse. Experiments on 2D synthetic data, CIFAR-10, and ImageNet 256$\times$256 with diverse rewards, including JPEG (in)compressibility, class probability, Black-and-White and CLIP alignment, show that our method achieves better reward alignment compared to baselines.

## Metadata
- **Published**: 2026-08-30T08:18:30Z
- **Authors**: Hoseong Hwang, Woorim Han, Joungin Chun, Jinseong Park, Jaewoong Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29647v1)