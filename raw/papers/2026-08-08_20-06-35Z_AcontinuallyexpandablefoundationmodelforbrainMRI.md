---
title: A continually expandable foundation model for brain MRI
published: 2026-08-08T20:06:35Z
authors: Michail Mamalakis, Carmen Jimenez-Mesa, Yonghao Li, Hao Chen, Chao Li, Antonios Mamalakis, John Suckling, Richard Bethlehem, Stephen J. Price, Richard J. Gilbertson, Pietro Lio
url: http://arxiv.org/abs/2608.08319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A continually expandable foundation model for brain MRI

## Abstract
Brain magnetic resonance imaging (MRI) is central to neuroscience and clinical assessment, but models are commonly developed for individual diseases, populations or imaging protocols. Foundation models promise more general representations, yet they are usually pretrained once and can lose earlier capabilities when updated with new data. Here we show that Alcmaeon, a three-dimensional brain MRI foundation model pretrained without manual labels on more than 425,000 volumes and derived imaging maps, can be expanded sequentially across clinical domains. Alcmaeon combines volumetric encoding and latent diffusion generation with Graph-Blueprint Pruning (GBP), which protects network modules important to earlier domains while leaving the remaining capacity trainable. Across expansion from healthy ageing and neurodegeneration to developmental, psychiatric and tumour imaging, GBP showed less forgetting than sequential adaptation and elastic weight consolidation across voxel-level reconstruction measures, with its largest advantage after adaptation to tumour imaging. The blueprints provided an inspectable record of how model capacity was protected and reused. Representations from different model levels supported image synthesis, disease classification, survival modelling and postoperative prediction, although no single representation was optimal for every task. These findings provide a route towards brain MRI foundation models that can grow with emerging data while retaining earlier capabilities.

## Metadata
- **Published**: 2026-08-08T20:06:35Z
- **Authors**: Michail Mamalakis, Carmen Jimenez-Mesa, Yonghao Li, Hao Chen, Chao Li, Antonios Mamalakis, John Suckling, Richard Bethlehem, Stephen J. Price, Richard J. Gilbertson, Pietro Lio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08319v1)