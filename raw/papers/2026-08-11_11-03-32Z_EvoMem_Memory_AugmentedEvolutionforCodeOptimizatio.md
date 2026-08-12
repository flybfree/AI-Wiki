---
title: EvoMem: Memory-Augmented Evolution for Code Optimization
published: 2026-08-11T11:03:32Z
authors: Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin, Danil Sivtsov, Nikita Glazkov, Olga Volkova, Konstantin Pchelin, Iaroslav Bespalov, Dmitry V. Dylov, Petr Anokhin, Ivan Oseledets
url: http://arxiv.org/abs/2608.10795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoMem: Memory-Augmented Evolution for Code Optimization

## Abstract
Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a persistent memory architecture for LLM-based evolutionary program search that captures and reuses candidate mutation knowledge. EvoMem converts successful mutation events into structured, task-aware advice for future runs. It operates in two phases: after each run, it extracts and stores promising ideas with provenance, and during subsequent evolution, it retrieves a small set of relevant instructions based on the current task and program context to guide mutation. Across geometric optimization, multi-hop question answering, GPU kernel optimization, and related benchmarks, our experiments show positive average improvements in target metrics or search speed for most evaluated settings, while also revealing variability across tasks. Overall, EvoMem provides evidence that persistent memory can reduce some redundant exploration and improve the reuse and adaptation of successful strategies in LLM-driven evolutionary search.

## Metadata
- **Published**: 2026-08-11T11:03:32Z
- **Authors**: Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin, Danil Sivtsov, Nikita Glazkov, Olga Volkova, Konstantin Pchelin, Iaroslav Bespalov, Dmitry V. Dylov, Petr Anokhin, Ivan Oseledets
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10795v1)