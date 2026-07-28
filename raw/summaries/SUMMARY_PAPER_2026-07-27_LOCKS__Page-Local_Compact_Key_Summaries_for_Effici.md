---
title: LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding
url: http://arxiv.org/abs/2607.24555v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_15-28-52Z_LOCKS_Page_LocalCompactKeySummariesforEfficientLon.md
generated_at: 2026-07-27 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LOCKS, a method for compressing the attention key‑value cache in long‑context language decoding. By creating page‑local spectral summaries that retain only the low‑rank bases and discarding page‑specific directions, LOCKS reconstructs within‑page logits, estimates each page’s attention mass via log‑sum‑exp, and selects only the top pages for attention. The approach reduces cache size to about a tenth of the original while preserving decoding quality on long documents.

## Key Takeaways
- LOCKS replaces the full KV cache with per‑page spectral summaries that are roughly one‑tenth the size of the original cache, enabling efficient storage and faster updates.
- The method reconstructs within‑page logits from these summaries, estimates each page’s attention mass using a log‑sum‑exp operation, and attends only to the top pages without reading any candidate keys or values.
- Evaluations on LongBench‑v1 QA show LOCKS stays within a point of the full cache oracle on retrieval‑dense RULER, while achieving large margins on long‑form reasoning benchmarks such as AIME26 and MATH‑500 where baseline selectors fail.

## Context
Long‑context decoding remains limited by the quadratic cost of maintaining dense attention matrices. Efficient compression techniques are crucial for serving massive language models at token budgets typical in production systems. LOCKS addresses this bottleneck with a novel, page‑local summarization strategy that maintains quality while dramatically reducing memory and compute demands.

## Implications
For industry practitioners, LOCKS offers a drop‑in plugin for vLLM that halves per‑token decode latency even at millions of tokens, making long‑context inference feasible within tight budget constraints. The approach could enable cheaper deployment of large models in real‑time applications where every millisecond and megabyte counts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24555v1)
