---
title: Remember Before You're Asked: MemDream for Self-Probing Memory Evolution
published: 2026-09-28T08:07:24Z
authors: Mingfei Lu, Mengjia Wu, Runsong Jia, Zhe Luo, Yi Zhang
url: http://arxiv.org/abs/2609.34545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Remember Before You're Asked: MemDream for Self-Probing Memory Evolution

## Abstract
Memory is essential for enabling LLM-based agents to maintain coherent, personalized behavior over long-horizon interactions. However, existing memory systems share a fundamental limitation: they never proactively test their own memory, repairing it only after real queries expose weaknesses. This reactive paradigm means every retrieval failure corresponds to a real interaction in which the cost has already been paid. We propose MemDream, a framework that enables self-probing memory evolution for LLM agents. Our framework periodically enters offline dream cycles where three specialized agents (Dreamer, Analyst, Consolidator) collaboratively probe, diagnose, and repair the memory graph before failures occur. A policy trained via Group Relative Policy Optimization learns which repair operations produce durable retrieval improvements, while a soft decay mechanism provides reversible forgetting driven by the same anticipatory signal. Experiments on LoCoMo and MemoryAgentBench demonstrate that MemDream improves answer F1 by 4.5 points on LoCoMo and achieves a 9.1-point higher overall score on MAB over the strongest reactive-evolution baselines.

## Metadata
- **Published**: 2026-09-28T08:07:24Z
- **Authors**: Mingfei Lu, Mengjia Wu, Runsong Jia, Zhe Luo, Yi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34545v1)