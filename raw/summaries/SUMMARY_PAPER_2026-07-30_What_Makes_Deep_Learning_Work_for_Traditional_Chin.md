---
title: What Makes Deep Learning Work for Traditional Chinese Medicine Tongue Diagnosis? A Comprehensive Ablation Study
url: http://arxiv.org/abs/2607.28148v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-55-05Z_WhatMakesDeepLearningWorkforTraditionalChineseMedi.md
generated_at: 2026-07-30 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts an extensive ablation study to identify design choices that improve deep learning performance for tongue diagnosis in traditional Chinese medicine. Using 20+ model variants across multiple datasets, the authors demonstrate that ConvNeXt‑Tiny with specific loss and augmentation strategies yields the highest accuracy, achieving a weighted F1 of 0.78 on the larger dataset.

## Key Takeaways
- ConvNeXt‑Tiny provides optimal parameter efficiency, reducing computational load while maintaining high diagnostic performance.
- Binary cross‑entropy loss outperforms asymmetric loss by about 2.7 percentage points in this task.
- Weak‑group ensemble replacement improves results by roughly 2.1% compared with simple probability averaging.

## Context
The study contributes to the growing interest in applying convolutional neural networks to multimodal medical imaging, where class imbalance and limited labeled data are common challenges. By systematically varying model architecture, loss function, augmentation, and training strategy, it offers a practical guide for researchers seeking reliable diagnostic tools without sacrificing efficiency.

## Implications
These findings suggest that lightweight architectures combined with well‑tuned loss functions can deliver clinically useful predictions in resource‑constrained settings. Practitioners should avoid expanding label dimensions beyond the optimal range to prevent catastrophic performance drops and consider ensemble methods that balance accuracy and interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28148v1)
