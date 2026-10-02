---
title: Learning to Ask: Information Acquisition for SLM-LLM Collaboration, under a budget
published: 2026-10-01T07:36:26Z
authors: Yongjun Kim, Xiaoxiao Li, Jaeho Lee
url: http://arxiv.org/abs/2610.01236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Ask: Information Acquisition for SLM-LLM Collaboration, under a budget

## Abstract
Collaboration between a small language model (SLM) and a large language model (LLM) offers an opportunity to combine the efficiency of smaller models with the strong reasoning capabilities of larger ones. Existing approaches primarily frame such collaboration as a computation allocation problem, determining which model should handle each portion of the reasoning process. In black-box API-based settings, however, this paradigm can be inefficient due to coarse-grained delegation or repeated transmission of context across model switches. In this work, we instead formulate SLM-LLM collaboration as an information acquisition problem, under an API budget constraint. The SLM remains the primary reasoner and selectively queries a black-box LLM advisor only when needed, issuing targeted queries rather than delegating the reasoning process itself. To realize this strategy, we develop a three-stage RLVR framework that learns whether to call the advisor, how to formulate useful queries, and how to integrate the collaboration into the reasoning process by jointly refining advisor invocation and information use. Across mathematical reasoning and coding tasks, our approach improves the performance--cost tradeoff over existing collaboration baselines and, in some settings, matches or exceeds oracle problem-level routing. Finally, we show that our strategy can transfer to other advisor model families, without further training.

## Metadata
- **Published**: 2026-10-01T07:36:26Z
- **Authors**: Yongjun Kim, Xiaoxiao Li, Jaeho Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01236v1)