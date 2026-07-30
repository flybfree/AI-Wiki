---
title: Weight and Height Estimation from a Single Human Image Captured in the Wild
url: http://arxiv.org/abs/2607.26104v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_08-39-11Z_WeightandHeightEstimationfromaSingleHumanImageCapt.md
generated_at: 2026-07-29 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a new dataset of 6105 in‑wild images to estimate height, weight and BMI from single human photos. Experiments show that full‑body images outperform half‑body or facial inputs when using CNN backbones such as VGG, Densenet and ResNet, highlighting the importance of pose and body context for accurate BMI estimation.

## Key Takeaways
- The proposed dataset includes frontal, back, full and half body poses with varying backgrounds, capturing real‑world variability in ethnicity, age and gender.  
- Full‑body images consistently yield better predictions than face or partial body images across multiple CNN architectures.  
- Multi‑modal inputs (RGB, depth‑maps, pose‑affinity maps, edge‑maps) can improve robustness but full‑body data remains the most effective source for BMI estimation.

## Context
Accurate health metrics like BMI are valuable for personal monitoring and predictive analytics yet extracting them from single images is challenging due to pose, lighting and occlusion. This work addresses that challenge by providing a large, diverse in‑wild dataset and demonstrating how full‑body context enhances deep learning performance.

## Implications
For practitioners, the findings suggest focusing on capturing full bodies when building health‑related image models to reduce error rates. The dataset can serve as a benchmark for future research aiming at automated health assessment tools that rely on single photos.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26104v1)
