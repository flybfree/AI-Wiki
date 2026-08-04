---
title: Auditing Semantic Gains in Sequential Recommendation: A Lightweight Recovery Test
published: 2026-08-02T14:15:50Z
authors: Kong Wang, Zhongke He, Xiang Chen, Hongwei Zeng, Kai Deng, Long Wang, Kehua Yang
url: http://arxiv.org/abs/2608.01260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Semantic Gains in Sequential Recommendation: A Lightweight Recovery Test

## Abstract
Recent semantic and generative-retrieval recommenders report substantial improvements over ID-only sequential baselines, but it remains unclear whether these gains arise from language-model reasoning, semantic-ID generation, end-to-end semantic architectures, stronger offline item representations, or complementary semantic and collaborative signals. We investigate this attribution ambiguity through LIME-Rec, a lightweight and auditable recovery test. LIME-Rec combines three independent experts: a SASRec sequential expert, an ItemCF co-occurrence expert, and a semantic expert based on frozen BAAI/bge-base-en-v1.5 item embeddings. Their full-catalog scores are normalized per user and combined through auditable score-level fusion followed by bounded history calibration. The fusion gate and calibration head are fitted on validation data only, require no serving-time language-model inference, and keep each expert contribution separately inspectable. On Amazon Beauty, Toys, and Sports, LIME-Rec achieves R@10 scores of 0.0996, 0.1105, and 0.0593, outperforming the strongest comparison baseline by 7.0%-12.0%. Three-expert fusion without history calibration consistently outperforms calibrated SASRec, showing that calibration alone does not explain the recovery. Randomly permuting item-text embeddings across item IDs reduces R@10 by 13.6%-17.5%, indicating that the gains depend on genuine item-text correspondence rather than additional representation capacity. These results suggest that lightweight recovery from offline item representations and transparent fusion should be ruled out before improvements are attributed to serving-time language modeling, semantic-ID generation, or heavier semantic machinery.

## Metadata
- **Published**: 2026-08-02T14:15:50Z
- **Authors**: Kong Wang, Zhongke He, Xiang Chen, Hongwei Zeng, Kai Deng, Long Wang, Kehua Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01260v1)