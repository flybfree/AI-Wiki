---
title: MURANO: Design, Run, and Reproduce Mechanistic Interpretability Experiments as Composable Pipelines
published: 2026-08-31T12:02:35Z
authors: Alireza Bayat Makou, Emirhan Böge, Phu Gia Hoang, Federico Tiblias, Jingcheng Niu, Subhabrata Dutta, Richard Eckart de Castilho, Iryna Gurevych
url: http://arxiv.org/abs/2608.30662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MURANO: Design, Run, and Reproduce Mechanistic Interpretability Experiments as Composable Pipelines

## Abstract
This paper presents Murano, an open source framework for designing, running, and reproducing mechanistic interpretability studies of large language models, intended for researchers across disciplines. These studies often combine loading, recording, attribution, intervention, and evaluation, while existing libraries tend to focus on different parts of this workflow. As a result, researchers using several libraries may need to adapt outputs from one for use by another. To bridge this gap, Murano represents operations from these five areas as composable steps. Steps exchange named result artifacts and declare the inputs they require and the outputs they produce. A pipeline executes its steps in the order supplied, and Murano uses canonical addresses when component identities pass between operations. Murano builds on existing interpretability and machine learning libraries. We demonstrate Murano through two reproductions of established interpretability studies and one illustrative sparse autoencoder case study.

## Metadata
- **Published**: 2026-08-31T12:02:35Z
- **Authors**: Alireza Bayat Makou, Emirhan Böge, Phu Gia Hoang, Federico Tiblias, Jingcheng Niu, Subhabrata Dutta, Richard Eckart de Castilho, Iryna Gurevych
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30662v1)