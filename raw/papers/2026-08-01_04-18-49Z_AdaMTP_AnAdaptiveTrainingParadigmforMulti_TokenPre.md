---
title: AdaMTP: An Adaptive Training Paradigm for Multi-Token Prediction
published: 2026-08-01T04:18:49Z
authors: Ziqiang Cui, Han Shi, Bowei He, Yu Pan, Peiyang Liu, Shengyin Sun, Yankai Chen, Haoli Bai, Yichun Yin, Xue Liu, Chen Ma
url: http://arxiv.org/abs/2608.00434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdaMTP: An Adaptive Training Paradigm for Multi-Token Prediction

## Abstract
Multi-Token Prediction (MTP) has emerged as an effective paradigm that augments a shared Large Language Model backbone with auxiliary heads, training the model to predict several future tokens in parallel to enrich its supervision signal and accelerate inference. However, existing training frameworks adopt a rigid, fixed-length prediction horizon, disregarding the highly non-uniform information density of natural language and code. Forcing the auxiliary heads to predict across high-entropy semantic boundaries injects noisy, conflicting training signals; because these heads share the backbone's latent representations, the resulting gradients backpropagate and interfere with the model's core capabilities. We propose AdaMTP, an adaptive training paradigm that dynamically aligns the prediction horizon with the intrinsic predictability of the sequence. At its core, an entropy-based segmentation algorithm leverages the base model to detect sudden surges in uncertainty as semantic boundaries, partitioning sequences into variable-length groups. Each token is assigned an adaptive prediction depth, and a dynamically masked MTP objective suppresses the loss for predictions that cross these boundaries, attenuating the noisy gradients that degrade the backbone. Across mathematical reasoning, code generation, and general benchmarks on three backbones (Llama-3.1-8B, Qwen-2.5-7B, Gemma-3-12B), AdaMTP consistently outperforms standard MTP in both task performance and inference speedup.

## Metadata
- **Published**: 2026-08-01T04:18:49Z
- **Authors**: Ziqiang Cui, Han Shi, Bowei He, Yu Pan, Peiyang Liu, Shengyin Sun, Yankai Chen, Haoli Bai, Yichun Yin, Xue Liu, Chen Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00434v1)