---
title: Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering
url: http://arxiv.org/abs/2608.27925v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_05-03-33Z_Entity_MemoryGraphRetrievalImprovesEvidenceCoverag.md
generated_at: 2026-08-30 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Entity-Memory graph retrieval for long‑conversation question answering, demonstrating that it boosts evidence recall at the top‑25 without harming final answer F1. On 1,986 questions from ten LoCoMo conversations, recall rises from 79.7468 % to 84.4842 %, while F1 remains unchanged.

## Key Takeaways
- Graph retrieval treats dialogue turns as verbatim Memory nodes, links repeated mentions through shared Entities, and connects adjacent Memories with chronological edges, enabling dense backfill that cosine ranking may omit. - The matched dense control shares the Memory vector, context budget, answer protocol, and evaluator, isolating graph structure from embedding changes; recall advantage persists from top‑5 to 50 but F1 shows no difference. - Embedding robustness is mixed: F1 is unaffected by embeddings, while recall is sensitive to embedding artifacts.

## Context
Long‑conversation QA systems often suffer from limited evidence coverage due to narrow retrieval budgets and noisy embeddings. This work shows that a structured graph approach can recover omitted memories without sacrificing answer quality, highlighting the value of memory‑centric reasoning in dialogue understanding.

## Implications
Practitioners can integrate graph‑based retrieval as a lightweight augmentation to improve evidence recall in chatbots, treating it as a coverage boost rather than an F1 gain. Researchers should caution against overstating model or embedding equivalence and address embedding artifacts when recall is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27925v1)
