---
title: Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support
published: 2026-08-23T20:31:34Z
authors: Kushagra Yadav, Nalin Prabhath, Amit Lamba, Goeun Han, Yining Mao
url: http://arxiv.org/abs/2608.22583v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support

## Abstract
Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather than treating a clinical knowledge graph as a static extraction artifact, we treat it as a predictive patient-state representation. For each admission, the system constructs an evidence-scored graph from structured MIMIC-IV records and inferred clinical cross-links, then learns to recover held-out clinical relations from the observed graph context. We evaluate the refiner with leakage-free leave-one-out edge recovery (MRR and Hits@k) and held-out batch-mask evaluation (AUC and MRR). To isolate the contribution of discharge-note context, we compare a note-embedding-free configuration with a note-augmented configuration that injects real discharge-note representations only into note-grounded entities. Under the same cohort and evaluation protocol, entity-grounded note injection improves overall leave-one-out MRR by 31% relative improvement.

## Metadata
- **Published**: 2026-08-23T20:31:34Z
- **Authors**: Kushagra Yadav, Nalin Prabhath, Amit Lamba, Goeun Han, Yining Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22583v1)