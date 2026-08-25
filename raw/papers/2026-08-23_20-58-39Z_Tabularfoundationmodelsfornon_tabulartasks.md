---
title: Tabular foundation models for non-tabular tasks
published: 2026-08-23T20:58:39Z
authors: Goran Nakerst, John Brennan, Wouter Beugeling, Masudul Haque
url: http://arxiv.org/abs/2608.22594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tabular foundation models for non-tabular tasks

## Abstract
Tabular foundation models (TFMs) have recently emerged as a promising paradigm for machine learning on tabular data, offering the ability to generalize across datasets without task-specific training. Since many machine learning datasets can be represented as tables, this raises the question: does TFM capability extend beyond tasks traditionally regarded as tabular? We address this question by using TabPFN v3 on three non-tabular classification problems: handwritten digit recognition on MNIST, language identification of French and German words, and image classification on Tiny ImageNet. In each case, the original data are represented as rows of a table and classification is formulated as prediction of a missing label. We evaluate performance as a function of the number of context samples provided to the pretrained model, with no additional training or fine-tuning. Despite having no explicit access to the spatial or sequential structure characterizing the data, TabPFN v3 in some cases achieves accuracies comparable with that of models or methods geared specifically toward the corresponding tasks.

## Metadata
- **Published**: 2026-08-23T20:58:39Z
- **Authors**: Goran Nakerst, John Brennan, Wouter Beugeling, Masudul Haque
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22594v1)