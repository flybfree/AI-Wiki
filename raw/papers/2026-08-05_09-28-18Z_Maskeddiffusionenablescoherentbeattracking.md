---
title: Masked diffusion enables coherent beat tracking
published: 2026-08-05T09:28:18Z
authors: Francesco Foscarin, Filip Korzeniowski, Richard Vogl
url: http://arxiv.org/abs/2608.04624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Masked diffusion enables coherent beat tracking

## Abstract
Current neural networks for beat tracking generate invalid outputs, such as consecutive downbeats and erratic tempo changes, even when these are not present in the training data. Heavy post-processing techniques can alleviate these problems, but the original cause of this inconsistent behaviour remains unknown. We hypothesise that it stems from inadequate modelling of multiple plausible output beat grids, resulting in an invalid mixture of competing interpretations. We propose a masked diffusion approach that properly models multiple outputs and enables the model to build coherent predictions through iterative inference. We devise three modifications to standard masked diffusion that enable its application to beat tracking: independent masking of beats and downbeats during training and inference, a balanced masking scheduler for inference, and peak-picking across inference steps. Our approach reduces erratic behaviours and improves beat-tracking performance.

## Metadata
- **Published**: 2026-08-05T09:28:18Z
- **Authors**: Francesco Foscarin, Filip Korzeniowski, Richard Vogl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04624v1)