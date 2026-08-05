---
title: GoT-CD: Graph-of-Thoughts Causal Discovery and the Fragility of Post-hoc Path-Specific Fairness Audits
url: http://arxiv.org/abs/2608.02877v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_20-59-26Z_GoT_CD_Graph_of_ThoughtsCausalDiscoveryandtheFragi.md
generated_at: 2026-08-05 01:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GoT-CD, a method that combines graph-of-thoughts reasoning with causal discovery to generate valid directed acyclic graphs (DAGs) for fairness audits. The authors demonstrate that while the discovered DAGs can be structurally competitive with large language model baselines, path-specific counterfactual fairness assessments can still produce misleading results when the sensitive pathway is absent from the graph.

## Key Takeaways
- GoT-CD generates acyclic graphs by exploring all candidate edges in parallel and merging them under a hard union constraint that forbids invented edges.  
- The method achieves the best DAG‑valid F1 score among LLM methods on three benchmark datasets, yet structural fidelity alone does not guarantee fair audit outcomes.  
- In an Alzheimer’s dataset with a known unfair path, five of eight discovered graphs omit the sensitive attribute to outcome edge, causing null overall effects while mediated effects remain.

## Context
Causal discovery is widely used in AI to uncover hidden relationships and support fairness audits, yet most approaches treat edges uniformly and ignore how specific pathways affect downstream analyses. This gap leaves practitioners vulnerable to false negatives when path‑specific metrics depend on edges that may be dropped by the discovery algorithm.

## Implications
For developers of predictive models, relying solely on a discovered DAG can lead to inaccurate fairness conclusions, undermining trust in automated audits. Practitioners must combine structural discovery with explicit pathway analysis to ensure that post‑hoc fairness assessments reflect genuine causal mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02877v1)
