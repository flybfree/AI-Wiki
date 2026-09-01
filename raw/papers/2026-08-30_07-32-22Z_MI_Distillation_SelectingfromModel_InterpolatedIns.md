---
title: MI-Distillation: Selecting from Model-Interpolated Instruct-Reasoning Data Spectrum for Chain-of-Thought Distillation
published: 2026-08-30T07:32:22Z
authors: Yangsong Lan, Renkai Hu, HongKai Zheng, Bo Zhang, Renzhi Wang, Hongliang Dai, Piji Li
url: http://arxiv.org/abs/2608.29623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MI-Distillation: Selecting from Model-Interpolated Instruct-Reasoning Data Spectrum for Chain-of-Thought Distillation

## Abstract
Recent advances in large reasoning models (LRMs) have shown strong performance on complex problems through long chain-of-thought (Long CoT) reasoning. However, distilling such trajectories into smaller student models remains challenging: direct Long CoT supervision often provides limited gains and can be less effective than concise Short CoT rationales. In this work, we investigate this phenomenon from a gradient-centric perspective. Our analysis shows that Long CoT induces larger gradient magnitudes and more concentrated update directions than Short CoT, with this effect becoming more pronounced as student model capacity increases. These findings suggest that effective Long CoT distillation requires balancing the reasoning information density of reasoning trajectories with their distributional alignment to the student model. Motivated by this insight, we propose \textbf{M}odel \textbf{I}nterporlation \textbf{Distillation} (\textbf{MI-Distillation}), a framework that constructs a continuous Instruct-Reasoning data spectrum through model interpolation. To select suitable trajectories from this spectrum, we further introduce \textbf{Seq}uential \textbf{L}earnable \textbf{S}urprisal \textbf{S}core (\textbf{SeqLSS}), which favors reasoning paths that are both informative and learnable for the student. Extensive experiments on reasoning benchmarks show that MI-Distillation consistently improves small model CoT distillation over strong Long CoT baselines.

## Metadata
- **Published**: 2026-08-30T07:32:22Z
- **Authors**: Yangsong Lan, Renkai Hu, HongKai Zheng, Bo Zhang, Renzhi Wang, Hongliang Dai, Piji Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29623v1)