---
title: FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery
url: http://arxiv.org/abs/2607.25276v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-26-26Z_FunnelAL_Retrieve_then_RankActiveLearningforSingle.md
generated_at: 2026-07-28 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
FunnelAL introduces a retrieve-then-rank active learning framework designed for single‑class discovery. The system outperforms existing methods in both final classification quality and annotation efficiency on three image benchmarks, especially when annotator errors are present.

## Key Takeaways
- FunnelAL achieves the highest final F1 score among all evaluated approaches while using the fewest annotation rounds.  
- Its multi‑stage pipeline—embedding retrieval, precision‑triggered ranking with RankNet, and committee‑based exploration—maintains high accuracy even when annotators make mistakes.  
- Compared to classic uncertainty‑based methods, FunnelAL degrades two to three times slower under realistic labeling errors.

## Context
Active learning seeks to minimize human annotation effort by iteratively selecting informative samples. Single‑class discovery is challenging because embeddings often fail to separate positives from negatives, and large corpora make sampling inefficient. Prior work typically treats selection as a single stage, limiting performance when data quality varies.

## Implications
FunnelAL bridges the gap between industrial recommender architectures and active learning, offering a scalable pipeline for real‑world applications such as medical imaging or autonomous inspection. Practitioners can reduce annotation costs without sacrificing accuracy, making high‑quality discovery feasible at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25276v1)
