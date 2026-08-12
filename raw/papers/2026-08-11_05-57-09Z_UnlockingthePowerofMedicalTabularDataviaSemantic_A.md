---
title: Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training
published: 2026-08-11T05:57:09Z
authors: Yingsheng Liu, Haiming Li, Jingmin Zhu, Jiajun Sun, Victoria Mar, Monika Janda, H. Peter Soyer, Zongyuan Ge, Zhen Yu
url: http://arxiv.org/abs/2608.10522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training

## Abstract
While vision-language models dominate medical representation learning, unstructured text lacks the dense, quantitative diagnostic phenotypes inherent in structured clinical tables. However, existing multimodal pre-training methods underutilize this potential due to semantic-agnostic designs that treat tabular inputs as flat vectors and employ unstable continuous regression objectives. To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional structure of tabular data. First, addressing the inter-feature hierarchy of varying diagnostic importance, we introduce Importance-Aware Adaptive Masking to construct a label-free curriculum prioritizing salient features. Second, addressing the intra-feature continuity-discreteness duality, we propose a Soft-Label Discretized Module that replaces unstable numerical regression with stable distribution matching, thereby mathematically preserving ordinal relationships. Extensive experiments across large-scale dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets establish a new state-of-the-art (SOTA), demonstrating exceptional robustness and cross-domain generalizability.

## Metadata
- **Published**: 2026-08-11T05:57:09Z
- **Authors**: Yingsheng Liu, Haiming Li, Jingmin Zhu, Jiajun Sun, Victoria Mar, Monika Janda, H. Peter Soyer, Zongyuan Ge, Zhen Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10522v1)