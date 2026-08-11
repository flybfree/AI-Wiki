---
title: Dynamic Distribution-Aware Uncertainty Tracking in Vision-Language Representation Learning
published: 2026-08-10T01:53:28Z
authors: Ao Zhou, Zhiwei Jiang, Zifeng Cheng, Cong Wang, Shufan Yang, Haoru Chen, Qing Gu
url: http://arxiv.org/abs/2608.09011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Distribution-Aware Uncertainty Tracking in Vision-Language Representation Learning

## Abstract
Uncertainty Quantification (UQ) aims to measure the reliability of model predictions, serving as a critical safeguard for deploying Vision-Language Models (VLMs) in safety-critical scenarios. Post-hoc approaches are widely adopted due to their lightweight nature, mapping the outputs of VLMs to uncertainty measures through learnable modules or inductive summarization. However, Post-hoc approaches remain inherently confined to fitting the failure patterns of the source domain, ignoring the dynamic nature of test distributions. To address this challenge, we propose a Dynamic Distribution-Aware Uncertainty Quantification framework (DDA-UQ) that shifts the paradigm from static mapping to a dynamic distribution-aware process. During training, we leverage a Gaussian Mixture Model to model the VVLMs'embedding space and extract distributional evidence, thereby dynamically deriving uncertainty estimates. During inference, the design dynamically responds to changes in the data distribution. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods.

## Metadata
- **Published**: 2026-08-10T01:53:28Z
- **Authors**: Ao Zhou, Zhiwei Jiang, Zifeng Cheng, Cong Wang, Shufan Yang, Haoru Chen, Qing Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09011v1)