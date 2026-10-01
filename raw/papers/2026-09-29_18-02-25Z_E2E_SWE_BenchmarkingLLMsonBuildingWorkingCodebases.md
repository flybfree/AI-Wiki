---
title: E2E-SWE: Benchmarking LLMs on Building Working Codebases from Scratch
published: 2026-09-29T18:02:25Z
authors: Hantian Ding, Chloe Bi, Jiacheng Zhu, John Yang, Matt Deitke, Pengcheng Yin, Zijian Wang, Rui Hou
url: http://arxiv.org/abs/2609.38335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# E2E-SWE: Benchmarking LLMs on Building Working Codebases from Scratch

## Abstract
Coding agents powered by large language models (LLMs) are evolving from making localized code changes to developing complete software repositories. However, evaluating repository-scale generation remains challenging: tasks must demand system-level reasoning while ensuring that all evaluated behaviors are precisely specified and independent of any particular implementation. We introduce E2E-SWE, a benchmark for evaluating whether coding agents can build complete, functional software repositories end to end. E2E-SWE contains 186 whole-repository generation tasks spanning 11 programming languages. Given only a natural-language specification and an empty workspace, an agent must implement a complete, installable project that satisfies a comprehensive suite of hidden tests. Each task is constructed by a software engineer in collaboration with an LLM; together, they develop the test suite and a corresponding implementation-independent specification. To ensure that tasks are well specified and practically solvable, we further subject them to an iterative verification process in which autonomous agents audit and repair task defects using static inspection and failures observed from real model rollouts. Evaluating 13 frontier models, we find substantial variation in end-to-end repository generation ability, with pass@1 ranging from 11.7% to 67.7%, providing strong model differentiation while leaving considerable headroom for future progress. Analysis of agent trajectories further reveals long, front-loaded reasoning patterns, highlighting the planning and system-level reasoning required to construct working codebases from scratch.

## Metadata
- **Published**: 2026-09-29T18:02:25Z
- **Authors**: Hantian Ding, Chloe Bi, Jiacheng Zhu, John Yang, Matt Deitke, Pengcheng Yin, Zijian Wang, Rui Hou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38335v1)