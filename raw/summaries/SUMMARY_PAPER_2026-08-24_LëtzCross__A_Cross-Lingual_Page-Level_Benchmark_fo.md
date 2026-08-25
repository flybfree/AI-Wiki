---
title: LëtzCross: A Cross-Lingual Page-Level Benchmark for Multimodal Retrieval over Luxembourgish Documents
url: http://arxiv.org/abs/2608.21714v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_01-35-00Z_LëtzCross_ACross_LingualPage_LevelBenchmarkforMult.md
generated_at: 2026-08-24 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LëtzCross, a cross‑lingual page‑level retrieval benchmark built from Luxembourgish PDF documents where each page is indexed as an image and queries are provided in English, French, German, or Luxembourgish. The study compares OCR‑based text‑only retrievers with ColPali‑style page‑image retrievers and finds the latter outperform across all query languages. Fine‑tuning analysis shows that multilingual models, especially those including Luxembourgish, achieve the strongest results.

## Key Takeaways
- The benchmark demonstrates that visual retrieval benefits persist in low‑resource cross‑lingual settings, outperforming text‑only methods on both English and Luxembourgish queries.  
- Single‑language fine‑tuning yields best performance for French queries, while multilingual models with Luxembourgish inclusion markedly improve retrieval accuracy for native Luxembourgish queries.  
- The results highlight the importance of multimodal data (text + image) in RAG systems where document pages are richly visual.

## Context
Luxembourgish is a low‑resource language, and few datasets exist that evaluate cross‑lingual retrieval beyond simple translation tasks. This work addresses that gap by creating a page‑level benchmark that integrates both textual and visual cues, offering a realistic test for Retrieval‑Augmented Generation (RAG) systems in multilingual environments.

## Implications
For developers building RAG pipelines, the findings suggest prioritizing multimodal retrieval to capture document layout and visual information. Practitioners can leverage fine‑tuned multilingual models to serve diverse user queries without sacrificing performance on low‑resource languages like Luxembourgish.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21714v1)
