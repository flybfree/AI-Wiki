---
title: RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models
url: http://arxiv.org/abs/2609.02731v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_15-40-40Z_RVSD_RetrievalVisionSparseDecodingforMitigatingVis.md
generated_at: 2026-09-03 00:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RVSD, a training‑free and plug‑and‑play decoding framework that tackles visual hallucinations in large vision‑language models without requiring extra datasets or multi‑round processing. By unifying token sparsification with semantic‑space visual retrieval (SSVR), RVSD reduces computational load while improving reliability.

## Key Takeaways
- The semantics‑directed token selection strategy selectively sparsifies redundant tokens, preserving essential visual information during generation.  
- SSVR reformulates visual compensation as an on‑demand cross‑modal retrieval process within a shared semantic space.  
- RVSD achieves state‑of‑the‑art performance in mitigating visual hallucinations and maintains robust suppression even under long‑context generation.

## Context
Large vision‑language models excel at many tasks but are still vulnerable to visual hallucinations, which can degrade real‑world usefulness. Traditional fixes often involve costly data curation or additional training rounds, limiting practical deployment.

## Implications
RVSD offers a lightweight solution that can be integrated directly into existing pipelines, reducing overhead and enhancing model trustworthiness. This advancement is valuable for industry practitioners seeking reliable AI systems with minimal resource investment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02731v1)
