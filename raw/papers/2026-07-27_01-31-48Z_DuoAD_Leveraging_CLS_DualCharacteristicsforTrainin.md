---
title: DuoAD: Leveraging [CLS] Dual Characteristics for Training-Free Few-Shot Anomaly Detection
published: 2026-07-27T01:31:48Z
authors: Jyun-Ze Tang, Po-Han Huang, Ming-Ching Chang, Chih-Fan Hsu, Jeng-Lin Li
url: http://arxiv.org/abs/2607.23924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuoAD: Leveraging [CLS] Dual Characteristics for Training-Free Few-Shot Anomaly Detection

## Abstract
Vision foundation models have enabled strong training-free anomaly detection (AD). However, most existing approaches rely primarily on independent local patch features, leaving the global contextual information encoded by Vision Transformers (ViTs) underexploited. In this work, we identify the dual characteristics of the ViT [CLS] token: its embedding provides anomaly-invariant global semantic representation, while its attention maps implicitly highlight spatially abnormal regions. Building on this observation, we propose a fully automated AD framework leveraging global context to remove manual tunings. Our framework introduces (1) an automatic augmentation selection strategy driven by [CLS]-level semantic consistency, and (2) an attention-guided feature reweighting mechanism that dynamically adjusts patch contributions according to [CLS] attention saliency. By integrating these components over multi-level features, our method achieves stable anomaly scoring and precise localization without training or parameter tuning. Under the one-shot setting, it achieves Image-AUC scores of 97.7%, 93.2%, and 84.5% on MVTec-AD, VisA, and Real-IAD. Using a single fixed configuration across categories, backbones, and datasets, the method establishes a new state-of-the-art for plug-and-play, training-free anomaly detection while maintaining strong robustness and practical scalability.

## Metadata
- **Published**: 2026-07-27T01:31:48Z
- **Authors**: Jyun-Ze Tang, Po-Han Huang, Ming-Ching Chang, Chih-Fan Hsu, Jeng-Lin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23924v1)