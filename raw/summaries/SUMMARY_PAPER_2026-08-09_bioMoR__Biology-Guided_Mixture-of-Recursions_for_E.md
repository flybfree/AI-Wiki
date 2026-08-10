---
title: bioMoR: Biology-Guided Mixture-of-Recursions for Effective Genomic Learning
url: http://arxiv.org/abs/2608.06727v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_02-44-11Z_bioMoR_Biology_GuidedMixture_of_RecursionsforEffec.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
bioMoR is the first framework that applies Mixture-of-Recursions to gene‑level and pathway‑level learning in high‑dimensional omics data. The authors report significant gains, with average macro‑F1 improving by 8.2 points and balanced accuracy by 7.1 points over a strong biology‑agnostic MoR baseline while using far fewer parameters.

## Key Takeaways
- bioMoR integrates three biological knowledge sources: graph‑based token embedding refinement, structural bias that steers self‑attention toward related tokens, and a graph‑aware router that decides recursion depth based on neighborhood information.  
- The framework reduces total parameters by 75 % and FLOPs by up to 58 % compared with non‑recursive Transformers, demonstrating efficiency gains without sacrificing performance.  
- Selected marker genes or pathways are returned as interpretable outputs, and token‑specific recursion depths expose how computation is allocated across the model.

## Context
Transformer models dominate omics analysis yet often over‑compute irrelevant features because they treat all tokens equally. bioMoR addresses this by aligning learning with biological structure, offering a principled way to allocate computational resources where they matter most.

## Implications
For researchers and industry practitioners, bioMoR provides a scalable template for integrating domain knowledge into neural architectures, enabling more accurate predictions while conserving compute. This approach could be extended to other fields where structured data and interpretability are valuable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06727v1)
