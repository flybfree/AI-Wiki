---
title: Invisible Shortcuts: Why Vision Encoders Know Your Camera
published: 2026-08-05T21:36:34Z
authors: Vladan Stojnić, Ryan Ramos, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias
url: http://arxiv.org/abs/2608.05424v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Invisible Shortcuts: Why Vision Encoders Know Your Camera

## Abstract
Deep vision models exploit shortcuts, relying on cues that correlate with supervision signals. Prior work has focused on visible biases, such as object-background or texture correlations. We identify a different source of shortcut learning: invisible metadata traces embedded at the pixel level, for metadata such as image processing and photo acquisition. We hypothesize that large-scale semantic supervision, whether through categorical labels (ImageNet) or billion-scale captions (LAION), naturally induces metadata-semantics correlations during pretraining, leading models to convert low-level signals into predictive features. By introducing controlled metadata-semantics correlations, we show that stronger ones produce systematically higher sensitivity to metadata traces and larger performance degradation under metadata distribution shifts. We further explore mitigation strategies applied during and after pretraining that reduce sensitivity not only to targeted metadata but also to unseen ones, without sacrificing performance on downstream tasks. Metadata sensitivity also has a positive side: it partly explains the strong generated-image detection ability of some encoders, while its mitigation can improve out-of-distribution generalization. Code: https://github.com/ryan-caesar-ramos/visual-encoder-traces

## Metadata
- **Published**: 2026-08-05T21:36:34Z
- **Authors**: Vladan Stojnić, Ryan Ramos, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05424v1)