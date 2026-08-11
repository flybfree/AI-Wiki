---
title: Decoding Phenotypes: A Framework for Fusing Genomic Language Models and Neuroimaging
published: 2026-08-09T21:40:17Z
authors: Tianli Tao, Ziyang Wang, Emma Robinson, Rachel Sparks, Le Zhang
url: http://arxiv.org/abs/2608.08926v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoding Phenotypes: A Framework for Fusing Genomic Language Models and Neuroimaging

## Abstract
Neuroimaging and genetic testing are two important clinical references for nervous system diseases, offering complementary diagnostic information. However, integrating genomic and neuroimaging data for precise disease diagnosis is challenging due to cross-modality heterogeneity. Existing imaging-genetics approaches mainly encode genetic information as hard-coded labels, which lose the local sequence context around disease-associated variants. To address this limitation, we propose GeneFuse, a multimodal learning framework that aligns genetic representations from pre-trained Genomic Language Models (GLMs) with features extracted from images. GeneFuse integrates two components: (1) Genotype-Conditioned Feature Modulation (GCFM), a FiLM-inspired module that uses genomic embeddings to modulate image feature maps; and (2) Uncertainty-aware Genomic Residual Fusion (U-GRF), a fusion strategy that uses imaging-derived predictive uncertainty to gate the contribution of genotypic features. We evaluate GeneFuse on early cognitive decline identification (NC vs. MCI) and dementia screening (NC vs. AD). In the APOE-centered setting, GeneFuse achieves AUROCs of 0.77 and 0.83, outperforming existing imaging-genetics fusion methods. These results indicate that GLM-derived genomic embeddings provide additional information to imaging.

## Metadata
- **Published**: 2026-08-09T21:40:17Z
- **Authors**: Tianli Tao, Ziyang Wang, Emma Robinson, Rachel Sparks, Le Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08926v1)