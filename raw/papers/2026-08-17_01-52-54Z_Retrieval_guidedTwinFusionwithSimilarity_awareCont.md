---
title: Retrieval-guided Twin Fusion with Similarity-aware Contrast for Molecule-Text Alignment
published: 2026-08-17T01:52:54Z
authors: Shunshun Gu, Shengqi Qiu, Hang Zhou, Xiao Luo
url: http://arxiv.org/abs/2608.16005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-guided Twin Fusion with Similarity-aware Contrast for Molecule-Text Alignment

## Abstract
This paper studies the problem of molecule-text alignment, which aims to project molecules and their textual descriptions into a joint latent space for downstream tasks including molecule search and molecular property prediction. Previous approaches typically combine graph structure mining with contrastive learning to enhance joint representation learning. However, they typically neglect fine-grained semantic relationships between substructures and texts, leading to suboptimal performance on downstream tasks. Towards this end, we propose a novel approach named Retrieval-guided Twin Fusion with Similarity-aware Contrast (RISEN) for molecule-text alignment. The core idea of RISEN is to construct a latent twin molecule for each substructure with cross-modal retrieval for semantic enhancement. In particular, for each substructure query, we retrieve relevant textual descriptions and sample several molecules that share similar descriptions of substructures. Then, we aggregate their representations via attention pooling for a twin latent representation, which would be further fused with the original substructure for representation enrichment. In addition, we measure the similarity across substructures and texts, which would further guide cross-modal contrastive learning with soft thresholding. Extensive experiments on benchmark datasets validate the superiority of the proposed RISEN in comparison with existing baselines.

## Metadata
- **Published**: 2026-08-17T01:52:54Z
- **Authors**: Shunshun Gu, Shengqi Qiu, Hang Zhou, Xiao Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16005v1)