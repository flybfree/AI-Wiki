---
title: FITTER: Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs
url: http://arxiv.org/abs/2608.10668v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-47-58Z_FITTER_Vocabulary_AgnosticCross_DomainInferenceonT.md
generated_at: 2026-08-11 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FITTER, a vocabulary-agnostic structural model for predicting links in temporal knowledge graphs that can handle unseen entities, relations, and timestamps across domains. It demonstrates that the model outperforms existing inductive baselines without retraining on six cross-domain benchmarks. The key contribution is its time-shift invariant encoding of relative ordering.

## Key Takeaways
- FITTER treats each predicate as a pattern of interactions with other predicates and encodes temporal order using relative rather than absolute timestamps, making it immune to shifts in the timeline.
- The model generates embeddings that are vocabulary-agnostic, allowing inference on unseen entities, relation names, and timestamps from different domains without retraining.
- Evaluation across six diverse temporal knowledge graph benchmarks shows consistent improvement over inductive approaches, proving cross-domain transfer is feasible.

## Context
Temporal knowledge graphs capture evolving relationships between entities over time, a core challenge for semantic web applications. Existing methods are limited by fixed vocabularies and cannot generalize to new domains, hindering practical deployment across heterogeneous data sources.

## Implications
This work opens the door to scalable inference systems that can operate on any temporal graph regardless of its vocabulary, benefiting researchers and industry practitioners seeking robust cross-domain insights. The approach may enable automated knowledge integration without costly retraining pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10668v1)
