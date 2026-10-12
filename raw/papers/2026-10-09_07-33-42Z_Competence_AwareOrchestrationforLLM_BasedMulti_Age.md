---
title: Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
published: 2026-10-09T07:33:42Z
authors: Songmiao Wang, Yuchen Wang, Chenglin Yu, Hongxia Yang, Ming Li
url: http://arxiv.org/abs/2610.13144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Competence-Aware Orchestration for LLM-Based Multi-Agent Systems

## Abstract
LLM-based multi-agent systems (MAS) have emerged as a promising paradigm for enhancing complex reasoning through role specialization and collaboration, yet a key challenge remains: how can collaboration be adapted to a backbone's competence on the current query? This problem matters because more collaboration is not always better--richer coordination may help on difficult cases, but it also incurs additional token cost and redundant interactions. We propose a two-stage competence-aware framework for automatic MAS orchestration. It first models the LLM backbone's task-conditioned competence for the current query, and then uses this signal to adapt role activation and the communication graph. Across six benchmarks, our method achieves an average score of 93.81%. Experiments with six LLM backbones of varying competence levels further show that our method adjusts collaboration according to the inferred competence: for higher-competence backbones, it improves average accuracy from 87.22 to 89.97 while reducing token cost by 36.26%; for lower-competence backbones, it yields a further average gain of 4.58 points over existing methods. The same trend also holds on unseen backbones.

## Metadata
- **Published**: 2026-10-09T07:33:42Z
- **Authors**: Songmiao Wang, Yuchen Wang, Chenglin Yu, Hongxia Yang, Ming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13144v1)