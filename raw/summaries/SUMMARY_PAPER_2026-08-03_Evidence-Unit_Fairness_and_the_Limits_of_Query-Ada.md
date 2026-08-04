---
title: Evidence-Unit Fairness and the Limits of Query-Adaptive Sparse-Dense Fusion in Financial Document Retrieval
url: http://arxiv.org/abs/2608.00183v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_18-06-58Z_Evidence_UnitFairnessandtheLimitsofQuery_AdaptiveS.md
generated_at: 2026-08-03 23:46
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why sparse-dense hybrid retrieval struggles on financial filings and proposes segmenting documents to align encoder windows with evidence units. It finds that without segmentation the dense model misses most labeled evidence, reducing performance. On a corrected corpus fusing BM25 with a compact dense encoder raises Hit@10 by about 28 percent.

## Key Takeaways
- Retrieval units larger than the dense encoder’s input window cause the dense model to see only a small fraction of annotated evidence, which biases comparisons against full‑text sparse baselines.  
- Segmenting the corpus into encoder‑sized windows restores a fair comparison and yields a 28 percent improvement in Hit@10 when BM25 is fused with a compact dense encoder.  
- Simple fixed fusion outperforms three lightweight adaptive routers that were tested, indicating that per‑query weighting does not reliably capture additional headroom.

## Context
Financial document retrieval remains challenging because queries are short and contain many acronyms while answers reside in long, table‑dense filings. Retrieval systems often combine a fast sparse component with a dense encoder to balance speed and relevance. This work contributes to the broader effort of aligning model capabilities with real‑world data structures.

## Implications
Practitioners can improve retrieval accuracy on corporate filings by ensuring that encoding windows match evidence units rather than assuming full visibility. The finding that simple fusion is robust suggests that complex adaptive methods may be unnecessary for many applications, guiding resource allocation in industry pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00183v1)
