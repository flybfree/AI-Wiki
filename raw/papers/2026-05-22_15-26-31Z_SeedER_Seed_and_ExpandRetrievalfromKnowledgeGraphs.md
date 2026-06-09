---
title: SeedER: Seed-and-Expand Retrieval from Knowledge Graphs
published: 2026-05-22T15:26:31Z
authors: Hamed Shirzad, Frederik Wenkel, Dominique Beaini, Danica J. Sutherland, Emmanuel Noutahi
url: http://arxiv.org/abs/2605.23753v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SeedER: Seed-and-Expand Retrieval from Knowledge Graphs

## Abstract
Knowledge graphs (KGs) offer a rich representation for relational knowledge, but their irregular structure makes retrieval challenging: ego-graph expansion grows rapidly, and dense embedding methods struggle with multi-hop compositional queries. Existing agent-based graph exploration approaches, while expressive, are often too expensive for large-scale retrieval. We introduce SeedER (Seed-and-Expand Retrieval), a retrieval framework that explicitly leverages KG structure through iterative, low-cost expansion. SeedER first seeds a compact set of core nodes using lightweight dense and entity-based retrieval, then selectively expands this set via a learned graph-aware policy trained with reinforcement learning. This design decomposes global reasoning into reusable local decisions, enabling efficient discovery of query-relevant nodes while tightly controlling expansion cost. We show theoretical limitations of dense retrieval on compositional graph queries, and establish advantages of SeedER from both compositional generalization and graph-constrained submodular optimization perspectives. Empirically, SeedER substantially improves recall with compact candidate sets over strong dense and graph-augmented baselines, making it an effective first-stage retriever for knowledge-intensive reasoning systems.

## Metadata
- **Published**: 2026-05-22T15:26:31Z
- **Authors**: Hamed Shirzad, Frederik Wenkel, Dominique Beaini, Danica J. Sutherland, Emmanuel Noutahi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23753v1)