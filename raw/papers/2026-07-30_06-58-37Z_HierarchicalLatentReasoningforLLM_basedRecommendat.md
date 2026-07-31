---
title: Hierarchical Latent Reasoning for LLM-based Recommendation
published: 2026-07-30T06:58:37Z
authors: Peiyu Hu, Siying Gu, Weihai Lu, Zhuodong Liu, Yuntian Tang, Jiahao Liang, Yiying Xie, Jiang Rong, Zhaokai Luo, Zhiyong Wang, Jia Wang
url: http://arxiv.org/abs/2607.27760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Latent Reasoning for LLM-based Recommendation

## Abstract
Large Language Models (LLMs) have shown strong potential for recommendation by leveraging their semantic understanding and contextual modeling capabilities. Recent studies further introduce reasoning mechanisms to improve user preference modeling. However, explicit natural-language reasoning incurs substantial inference overhead, whereas existing latent reasoning methods mainly focus on generating or verifying intermediate states, leaving their layer-wise preference roles and contributions insufficiently characterized. We propose HiLaR, a Hierarchical Latent Reasoning framework with layer-aware reinforcement optimization for LLM-based recommendation. HiLaR constructs temporal-guided hierarchical user preference representations, aligns them with multiple LLM latent reasoning states, and organizes the reasoning process from broad preferences to fine-grained current intents. To further optimize the reasoning trajectory, HiLaR combines final recommendation feedback with layer-aware process rewards derived from the marginal target-likelihood gain of each state. Experiments on four Amazon benchmark datasets show that HiLaR generally outperforms strong sequential, generative, and LLM-based recommendation baselines. Ablation and sensitivity analyses further verify the contribution of hierarchical representation learning, latent alignment, and process-level optimization. Our code is available in https://github.com/hupeiyu21/HiLaR.

## Metadata
- **Published**: 2026-07-30T06:58:37Z
- **Authors**: Peiyu Hu, Siying Gu, Weihai Lu, Zhuodong Liu, Yuntian Tang, Jiahao Liang, Yiying Xie, Jiang Rong, Zhaokai Luo, Zhiyong Wang, Jia Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27760v1)