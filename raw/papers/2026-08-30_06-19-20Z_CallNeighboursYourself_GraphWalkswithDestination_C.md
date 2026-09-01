---
title: Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation
published: 2026-08-30T06:19:20Z
authors: Yilun Liu, Boyu Luo, Yanran Tang, Ruihong Qiu, Zi Huang
url: http://arxiv.org/abs/2608.29588v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation

## Abstract
Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood. Existing methods fix the set of accessible neighbours before generation, forcing reasoning to operate over a static context and preventing the model from acquiring missing evidence during inference. We argue that neighbour selection should itself be part of the reasoning process. To this end, we propose Call Neighbours Yourself (CNY), a framework that enables LLMs to proactively explore graph neighbourhoods through topology-constrained graph-walk actions. Instead of reasoning over a pre-selected neighbour set, CNY exposes lightweight neighbour previews and learns when to expand candidate neighbours for additional evidence. To address the delayed-credit challenge of neighbour exploration, we introduce destination-conditioned on-policy self-distillation, which retrospectively evaluates a selected neighbour after its content is revealed and converts the resulting change in action preference into an action-level training signal. Experiments on standard TAG reasoning benchmarks under a unified raw-text setting show that CNY consistently outperforms fixed-context post-training baselines. Furthermore, the learned exploration policy transfers to unseen graphs and to a graph-level task not encountered during training. Code is available at https://github.com/superallen13/CNY.

## Metadata
- **Published**: 2026-08-30T06:19:20Z
- **Authors**: Yilun Liu, Boyu Luo, Yanran Tang, Ruihong Qiu, Zi Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29588v1)