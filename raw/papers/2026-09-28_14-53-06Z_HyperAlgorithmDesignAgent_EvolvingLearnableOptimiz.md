---
title: Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero
published: 2026-09-28T14:53:06Z
authors: Zipei Yu, Yue-Jiao Gong, Zeyuan Ma, Yuncheng Jiang, Zhiguang Cao
url: http://arxiv.org/abs/2609.35328v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero

## Abstract
Meta-Black-Box Optimization (MetaBBO) is one of the highlights in the recent AI for Optimization trend. This paradigm's bi-level workflow leverages the learnable algorithm design policy at meta level to ensure the performance and generalization improvement on the low-level optimization task. While MetaBBO helps advance the performance lower bound of the resulted optimization system, it is currently handcrafted and customized case by case to adapt different optimization problems, which inevitably introduces inherent subjectivity and hence restricts the performance upper bound and usability in practice. In this paper, we address this issue by regarding MetaBBO's design loop as coding task, where we could introduce openendedness into MetaBBO with recursive self-improvement capability of advanced coding agents. Specifically, we propose a dual-agent framework: i) a task agent continuously refines the codebase of a target MetaBBO approach through code evolution; ii) a hyper agent progressively modifies the task agent and itself to provide open-ended design behavior; iii) the evolved MetaBBO codebase is evaluated and all in-execution information is fed back to the agents for recursive self-referential improvement. As a result, given a naive MetaBBO template, our framework automates a design evolution and finds novel variants superior to up-to-date human-made MetaBBO baselines. Surprisingly, the experimental results also demonstrate that our framework supports fast adaption across different optimization domains. Solid interpretation analysis further reveals interesting design principles emerge in such open-ended process. This work serves as the first exploration on automating design of complex learning-assisted optimization algorithms.

## Metadata
- **Published**: 2026-09-28T14:53:06Z
- **Authors**: Zipei Yu, Yue-Jiao Gong, Zeyuan Ma, Yuncheng Jiang, Zhiguang Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35328v1)