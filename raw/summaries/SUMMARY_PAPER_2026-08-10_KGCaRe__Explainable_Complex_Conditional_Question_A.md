---
title: KGCaRe: Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retrieval with LLMs
url: http://arxiv.org/abs/2608.09779v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_16-05-58Z_KGCaRe_ExplainableComplexConditionalQuestionAnswer.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KGCaRe, a hybrid retrieval and reasoning framework that augments RAG with knowledge graph construction to answer complex conditional questions. It outperforms baselines across multiple LLMs on two datasets.

## Key Takeaways
- KGCaRe builds a KG from documents via multi-prompt extraction and stores it in a graph database while embedding docs for neural retrieval.
- The system iteratively traverses the KG guided by the LLM to extract relevant triples, prune noise, and re‑traverse when needed.
- Relevant triples combined with retrieved text are fed into custom prompts to generate answers with explanations.

## Context
Current RAG struggles with domain‑specific conditional queries because LLMs lack structured knowledge. Knowledge graphs provide explicit relationships that can complement neural retrieval for richer context.

## Implications
This approach enables more accurate, explainable QA in specialized fields such as healthcare and legal advice where reasoning over facts matters. Practitioners can integrate KG pipelines into existing RAG stacks to boost performance without retraining models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09779v1)
