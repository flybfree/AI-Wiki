---
title: Rethinking Multi-Agent Collaboration: When More Is Less
published: 2026-09-17T06:29:12Z
authors: Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, Yifan Li, Jiaheng Liu
url: http://arxiv.org/abs/2609.19759v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Multi-Agent Collaboration: When More Is Less

## Abstract
The rapid advancement of large language models and single-agent harnesses has reshaped the landscape of autonomous systems, raising a critical question of when multi-agent collaboration offers genuine value. As individual agent capabilities continue to scale, multi-agent collaboration faces diminishing returns while incurring growing context overhead. Through systematic analysis, we delineate the capability boundaries of multi-agent collaboration relative to single-agent alternatives, showing that it confers systematic benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows. Building on these insights, we propose SAIGE, a lightweight multi-agent collaboration mechanism based on Semantic-Aware Incremental Graph Evolution. SAIGE models collaboration as a dynamically evolving graph, where nodes are agent instances spawned on demand and edges encode semantic dependencies established through content-based information retrieval. Experiments on long-horizon, complex task benchmarks show that SAIGE achieves a favorable trade-off between context efficiency and task performance, and that scaling the agent pool or deepening the recursion level does not consistently improve outcomes. Our findings suggest that multi-agent superiority is bounded by task structure rather than universal, and that more agents do not necessarily make a system more intelligent.

## Metadata
- **Published**: 2026-09-17T06:29:12Z
- **Authors**: Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, Yifan Li, Jiaheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19759v1)