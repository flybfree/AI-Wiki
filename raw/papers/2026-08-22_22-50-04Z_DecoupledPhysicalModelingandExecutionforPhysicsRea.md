---
title: Decoupled Physical Modeling and Execution for Physics Reasoning
published: 2026-08-22T22:50:04Z
authors: Ye Zhang, Xuehang Guo, Rui Pan, Pengfei Yu, Denghui Zhang, Manling Li, Qingyun Wang
url: http://arxiv.org/abs/2608.22126v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupled Physical Modeling and Execution for Physics Reasoning

## Abstract
Physics reasoning requires constructing a consistent model of the underlying physical system rather than relying solely on symbolic or formula-based manipulation. Although large language models have shown strong ability in solving math and coding problems, they still struggle with physics problems, as these problems entangle the physical modeling process with mathematical calculations. Humans approach physics by first building a representation of the system before performing calculations. Inspired by this, we introduce a unified framework that distills intermediate representations that explicitly encode the physical modeling process and adopt a two-stage post-training strategy, where supervised fine-tuning establishes structured modeling, and reinforcement learning with rubric-based feedback improves the quality of the modeling process. Experiments on multiple multimodal physics benchmarks show that our approach leads to consistent improvements in reasoning performance across different models and datasets. On PhysReason, PhyX and SeePhys benchmarks, physical modeling output performs GRPO by an average ~3%, showing that explicit physical modeling is an efficient strategy of improving physics reasoning for small LLMs.

## Metadata
- **Published**: 2026-08-22T22:50:04Z
- **Authors**: Ye Zhang, Xuehang Guo, Rui Pan, Pengfei Yu, Denghui Zhang, Manling Li, Qingyun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22126v1)