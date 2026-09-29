---
title: EAT: Expert Account Tracker for Efficient MoE Inference
published: 2026-09-27T14:28:53Z
authors: Yuexian Li, Yifei Yang, Zouying Cao, Hai Zhao
url: http://arxiv.org/abs/2609.33614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EAT: Expert Account Tracker for Efficient MoE Inference

## Abstract
Mixture-of-Experts (MoE) models have emerged as a revolutionary method to scale Transformer models. However, traditional MoE architecture still suffers from inefficiency since a large number of experts are unnecessarily activated. Existing approaches for reducing the number of activated experts often overlook the historical performance of each expert. In this paper, we propose EAT, a novel method called Expert Account Tracker (EAT), which utilizes history-awareness metrics and adaptive thresholding to dynamically select the most important experts, thereby reducing the activated expert number while effectively maintaining the model performance. Experiments show that EAT outperforms the existing baseline Top-P method across multiple models and datasets, achieving over 25% an average reduction compared to the vanilla method in the number of activated experts and performing better token generation speed compared to the baseline. Furthermore, the performance of pruned models can be efficiently recovered via OPD using only 9K data. Additionally, through ablation studies, we find that excessively reducing the number of activated experts can significantly harm model performance, and the importance of experts varies across layers, with higher-level experts being generally more critical.

## Metadata
- **Published**: 2026-09-27T14:28:53Z
- **Authors**: Yuexian Li, Yifei Yang, Zouying Cao, Hai Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33614v1)