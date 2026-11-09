---
title: A Proxy-Based Method for Measuring Racial Disparities in~Text-to-Image~Generators
published: 2026-11-04T20:58:20Z
authors: Nia Mucher, Ngan Pham, Jason Chin, Aaron Brown, David Evans
url: http://arxiv.org/abs/2611.07132v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Proxy-Based Method for Measuring Racial Disparities in~Text-to-Image~Generators

## Abstract
We present an automated method for auditing text-to-image generators for representational bias against ground-truth demographic benchmarks. Our approach adapts the racial proxy variables used in U.S. antidiscrimination law to provide a fine-grained comparative analysis of variations in racial representation in generated images. We classify each generated image by race and then compare the model's distribution to publicly available demographic benchmark data to identify patterns of over- and under-representation. We also measure skin tone using CIELAB values and calculate cosine similarity amongst groups of images in order to capture biases that don't show up in demographic comparisons such as differences in image quality across races and skin tones. We report on experiments testing three models (Imagen 4 Fast, Stable Diffusion 3.5 Large Turbo, and Flux Schnell) using three categories of proxies (geographic, occupational, and surname) and 50 variants within each category. We find notable variation across the models as well as by proxy category. For example, Imagen 4 Fast overrepresents white classified images more than the other models tested and produces images with lighter, more homogeneous skin tones. Imagen 4 Fast also had the largest representational disparity for Black demographics among surname and geographical prompts. Stable Diffusion 3.5 Large Turbo produces results that overall diverge most from census data but yield the most diverse range of skin tones. Our method yields a generalizable and legally-grounded auditing tool that surfaces detailed information about model outputs without relying on implicit normative definitions of fairness.

## Metadata
- **Published**: 2026-11-04T20:58:20Z
- **Authors**: Nia Mucher, Ngan Pham, Jason Chin, Aaron Brown, David Evans
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.07132v1)