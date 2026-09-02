---
title: Instella-MoE Technical Report
published: 2026-09-01T06:38:17Z
authors: Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh, Jialian Wu, Ximeng Sun, Wen Xie, Chaojun Hou, Vikram Appia, Zhenyu Gu, Zicheng Liu, Emad Barsoum
url: http://arxiv.org/abs/2609.00791v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instella-MoE Technical Report

## Abstract
In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs. Instella-MoE combines a sparsely activated MoE design with architectural and system-level innovations, including Gated Multi-head Latent Attention (Gated MLA) and FarSkip-Collective connectivity, enabling efficient large-scale training and inference. The model is developed through a multi-stage pipeline comprising pre-training, mid-training, long-context extension, supervised fine-tuning with feedback-driven data curation, direct preference optimization, and reinforcement learning with Multi-Teacher On-Policy Distillation. Instella-MoE achieves an average score of 76.7 across standard pre-training benchmarks, outperforming prior fully open models including OLMo-3-7B, SmolLM3-3B, and OLMoE-1B-7B, while remaining competitive with open-weight MoE and dense baselines at comparable active-parameter scales, including Moonlight-16B-A3B and Qwen3.5-4B. After post-training, our final Think checkpoint achieves an average score of 73.2 across instruction-following, reasoning, math, coding, and chat benchmarks, outperforming both fully open and open-weight models with comparable or larger active parameter counts in our evaluation. To support transparent and reproducible research, we release the complete Instella-MoE model flow, including model weights, training configurations, data mixtures, and training code. Together, these contributions establish Instella-MoE a strong, fully open foundation for efficient, high-performing MoE models and reproducible research.

## Metadata
- **Published**: 2026-09-01T06:38:17Z
- **Authors**: Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh, Jialian Wu, Ximeng Sun, Wen Xie, Chaojun Hou, Vikram Appia, Zhenyu Gu, Zicheng Liu, Emad Barsoum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00791v1)