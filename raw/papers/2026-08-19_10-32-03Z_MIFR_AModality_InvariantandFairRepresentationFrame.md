---
title: MIFR: A Modality-Invariant and Fair Representation Framework for Skin Disease Classification
published: 2026-08-19T10:32:03Z
authors: Asonyu Senge Njih, Yvan Guifo Fodjo, Vianney Kengne Tchendji, Jerry Lacmou Zeutouo, Kerol Djoumessi
url: http://arxiv.org/abs/2608.18774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MIFR: A Modality-Invariant and Fair Representation Framework for Skin Disease Classification

## Abstract
Skin diseases represent a major global public health burden, yet machine learning tools developed to assist in their diagnosis suffer from two critical limitations: reliance on only one modality for diagnosis and systematic performance disparities across skin tones. While existing approaches address each challenge separately, this work proposes a modality-invariant framework with fair representation (MIFR) for skin disease classification. The architecture pairs clinical photographs with dermoscopic images using ViT-based encoders, projecting each input into a high-dimensional embedding space via modality-specific projection heads. The resulting model is trained with a five-component multi-objective loss including weighted cross-entropy for classification, confusion and skin-type classification losses for fairness, per-modality supervised contrastive loss for class alignment, and a modality-invariance loss for clinical and dermoscopic modality alignment. Experiments on the HIBA+Derm7pt paired dataset and the external PAD-UFES-20 and ISIC 2019 datasets showed that modality-invariant representation learning provides competitive predictive performance compare to relevant baseline models and competitive fairness on the internal dataset. t-SNE visualizations confirmed that clinical and dermoscopic embeddings of the same disease are geometrically aligned, validating the joint objectives.

## Metadata
- **Published**: 2026-08-19T10:32:03Z
- **Authors**: Asonyu Senge Njih, Yvan Guifo Fodjo, Vianney Kengne Tchendji, Jerry Lacmou Zeutouo, Kerol Djoumessi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18774v1)