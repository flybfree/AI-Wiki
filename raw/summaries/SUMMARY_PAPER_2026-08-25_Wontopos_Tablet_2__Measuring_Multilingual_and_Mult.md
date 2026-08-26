---
title: Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching
url: http://arxiv.org/abs/2608.23920v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-54-08Z_WontoposTablet2_MeasuringMultilingualandMultimodal.md
generated_at: 2026-08-25 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates a long‑term memory engine called Tablet‑2 that retrieves information without using lexical matching or language models, measuring both multilingual and multimodal recall on established benchmarks. It achieves high scores on LongMemEval‑S (95.7 %) and BEAM‑1M (67.5 %), while also showing strong cross‑lingual performance on captionless photographs across 14 languages.

## Key Takeaways
- The engine’s recall is highly sensitive to minor changes in query sampling intervals, moving only a few points when the reader moves or the re‑ask budget changes, indicating that reported scores are not stable.  
- Lexical methods such as BM25 fail dramatically on captionless images, reaching 19 % mean recall@5 where Tablet‑2 reaches 95 %, highlighting the advantage of non‑lexical retrieval.  
- Low‑resource languages like Swahili and Telugu suffer sharp degradation (53 % and 64 % respectively), and adding captions reduces cross‑lingual accuracy by about 11 points, whereas omitting a stage costs 37 points in Korean top‑1 recall.

## Context
This work contributes to the growing interest in long‑term memory retrieval for large language models, especially when lexical cues are unavailable. By demonstrating that non‑lexical pathways can outperform traditional methods on multimodal data, it challenges assumptions about the necessity of keyword scoring and highlights the importance of robust cross‑lingual performance.

## Implications
For industry practitioners, Tablet‑2 suggests that building retrieval systems without relying on lexical matching may be more effective for diverse user bases. Practitioners should focus on stable evaluation metrics and consider language‑specific tuning to mitigate degradation in low‑resource settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23920v1)
