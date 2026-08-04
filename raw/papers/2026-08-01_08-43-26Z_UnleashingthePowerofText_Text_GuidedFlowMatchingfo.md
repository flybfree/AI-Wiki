---
title: Unleashing the Power of Text: Text-Guided Flow Matching for Image Fusion under Complex Degradations
published: 2026-08-01T08:43:26Z
authors: Axi Niu, Jieheng Li, Kang Zhang, Qingsen Yan, Jinqiu Sun, Yanning Zhang
url: http://arxiv.org/abs/2608.00530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unleashing the Power of Text: Text-Guided Flow Matching for Image Fusion under Complex Degradations

## Abstract
Infrared-visible image fusion under realistic degradation scenarios is a challenging task, as degradations not only cause a loss of reliable modality-specific information in observed images but also hinder the fusion process. Recent studies indicate that text can provide prior information about degradation characteristics, complementing the limited evidence available from corrupted input images and facilitating fusion. However, existing methods typically inject fixed global text representations into visual features, making it difficult for textual guidance to adapt to spatially varying degradations, local structures, and thermal saliency. To this end, we propose TGFusion, a text-guided latent-space flow matching framework that unifies degradation suppression and cross-modal fusion. TGFusion encodes task, degradation, and generation cues into structured prompts. To fully exploit these priors, we design a Prompt-conditioned Multi-stream Joint Flow Transformer that represents text as an independent semantic stream alongside fusion, visible, and infrared streams. Joint attention enables token-level bidirectional interaction and layer-wise updating among semantic and visual representations, allowing degradation semantics to dynamically guide reliable information selection and fusion latent generation. Extensive experiments on public benchmarks and complex degradation scenarios demonstrate that TGFusion achieves superior or competitive performance in perceptual quality, image naturalness, structural-detail preservation, and infrared-saliency retention, while remaining robust across diverse single and compound degradations.

## Metadata
- **Published**: 2026-08-01T08:43:26Z
- **Authors**: Axi Niu, Jieheng Li, Kang Zhang, Qingsen Yan, Jinqiu Sun, Yanning Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00530v1)