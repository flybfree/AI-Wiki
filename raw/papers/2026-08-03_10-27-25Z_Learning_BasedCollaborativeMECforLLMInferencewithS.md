---
title: Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO
published: 2026-08-03T10:27:25Z
authors: Ngoc Hung Nguyen, Bjorn Landfeldt
url: http://arxiv.org/abs/2608.02031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO

## Abstract
This paper investigates collaborative mobile edge computing (MEC) servers for large language model (LLM) inference under soft deadline constraints. In this system, to improve the quality of service, computations are expected to be completed within their deadlines. However, due to dependencies among tasks or subtasks, any missed deadline can lead to catastrophic consequences for the entire request. In this context, this work proposes an extended deadline mechanism with constrained flexibility. The main challenges lie in handling large-scale computations under strict latency constraints while limiting the number of allowable deadline extensions, especially in the presence of task dependencies within each request. To tackle these challenges, we develop a transformer-enhanced proximal policy optimization (PPO) framework that enables efficient collaboration among MEC servers. The proposed approach aims to maximize the number of tasks completed within their deadlines while minimizing the use of deadline extensions. By capturing temporal dependencies and cross-server interactions, the transformer improves decision-making for task migration. Simulation results demonstrate that the proposed method significantly outperforms conventional PPO and heuristic-based approaches in terms of task completion rate and overall system efficiency.

## Metadata
- **Published**: 2026-08-03T10:27:25Z
- **Authors**: Ngoc Hung Nguyen, Bjorn Landfeldt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02031v1)