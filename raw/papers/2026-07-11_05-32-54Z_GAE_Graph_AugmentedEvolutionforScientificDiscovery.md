---
title: GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization
published: 2026-07-11T05:32:54Z
authors: Xuanzhou Chen, Taoli Cheng
url: http://arxiv.org/abs/2607.10127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization

## Abstract
Evolutionary program search guided by Large Language Models (LLMs) has emerged as a powerful paradigm for automated scientific discovery. However, current approaches are fundamentally constrained by three bottlenecks: structurally blind parent selection, sparse whole-program evaluation rewards, and static mutation operators that fail to adapt during search. We present GAE (Graph-Augmented Evolution), a framework that resolves these limitations through a tightly coupled, three-pillar architecture. First, a relational graph neural network (GNN) parses programs into typed computation graphs, producing structure-aware embeddings. Second, an RL-optimized meta-controller leverages these embeddings to replace blind evolutionary sampling with a directed policy, dynamically selecting optimal parents and mutation directions based on reward history. Third, an online GRPO fine-tuning loop continuously updates the LLM mutation operator at test-time using group-normalized evaluation rewards, directly aligning the model's generation distribution with high-fitness structural edits. We evaluate GAE on a challenging scientific discovery task: symbolic regression for complex nonlinear oscillator systems. By transforming stochastic search into a directed, self-improving trajectory, GAE efficiently discovers closed-form physical equations, consistently matching or outperforming static LLM-driven baselines and achieving state-of-the-art out-of-distribution performance.

## Metadata
- **Published**: 2026-07-11T05:32:54Z
- **Authors**: Xuanzhou Chen, Taoli Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.10127v1)