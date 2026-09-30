---
title: IronLLM: Forging Compact Edge-Native Language Models for Real-Time Embodied Intelligence
published: 2026-09-29T07:03:39Z
authors: Changdi Yang, Fengquan Jiao, Haochih Lin, Haoran Yang, Jing Xiao, Liangyu Huo, Suxin Lu, Tiance Chen, Wei Liu, Yinggan Xu, Yunxiang Lu, Zai Zheng, Zhirui Xie, Zhongyang Che, Ziyan Tang, Zuoxiang Zhao, Jian Yao
url: http://arxiv.org/abs/2609.36860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IronLLM: Forging Compact Edge-Native Language Models for Real-Time Embodied Intelligence

## Abstract
We present IronLLM-0.6B, a 654M-parameter language model designed for efficient on-device inference. IronLLM-0.6B combines a hybrid attention architecture with X-MTP, a lightweight shared-KV multi-token prediction design that eliminates per-depth KV-cache replay and employs a lightweight verification head for rollback-free drafting, achieving a 1.48x decoding speedup. The model is pretrained on approximately 6.2 trillion tokens using a quality-oriented data pipeline and is further post-trained with Multi-Domain On-Policy Distillation to integrate capabilities from domain-specialized teachers. To better meet the low-latency requirements of on-device scenarios, IronLLM-0.6B adopts an Instruct-Only design. Evaluations show that IronLLM-0.6B achieves competitive performance relative to larger models such as Qwen3.5-0.8B and MiniCPM5-1B, while producing more concise responses on many tasks. We further present IronLLM-0.6B-Light, which replaces RMSNorm with Dynamic Tanh and simplifies several computationally expensive components to improve inference and quantization efficiency. Together, the IronLLM models provide an effective performance-efficiency trade-off for resource-constrained deployment.

## Metadata
- **Published**: 2026-09-29T07:03:39Z
- **Authors**: Changdi Yang, Fengquan Jiao, Haochih Lin, Haoran Yang, Jing Xiao, Liangyu Huo, Suxin Lu, Tiance Chen, Wei Liu, Yinggan Xu, Yunxiang Lu, Zai Zheng, Zhirui Xie, Zhongyang Che, Ziyan Tang, Zuoxiang Zhao, Jian Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36860v1)