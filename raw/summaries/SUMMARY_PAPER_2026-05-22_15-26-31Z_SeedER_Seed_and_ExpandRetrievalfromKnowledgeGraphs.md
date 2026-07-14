---

title: "Summary: SeedER: Seed-and-Expand Retrieval from Knowledge Graphs"
url: http://arxiv.org/abs/2605.23753v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_15-26-31Z_SeedER_Seed_and_ExpandRetrievalfromKnowledgeGraphs.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-22 15-26-31Z Seeder Seed And Expandretrievalfromknowledgegraphs


## Summary
The paper introduces SeedER, a retrieval framework that seeds compact core nodes using lightweight dense and entity‑based methods and then expands them iteratively via a learned graph‑aware policy to improve recall for knowledge‑graph queries while controlling computational cost. It demonstrates theoretical limits of dense retrieval on compositional queries and shows empirical gains over baselines with smaller candidate sets.

## Key Takeaways
- The method uses lightweight dense and entity‑based retrieval to create an initial seed set, avoiding expensive full graph traversals.
- Expansion is guided by a reinforcement learning policy that selects nodes maximizing submodular gain while respecting cost constraints.
- Empirically SeedER achieves higher recall with fewer candidates compared to dense embeddings and graph‑augmented baselines.

## Context
Knowledge graphs are central to AI applications requiring relational reasoning, yet existing retrieval methods either scale poorly or cannot capture multi‑hop compositional queries. This work addresses the gap by combining structural awareness with efficient iterative expansion.

## Implications
The approach offers a scalable first‑stage retriever for large KG systems, reducing latency and computational load while preserving relevance. Practitioners can adopt SeedER to build knowledge‑intensive pipelines that balance speed and accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23753v1)
