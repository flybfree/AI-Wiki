---
title: DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation
published: 2026-09-27T11:52:58Z
authors: Guanzheng Chen, Viet Dac Lai, Subhojyoti Mukherjee, Branislav Kveton, Seunghyun Yoon, Franck Dernoncourt, Qizhe Xie, Trung Bui
url: http://arxiv.org/abs/2609.33485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation

## Abstract
While Large Language Models (LLMs) advertise million-token context windows, reasoning quality often collapses as inputs grow -- a phenomenon termed context rot. This failure stems from a structural entanglement in monolithic architectures, where the massive search burden of contextual grounding exhausts the representational capacity needed for complex reasoning. To resolve this, we propose Grounding-Reasoning Disaggregation via DIStributed long COntext scaling (DISCO). Inspired by distributed computing frameworks like Apache Spark, DISCO partitions long context across a fleet of Worker LLMs dedicated exclusively to parallel, localized grounding. A central Driver LLM, trained via Reinforcement Learning (GRPO) to optimize planning, orchestrates execution by dynamically mapping queries into atomic extraction tasks and reducing the gathered evidence to synthesize a final answer. By isolating reasoning from raw context noise, DISCO effectively eliminates context rot. On RULER-QA (1M tokens), it maintains 78.4% accuracy where standard baselines collapse. Furthermore, it outperforms full-context models by up to 9.8 points on LongBench v2 and matches frontier models like Gemini-3-Pro-Preview while reducing inference costs by over 80%, establishing a highly efficient paradigm for robust long-context inference.

## Metadata
- **Published**: 2026-09-27T11:52:58Z
- **Authors**: Guanzheng Chen, Viet Dac Lai, Subhojyoti Mukherjee, Branislav Kveton, Seunghyun Yoon, Franck Dernoncourt, Qizhe Xie, Trung Bui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33485v1)