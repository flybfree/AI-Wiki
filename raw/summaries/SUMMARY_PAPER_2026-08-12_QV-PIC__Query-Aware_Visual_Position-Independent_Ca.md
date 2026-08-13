---
title: QV-PIC: Query-Aware Visual Position-Independent Caching for Efficient RAG Serving
url: http://arxiv.org/abs/2608.12121v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_14-40-43Z_QV_PIC_Query_AwareVisualPosition_IndependentCachin.md
generated_at: 2026-08-12 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces QV-PIC, a query‑aware dual‑resolution Position‑Independent Caching framework that tackles the quality gap between visual and textual PIC in Retrieval‑Augmented Generation. By compiling visual caches under the model’s native chat template offline and using cumulative relevance scores online, QV-PIC restores fine‑grained text evidence while preserving low‑resolution global context, achieving a 21.6‑point F1 gain over vanilla rendered‑image PIC and an 83.8 % reduction in TTFT compared to full prefill.

## Key Takeaways
- Rendering text chunks as images reduces token volume but introduces severe quality degradation due to contextual mismatches between independently compiled caches and loss of fine‑grained textual evidence during visual compression.
- Existing PIC repair methods address the mismatch through selective recomputation, which incurs online computation time and cannot recover lost textual details.
- QV-PIC compiles visual caches under the model’s native chat‑template prefix offline, preserving global context at low resolution while restoring fine‑grained textual evidence within a high‑resolution budget using cumulative query relevance scores.

## Context
RAG systems repeatedly reuse precomputed Key‑Value pairs across queries, yet large token volumes limit this benefit. Visual compression offers efficiency gains but suffers from quality loss; existing solutions either sacrifice performance or add costly online recomputation. This paper bridges the gap by aligning visual caches with model templates and leveraging relevance‑driven reconstruction.

## Implications
For AI practitioners, QV-PIC demonstrates that query‑aware caching can dramatically cut response latency while maintaining high retrieval accuracy, offering a scalable path to more efficient RAG deployment. The approach reduces operational costs and improves user experience, encouraging adoption across large‑scale generative applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12121v1)
