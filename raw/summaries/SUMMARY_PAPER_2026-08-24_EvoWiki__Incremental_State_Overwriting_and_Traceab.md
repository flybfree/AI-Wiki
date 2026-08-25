---
title: EvoWiki: Incremental State Overwriting and Traceable Question Answering for Cross-Meeting Knowledge Evolution
url: http://arxiv.org/abs/2608.23265v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_13-52-17Z_EvoWiki_IncrementalStateOverwritingandTraceableQue.md
generated_at: 2026-08-24 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EvoWiki, an incremental question-answering system that models knowledge evolution across multiple meetings by explicitly tracking state changes and provenance. It separates offline BUILD construction from online READ processing to avoid storing conflicting facts and to retrieve only current valid states. Experiments on a bilingual CrossMeet benchmark show significant improvements in accuracy over prior methods.

## Key Takeaways
- EvoWiki uses entity version chains and a State‑Overwrite Protocol to distinguish current valid states from superseded history while preserving meeting-level provenance anchors.
- The READ phase performs deterministic entity addressing, temporal resolution, and cross‑entity multi‑hop aggregation instead of relevance‑based Top‑k retrieval.
- On six datasets and two reader models EvoWiki boosts macro‑average Judge Accuracy by 9.72 to 10.00 percentage points compared with the strongest baselines.

## Context
Long‑term knowledge collaboration often involves frequent revisions, yet most long‑context AI systems treat history as static or append‑only, leading to stale or contradictory information retrieval. This work addresses that gap by modeling dynamic state lifecycles and providing traceable answers across meetings.

## Implications
For practitioners, EvoWiki offers a framework to maintain factual consistency in collaborative environments such as research teams or customer support wikis. The approach could be adopted to improve reliability of AI assistants that must answer questions grounded in up‑to‑date, verifiable knowledge.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23265v1)
