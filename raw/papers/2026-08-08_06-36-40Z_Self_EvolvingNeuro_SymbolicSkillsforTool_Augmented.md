---
title: Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning
published: 2026-08-08T06:36:40Z
authors: Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li
url: http://arxiv.org/abs/2608.07955v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning

## Abstract
Large vision-language models have achieved strong performance in multimodal reasoning, but they remain unreliable on fine-grained spatial tasks that demand both precise spatial perception and fine-grained geometric computation beyond end-to-end generation. Tool augmentation offers a natural solution, while existing methods either plan tool calls from scratch without explicit dependency constraints or rely on fixed pipelines that are redundant and generalize poorly across spatial tasks. An effective spatial reasoning agent should instead accumulate reusable experience and adaptively compose it for new problems. To this end, we propose NeSy-Spatial, a neuro-symbolic framework for self-evolving spatial skills. NeSy-Spatial abstracts tool interactions and geometric operations into typed executable atomic instructions and composes them into two complementary skill types: Tool-Use Skills for organizing tool execution and Geometry Skills for structured geometric reasoning. During inference, NeSy-Spatial retrieves and executes relevant skills in a closed-loop process. During evolution, it analyzes buffered successful and failed trajectories to refine skill structures and prune unreliable or inactive entries. Experiments on three spatial reasoning benchmarks show that NeSy-Spatial consistently improves reasoning accuracy with more precise tool utilization.

## Metadata
- **Published**: 2026-08-08T06:36:40Z
- **Authors**: Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07955v1)