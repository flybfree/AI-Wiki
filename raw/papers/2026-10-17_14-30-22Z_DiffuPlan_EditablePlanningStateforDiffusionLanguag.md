---
title: DiffuPlan: Editable Planning State for Diffusion Language Model Agents
published: 2026-10-17T14:30:22Z
authors: Qisheng Zhou, Zhen Xiong, Qiaoyu Tan
url: http://arxiv.org/abs/2610.24717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DiffuPlan: Editable Planning State for Diffusion Language Model Agents

## Abstract
Diffusion language models (dLLMs) are emerging as an alternative to autoregressive (AR) language models, yet dLLM agents largely inherit an interaction protocol designed for AR generation: once intermediate state is written, later observations can only be incorporated by appending more text. This is a poor match to a defining capability of dLLMs -- reconstructing earlier text conditioned on context that appears both before and after it. We ask whether this capability can support a different agent-state paradigm in which intermediate planning state is directly revisable as evidence arrives. We introduce DiffuPlan, a diffusion search agent that maintains a single editable planning state and reconstructs only the affected steps when later evidence resolves an entity or changes the search route. To support variable-length revisions, we introduce Expansion-Partition Marginalization (EPM), which marginalizes over equivalent expansion paths. We further adapt diffusion trajectory RL to multi-turn search. Across four multi-hop QA benchmarks, DiffuPlan achieves 50.24 average F1, outperforming strong AR search agents. More importantly, under identical data and training, editable planning state improves the diffusion agent by 2.44 F1 versus only 0.47 for its AR source model. These results show that dLLMs need not imitate append-only AR agents: revising committed state is a distinct agentic advantage.

## Metadata
- **Published**: 2026-10-17T14:30:22Z
- **Authors**: Qisheng Zhou, Zhen Xiong, Qiaoyu Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24717v1)