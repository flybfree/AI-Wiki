---
title: Robustness of AI-Art Detectors under Generator Shift
published: 2026-08-12T04:41:38Z
authors: Shivank Singh Thakur, Meien Li, Mark Stamp
url: http://arxiv.org/abs/2608.11643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robustness of AI-Art Detectors under Generator Shift

## Abstract
Text-to-image generative models have advanced rapidly, with modern Diffusion Transformer architectures producing images that are increasingly difficult to distinguish from human-created artwork. This development has raised significant concerns regarding copyright protection, misinformation, fraud, impersonation, and the authenticity of digital content. Most AI-art detectors are trained and evaluated on the same generator family, leaving robustness to newer architectures underexplored. In this chapter, we analyze generator shift based on a Stable Diffusion 3.5 Medium (SD3.5m) artwork dataset spanning ten art styles through reverse prompting of held-out human artwork samples. Five detectors are trained on U-Net-based latent diffusion artwork and evaluated in a zero-shot cross-generator setting on the SD3.5m dataset. Deep learning models perform strongly in-distribution but degrade under generator shift, misclassifying many SD3.5m images as human while human false positives remain low. The CLIP ViT-L/14 model performs best overall, while Grad-CAM analysis reveals weaker and more diffuse activation on false negatives. These findings highlight a generalization gap in current AI-art detectors and motivate the development of detectors as one component of a layered defense that remains reliable across rapidly evolving generative architectures.

## Metadata
- **Published**: 2026-08-12T04:41:38Z
- **Authors**: Shivank Singh Thakur, Meien Li, Mark Stamp
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11643v1)