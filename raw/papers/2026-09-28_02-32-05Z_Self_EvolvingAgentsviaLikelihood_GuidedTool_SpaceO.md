---
title: Self-Evolving Agents via Likelihood-Guided Tool-Space Optimization
published: 2026-09-28T02:32:05Z
authors: Xuanqi Zhang, Ruinan Jin, Running Yang, Yuxuan Zhang, Minghui Chen, Wenlong Deng, Xiaoxiao Li
url: http://arxiv.org/abs/2609.34151v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Evolving Agents via Likelihood-Guided Tool-Space Optimization

## Abstract
Self-evolving agents can continually improve their behavior, while tools define the executable action space through which they interact with the environment. However, exposing the full tool library to model introduces substantial irrelevant context and can impair tool-use decisions. We study tool-space self-evolution, where each recurring task type maintains a persistent tool space which is constructed from accumulated output experience. We identify three limitations of existing methods: (1) output-unaware selection: they rely primarily on tool descriptions or model priors rather than observed tool outputs; (2) statelessness across request: they select tools independently for each request without consolidating prior output experience into persistent task-specific state; (3) inference cost: they repeatedly search, rank, or reason over candidate tools for subsequent requests of the same task. We address these limitations through output-aware tool scoring, persistent task-specific tool spaces, amortized tool selection, and reusable configurations across models. We introduce LOTS (Likelihood-Only Tool Scoring), which evolves an agent's tool space from accumulated output experience while keeping model parameters fixed. After each request, LOTS holds the model's generated answer and estimates each tool's contribution by measuring how much the answer likelihood changes when its observed output is removed. These contributions are aggregated within each recurring task to rank tools and update its persistent space. Across three benchmarks, LOTS improves task performance while substantially reducing tool context. More importantly, sequential experiments demonstrate that task-specific spaces persist and continue to improve over time, while cross-model experiments show that learned configurations transfer across different models.

## Metadata
- **Published**: 2026-09-28T02:32:05Z
- **Authors**: Xuanqi Zhang, Ruinan Jin, Running Yang, Yuxuan Zhang, Minghui Chen, Wenlong Deng, Xiaoxiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34151v1)