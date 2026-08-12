---
title: MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment
published: 2026-08-11T17:28:52Z
authors: Changhao Xiang, Shangyu Xing, Zhen Wu, Jianbing Zhang, Xinyu Dai
url: http://arxiv.org/abs/2608.11167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment

## Abstract
Existing Multimodal Large Language Models (MLLMs) predominantly rely on image-text pairs for modality alignment pretraining, mapping global image representations to long textual descriptions. However, this image-level alignment suffers from referential ambiguity: models struggle to infer the correspondences between multiple visual objects and textual entities from the global representation, leading to data inefficiency and suboptimal semantic grounding. To address this, we propose MultiModal Code-Switching (MMCS), a novel pretraining paradigm that provides explicit object-level supervision. Inspired by the linguistic phenomenon of code-switching, MMCS interleaves vision and language by replacing textual entities with their corresponding visual objects, enforcing local vision-language grounding. We further develop a scalable data synthesis pipeline to generate a pretraining dataset of 773K samples with accurate object-entity correspondences. Experiments show that MMCS is highly data-efficient: with only 50K samples, it matches or surpasses models trained on 600K image-text pairs. Furthermore, MMCS consistently improves visual grounding and perception capabilities across varying model scales.

## Metadata
- **Published**: 2026-08-11T17:28:52Z
- **Authors**: Changhao Xiang, Shangyu Xing, Zhen Wu, Jianbing Zhang, Xinyu Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11167v1)