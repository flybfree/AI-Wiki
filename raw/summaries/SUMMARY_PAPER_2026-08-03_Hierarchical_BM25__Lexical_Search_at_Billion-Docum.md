---
title: Hierarchical BM25: Lexical Search at Billion-Document Scale
url: http://arxiv.org/abs/2608.00229v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_19-18-37Z_HierarchicalBM25_LexicalSearchatBillion_DocumentSc.md
generated_at: 2026-08-03 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Hierarchical BM25, a memory‑efficient retrieval system designed for one‑billion‑document corpora where flat indexing is infeasible due to size and latency constraints. By replacing exact ranking with a coarse index that selects a limited set of topical groups, the approach achieves sub‑second query times while keeping the resident footprint around 4.4 GB.

## Key Takeaways
- The resident coarse index selects ~1K topical, size‑balanced document groups using both total term frequency and co‑occurrence signals for informative terms.
- Exact top‑k ranking is abandoned in favor of fixed latency (~300 ms) and a memory footprint independent of corpus size.
- Sixteen‑term queries over one billion documents return in ~300 ms, delivering 4.7× to 5.6× the throughput of a flat multi‑threaded index.

## Context
Large‑scale lexical search remains a bottleneck for AI applications that require real‑time relevance at massive scale, where storing billions of documents is impractical and disk latency is unacceptable. This work addresses those constraints with a novel hierarchical structure that balances memory use and response time.

## Implications
Industries can deploy scalable retrieval services without the prohibitive cost of full‑size indexes, enabling interactive applications such as search engines and recommendation systems to operate at billions of documents while meeting user latency budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00229v1)
