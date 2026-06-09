---
title: On Predicting the Post-training Potential of Pre-trained LLMs
published: 2026-05-12T11:33:49Z
authors: Xiaoyuan Li, Yubo Ma, Kexin Yang, Moxin Li, Keqin Bao, Wenie Wang, Fuli Feng, Dayiheng Liu
url: http://arxiv.org/abs/2605.11978v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Predicting the Post-training Potential of Pre-trained LLMs

## Abstract
The performance of Large Language Models (LLMs) on downstream tasks is fundamentally constrained by the capabilities acquired during pre-training. However, traditional benchmarks like MMLU often fail to reflect a base model's plasticity in complex open-ended scenarios, leading to inefficient model selection. We address this by introducing a new task of predicting post-training potential - forecasting a base model's performance before post-training. We propose RuDE (Rubric-based Discriminative Evaluation), a unified framework that bypasses the generation gap of base models by leveraging response discrimination. Guided by our systematic 4C Taxonomy, RuDE constructs controlled contrastive pairs across diverse domains by fine-grained rubric violations. Extensive experiments demonstrate a correlation greater than 90% with post-training performance. Crucially, validation via Reinforcement Learning (RL) confirms that RuDE effectively identifies high-potential smaller models that outperform larger counterparts, offering a compute-efficient mechanism for foundation model development.

## Metadata
- **Published**: 2026-05-12T11:33:49Z
- **Authors**: Xiaoyuan Li, Yubo Ma, Kexin Yang, Moxin Li, Keqin Bao, Wenie Wang, Fuli Feng, Dayiheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11978v1)