---
title: Adaptive $k$ Nearest Neighbors Classifier via Granular Ball Computing
published: 2026-08-13T07:39:46Z
authors: Xiaoyu Lian, Shuyin Xia, Hongxuan He, Lifeng Shen, Guoyin Wang, Xinbo Gao
url: http://arxiv.org/abs/2608.12903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive $k$ Nearest Neighbors Classifier via Granular Ball Computing

## Abstract
The $k$-Nearest Neighbor~(KNN) algorithm is widely used across various tasks. The selection of the $k$ value is a key issue because it significantly impacts performance. In this paper, an adaptive and efficient KNN approach via granular-ball computing is proposed. The method consists of two stages. \textcolor{black}{In the training stage, the dataset is first coarsely partitioned to reduce the complexity of data distributions within a granular ball, and then the Fisher criterion is introduced to control ball splitting and stopping, yielding a multi-granularity granular ball representation. In the prediction stage, the nearest granular ball is first located through a weighted distance mechanism, and an adaptive neighborhood is then constructed around the test sample. The effective $k$ value is dynamically determined by the actual number of samples contained in this neighborhood. The neighborhood induced by the nearest granular ball provides more stable local group information, thereby improving robustness against noise and local perturbations.} Experimental results demonstrate that the proposed method outperforms existing KNN variants across multiple datasets in terms of both accuracy and efficiency. The code has been open-sourced for reproducibility: https://github.com/lianxiaoyu724/Adaptive-GBKNN.

## Metadata
- **Published**: 2026-08-13T07:39:46Z
- **Authors**: Xiaoyu Lian, Shuyin Xia, Hongxuan He, Lifeng Shen, Guoyin Wang, Xinbo Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12903v1)