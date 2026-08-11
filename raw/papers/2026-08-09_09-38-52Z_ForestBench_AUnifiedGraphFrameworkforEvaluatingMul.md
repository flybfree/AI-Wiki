---
title: ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration
published: 2026-08-09T09:38:52Z
authors: Guo Chen, Ziwen Li, Reed Li, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
url: http://arxiv.org/abs/2608.08605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration

## Abstract
Multi-agent systems (MAS) built on Large Language Models (LLMs) are proliferating rapidly, but their heterogeneous execution traces provide no common basis for evaluation across methods. Outcome-only benchmarks discard collaborations, whereas LLM-as-Judge evaluation requires additional, model-dependent inference and can vary with the LLM and rubric. We introduce a generalizable evaluation framework that maps native MAS traces into a shared space of unified collaboration graphs, enabling different methods to be evaluated under the same representation, reference set, and metric panel. Candidate graphs are compared with a query-specific reference forest. Each forest is a benchmark-provided collection of verified-success graphs: it records diverse ways in which representative MAS methods can complete the task, rather than prescribing a unique optimal process. Instantiating the framework as ForestBench, we filter $844$ collaboration-necessary queries from seven public datasets, precompute ten successful target-conditioned reference graphs per query, and evaluate six representative MAS frameworks. Controlled backbone, reference-construction, and perturbation studies test the stability and scope of evaluation. Once the benchmark forests are built, ForestBench scores a trace in milliseconds without further LLM inference, providing a reusable structural basis for comparing diverse MAS collaboration traces.

## Metadata
- **Published**: 2026-08-09T09:38:52Z
- **Authors**: Guo Chen, Ziwen Li, Reed Li, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08605v1)