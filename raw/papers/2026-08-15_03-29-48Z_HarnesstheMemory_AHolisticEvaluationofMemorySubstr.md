---
title: Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents
published: 2026-08-15T03:29:48Z
authors: Wei-Chieh Huang, Weizhi Zhang, Yuchen Wu, Yankai Chen, Eric Hanchen Jiang, Wooseong Yang, Yiwei Yang, Henry Peng Zou, Hanrong Zhang, Ying Nian Wu, Haolun Wu, Kai-Wei Chang, Philip S. Yu, Xue Liu, Aylin Caliskan
url: http://arxiv.org/abs/2608.15008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

## Abstract
Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and activation-compatible context mechanisms. Across three backbone models and four benchmark suites spanning user-centric question answering and agent-centric decision-making, we instrument 26 performance and efficiency metrics under a unified harness. Our results show that no single substrate consistently dominates: broad retrieval benefits long-context factual QA, while excessive retrieval can harm sequential decision-making by shifting attention away from action-critical context. Scalability introduces a further routing axis, as substrates that perform well at moderate history lengths can become costly or brittle at longer horizons. These findings motivate substrate routing as a necessary component of adaptive agent memory systems and provide empirical guidance for designing efficient, reliable, and regime-aware long-term memory for LLM agents. Code will be made available upon acceptance.

## Metadata
- **Published**: 2026-08-15T03:29:48Z
- **Authors**: Wei-Chieh Huang, Weizhi Zhang, Yuchen Wu, Yankai Chen, Eric Hanchen Jiang, Wooseong Yang, Yiwei Yang, Henry Peng Zou, Hanrong Zhang, Ying Nian Wu, Haolun Wu, Kai-Wei Chang, Philip S. Yu, Xue Liu, Aylin Caliskan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15008v1)