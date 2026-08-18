---
title: PaSTel: Anchoring Histology in Spatial Transcriptomics via Multi-Scale Hierarchical Bio-Prior Contrastive Pretraining
published: 2026-08-14T22:26:17Z
authors: Azim Dehghani Amirabad, Junchao Zhu, Pushpak Pati, Walid Abdelmoula, Tommaso Mansi, Rui Liao
url: http://arxiv.org/abs/2608.14924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PaSTel: Anchoring Histology in Spatial Transcriptomics via Multi-Scale Hierarchical Bio-Prior Contrastive Pretraining

## Abstract
Spatial transcriptomics (ST) links tissue morphology with molecular programs, motivating multimodal pretraining methods that align histology images with gene expression. However, existing approaches suffer from two key limitations: spatially informative gene selection is often dominated by ubiquitous housekeeping genes, leading to weakly discriminative representations, and independent spot-patch alignment fails to capture spatial dependencies that are critical for tissue organization. To address these challenges, we introduce PaSTel, a hierarchical multimodal pretraining framework that integrates biological priors at three levels. At the spot level, TF-IDF reweighting is used to identify spatially informative genes; at the functional level, curated KEGG pathways serve as anchors for encoding global biological semantics; and at the regional level, spatial clustering aggregates neighboring spots to model meso-scale tissue structure. Across multiple downstream tasks, PaSTel consistently outperforms existing vision and vision-omics encoders, demonstrating that incorporating multiscale biological priors yields more informative and transferable representations for spatial transcriptomics.

## Metadata
- **Published**: 2026-08-14T22:26:17Z
- **Authors**: Azim Dehghani Amirabad, Junchao Zhu, Pushpak Pati, Walid Abdelmoula, Tommaso Mansi, Rui Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14924v1)