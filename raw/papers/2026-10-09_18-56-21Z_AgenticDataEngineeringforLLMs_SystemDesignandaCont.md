---
title: Agentic Data Engineering for LLMs: System Design and a Controlled Empirical Study
published: 2026-10-09T18:56:21Z
authors: Ruomeng Ding, Qianli Shen, Zhaoyang Han, Meixin Chen, Daoyuan Chen, Yaliang Li
url: http://arxiv.org/abs/2610.14238v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Data Engineering for LLMs: System Design and a Controlled Empirical Study

## Abstract
LLM data engineering requires iterative experimentation to determine how data selection, rewards, and curricula affect model learning, making it a natural setting for AI-for-AI (AI4AI) research. Can agents use experimental feedback to progressively improve strategies, and do the resulting strategies improve target-model performance on held-out data? We study how agents use experimental feedback to develop data-engineering strategies under fixed training and evaluation protocols. Our Agentic Data Engineering (ADE) framework lets agents pursue, revise, or combine research directions using cumulative findings. Strategies are selected by in-loop scores and evaluated on held-out benchmarks. Across four tasks-math and code data selection, math reward design, and math curriculum learning-selected strategies achieve absolute gains over generic baselines of up to 13.34% on AIME25 Pass@32 and 5.85% averaged across four held-out benchmarks under fixed training conditions. In-loop scores improve over successive experiments, while held-out trajectories show that later in-loop gains do not always improve generalization. Comparisons of research organization and feedback access favor combining evidence analysis with cumulative findings. Research trajectories show how earlier findings inform strategy revisions and combinations across research directions.

## Metadata
- **Published**: 2026-10-09T18:56:21Z
- **Authors**: Ruomeng Ding, Qianli Shen, Zhaoyang Han, Meixin Chen, Daoyuan Chen, Yaliang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14238v1)