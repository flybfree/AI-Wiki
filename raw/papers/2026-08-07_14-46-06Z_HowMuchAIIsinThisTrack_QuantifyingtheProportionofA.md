---
title: How Much AI Is in This Track? Quantifying the Proportion of AI-Generated Stems in Hybrid Music Mixtures
published: 2026-08-07T14:46:06Z
authors: Fernando Garcia de la Cruz, David López-Ayala, Pablo Zinemanas, Emilio Molina, Martín Rocamora
url: http://arxiv.org/abs/2608.07285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Much AI Is in This Track? Quantifying the Proportion of AI-Generated Stems in Hybrid Music Mixtures

## Abstract
AI-generated music is increasingly used at the stem level, with producers integrating synthetic drums, basslines, or vocals alongside human-performed instruments. However, current AI music detection systems are binary, treating tracks as either fully AI or fully human. In this paper, we reformulate AI music detection as a regression problem on a continuous AI energy ratio, alpha in [0, 1]. We propose a methodology that leverages a multi-track music dataset to assemble mixtures of human-performed and AI-reconstructed stems (obtained using a neural audio codec) with known proportions of each content type. Using this approach, we first show that a CNN-based model trained on fully AI-generated or human-performed tracks, which achieves >99% accuracy as a binary detector, when faced with mixed content, yields an output that rises with the AI stems' energy contribution, acting as a noisy and miscalibrated estimator. Our analysis of the influence of different stems shows that detection sensitivity depends on the instrument and reflects its frequency content: drums and guitar carry strong codec-artifact signatures, while vocals and bass are less detectable. Based on these insights, we train a similar CNN-based model for regression of alpha, achieving MAE = 0.076 and R^2 = 0.85 on held-out mixtures from the same pipeline. These results suggest that the regression formulation is an initial promising step towards AI-music detection in realistic music production workflows.

## Metadata
- **Published**: 2026-08-07T14:46:06Z
- **Authors**: Fernando Garcia de la Cruz, David López-Ayala, Pablo Zinemanas, Emilio Molina, Martín Rocamora
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07285v1)