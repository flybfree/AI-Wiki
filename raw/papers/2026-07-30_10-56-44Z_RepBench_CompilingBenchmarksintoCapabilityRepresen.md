---
title: RepBench: Compiling Benchmarks into Capability Representations for Large Language Models
published: 2026-07-30T10:56:44Z
authors: Yanshi Li, Xueru Bai, Shuman Liu, Long Zhang
url: http://arxiv.org/abs/2607.28008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepBench: Compiling Benchmarks into Capability Representations for Large Language Models

## Abstract
Representation engineering reads and steers capability directions in large language models, yet methods are typically evaluated on paper-specific synthetic data. The resulting measurements are difficult to compare or reproduce and may reflect surface patterns rather than capabilities. We present RepBench, a benchmark-grounded data layer for capability-aligned representation probing. Crawling 13,427 benchmark papers yields a taxonomy of 182 capability clusters in 13 families; harvesting 353 public benchmark datasets yields 46,149 audited probe texts covering 94 capabilities, each supported by at least two independent benchmarks. This multi-benchmark design reduces dependence on any single source: raw per-text vectors exhibit no natural cluster granularity, whereas benchmark-pooled capability vectors show an interior clustering optimum at a small number of clusters on all 12 evaluated models, with low agreement to the human taxonomy. Under cross-benchmark transfer evaluation across twelve models completed by all four readouts, difference-in-means attains the highest model-level mean on ten models, while logistic regression wins the most capability-model cells. This disagreement shows that the readout method and aggregation criterion are meaningful evaluation dimensions. The pipeline, corpus, and evaluation code are released as a reusable closed-loop workflow.

## Metadata
- **Published**: 2026-07-30T10:56:44Z
- **Authors**: Yanshi Li, Xueru Bai, Shuman Liu, Long Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28008v1)