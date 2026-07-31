---
title: MUL-T: Decoding Spatial Cellular Architecture in Multiplexed Tissue Images
published: 2026-07-30T11:15:12Z
authors: Farzaneh Seyedshahi, Kai Rakovic, Adalberto Claudio Quiros, John LeQuesne, Ke Yuan
url: http://arxiv.org/abs/2607.28030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MUL-T: Decoding Spatial Cellular Architecture in Multiplexed Tissue Images

## Abstract
Understanding tissue organisation in multiplexed imaging requires modelling both cellular phenotypes and their spatial context. Existing approaches typically rely on handcrafted features, such as marker intensity statistics or cell-type proportions, which often fail to scale or generalise across cohorts with heterogeneous marker panels. We introduce MUL-T, a lightweight transformer framework that reframes tissue architecture as a masked contextual prediction task over discrete cell tokens. By learning contextualised [CLS] embeddings without task-specific supervision, the model captures higher-order cellular interactions while remaining computationally efficient. We evaluate MUL-T on several clinically relevant downstream tasks, including core-level tumour pattern classification, patient-level grading, PD-L1 positivity prediction, and cross-dataset treatment response prediction. Across tasks, MUL-T consistently outperforms classical feature-based baselines and achieves performance comparable to a foundation ViT model, despite substantially fewer parameters and lower training cost.

## Metadata
- **Published**: 2026-07-30T11:15:12Z
- **Authors**: Farzaneh Seyedshahi, Kai Rakovic, Adalberto Claudio Quiros, John LeQuesne, Ke Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28030v1)