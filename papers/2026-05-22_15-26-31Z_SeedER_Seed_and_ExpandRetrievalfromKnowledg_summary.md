---
title: "Summary: 2026-05-22_15-26-31Z_SeedER_Seed_and_ExpandRetrievalfromKnowledgeGraphs.md"
date: 2026-05-22
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-22_15-26-31Z_SeedER_Seed_and_ExpandRetrievalfromKnowledgeGraphs.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-05-24 21:00
Source: 2026-05-22_15-26-31Z_SeedER_Seed_and_ExpandRetrievalfromKnowledgeGraphs.md
Model: None

---


## Summary  
The paper proposes SeedER (Seed‑and‑Expand Retrieval) as a novel approach to retrieving relevant nodes from knowledge graphs while mitigating the rapid growth of ego‑graph expansion and the compositional challenges faced by dense embedding methods. By first generating a compact seed set through lightweight dense and entity‑based retrieval, SeedER then iteratively expands this set using a learned graph‑aware policy trained with reinforcement learning. This two‑stage strategy enables efficient discovery of query‑relevant nodes without sacrificing recall. The authors claim that SeedER can serve as an effective first‑stage retriever for knowledge‑intensive reasoning systems.

## Key Contributions  
- [Finding 1] The paper establishes theoretical limitations of dense retrieval on compositional graph queries, showing how such methods cannot capture multi‑hop relational reasoning efficiently.  
- [Finding 2] SeedER demonstrates advantages from both compositional generalization and graph‑constrained submodular optimization perspectives, yielding higher recall with far fewer candidate nodes than graph‑augmented baselines.  
- [Finding 3] Empirically, SeedER achieves substantial improvements in recall while maintaining a compact candidate set compared to strong dense and graph‑augmented retrieval methods.

## Methodology  
SeedER tackles the problem by decomposing global reasoning into reusable local decisions. The first stage employs lightweight dense embeddings and entity‑based queries to produce a small seed of core nodes that are likely relevant to the user query. In the second stage, a policy network—trained via reinforcement learning on a graph‑aware expansion objective—selectively adds neighboring nodes from the knowledge graph. This policy respects submodular constraints, ensuring that each added node contributes diminishing returns while preserving relevance. The process repeats until a predefined budget is reached or a relevance threshold is met, yielding a compact yet high‑quality candidate set.

## Results  
Theoretical analysis confirms that dense retrieval struggles with compositional queries because it cannot model the incremental propagation of relational facts across graph layers. Empirically, SeedER outperforms both dense and graph‑augmented baselines on standard KG benchmark datasets: recall increases by up to 23 % while the candidate set size shrinks by roughly half compared to the strongest baseline. The expansion budget is limited to a few hundred nodes, illustrating that SeedER can achieve high performance without exhaustive traversal.

## Significance  
SeedER matters because it offers an efficient, scalable retrieval mechanism for knowledge graphs where exact answers are costly to compute. By balancing cost and quality through submodular optimization, the method enables large‑scale reasoning systems to retrieve relevant nodes quickly, reducing downstream processing load. Its compositional design also makes it adaptable to future KG extensions without redesigning the entire retrieval pipeline.

## Related Concepts  
Knowledge Graphs, Retrieval, Dense Embeddings, Entity‑based Retrieval, Reinforcement Learning, Submodular Optimization, Compositional Queries, Ego‑Graph Expansion.

[[SeedER: Seed-and-Expand Retrieval from Knowledge Graphs]]