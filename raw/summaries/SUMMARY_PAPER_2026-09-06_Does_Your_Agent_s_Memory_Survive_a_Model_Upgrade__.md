---
title: Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability
url: http://arxiv.org/abs/2609.05339v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_16-44-17Z_DoesYourAgent_sMemorySurviveaModelUpgrade_AControl.md
generated_at: 2026-09-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how memory survives when a language model is upgraded, using synthetic histories and two open‑weight models under ten billion parameters. It shows that certain memory representations transfer reliably while others degrade sharply after migration.

## Key Takeaways
- Fixed‑schema knowledge graphs (KG‑fixed) preserve accuracy almost unchanged after swapping writers, with only a tiny statistical shift of +0.0004 ± 0.0020.  
- Compressed natural‑language notes (NOTES) suffer large asymmetric errors: migration from raw to NOTES can drop accuracy by up to 13.28 percentage points, while the reverse gain is only about 9.91 points.  
- Retrieval‑augmented generation systems lose most of their benefit when using mixed embeddings; full re‑embedding yields an 11.90‑point improvement, whereas a 50/50 split captures just 4.96 points.

## Context
Memory migration is rarely handled automatically in model upgrades, leading to unexpected performance drops that are hard to diagnose. This study provides the first controlled comparison of how different memory formats interact with model version changes, offering empirical evidence for the challenges of preserving knowledge continuity.

## Implications
For practitioners, the findings stress the need for direction‑specific testing and strict embedding isolation when moving models. Retaining raw source histories is crucial for reliable repair, suggesting that future upgrades should prioritize preserving unprocessed data over compressed representations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05339v1)
