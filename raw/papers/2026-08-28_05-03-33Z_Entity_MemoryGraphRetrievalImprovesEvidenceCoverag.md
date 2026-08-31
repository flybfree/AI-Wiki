---
title: Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering
published: 2026-08-28T05:03:33Z
authors: Shumao Sun
url: http://arxiv.org/abs/2608.27925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering

## Abstract
Entity-Memory graph retrieval keeps dialogue turns as verbatim Memory nodes, links repeated mentions through shared Entities, and connects adjacent Memories with directed chronological edges. At query time the retriever moves from Entity gating through semantic fusion and one-hop chronological recovery to dense backfill. The path can keep a neighboring Memory that dense cosine ranking would otherwise omit. A matched dense control shares the Memory and query vectors, context budget, requested answer protocol, and evaluator, isolating graph structure from changes to the reader.   On 1,986 questions from ten LoCoMo conversations, graph retrieval raises official evidence recall at top-k 25 from 79.7468% to 84.4842%. The recall advantage is supported from top-k 5 to 50, while no matched cutoff supports an overall final-answer F1 difference. Four paper-eligible requested configurations support empirical robustness across the tested GPT-3.5 and DeepSeek extractors on both outcomes. Embedding robustness is mixed: F1 has no supported contrast, but recall is sensitive to the embedding artifact. The comparison isolates a retrieval-coverage gain from graph structure. It does not establish a final-answer F1 gain, model or embedding equivalence, or cross-dataset generalization.

## Metadata
- **Published**: 2026-08-28T05:03:33Z
- **Authors**: Shumao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27925v1)