---
title: Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer
published: 2026-09-07T07:36:52Z
authors: Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Gengming Zhang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Wei Liu, Chunchao Guo
url: http://arxiv.org/abs/2609.07137v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer

## Abstract
Recent image-to-3D generation models built on flow-matching diffusion Transformers (DiT) can produce high-fidelity meshes, yet their post-training strategy remains largely unexplored. There exist several critical bottlenecks in reinforcement learning: the inherent difficulty of defining comprehensive rewards for 3D geometric quality, and the gradient interference that arises when jointly optimizing heterogeneous objectives. Inspired by the practicability of on-policy distillation (OPD) in large language models and image generation, we propose \textbf{Flow3D-OPD}, a two-stage post-training framework that introduces multi-teacher distillation into 3D geometry generation. In the first stage, we utilize the semi-policy to enhance the foundational capability of the pretrained model and then design an agentic verifier for 3D geometric quality evaluation. Based on the verifier, we could cultivate domain-specialized teacher models via direct preference optimization (DPO). In the second stage, we consolidate heterogeneous expertise into a unified student model through on-policy distillation with hard task-routing sampling and gradient accumulation, which could mitigate the gradient interference in joint optimization. Without relying on elaborate modifications, our straightforward yet effective design achieves consistent improvements across all geometric quality dimensions and surpasses all teacher models in the average metric. Extensive experiments demonstrate that our approach provides an effective paradigm for reinforcement learning in 3D generation.

## Metadata
- **Published**: 2026-09-07T07:36:52Z
- **Authors**: Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Gengming Zhang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Wei Liu, Chunchao Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07137v1)