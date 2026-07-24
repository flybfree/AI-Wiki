---
title: SelfMem: Self-Optimizing Memory for AI Agents
published: 2026-07-04T06:27:19Z
authors: Shu Yang, Junchao Wu, Derek F. Wong, Di Wang
url: http://arxiv.org/abs/2607.03726v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SelfMem: Self-Optimizing Memory for AI Agents

## Abstract
While current AI agents support increasingly long context windows, tool use, and skill execution for long-horizon tasks, they still require memory systems to effectively leverage historical experience. Existing memory frameworks typically rely on fixed storage, retrieval, and summarization mechanisms, which can be rigid across different tasks and often require manual tuning. To address this limitation, we propose SelfMem, a self-optimizing memory framework. Inspired by prior work on self-improving AI, we follow the principle of "teaching an agent to fish rather than giving it a fish." Instead of forcing the model to follow a predefined memory strategy or format, SelfMem provides an environment with memory tools and feedback signals that allow the agent to explore, evaluate, and refine its own memory strategy. Our results show that SelfMem consistently outperforms retrieval, compression, and agent-memory baselines on BEAM across conversation scales from 100K to 1M tokens. Compared with the strongest baseline, SelfMem improves the official score by 48.7%, 40.8%, and 41.9% at 100K, 500K, and 1M, respectively. Further question-type analysis shows broad robustness across diverse memory demands, and our optimization study shows that model-guided strategy refinement further improves performance.

## Metadata
- **Published**: 2026-07-04T06:27:19Z
- **Authors**: Shu Yang, Junchao Wu, Derek F. Wong, Di Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03726v1)