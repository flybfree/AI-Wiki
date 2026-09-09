---
title: DI-Bench: Systematically Generating In-Domain Data Intelligence Benchmarks for Enterprise Agents
published: 2026-09-04T23:53:21Z
authors: Jiangyun Zhang, Kristen Surrao, Torpong Nitayanont, Yupei Zhang, Roopali Singh, Zhiyu Chen, Julia Huang, Zhou Tang, Shayan Ali Akbar, Omar Alonso, Erwin Cornejo, Yuan Li, Yi Zhang
url: http://arxiv.org/abs/2609.05776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DI-Bench: Systematically Generating In-Domain Data Intelligence Benchmarks for Enterprise Agents

## Abstract
Evaluating enterprise agents on domain-specific benchmarks is critical, yet public benchmarks rarely evaluate whether agents can integrate business knowledge with analytical computation, and constructing such benchmarks manually is costly. We present DI-Bench, a pipeline for generating realistic benchmarks for data intelligence (DI), the practice of extracting insights from large volumes of enterprise data. To emulate realistic DI tasks that require both computation and knowledge retrieval, DI-Bench builds an artifact linkage graph over data tables, dimensions, metrics, and documents to form questions involving structured data and associated knowledge. Ground truth answers are derived via query execution, followed by LLM question generation and validation. Applied to two public datasets, the pipeline produces a 731-task benchmark covering knowledge retrieval, analytical computation, and rule-grounded reasoning. To show the discriminatory capability and difficulty of the benchmark, we evaluate four models, revealing a substantial finding: models achieve only 32% accuracy when doing computational tasks where retrieved business rules modify the computation.

## Metadata
- **Published**: 2026-09-04T23:53:21Z
- **Authors**: Jiangyun Zhang, Kristen Surrao, Torpong Nitayanont, Yupei Zhang, Roopali Singh, Zhiyu Chen, Julia Huang, Zhou Tang, Shayan Ali Akbar, Omar Alonso, Erwin Cornejo, Yuan Li, Yi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05776v1)