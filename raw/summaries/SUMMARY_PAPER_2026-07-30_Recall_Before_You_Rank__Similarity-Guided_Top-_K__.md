---
title: Recall Before You Rank: Similarity-Guided Top-$K$ Reuse for Efficient Long-Context Attention
url: http://arxiv.org/abs/2607.27692v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_05-25-23Z_RecallBeforeYouRank_Similarity_GuidedTop__K_Reusef.md
generated_at: 2026-07-30 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
ReTopK is a training‑free technique that speeds up dynamic Top‑K sparse attention by reusing historical query‑support decisions instead of recomputing scores each time. The method builds a bounded cache per head, retrieves the most similar past queries, merges their supports with a recent window, and reranks only this compact set using exact current scores. Experiments on contexts up to 128 K show ReTopK matches Exact Top‑K perplexity within 0.5 % while accelerating computation by over three times.

## Key Takeaways
- Historical retrieval decisions are reused across many queries, reducing the need for full‑history scoring and limiting cache drift through periodic exact refreshes.  
- The union of supports from similar cached queries plus a recent window creates a compact candidate set that preserves most of the attention mass without sacrificing quality.  
- ReTopK only selects indices to attend to; it does not reuse scores, weights, or outputs, keeping the full KV cache intact while improving speed.

## Context
Long‑context language models face a quadratic bottleneck when using exact Top‑K attention because each new query must score against all key‑value pairs. Approximate methods that rely on random sampling often degrade performance at scale, making ReTopK’s similarity‑guided reuse a practical solution for real‑world decoding pipelines.

## Implications
This work demonstrates that intelligent reuse of past decisions can dramatically reduce computational cost without compromising model quality, offering a template for efficient attention mechanisms in large language systems. Practitioners can adopt ReTopK to build faster inference services while maintaining high perplexity scores on long documents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27692v1)
