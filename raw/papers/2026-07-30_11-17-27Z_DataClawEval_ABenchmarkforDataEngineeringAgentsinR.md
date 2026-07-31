---
title: DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness
published: 2026-07-30T11:17:27Z
authors: Debin Meng, Jiaming Yang, Zefang Zong, Tengyue Xu, Haining Xie, Yang Li, Peng Chen
url: http://arxiv.org/abs/2607.28033v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness

## Abstract
Large language models (LLMs) and LLM-based agents are increasingly being deployed to automate complex workflows, promising to revolutionize data management and processing. However, existing benchmarks predominantly focus on simplified Text-to-SQL translation or data analysis, leaving the critical and complex domain of end-to-end data engineering largely unexplored. To bridge this gap, we introduce DataClawEval, the first comprehensive benchmark designed specifically to evaluate the end-to-end task completion capabilities of autonomous agents in real-world data engineering scenarios. Built upon production-grade code authored by professional enterprise data engineers, it comprises 100 rigorous, end-to-end tasks spanning five execution engines: PySpark, MySQL, HiveSQL, PrestoSQL/Trino, and FlinkSQL. Rather than non-deterministic LLM-as-a-judge scoring, each task is executed within a case-specific, isolated sandbox and graded by deterministic, rule-based scripts. Evaluating 16 frontier agents exposes critical limitations: The strongest model attains only 74.9 overall, and no single model dominates, as each excels on a different engine, revealing strict domain specialization rather than omnipotent proficiency. Thus, autonomous data engineering remains a formidable, unresolved challenge. We release our dataset, containerized environments, and deterministic evaluation scripts at https://github.com/Dicemy/DataClawEval/tree/master

## Metadata
- **Published**: 2026-07-30T11:17:27Z
- **Authors**: Debin Meng, Jiaming Yang, Zefang Zong, Tengyue Xu, Haining Xie, Yang Li, Peng Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28033v1)