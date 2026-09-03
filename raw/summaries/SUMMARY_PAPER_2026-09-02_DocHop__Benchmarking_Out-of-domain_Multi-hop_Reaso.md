---
title: DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents
url: http://arxiv.org/abs/2609.02059v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_03-35-12Z_DocHop_BenchmarkingOut_of_domainMulti_hopReasoning.md
generated_at: 2026-09-02 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
DocHop introduces a benchmark for integrated chart‑context reasoning in document‑style images, where models must resolve semantic references from narrative to select and aggregate evidence across multiple charts. Experiments reveal a large gap between human performance (over 90% accuracy) and the best model’s result (62.83%), with reasoning‑enhanced approaches improving results but suffering degradation as complexity rises.

## Key Takeaways
- annotators achieve over 90% accuracy while the best model reaches only 62.83%
- DocHop uses a stochastic logic‑first generation pipeline that controls reasoning depth and visual density, enabling systematic evaluation across six task categories
- performance consistently improves with added reasoning but deteriorates as reasoning complexity increases

## Context
Multimodal Large Language Models excel at isolated tasks such as chart question answering but often fail to integrate textual context when selecting or aggregating evidence. This paper addresses that limitation by creating a benchmark that forces models to perform multi‑step, cross‑modal reasoning.

## Implications
The findings highlight the need for benchmarks that evaluate integrated reasoning across modalities, guiding researchers and practitioners toward more realistic evaluation protocols. For industry users, DocHop suggests that current MLLMs may underperform in real‑world document analysis tasks requiring contextual evidence aggregation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02059v1)
