---
title: 'FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models'
published: 2026-05-27T11:51:25Z
authors: Xucong Wang, Pengkun Wang, Zhe Zhao, Liheng Yu, Shuang Wang, Yang Wang
url: http://arxiv.org/abs/2605.28347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models

## Abstract
Multi-Label Recognition (MLR) based on Vision-Language Models (VLMs) aims to leverage their pre-trained knowledge to better adapt complex recognition scenarios, thereby enhancing model robustness. However, for realistic decentralized applications requiring federated learning, adapting VLMs to each client that possesses private and heterogeneous data can cause the model to overfit spurious label correlations, consequently triggering irrelevant categories when encountering new samples. To tackle this problem, we reconsider the federated learning for MLR with a causal model, in which we adopt a front-door adjustment and decouple the MLR modeling process by intermediate variables that magnify the oracle label co-occurrence. Guided by our analysis, we propose our FedMPT, the first method specifically designed for federated MLR. The core idea of FedMPT is to leverage generalizable conditions to steer federated MLR to mitigate erroneous label activations. To achieve this, FedMPT introduces an Large Language Model (LLM)-driven pipeline to decipher the underlying conditions that govern label dependencies. Furthermore, we introduce an optimal transport between the condition-enriched prompts and the image patches to uncover multiple region-level semantics. Finally, we generate synergistic predictions from different conditions with a crafted gating mechanism. Experiments on multiple benchmark datasets show that our proposed approach achieves competitive results and outperforms SOTA methods under varied settings.

## Metadata
- **Published**: 2026-05-27T11:51:25Z
- **Authors**: Xucong Wang, Pengkun Wang, Zhe Zhao, Liheng Yu, Shuang Wang, Yang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28347v1)