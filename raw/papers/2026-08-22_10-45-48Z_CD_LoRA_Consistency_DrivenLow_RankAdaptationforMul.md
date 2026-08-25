---
title: CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning
published: 2026-08-22T10:45:48Z
authors: Qian Zha, Jinda Liu, Yuan Wu, Yi Chang
url: http://arxiv.org/abs/2608.21909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning

## Abstract
While Multi-Task Learning (MTL) is essential for adapting Large Language Models (LLMs) to diverse domains, prevailing LoRA-based methods rely on complex routing mechanisms that partition task-specific knowledge. In this work, we reveal that such routing-based designs are prone to a training-inference discrepancy, where stochastic routing decisions under distribution shifts compromise inference stability. Driven by a second-order Taylor analysis that exposes the instability induced by routing variance, we challenge the training-inference discrepancy and propose Consistency-Driven Low-Rank Adaptation (CD-LoRA). By eliminating routers entirely, CD-LoRA employs a consistency-driven alignment mechanism to enforce representation congruence across tasks in a shared low-rank space. This paradigm fosters robust, task-agnostic features without explicit partitioning overhead. Extensive experiments show that CD-LoRA consistently outperforms state-of-the-art multi-adapter baselines, offering a simpler, router-free, and more stable solution for multi-task PEFT. The code is available at the anonymous link https://github.com/zhaqian21/CD-LoRA.

## Metadata
- **Published**: 2026-08-22T10:45:48Z
- **Authors**: Qian Zha, Jinda Liu, Yuan Wu, Yi Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21909v1)