---
title: Learning to Zoom Efficiently with a Contrastive Curriculum
published: 2026-09-02T22:43:54Z
authors: Falko Helm, Iryna Gurevych
url: http://arxiv.org/abs/2609.03206v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Zoom Efficiently with a Contrastive Curriculum

## Abstract
Using a zoom-in tool is an important foundational part of modern visual agents, because it allows to efficiently handle tasks involving high-resolution images. Most previous methods need an extensive warm-start supervised fine-tuning phase for teaching models zoom-in. We show that this is not necessary by proposing a new intrinsic reward for learning tool use in MLLMs without the need for additional labels or warm-start SFT. Our InfoNCE-style reward uses a curriculum of increasingly hard negative tool calls as a contrastive training signal. Empirical experiments on $V^*$, HRBench and MME-RealWorld show that our approach is competitive while being more efficient. When used as a drop-in replacement for SFT, we even outperform all baselines. To directly measure the zoom-in ability of models, we further introduce the scalable synthetic Muffin&Chihuahua (M&C) dataset. Each image consists of a grid with every cell either showing a muffin or chihuahua. Leveraging the M&C dataset's unique region of interest labels, we find that recall is the metric that most strongly correlates the zoom-in region with final task performance. Our model and code for reproduction is publicly available under https://github.com/UKPLab/emnlp2026-zoom-in

## Metadata
- **Published**: 2026-09-02T22:43:54Z
- **Authors**: Falko Helm, Iryna Gurevych
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03206v1)