---
title: GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning
published: 2026-05-14T13:46:04Z
authors: Paolo Mandica, Michał Brzozowski, Zuzanna Dubanowska, Neo Christopher Chung
url: http://arxiv.org/abs/2605.14841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning

## Abstract
Low-rank adaptation (LoRA) has become the dominant paradigm for parameter-efficient fine-tuning (PEFT) of large language models (LLMs). However, its bilinear structure introduces a critical limitation: the mapping from trainable parameters to weight updates is not distance-preserving, distorting the optimization landscape. Methods that project a low-dimensional vector into LoRA's parameter space, such as Uni-LoRA, improve parameter efficiency, but the subsequent bilinear LoRA map breaks end-to-end isometry, leaving the core distance-preservation problem unresolved. We propose GPart (Global Partition fine-tuning), a highly parameter-efficient fine-tuning method which removes the low-rank bottleneck entirely. Our method uses a single isometric partition matrix to map a $d$-dimensional trainable vector directly into the full weight space of the model. The result is an extremely minimal fine-tuning pipeline: one random projection, end-to-end isometric, with a single clean hyperparameter ($d$) and storage cost of $d+1$ values (the trainable vector plus a random seed). GPart builds on the theoretical premise that effective fine-tuning can emerge from random low-dimensional subspaces of the full weight space, without imposing low-rank matrix structure. We empirically demonstrate the superior or comparable performance of GPart to existing PEFT methods on natural language understanding, computer vision tasks, and mathematical reasoning. Overall, GPart achieves state-of-the-art efficiency and performance by removing structural constraints, offering a straightforward and elegant path to PEFT.

## Metadata
- **Published**: 2026-05-14T13:46:04Z
- **Authors**: Paolo Mandica, Michał Brzozowski, Zuzanna Dubanowska, Neo Christopher Chung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.14841v1)