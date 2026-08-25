---
title: When Names Cross Scripts: A Source-Grounded Benchmark for Historical Entity Reconciliation in the Mongol World
url: http://arxiv.org/abs/2608.23507v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_17-10-36Z_WhenNamesCrossScripts_ASource_GroundedBenchmarkfor.md
generated_at: 2026-08-24 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MHER, a provenance‑controlled benchmark for reconciling person names across languages and scripts in the Mongol world. Experiments on five generative systems show that adding source‑grounded evidence boosts test accuracy from 12.96 % to up to 94.44 %, while name‑only inputs fail completely on many cases.

## Key Takeaways
- Source‑grounded evidence dramatically improves identity resolution, raising accuracy by over eight percentage points compared with name‑only input.
- Historical descriptions often contain critical identity information that models can exploit when provenance is available.
- Restoring surface forms can backfire for some models, causing false merges even when the context is correct.

## Context
Historical NLP struggles with entity reconciliation because names appear under varied scripts and transcription traditions. This work provides a controlled dataset to study how provenance‑controlled evidence influences model decisions in such complex scenarios.

## Implications
Practitioners can use MHER to evaluate whether their models correctly incorporate source evidence rather than relying solely on surface strings. The findings highlight the need for provenance‑aware design in historical NLP applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23507v1)
