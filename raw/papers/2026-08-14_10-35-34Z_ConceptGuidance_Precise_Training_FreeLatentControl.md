---
title: Concept Guidance: Precise, Training-Free Latent Control for Text-to-Image Generation
published: 2026-08-14T10:35:34Z
authors: Nikolai Röhrich, Isabell Hans, Felix Krause, Björn Ommer
url: http://arxiv.org/abs/2608.14172v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Concept Guidance: Precise, Training-Free Latent Control for Text-to-Image Generation

## Abstract
Text-to-image diffusion models have two major drawbacks that severely limit their practical utility: (1) standard models lack an intrinsic mechanism for continuous, concept-specific guidance (e.g., for precisely controlling how aesthetically pleasing an image looks), and (2) they lack reliability for tasks requiring high local coherence (e.g., generating text or human hands). To tackle these issues, we introduce a novel notion of concept-wise mutual information and find large, concept-dependent differences between individual layers, demonstrating that the generation of specific structures is localized in distinct parts of the network. We exploit this insight by reinforcing the impact of concept-relevant layers in Concept Guidance (CoG), a precise, target-specific guidance method that works for models out-of-the-box without additional training, external models, gradients, or prompt engineering. CoG first quantifies each layer's concept-specific impact and then guides denoising using a weighted combination of predictions generated with concept-relevant layers skipped. We demonstrate performance increases across various targets and popular models like PixArt-alpha, SD3, SD3.5, and FLUX.1-dev. Code is available at https://github.com/CompVis/concept_guidance

## Metadata
- **Published**: 2026-08-14T10:35:34Z
- **Authors**: Nikolai Röhrich, Isabell Hans, Felix Krause, Björn Ommer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14172v1)