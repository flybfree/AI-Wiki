---
title: FITTER: Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs
published: 2026-08-11T08:47:58Z
authors: Jiaxin Pan, Mojtaba Nayyeri, Osama Mohammed, Daniel Hernandez, Rongchuan Zhang, Cheng Cheng, Steffen Staab
url: http://arxiv.org/abs/2608.10668v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FITTER: Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs

## Abstract
Temporal knowledge graphs are central to many uses of the Semantic Web, but existing completion methods assume the entities, relation names, and timestamps to be reasoned about are already known at training time, restricting each model to a single graph and vocabulary. We propose FITTER, the first fully-inductive structural model for temporal knowledge graph link prediction that supports cross-domain transfer: the inference graph may contain entirely unseen entities, relation names, and timestamps drawn from a different domain. FITTER represents each predicate by its interaction patterns with others and time through encodings of relative rather than absolute ordering; message-passing fuses local and global temporal context to produce vocabulary-agnostic embeddings. We prove the temporal encoding is time-shift invariant and evaluate FITTER on cross-domain, cross-graph transfer over six temporal knowledge graph benchmarks of diverse domains, granularities, and time spans. FITTER consistently outperforms inductive baselines without retraining, indicating that vocabulary-agnostic structural learning is a viable foundation for inference over the heterogeneous knowledge graphs of the Semantic Web.

## Metadata
- **Published**: 2026-08-11T08:47:58Z
- **Authors**: Jiaxin Pan, Mojtaba Nayyeri, Osama Mohammed, Daniel Hernandez, Rongchuan Zhang, Cheng Cheng, Steffen Staab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10668v1)