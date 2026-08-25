---
title: SSE-Bio: A Structured Self-Evolving Agent with Agentic Retrieval Policy for Multi-Hop Biomedical Reasoning
url: http://arxiv.org/abs/2608.22132v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_23-08-56Z_SSE_Bio_AStructuredSelf_EvolvingAgentwithAgenticRe.md
generated_at: 2026-08-24 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SSE-Bio, a structured self‑evolving agent designed for multi‑hop biomedical reasoning that links evidence across diseases, drugs, proteins and phenotypes. By using an agentic retrieval policy that selects knowledge triplets and prior templates without globally rewriting instructions, the model avoids instruction drift while improving its reasoning memory through fine‑grained template editing. Experiments on three benchmarks show SSE-Bio outperforms existing baselines by 6.56 absolute points over the strongest self‑evolving approach.

## Key Takeaways
- The agent maintains a structured state and uses a trainable proxy policy to retrieve relevant knowledge triplets and templates, allowing selective evidence access across multiple hops.
- Retrieval decisions are optimized via group relative policy optimization with decision‑contrastive groups, enabling the model to compare alternative retrieval choices and select the best ones.
- Fine‑grained template editing improves the reasoning memory, leading to consistent gains over static self‑evolving agents.

## Context
Biomedical QA demands models that can traverse complex knowledge graphs where each hop introduces new entities. Traditional approaches often suffer from instruction drift when updating reasoning procedures, limiting their adaptability. SSE-Bio addresses this by decoupling instruction updates from retrieval decisions, offering a more flexible and stable framework for evolving agents.

## Implications
For researchers, SSE-Bio provides a practical method to maintain consistent performance across diverse biomedical datasets without manual prompt engineering. In industry, the approach can be integrated into clinical decision support systems that require up‑to‑date knowledge linking, enhancing both accuracy and scalability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22132v1)
