---
title: Memory as Code: Declarative Retrieval over Codified Long-Term Memory
url: http://arxiv.org/abs/2610.27700v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_06-17-51Z_MemoryasCode_DeclarativeRetrievaloverCodifiedLong_.md
generated_at: 2026-10-20 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Memory as Code (MaC), a unified long-term memory framework for LLM agents that jointly designs memory construction and retrieval through a shared code abstraction. By coupling codified construction—which builds a three-layer executable memory structure—with declarative retrieval—which translates queries into structured retrieval programs—MaC achieves up to 15.91% relative gains in LLM-judge accuracy over the strongest baselines on LoCoMo and LongMemEval benchmarks while substantially reducing token consumption.

## Key Takeaways
- MaC proposes a three-layer executable memory structure progressing from an atomic function layer, through a relational layer, to a modular composition layer. This codified construction approach treats memories as executable code abstractions rather than flat text embeddings, enabling structured composition of facts that are scattered across sessions and whose relationships evolve over time.
- Declarative retrieval fundamentally reframes the retrieval problem: instead of relevance-based fact selection (the dominant paradigm in existing memory systems), queries are translated into structured retrieval programs that operate over the codified memory. This shift from similarity search to declarative query processing allows the system to compose scattered facts and handle evolving relationships across diverse query types.
- The framework demonstrates practical efficiency gains alongside accuracy improvements, showing up to 15.91% relative improvement in overall LLM-judge accuracy on both LoCoMo and LongMemEval while substantially reducing token consumption, indicating that the code-based abstraction reduces the need for verbose context injection during inference.

## Context
Long-term memory for LLM agents has become a critical bottleneck as agents are deployed in increasingly complex, multi-session scenarios where facts are distributed across interactions and their relationships shift over time. Existing memory systems typically rely on embedding-based retrieval or flat fact stores, which struggle to compose scattered information or adapt to diverse query patterns. MaC draws on the well-established principles of modularity and composability from software engineering to address these limitations, representing a paradigm shift from treating memory as a retrieval problem to treating it as a programmable data structure.

## Implications
For practitioners building agentic systems, MaC suggests that memory architectures should move beyond vector-database retrieval toward structured, composable abstractions that can be queried programmatically, potentially reducing both operational costs (token consumption) and accuracy failures in long-horizon tasks. For the broader AI research community, this work signals a convergence between programming-language design principles and memory-augmented reasoning, opening new directions for how agents store, organize, and reason over accumulated knowledge across extended interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27700v1)
