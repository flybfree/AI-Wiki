---
title: IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD
published: 2026-07-30T11:28:21Z
authors: Nianchen Deng, Jiaxin Ai, Tao Hu, Shu Zou, Yurui Dong, Siqi Li, Xinyu Cai, Xuemeng Yang, Licheng Wen, Hongbin Zhou, Hairong Zhang, Pinlong Cai, Botian Shi
url: http://arxiv.org/abs/2607.28050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD

## Abstract
Automating industrial CAD design and manufacturing places distinctive demands on multimodal foundation models: the model must see engineering drawings and 3D geometry screenshots, write correct parametric-modelling scripts and Windows COM API code, and cover the full range from single parts to assemblies. General-purpose multimodal models fall short on these tasks, while single-task fine-tuning is too narrow to support the diverse calls that upper-layer agents issue. We build IndustryForge-27B on top of Qwen3.5-VL-27B by curating and integrating six industrial-CAD sub-corpora totalling $\sim$52k multimodal samples---CAD Visual QA (CAD-VQA), parametric CAD code (text2cadquery), assembly-level CAD code (text2cadquery-assembly), and three COM sub-corpora for Inventor / SolidWorks (com_2d / com_3d / com_assembly)---and training with a unified multi-task SFT recipe. Across four CAD-domain benchmarks IndustryForge-27B lifts the base model by $+33.65$~pp on average and outperforms the strong closed-source model GPT-5.4 on all four; across eleven general-capability benchmarks it retains, and slightly improves upon, the base model ($+1.56$~pp mean, no catastrophic forgetting). IndustryForge-27B will serve as the common substrate for downstream industrial-agent projects, providing a unified starting point for a full-stack industrial agent that spans from CAD design to industrial-software operation, from parts to assemblies, and from single-shot generation to closed-loop self-improvement.

## Metadata
- **Published**: 2026-07-30T11:28:21Z
- **Authors**: Nianchen Deng, Jiaxin Ai, Tao Hu, Shu Zou, Yurui Dong, Siqi Li, Xinyu Cai, Xuemeng Yang, Licheng Wen, Hongbin Zhou, Hairong Zhang, Pinlong Cai, Botian Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28050v1)