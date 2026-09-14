---
title: Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models
published: 2026-09-11T16:04:00Z
authors: Utkarsh Soni, Syed Shariyar Murtaza, Yifan Nie, Sachin Chandrasekhar, Eugene Wen
url: http://arxiv.org/abs/2609.13005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models

## Abstract
Large language models (LLMs) have achieved strong performance on a wide range of natural language tasks, and recent benchmarks suggest that they are increasingly adept at multi-hop reasoning. However, these benchmarks are typically short-horizon, requiring only a small number of retrieval or inference steps, and provide limited evidence of reliability on real-world tasks that involve following manuals spanning hundreds of pages with complex, interdependent guidelines. In this paper, we introduce Tasks over Application Manuals (TAM), a benchmark for evaluating long-horizon procedural reasoning. We construct TAM by curating real-world tasks from two domains: ICD-10-CM clinical coding (mapping medical conditions to diagnostic codes) and U.S. federal sentencing (computing crime sentencing guideline outcomes, specifically offense levels), with human-validated labels. Each task requires following an authoritative manual with tens of thousands of rules and executing a sequence of interdependent steps across different sections to produce an exact answer. We evaluate general-purpose prompting approaches, including retrieval-augmented generation, ReAct-style prompting, and an agent-harness baseline on GPT-5, and find that the best exact-match performance remains extremely low: 1% on ICD-10-CM coding and 15.5% on sentencing tasks. These results show that current benchmarks may overestimate LLM reasoning ability and miss a key challenge: reliably following long, rule-based procedures. The complete TAM data and code are publicly available.

## Metadata
- **Published**: 2026-09-11T16:04:00Z
- **Authors**: Utkarsh Soni, Syed Shariyar Murtaza, Yifan Nie, Sachin Chandrasekhar, Eugene Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13005v1)