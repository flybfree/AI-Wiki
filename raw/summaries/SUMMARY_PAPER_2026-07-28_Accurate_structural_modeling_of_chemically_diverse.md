---
title: Accurate structural modeling of chemically diverse molecular interfaces with Vilya-2
url: http://arxiv.org/abs/2607.25156v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_00-01-54Z_Accuratestructuralmodelingofchemicallydiversemolec.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Vilya‑2, a diffusion transformer that models peptide-protein interfaces using an all‑atom representation, achieving sub‑2 Å RMSD for many peptide targets. It outperforms co‑folding models and works on new protein‑small molecule complexes as well as large macrocycles.

## Key Takeaways
- Vilya‑2 recovers 59.1% of peptide interfaces to sub‑2 Å backbone RMSD, surpassing a representative co‑folding model even when the bound receptor is provided.
- The all‑atom representation enables transfer learning across different molecular types and generalizes to novel protein‑small molecule complexes not seen in training.
- Vilya‑2 also models large macrocycles and disulfide‑stapled miniproteins, far exceeding the size of any molecule in its training set.

## Context
Current AI methods for protein design rely on co‑evolutionary statistics that work well for proteins but struggle with peptides due to non‑canonical residues. The all‑atom diffusion transformer addresses this gap by providing a unified framework for diverse chemical spaces.

## Implications
This model will accelerate de novo peptide drug discovery, allowing rapid generation of accurate structural ensembles and fine‑tuning for hit enrichment. It sets the standard for foundation models in molecular design across both peptides and small molecules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25156v1)
