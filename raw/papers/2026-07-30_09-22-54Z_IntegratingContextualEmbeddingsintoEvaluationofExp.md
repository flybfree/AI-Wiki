---
title: Integrating Contextual Embeddings into Evaluation of Expressive MIDI Piano Performances
published: 2026-07-30T09:22:54Z
authors: Dmitrii Gavrilev, Ilya Borovik, Vladimir Viro
url: http://arxiv.org/abs/2607.27909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Integrating Contextual Embeddings into Evaluation of Expressive MIDI Piano Performances

## Abstract
Objective evaluation of expressive MIDI piano performances typically relies on attribute statistics such as timing, velocity, and duration of individual notes. However, these methods often disregard dependencies between notes, which poses a potential limitation in assessing the similarity between two sets of performances. In generative applications, the wide variety of expressive attributes makes it difficult to aggregate them into a single scalar metric for model selection. In this work, we reexamine attribute-scoped metrics and explore the perceptual properties of contextual embeddings from self-supervised symbolic music models, Aria and CLaMP3. Results from our listening study indicate that these models can be used as perceptual proxies, showing agreement with per-sample human ratings on par with traditional metrics. To measure conditional distributional similarity, we adapt Kernel Audio Distance to the symbolic music domain. Unlike Pearson correlation and reconstruction error, kernel-based methods on contextual embeddings do not require note alignment and are sensitive to contextual perturbations. To facilitate reproducibility, we release Pereval, an open-source library that integrates performance evaluation utilities, including both attribute-scoped and deep feature metrics.

## Metadata
- **Published**: 2026-07-30T09:22:54Z
- **Authors**: Dmitrii Gavrilev, Ilya Borovik, Vladimir Viro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27909v1)