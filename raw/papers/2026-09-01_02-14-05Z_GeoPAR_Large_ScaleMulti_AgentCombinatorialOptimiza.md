---
title: GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning
published: 2026-09-01T02:14:05Z
authors: Wenjian Wu, Zesheng Jia, Jiaying Tang, Benyuan Yang, Jin Wang
url: http://arxiv.org/abs/2609.00577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning

## Abstract
Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely attributable to weak modeling of local geometric structures and the fact that conflicting task selections are handled only after action generation. To address these limitations, we propose GeoPAR, a geometry-guided parallel autoregressive reinforcement learning framework for scalable multi-agent combinatorial optimization. GeoPAR integrates three key components: (1) a projection-window sparse geometry mechanism that builds lightweight local candidate neighborhoods through multi-directional projections, (2) sparse edge-biased attention that injects these geometric relations into node representations, and (3) cache-guided conflict-aware assignment that reuses the geometric cache during decoding to suppress duplicate selections of exclusive tasks. Experiments on heterogeneous vehicle routing and open multi-depot pickup-and-delivery problems show that GeoPAR improves large-scale zero-shot generalization while substantially reducing rollout steps and maintaining efficient inference.

## Metadata
- **Published**: 2026-09-01T02:14:05Z
- **Authors**: Wenjian Wu, Zesheng Jia, Jiaying Tang, Benyuan Yang, Jin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00577v1)