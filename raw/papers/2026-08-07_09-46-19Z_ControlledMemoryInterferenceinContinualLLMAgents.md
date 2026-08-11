---
title: Controlled Memory Interference in Continual LLM Agents
published: 2026-08-07T09:46:19Z
authors: Ao Ding, Hongzong LI, Shiqin Tang, Li Zhang, Liang Chen, Xuyang Chen, Zi Liang
url: http://arxiv.org/abs/2608.07622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Controlled Memory Interference in Continual LLM Agents

## Abstract
Long-term memory enables AI agents to maintain continuity across sessions, personalize behavior, and evolve through accumulated experience. Yet memory evolution is not simply a process of storing more information: new experiences may reinforce, revise, or interfere with existing memory states. Existing systems mainly emphasize memory construction and relevance-based retrieval, but several memories may remain simultaneously relevant while differing in state, temporal validity, or authority. We introduce Controlled Memory Interference (CMI), a controlled diagnostic and data-generation framework for studying how agent memory evolves under different memory relationships. Across controlled memory evolution, benign accumulation has limited effects, whereas relationship-specific interference sharply suppresses update plasticity with little stability gain, either by blocking target-memory exposure or by disrupting its downstream use. Lexical and Dense retrieval exhibit distinct interference pathways, while poisoning is more sensitive to update-authority cues than to recency alone. Beyond diagnosis, CMI provides targeted examples for interference-aware memory learning, improving the distinction between valid updates and interference-inducing memories while preserving performance on original memory tasks. These findings show that memory evolution is shaped not only by memory scale, but also by interactions among accumulated experiences. More broadly, memory interference emerges as an important factor for reliable continual agent memory systems.

## Metadata
- **Published**: 2026-08-07T09:46:19Z
- **Authors**: Ao Ding, Hongzong LI, Shiqin Tang, Li Zhang, Liang Chen, Xuyang Chen, Zi Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07622v1)