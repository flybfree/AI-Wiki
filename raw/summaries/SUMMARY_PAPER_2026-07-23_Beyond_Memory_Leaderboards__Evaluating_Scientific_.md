---
title: Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration
url: http://arxiv.org/abs/2607.16848v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientificMemor.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces two full‑text scientific memory benchmarks, Public AI Memory and Public Transformers, to evaluate how LLM agents restore evidence from research papers under realistic constraints. By comparing eight retrieval systems—including Theoria and a no‑retrieval baseline—the authors demonstrate that leaderboard rankings are highly sensitive to the evaluation protocol; for instance, Graphiti’s advantage vanishes when retrieval budget is fixed, while hybrid methods outperform pure approaches on PTr after controlling for context size.

## Key Takeaways
- Memory leaderboards require full protocol details such as ingestion granularity and raw‑text preservation, otherwise results are misleading.  
- Controlling the retrieved context budget dramatically changes performance, showing that Graphiti’s lead disappears under a 2.6 M character limit.  
- Hybrid retrieval strategies (e.g., sparse‑dense) become most effective when combined with BM25, yielding top scores within a narrow margin.

## Context
The study highlights a gap in current memory benchmarking, which often ignores the budget and modality of context restoration needed for scientific reasoning tasks. This limitation obscures true capabilities of retrieval‑augmented models in complex knowledge retrieval scenarios.

## Implications
For researchers and industry practitioners, adopting protocol‑aware evaluation will lead to more reliable comparisons and guide the design of memory systems that respect resource constraints. The released datasets and tools enable reproducible research, fostering trustworthy progress toward robust scientific recall.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16848v1)
