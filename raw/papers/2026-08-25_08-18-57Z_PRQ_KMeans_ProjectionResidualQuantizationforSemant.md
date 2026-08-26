---
title: PRQ-KMeans: Projection Residual Quantization for Semantic ID Tokenization
published: 2026-08-25T08:18:57Z
authors: Yunxiao Luo, Siyuan Wang, Ben Chen, Chenyi Lei
url: http://arxiv.org/abs/2608.24207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRQ-KMeans: Projection Residual Quantization for Semantic ID Tokenization

## Abstract
Semantic identifiers (SIDs) represent entities as hierarchical token sequences for generative retrieval and recommendation. Residual-quantization tokenizers construct these sequences by selecting a codeword at each level and passing a residual to the next. We view this process as progressive commonality removal: each token captures a component shared within its group, while later tokens should model the remaining differences. This view reveals three limitations: a corpus-wide shared component can consume first-level capacity, hard assignment ignores graded similarities to nearby codewords, and full-codeword subtraction can leave variation along the selected-codeword direction in the next residual. We therefore develop our solution in the post-hoc setting, where residual construction is not constrained by input reconstruction. Specifically, we propose PRQ-KMeans, which removes the global-mean component, refines centroids with Top-k similarity-weighted updates, and replaces full-codeword subtraction with a projection residual that removes each representation's selected-centroid component. Experiments on a large-scale industrial search dataset and four public recommendation benchmarks show that PRQ-KMeans achieves the strongest overall performance among the evaluated tokenizers, including gains of up to 7.4% in HitRate and 11.8% in MRR on the industrial dataset.

## Metadata
- **Published**: 2026-08-25T08:18:57Z
- **Authors**: Yunxiao Luo, Siyuan Wang, Ben Chen, Chenyi Lei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24207v1)