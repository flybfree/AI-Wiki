---
title: Which RAG Paradigm Wins at Scale? A Scaling Study of Retrieval-Augmented Generation Paradigms
url: http://arxiv.org/abs/2607.26497v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_05-46-11Z_WhichRAGParadigmWinsatScale_AScalingStudyofRetriev.md
generated_at: 2026-07-29 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts a controlled corpus‑scaling study of four retrieval‑augmented generation paradigms to reveal how their accuracy and cost evolve as the dataset grows. The results show that BM25 remains optimal across all scales, while other methods suffer from high token usage or limited performance.

## Key Takeaways
- BM25 defines the low‑cost end of the Pareto frontier at every measured tier and leads accuracy from mid‑scale onward without LLM‑based construction.  
- File‑System Agent matches or slightly exceeds BM25 at the smallest tiers but uses 39 times more query tokens per answer at the bedrock and falls nearly 20 points behind at full scale.  
- Graph‑based RAG hits a construction wall: its heaviest builders use up to 24.6 generative LLM tokens per indexed corpus token yet stop within the first 2% of the full corpus.

## Context
This study addresses the gap in evaluating RAG methods across varying data sizes, which is crucial for realistic deployment where resources and accuracy trade‑offs matter.

## Implications
For practitioners, the results suggest sticking with BM25 or hybrid retrieval‑augmented approaches avoids costly LLM token usage at scale; Graph‑based indexing may be impractical beyond tiny corpora. Industry should prioritize cost‑effective retrieval over complex graph structures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26497v1)
