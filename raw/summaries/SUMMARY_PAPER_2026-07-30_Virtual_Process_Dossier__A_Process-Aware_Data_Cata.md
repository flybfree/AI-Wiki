---
title: Virtual Process Dossier: A Process-Aware Data Catalogue
url: http://arxiv.org/abs/2607.27840v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-20-46Z_VirtualProcessDossier_AProcess_AwareDataCatalogue.md
generated_at: 2026-07-30 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the Virtual Process Dossier (VPD), a knowledge‑graph based catalogue that records both data and workflow provenance for multi‑stage manufacturing processes. It enables downstream AI optimisation by clearly separating datasets generated at each step, while providing FAIR access to these resources.

## Key Takeaways
- The VPD ontology acts as the semantic core of the catalogue, defining precise concepts such as “step”, “dataset”, and “provenance” that ensure consistent interpretation across users.  
- The provenance framework automatically links ontology instances to production events, making both prospective and retrospective traceability explicit without manual annotation.  
- A user‑friendly interface visualises the knowledge graph, allowing operators to explore data lineage, filter by workflow stage, and retrieve FAIR‑compliant datasets.

## Context
Manufacturing AI systems increasingly rely on heterogeneous data generated at multiple operational stages, yet existing catalogues often lack provenance metadata. This gap hampers reproducibility and trust in optimisation pipelines that depend on isolated dataset versions.

## Implications
VPD offers a scalable solution for enterprises seeking transparent, auditable AI workflows, reducing the risk of data drift and compliance issues. By standardising provenance within the knowledge graph, it supports regulatory requirements and accelerates collaborative research across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27840v1)
