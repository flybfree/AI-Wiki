---
title: Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering
published: 2026-07-25T16:29:38Z
authors: Hieu Man, Thien Huu Nguyen
url: http://arxiv.org/abs/2607.23278v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering

## Abstract
Multi-hop question answering requires coordinating relational and textual evidence across reasoning steps, a combination neither a text corpus nor a knowledge graph can supply alone. Prior work often emphasizes only part of this loop: graph-augmented RAG retrieves from a pre-built or query-updated graph, KGQA systems search within topic-centered subgraphs, and memory-augmented agents maintain evolving memories without continuously reconciling graph memory with textual context. We propose Co-E, a training-free system built around synchronized bidirectional graph-text working memory. A synchronization cycle consolidates textual memory, extracts relational triples into graph memory, and injects graph facts back into the generation context. Because both memories are maintained, they shape subsequent retrieval and generation. Evaluated on six multi-hop QA benchmarks, Co-E improves over comparable training-free open-backbone baselines and is competitive with larger or trained systems.

## Metadata
- **Published**: 2026-07-25T16:29:38Z
- **Authors**: Hieu Man, Thien Huu Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23278v1)