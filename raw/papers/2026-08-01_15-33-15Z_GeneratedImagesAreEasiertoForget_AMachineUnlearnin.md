---
title: Generated Images Are Easier to Forget: A Machine Unlearning Perspective for Synthetic Image Detection
published: 2026-08-01T15:33:15Z
authors: Jun Nie, Yonggang Zhang, Tongliang Liu, Yiu-ming Cheung, Bo Han, Xinmei Tian
url: http://arxiv.org/abs/2608.00716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generated Images Are Easier to Forget: A Machine Unlearning Perspective for Synthetic Image Detection

## Abstract
Robust detection of generated images is critical to counter the misuse of generative models. Existing methods primarily depend on learning from human-annotated training datasets, limiting their generalization to unseen distributions. In contrast, large-scale vision models (LVMs) pre-trained on web-scale datasets exhibit exceptional generalization power through exposure to diverse distributions, offering a transformative paradigm for this task. However, our experimental results reveal that LVMs pre-trained on natural-image-dominated data can effectively capture the features of both natural and generated images, yielding comparably low losses and thus limited discriminative capacity between them. This prompts a key question: When and how do LVMs exhibit different behaviors when capturing features of natural and generated images? This investigation reveals an insight: during unlearning, LVMs exhibit disparate forgetting dynamics with feature degradation for generated images escalating faster than natural ones. Inspired by the disparate dynamics, we introduce two detection methods: 1) data-free detection, which prunes model parameters to induce unlearning without data access, and 2) data-driven detection, which optimizes LVMs to unlearn knowledge tied to generated images. Extensive experiments conducted on various benchmarks demonstrate that our unlearning-based approach outperforms conventional detection methods. By recasting the detection task as a problem of machine unlearning, our work establishes a new paradigm for generated image detection.

## Metadata
- **Published**: 2026-08-01T15:33:15Z
- **Authors**: Jun Nie, Yonggang Zhang, Tongliang Liu, Yiu-ming Cheung, Bo Han, Xinmei Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00716v1)