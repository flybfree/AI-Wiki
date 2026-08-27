---
title: BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks
published: 2026-08-26T01:45:55Z
authors: Zane Koch, Asmamaw T. Wassie, Javier Valdes-Aleman, Jason Lee, Michaela M. Hinks, Samuel G. Rodriques, Andrew D. White, Jon M. Laurent
url: http://arxiv.org/abs/2608.25286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks

## Abstract
Artificial intelligence (AI) promises to accelerate biological research by automating computational analyses. Yet the ability of AI agents to carry out computational biology at the scale of complete research studies has not been systematically evaluated. Here we introduce BixBench3, a benchmark that measures the capacity of AI agents to process raw biological data through to scientific results. We designed BixBench3 tasks to mirror the delegation of work from a scientist to an agent: the scientist chooses the research question and high-level methods, then delegates implementation of all analyses to the agent. In each task, an agent receives a research objective, methodological guidance, and raw data derived from a published scientific study, and must execute a sequence of analyses to achieve the research objective. The data artifacts resulting from these analyses - such as peak call matrices or differential expression tables - are programmatically graded against the corresponding artifacts generated and reported in the original study. Across 20 BixBench3 tasks encompassing the generation of 138 unique artifacts, we find that 13 frontier models achieve scores ranging from 0.00 for Gemini 3.1 Flash Lite to 0.48 for GPT 5.6 Sol. Agents perform worse on tasks with larger raw datasets (0.36 on tasks with <100 GB versus 0.10 on tasks with >100 GB) and on analyses requiring more sequential steps (0.36 at 1-2 steps vs 0.24 at 3+). On average, agents use 6.8 hours, 102 million tokens, and $43 to complete each task, with the longest attempts consuming 24 hours, 1.07 billion tokens, and $525. Notably, the highest-scoring agents used fewer tokens and were cheaper than less performant options. These results reveal that LLMs vary substantially in their ability to (1) execute multiple sequential analysis steps coherently, (2) manage large quantities of raw data, and (3) work across scientific domains.

## Metadata
- **Published**: 2026-08-26T01:45:55Z
- **Authors**: Zane Koch, Asmamaw T. Wassie, Javier Valdes-Aleman, Jason Lee, Michaela M. Hinks, Samuel G. Rodriques, Andrew D. White, Jon M. Laurent
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25286v1)