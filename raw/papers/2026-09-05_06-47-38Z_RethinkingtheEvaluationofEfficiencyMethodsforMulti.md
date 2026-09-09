---
title: Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems
published: 2026-09-05T06:47:38Z
authors: Jiamu Zhang, Lingxi Zhang, Pengjun Lu, Qiyue Zhang, Yu-Neng Chuang, Zhengchen Li, Shuai Xu, Vipin Chaudhary, Hanjie Chen
url: http://arxiv.org/abs/2609.05933v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems

## Abstract
Efficiency is increasingly important for Large Language Model (LLM)-based multi-agent systems (MAS), as larger models and more agents introduce substantial execution costs. Recent methods aim to make MAS cheaper by pruning agents, removing communication edges, or searching for compact structures. However, we argue that existing evaluations may overestimate their true ability to improve MAS efficiency. Reported gains are often measured under method-specific prompts and starting topologies, making them difficult to attribute to the proposed structural changes. Moreover, many reported successes appear in non-MAS-demanding settings, where a single agent or a randomly pruned system can already preserve strong performance. To study these issues, we introduce a controlled and MAS-demanding diagnostic benchmark for representative MAS efficiency methods. We evaluate methods under a shared backbone model, agent registry, and runtime, across controlled variations in topology, scale, depth, and tool use. Our analysis shows that many reported gains are setup-dependent and may arise from structural collapse, disabled tool pathways, or starting systems where random pruning already preserves accuracy, rather than robust improvements in MAS efficiency.

## Metadata
- **Published**: 2026-09-05T06:47:38Z
- **Authors**: Jiamu Zhang, Lingxi Zhang, Pengjun Lu, Qiyue Zhang, Yu-Neng Chuang, Zhengchen Li, Shuai Xu, Vipin Chaudhary, Hanjie Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05933v1)