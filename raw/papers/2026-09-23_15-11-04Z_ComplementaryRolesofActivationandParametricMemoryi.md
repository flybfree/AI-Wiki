---
title: Complementary Roles of Activation and Parametric Memory in Few-Shot Learning
published: 2026-09-23T15:11:04Z
authors: Miaohe Niu, Runsong Zhao, Xinyu Liu, Bo Jin, Yucheng Qiao, Chunliang Zhang, Jingbo Zhu, Tong Xiao
url: http://arxiv.org/abs/2609.28250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Complementary Roles of Activation and Parametric Memory in Few-Shot Learning

## Abstract
At test time, large language models (LLMs) can encode historical information in activation memory (i.e., KV caches) and parametric memory (i.e., updated parameters). While activation memory is generally considered effective for factual recall and parametric memory for learning new tasks, their interplay remains unclear. In this work, we systematically investigate the role of memory in few-shot learning through controlled experiments. We find that activation memory is superior for recalling facts, whereas parametric memory does not consistently outperform activation memory in task learning. Moreover, our experiments show that the composite task, Conditional Arithmetic, requires the synergy of both memory types. Through neuron-level analysis, we find that the model activates distinct sets of neurons when accessing the same historical information through activation versus parametric memory. When both memory types are combined, the model recruits neurons from both sets, which is crucial for solving Conditional Arithmetic. These findings suggest that neither memory mechanism alone is sufficient for this composite task, highlighting the importance of their collaboration.

## Metadata
- **Published**: 2026-09-23T15:11:04Z
- **Authors**: Miaohe Niu, Runsong Zhao, Xinyu Liu, Bo Jin, Yucheng Qiao, Chunliang Zhang, Jingbo Zhu, Tong Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28250v1)