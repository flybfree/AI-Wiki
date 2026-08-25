---
title: SplitLite: Low-Rank Residual Compression for Split Learning
published: 2026-08-24T09:20:04Z
authors: Tao Li, Yulin Tang, Qi Guo, Xianhao Chen
url: http://arxiv.org/abs/2608.23018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SplitLite: Low-Rank Residual Compression for Split Learning

## Abstract
Federated fine-tuning of on-device large language models (LLMs) faces a significant computing burden. To overcome this limitation, split learning (SL) has emerged as a promising solution, which offloads the primary training workload to a powerful server. However, SL requires exchanging high-dimensional activations and gradients between clients and the server, resulting in prohibitive communication costs. To overcome this challenge, we propose SplitLite, a communication-efficient split federated LoRA fine-tuning method that exploits the low effective rank structure of consecutive-epoch activation and gradient residuals. Our key finding is that, when LoRA uses rank $r$ updates in parameter space, the activation and gradient residuals of the same data sample between adjacent epochs also exhibit effective rank-$2r$ and rank-$4r$ structures, respectively. By revealing this property, SplitLite transmits only quantized truncated singular value decomposition (SVD) residual factors, thereby significantly reducing both activation uplink and gradient downlink traffic. Extensive experiments on the GLUE benchmark across a series of advanced on-device LLMs demonstrate that our method reduces activation uplink communication costs by up to 93.5\% and total communication costs by up to 83.7\%, without performance degradation.

## Metadata
- **Published**: 2026-08-24T09:20:04Z
- **Authors**: Tao Li, Yulin Tang, Qi Guo, Xianhao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23018v1)