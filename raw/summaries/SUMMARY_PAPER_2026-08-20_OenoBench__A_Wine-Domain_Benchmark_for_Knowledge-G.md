---
title: OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models
url: http://arxiv.org/abs/2608.20106v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_14-37-22Z_OenoBench_AWine_DomainBenchmarkforKnowledge_Ground.md
generated_at: 2026-08-20 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
OenoBench is a wine-domain knowledge benchmark that evaluates large language models on 3,266 multiple‑choice questions spanning six pillars and four difficulty tiers. The study demonstrates that overall accuracy ranges from 53% to 84%, with o3 achieving the highest score at 83.6%.

## Key Takeaways
- Overall accuracy spans 53%-84%, led by o3 at 83.6%.  
- Reasoning‑mode lift concentrates in DeepSeek R1 (+6.8pp) and is absent in Claude Opus and Gemini Pro.  
- Frontier open‑weight models share the cost‑vs‑accuracy Pareto frontier with proprietary reasoning models.

## Context
This work addresses a gap in domain‑specific benchmarking for large language models, where most evaluations rely on generic or out‑of‑domain data. By grounding questions in verified wine facts and using an LLM‑driven audit pipeline, OenoBench provides a transparent, reproducible method to assess model performance on specialized knowledge.

## Implications
The results highlight that reasoning capabilities are not uniformly distributed across models, influencing design choices for applications requiring domain expertise. Practitioners can leverage this benchmark to select or fine‑tune models that balance accuracy and cost, especially when open‑weight alternatives compete with proprietary systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20106v1)
