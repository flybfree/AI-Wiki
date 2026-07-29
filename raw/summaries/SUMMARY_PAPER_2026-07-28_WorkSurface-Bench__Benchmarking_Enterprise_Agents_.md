---
title: WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing
url: http://arxiv.org/abs/2607.25765v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_14-19-59Z_WorkSurface_Bench_BenchmarkingEnterpriseAgentsonMu.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WorkSurface-Bench, a benchmark that evaluates how enterprise agents select and route knowledge across heterogeneous surfaces such as documents, tables, graphs, and file dependencies. The study demonstrates that while routing is highly accurate under strict tool access, the final answer quality remains low without proper surface guidance, highlighting the necessity of correct surface selection for task completion.

## Key Takeaways
- Agents achieve near‑perfect route F1 scores (98.7–99.8) when tools are correctly accessed but only modest Answer performance (56.1–75.3 %), indicating that routing alone does not guarantee correct answers.  
- Adding surface hints improves Answer quality for three of the four models, showing that explicit guidance can bridge the gap between routing and final output.  
- Removing irrelevant tools mainly affects routing efficiency rather than answer correctness, suggesting that tool relevance is a secondary factor compared to proper surface selection.

## Context
Enterprise agents must integrate diverse knowledge sources to perform complex tasks, yet existing benchmarks often ignore how agents decide which source to use first. WorkSurface-Bench addresses this gap by providing auditable reference answers and measuring both routing accuracy and answer correctness across multiple models and settings.

## Implications
The findings stress that improving agent performance requires not only better tool selection but also explicit surface hints or interventions, offering a practical direction for developers seeking higher-quality outputs in enterprise AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25765v1)
