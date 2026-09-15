---
title: AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery
published: 2026-09-14T16:24:27Z
authors: Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
url: http://arxiv.org/abs/2609.15820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery

## Abstract
Large language models have advanced automated algorithm discovery by synthesizing executable code, but existing frameworks trap them in rigid search pipelines with pre-defined control flows. This limitation restricts adaptive reasoning, blocks cross-paradigm transfer, and discards valuable execution feedback. We propose AlgoEvo, a unified agentic framework that transforms automated algorithm discovery into an interactive, knowledge-accumulating process. An autonomous agent dynamically inspects, diagnoses, and edits code based on runtime feedback. A design skill hub decouples paradigm-specific knowledge from the core discovery engine, allowing a single workflow to seamlessly handle single-objective, multi-objective, and multi-component design. Meanwhile, a hierarchical experience mechanism organizes search trajectories into a task-level tree to guide exploration and consolidates cross-task patterns into reusable skills. Across six representative benchmark tasks, AlgoEvo matches or surpasses specialized methods with substantially fewer evaluations and reduced token consumption, demonstrating strong intra-task accumulation, cross-task transfer, and the ability to reproduce or exceed existing state-of-the-art performance through flexible skill activation.

## Metadata
- **Published**: 2026-09-14T16:24:27Z
- **Authors**: Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15820v1)