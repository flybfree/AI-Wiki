---
title: LEED: Local Embedding Evolution Distance for over-smoothing estimation and virtual node selection in GNN
url: http://arxiv.org/abs/2608.09596v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_13-30-46Z_LEED_LocalEmbeddingEvolutionDistanceforover_smooth.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LEED, a local metric that measures over-smoothing by tracking how individual node embeddings change across GNN layers. Experiments demonstrate that LEED provides finer-grained diagnostics than Dirichlet energy and improves virtual node selection leading to better performance on benchmark datasets.

## Key Takeaways
- LEED quantifies over-smoothing at the node level, revealing heterogeneous patterns invisible to global Dirichlet energy.
- The metric generates embedding-driven centrality scores that can be used as importance indicators for nodes during training.
- Using LEED guides virtual node construction, reducing over-squashing and enhancing GNN accuracy across multiple datasets.

## Context
Graph Neural Networks aim to capture relational information efficiently but often suffer from representation degradation. Existing global metrics like Dirichlet energy lack resolution, prompting the need for local diagnostics that can inform architecture design.

## Implications
LEED offers practitioners a tool to diagnose and mitigate over-smoothing without sacrificing overall model evaluation. By integrating LEED into GNN pipelines, developers can achieve more robust representations and better scalability in real-world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09596v1)
