---
title: From Single- to Cross-Document: Benchmarking Multi-Granularity Event Analysis of Large Language Models
url: http://arxiv.org/abs/2607.27654v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_04-06-55Z_FromSingle_toCross_Document_BenchmarkingMulti_Gran.md
generated_at: 2026-07-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MiGUE‑Bench, a benchmark that evaluates large language models on multi‑granularity event analysis tasks. The study shows that while LLMs excel at individual granularities, they struggle with cross‑document and higher‑level tasks, highlighting gaps in current model capabilities.

## Key Takeaways
- MiGUE‑Bench provides a unified framework for assessing event detection, relation reasoning, structure induction, and future prediction across different document granularities.  
- The LLM‑driven self‑correcting annotation pipeline enables scalable collection of high‑quality labeled events, reducing human annotation bottlenecks.  
- Experiments reveal that state‑of‑the‑art LLMs perform well on atomic event detection but falter when linking events across documents or inferring complex narratives.

## Context
Event analysis remains a core challenge for AI systems that must understand real‑world information flow. Existing benchmarks often focus on single‑document tasks, limiting insights into how models handle multi‑granularity scenarios. This paper bridges that gap by creating a comprehensive benchmark and exposing the limitations of current approaches.

## Implications
For researchers, MiGUE‑Bench offers a clear roadmap to improve model robustness across granularities, guiding future training objectives. For industry practitioners, it signals the need for multimodal, cross‑document reasoning capabilities in applications like event summarization and knowledge graph construction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27654v1)
