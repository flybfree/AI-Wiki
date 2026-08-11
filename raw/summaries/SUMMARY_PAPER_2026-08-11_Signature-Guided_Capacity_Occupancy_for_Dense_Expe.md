---
title: Signature-Guided Capacity Occupancy for Dense Expert Merging
url: http://arxiv.org/abs/2608.09201v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_07-16-10Z_Signature_GuidedCapacityOccupancyforDenseExpertMer.md
generated_at: 2026-08-11 13:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SigMerge, a structured capacity assignment framework for dense expert merging that addresses three unresolved decisions in existing methods: where to open layer capacity from cross‑expert conflict, who should occupy that capacity based on domain demand, and how to admit the resulting support without costly recipe search. On 21 paired settings across seven dense base merges and three model pools, SigMerge improves every setting by an average of 15 % and achieves the best average rank (1.67) among six merging methods.

## Key Takeaways
- Conflict signatures set each layer's capacity from cross‑expert conflict, providing a principled way to allocate limited slots where conflicts arise.
- Positive base‑merge deficits define each domain’s share of that capacity, ensuring that the merged model respects domain demand.
- A sequential occupancy rule admits each expert delta up to the resulting layer‑domain budget, enabling efficient admission without exhaustive search.

## Context
Dense expert merging is a key technique for combining specialized language models into a single checkpoint, but current approaches lack a systematic method for allocating limited capacity. This work contributes a clear algorithmic solution that can be applied across diverse model configurations and training regimes.

## Implications
For researchers, SigMerge offers a reusable framework that simplifies the design of dense merges and improves performance without extensive experimentation. For industry practitioners, it enables faster deployment of high‑quality merged models with predictable capacity allocation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09201v1)
