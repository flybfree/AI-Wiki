---
title: MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation
published: 2026-07-24T04:50:39Z
authors: Qingyu Yang, Haonan He, Minglei Li, Jingqi Ye, Tao Chen, Lei Bai, Peng Ye
url: http://arxiv.org/abs/2607.21978v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation

## Abstract
Mixture-of-Experts (MoE) architectures have been widely adopted in large language models, yet parameter-efficient fine-tuning (PEFT) for MoE models remains underexplored. Existing PEFT methods for MoE either ignore router priors with uniform adapters, reducing efficiency and risking forgetting, or rely on static expert selection, limiting per-token capacity and cross-expert feature learning. In this paper, we make the first attempt to fine-tune MoE models with MoE-style low-rank adaptation: our method, entitled MoE$^2$-LoRA, deeply couples the pretrained expert specialization with task-specific adaptivity via a dual-channel Routing-Conditioned Projection (RCP) module, which reuses base router activations to inform LoRA routing. We further introduce a single global LoRA expert pool shared across all layers, enabling model-wide adaptation with emergent layer-wise affinities and balanced expert utilization. MoE$^2$-LoRA simultaneously benefits from the advantages of prior reuse, dynamic adapter routing, and model-wide knowledge sharing. Evaluated on multiple MoE backbones with varying scales and expert granularities, MoE$^2$-LoRA consistently achieves state-of-the-art downstream accuracy while retaining stronger general capabilities.

## Metadata
- **Published**: 2026-07-24T04:50:39Z
- **Authors**: Qingyu Yang, Haonan He, Minglei Li, Jingqi Ye, Tao Chen, Lei Bai, Peng Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21978v1)