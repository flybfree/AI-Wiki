---
title: PhaseShift: Topology-Aware Data Harmonization and Model Consolidation Across Signalized Intersections
url: http://arxiv.org/abs/2608.25275v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_01-22-49Z_PhaseShift_Topology_AwareDataHarmonizationandModel.md
generated_at: 2026-08-26 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PhaseShift, a topology‑aware framework that harmonizes heterogeneous traffic data from multiple intersections into a single reusable model backbone. The authors demonstrate that the pooled model reduces both average absolute deviation (ADE) and false detection error (FDE) compared with locally trained models across five Florida sites, achieving median improvements of 36.8 % in ADE and 22.0 % in FDE at a 10‑second horizon.

## Key Takeaways
- The framework creates an ego‑relative coordinate system that removes site‑specific conventions while preserving topology through normalized signal context and variable‑cardinality interaction tokens.  
- A single pooled backbone trained on balanced field data outperforms individual local models, lowering minADE and minFDE at all tested intersections.  
- Leave‑one‑intersection‑out deployment improves performance on four of five sites, especially under a fixed 100 k‑window budget, indicating effective cross‑site consolidation.

## Context
PhaseShift addresses the fragmentation problem in traffic‑behavior modeling where each intersection is trained independently, limiting knowledge sharing and increasing computational cost. By adopting an actor‑centric representation that abstracts away physical site details, the work aligns with broader AI trends toward unified, transferable representations across heterogeneous domains.

## Implications
For industry practitioners, PhaseShift offers a scalable solution to consolidate large portfolios of traffic models into one efficient backbone, reducing training time and deployment complexity. Practitioners can leverage this approach to improve real‑time decision support while maintaining adaptability for sites that still require fine‑tuning, thereby advancing both research and operational traffic management systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25275v1)
