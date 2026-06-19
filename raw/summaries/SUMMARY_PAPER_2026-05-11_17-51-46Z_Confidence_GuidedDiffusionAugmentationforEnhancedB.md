---

title: Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition
url: http://arxiv.org/abs/2605.10916v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-11_17-51-46Z_Confidence_GuidedDiffusionAugmentationforEnhancedB.md
generated_at: "2026-06-11 10:37"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces a confidence‑guided diffusion augmentation method to improve recognition of low‑resolution Bangla compound characters. The framework synthesizes high‑quality samples using class‑conditional diffusion and classifier guidance, then filters them with quality gates. Experiments on the AIBangla dataset show that the best model reaches 89.2% accuracy.

## Key Takeaways
- The confidence‑based filtering mechanism retains only synthetic images that are highly consistent with their predicted classes, preventing noisy augmentations.
- Squeeze‑and‑excitation enhanced residual blocks within the U‑Net backbone boost generation quality and stability.
- Retraining multiple classifiers on fused original and filtered data yields a 89.2% classification accuracy, exceeding prior benchmarks.

## Context
Handwritten character recognition in low‑resource scripts like Bangla faces severe data scarcity and high intra‑class variation, limiting model performance. Diffusion augmentation offers a way to generate realistic samples without collecting more images, aligning with recent trends toward generative models for limited datasets.

## Implications
This work demonstrates that quality‑aware synthetic data can significantly boost accuracy in character recognition tasks, offering a practical solution for practitioners working with scarce annotated text data. The approach may be adapted to other low‑resource scripts and low‑resolution image classification problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.10916v1)
