---
title: MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training
published: 2026-08-11T11:50:48Z
authors: Yikai Wang, Chuansai Zhou, Yuhang Zhou, Weiqiang Wu, Cong Wu, Yue Deng, Ben Feng, Mingming Zhu, Beirong Zhou, Zhibin Wang, Sheng Zhong, Chen Tian, Wangze Zhang
url: http://arxiv.org/abs/2608.10823v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training

## Abstract
Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead. In practice, factors such as framework adaptation, numerical precision, and operator implementation can cause failures, including gradient overflow and loss divergence. Reproducing such failures directly on large models requires considerable time and computational resources. This paper systematically analyzes failures encountered during large-scale RL training on the Huawei Ascend platform, summarizes representative failure types, and identifies three model-side factors relevant to fault reproduction. Based on these factors, we propose a proxy-model construction method for low-cost fault investigation and auxiliary diagnosis. It employs structure-preserving, clustering-based expert pruning to select representative experts while retaining the model's backbone architecture, routing mechanism, and basic task capabilities. Our experimental results show that the proxy models reduce accelerator requirements by 50%-87.5% and achieve up to a 33.3x reduction in per-step NPU-hour cost, while preserving major training dynamics and reproducing fault responses consistent with the original models. Overall, the proxy models can serve as low-cost surrogates for fault reproduction, targeted validation, and auxiliary diagnosis in RL post-training.

## Metadata
- **Published**: 2026-08-11T11:50:48Z
- **Authors**: Yikai Wang, Chuansai Zhou, Yuhang Zhou, Weiqiang Wu, Cong Wu, Yue Deng, Ben Feng, Mingming Zhu, Beirong Zhou, Zhibin Wang, Sheng Zhong, Chen Tian, Wangze Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10823v1)