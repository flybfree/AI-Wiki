---
title: DGA$_2$D: Directed Graph-Guided Automated Algorithm Design with Large Language Models
published: 2026-08-01T14:59:38Z
authors: Jiale Zhao, Zimu Chen, Sirui Mao, Wentao Yang, Yuxiang Bai, Liyuanjun Lai
url: http://arxiv.org/abs/2608.00700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DGA$_2$D: Directed Graph-Guided Automated Algorithm Design with Large Language Models

## Abstract
The rapid development of Large Language Models (LLMs) has opened new avenues for Automated Heuristic Design (AHD) for solving NP-hard combinatorial optimization problems (COPs). However, existing LLM-driven AHD methods are largely confined to rigid solver templates, relegating the search process to isolated module tuning. Transitioning to fully autonomous, system-level algorithm design is essential but fraught with low reliability of generated operators, extremely large search spaces, and ineffective credit assignment. To overcome these drawbacks, this paper proposes a Directed Graph-Guided Automated Algorithm Design framework, termed DGA$_2$D. It structures the open-ended program space as a directed graph, where each node represents a functional operator that can be instantiated using one of multiple candidate code implementations, while directed walks constitute complete algorithmic pipelines. A first-order path-dependent credit assignment mechanism is introduced to evaluate code variations strictly based on their topological context. Extensive experiments across 12 distinct COPs, ranging from complex scheduling to routing, demonstrate the consistent empirical advantages of DGA$_2$D. It reduces the average normalized gap by up to 10.96 percentage points compared to state-of-the-art LLM baselines.

## Metadata
- **Published**: 2026-08-01T14:59:38Z
- **Authors**: Jiale Zhao, Zimu Chen, Sirui Mao, Wentao Yang, Yuxiang Bai, Liyuanjun Lai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00700v1)