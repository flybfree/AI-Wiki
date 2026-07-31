---
title: Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation
published: 2026-07-30T13:25:09Z
authors: Marco Alecci, Francesco Marchiori, Iyiola Emmanuel Olatunji, Tegawendé F. Bissyandé, Jacques Klein
url: http://arxiv.org/abs/2607.28187v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation

## Abstract
While automated content-moderation systems have become essential for screening harmful content at scale, conventional task-specific classifiers often provide limited policy cov- erage and contextual understanding. Recently, commercial multimodal moderation APIs built on large foundation models have been introduced with the promise of providing broader and more capable safety filters. In this work, we analyze whether this shift also yields more robust image moderation. We conduct a large-scale black-box evaluation on three established commercial image-moderation services and compare their robustness. By evaluating seven simple, model-agnostic image transformations across multiple providers, datasets, harm categories, perceptual-similarity constraints, and transformation intensities, we find that: (1) all three commercial services can be bypassed using inexpensive image transformations that require no gradients, surrogate models, or knowledge of the target system; (2) even fixed transformations such as color inversion and grayscale conversion induce unsafe-to-safe decision changes while preserving content that remains recognizable to humans; (3) their robustness varies substantially across datasets and harm categories, with multimodal content and self-harm exhibiting pronounced vulnerabilities. This yields the conclusion that replacing conventional moderation classifiers with foundation-model-based APIs does not, by itself, provide a reliable security boundary. Such systems must be evaluated under realistic transformations and deployed as one component of a layered moderation pipeline rather than as standalone safety filters.

## Metadata
- **Published**: 2026-07-30T13:25:09Z
- **Authors**: Marco Alecci, Francesco Marchiori, Iyiola Emmanuel Olatunji, Tegawendé F. Bissyandé, Jacques Klein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28187v1)