---
title: ActiveAugment: Online Active Learning for Augmentation Selection in Deep Learning
published: 2026-08-28T22:45:54Z
authors: Noah Videcrantz, Mostafa Mehdipour Ghazi
url: http://arxiv.org/abs/2608.28923v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ActiveAugment: Online Active Learning for Augmentation Selection in Deep Learning

## Abstract
Data augmentation is a cornerstone of deep learning pipelines, yet existing strategies treat it as a static, model-agnostic preprocessing step, either relying on expensive dataset-specific policy search or applying transformations uniformly at random, regardless of what the model has already learned. We introduce ActiveAugment, a unified framework that treats augmentation selection as an online active learning problem. For each training minibatch, ActiveAugment generates a pool of candidate augmented views and scores each candidate using a combination of the model's predictive uncertainty and the feature discrepancy induced by the augmentation. The augmentation under which the current model is most fragile is selected per sample, and the model is then trained with a joint supervised classification and supervised contrastive objective that enforces intra-class invariance to the selected augmentations while maintaining inter-class separation. We evaluate ActiveAugment on eight benchmark datasets spanning natural and medical imaging, using CNN and transformer architectures across three training regimes (training from scratch, full fine-tuning, and linear probing), and comparing eight active selection strategies for augmentation scoring. ActiveAugment outperforms AutoAugment, RandAugment, and TrivialAugment under controlled augmentation shifts across all domains and budgets, with the most pronounced gains at low labelling budgets. On medical imaging datasets, where data is scarce and domain shift relative to natural-image pretrained models is large, ActiveAugment achieves higher test F1 than all baselines, demonstrating strong cross-domain adaptability. Our analysis reveals that the augmentation selection policy evolves meaningfully during training and that strategy choice has a direct impact on generalisation. Code is available at: https://github.com/noahvide/ActiveAugment.

## Metadata
- **Published**: 2026-08-28T22:45:54Z
- **Authors**: Noah Videcrantz, Mostafa Mehdipour Ghazi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28923v1)