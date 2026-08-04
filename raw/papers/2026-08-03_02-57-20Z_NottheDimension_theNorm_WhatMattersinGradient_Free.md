---
title: Not the Dimension, the Norm: What Matters in Gradient-Free Weight Perturbation of Language Models
published: 2026-08-03T02:57:20Z
authors: Taeyeong Kim, Ahhyun Kim, TaeHyeon Kim, Unggi Lee
url: http://arxiv.org/abs/2608.01624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not the Dimension, the Norm: What Matters in Gradient-Free Weight Perturbation of Language Models

## Abstract
Adapting a language model to a task no longer requires training all of its weights, and a line of parameter-efficient methods has driven the trainable count from billions down to a handful of scalars. Gradient-free adaptation, which samples random weight perturbations and keeps the ones that score well, has not followed that trajectory and still perturbs every entry of the weight tensor. It is unknown whether that full-weight search is necessary, and more fundamentally which property of a perturbation makes it work at all, because existing methods vary the search space, the perturbation scale, and the aggregation together. We resolve this by intervening on one factor at a time inside a fixed pipeline, holding candidate scoring and voting constant while we vary the search dimension, the subspace that carries the perturbation, and its norm. Perturbing a frozen frame of 12 to 16 scalars stays 1.8 accuracy points behind full-weight search on average across 49 model-benchmark cells, trailing it in 36 of them. Neither the dimension nor the choice of basis explains that performance. A random frame whose Grassmann overlap with the SVD frame is at chance level performs identically once a single scale factor is matched, and at large scales the SVD directions collapse first. What survives is the perturbation norm, whose usable range closes within a factor of five across seven models and stays flat inside. The perturbation norm is therefore the one factor with a failure mode, and its safe region transfers across scale and family. The design question narrows from which subspace to perturb to how hard to shake.

## Metadata
- **Published**: 2026-08-03T02:57:20Z
- **Authors**: Taeyeong Kim, Ahhyun Kim, TaeHyeon Kim, Unggi Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01624v1)