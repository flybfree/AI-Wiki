---
title: GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space
published: 2026-08-31T03:13:47Z
authors: Boqi Chen, Xudong Liu, Yunke Ao, Heejin Do, Jianing Qiu
url: http://arxiv.org/abs/2608.30188v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space

## Abstract
Large Language Models (LLMs) show great potential as clinical agents, yet existing benchmarks reduce clinical workflows to static predictions or unconstrained Markov Decision Processes (MDPs) with coarse action sets. To address this, we introduce GPAgentBench-2K, the first Constrained MDP (CMDP) LLM-agent benchmark for primary-care clinical decision-making, constructed from expert-validated records of real-world GP encounters. Our environment models a full spectrum of six foundational clinical actions, imposes a topological workflow prior over the action space, and operationalizes safety-informed abstention as a first-class outcome. Evaluating 16 state-of-the-art LLMs reveals a significant performance degradation as the action space scales. Crucially, we uncover a clinical quality-safety gap: even frontier models with the highest diagnosis accuracy violate safety constraints in over half of high-risk cases. Finally, we establish a reference point using Constrained Group Relative Policy Optimization (C-GRPO), and show that while explicitly modeling constraints improves performance over unconstrained RL methods, it remains far from clinically acceptable safety.

## Metadata
- **Published**: 2026-08-31T03:13:47Z
- **Authors**: Boqi Chen, Xudong Liu, Yunke Ao, Heejin Do, Jianing Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30188v1)