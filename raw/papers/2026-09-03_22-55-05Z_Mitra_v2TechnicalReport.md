---
title: Mitra-v2 Technical Report
published: 2026-09-03T22:55:05Z
authors: Yefan Tao, Xiyuan Zhang, Xinyi Liu, Boran Han, Danielle Maddix, Haoyang Fang, Zhen Han, Jiading Gai, Xuanqing Liu, Michael Bohlke-Schneider,  Yuyang,  Wang, Gerald Friedland, Kevan Mah, Chris Lee, Chris Kong
url: http://arxiv.org/abs/2609.04540v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mitra-v2 Technical Report

## Abstract
We introduce Mitra-v2, a tabular foundation model that delivers state-of-the-art performance on real-world classification and regression problems, from credit-risk scoring and clinical prediction to equipment-failure detection and house-price estimation. Mitra-v2 is trained only on synthetic data, with a pretraining distribution that is much larger and more diverse than Mitra-v1's. Built on a small 2D Transformer backbone, Mitra-v2 supports longer contexts and larger feature spaces. Improved optimization lets it learn from this larger task distribution. We evaluate Mitra-v2 on the TabArena and TALENT benchmarks, comprising more than 300 real-world datasets under two evaluation protocols. On the full TabArena benchmark, Mitra-v2 delivers state-of-the-art performance at the level of the industry-scale TabFM and EXAONE Tabular models, while surpassing TabPFN-3 by a wide margin in both classification and regression. Mitra-v2 matches the 1.6B-parameter TabFM with only 5% of its size (77M parameters), delivering frontier performance at a fraction of the cost. On TALENT, Mitra-v2 remains among the leading models, clearly outperforming TabPFN-3 and TabICLv2. It also ranks first on classification tasks with more than ten classes, even though it was pretrained only on tasks with at most ten classes. These results make Mitra-v2 one of the strongest and most broadly applicable open tabular foundation models released to date. We release the model weights, the inference and fine-tuning code, and our evaluation results under the Apache-2.0 license.

## Metadata
- **Published**: 2026-09-03T22:55:05Z
- **Authors**: Yefan Tao, Xiyuan Zhang, Xinyi Liu, Boran Han, Danielle Maddix, Haoyang Fang, Zhen Han, Jiading Gai, Xuanqing Liu, Michael Bohlke-Schneider,  Yuyang,  Wang, Gerald Friedland, Kevan Mah, Chris Lee, Chris Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04540v1)