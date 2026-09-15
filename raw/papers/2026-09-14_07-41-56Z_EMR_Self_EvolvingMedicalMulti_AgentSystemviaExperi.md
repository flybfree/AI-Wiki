---
title: EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
published: 2026-09-14T07:41:56Z
authors: Dongsheng Shi, Yue Li, Xin Yi, Linlin Wang
url: http://arxiv.org/abs/2609.15161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse

## Abstract
Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

## Metadata
- **Published**: 2026-09-14T07:41:56Z
- **Authors**: Dongsheng Shi, Yue Li, Xin Yi, Linlin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15161v1)