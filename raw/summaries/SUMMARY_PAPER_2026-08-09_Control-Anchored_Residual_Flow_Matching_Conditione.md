---
title: Control-Anchored Residual Flow Matching Conditioned on Gene Geometry for Virtual Cell Perturbation Modeling
url: http://arxiv.org/abs/2608.06824v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_05-29-00Z_Control_AnchoredResidualFlowMatchingConditionedonG.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GeneGeoFlow, a method that conditions transcriptional response predictions on gene-specific geometry derived from biological networks and control data, achieving high delta scores on benchmark datasets. The approach separates stable network structures from intervention-specific responses while using condition-wise optimal transport for training.

## Key Takeaways
- GeneGeoFlow uses multi‑scale spectral coordinates extracted from Gene Ontology and control‑derived coexpression networks to create gene geometry that is conditioned by the perturbation, not the static network.
- A gating module selects relevant structural scales per gene, producing intervention‑specific geometry without propagating target signals through the graph.
- Training employs condition‑wise optimal transport and a delta‑correlation objective to align predicted expression shifts with observed ones.

## Context
Virtual cell modeling requires models that can predict transcriptional outcomes for unseen genetic perturbations while respecting biological priors. Current graph‑based approaches often conflate stable gene relationships with response pathways, limiting their ability to capture intervention specificity.

## Implications
This work provides a framework that can be applied to drug combination testing and synthetic biology design, improving the reliability of virtual cell predictions without overfitting to network stability. Practitioners may adopt GeneGeoFlow’s geometry conditioning to obtain more accurate, perturbation‑aware models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06824v1)
