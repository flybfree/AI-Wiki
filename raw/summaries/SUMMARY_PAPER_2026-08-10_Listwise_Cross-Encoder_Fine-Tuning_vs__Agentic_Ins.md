---
title: Listwise Cross-Encoder Fine-Tuning vs. Agentic Instruction Tuning for LLM Rerankers: A Systematic Study in Medical Procedure Reranking
url: http://arxiv.org/abs/2608.09650v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_14-28-30Z_ListwiseCross_EncoderFine_Tuningvs_AgenticInstruct.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper compares two approaches to reranking medical procedures: a small cross‑encoder fine‑tuned with listwise learning and an instruction‑tuned large model using agentic optimization. On a dataset of 2,647 queries the 109M ListNet outperforms the 4B Qwen3‑Reranker by 2.6 NDCG@3 points and 13.3 Spearman correlation points while using far fewer parameters.

## Key Takeaways
- The 109M cross‑encoder achieves higher ranking quality than a 4B instruction model despite its smaller size.
- Listwise fine‑tuning with layer freezing yields better performance than prompt‑only optimization.
- The study demonstrates that parameter efficiency can match or exceed larger models in specialized medical retrieval.

## Context
Medical procedure reranking is essential for health insurance information systems where patients use lay language and clinicians rely on precise terminology. This work addresses the gap between clinical jargon and patient queries, showing how lightweight models can meet production needs without sacrificing accuracy.

## Implications
Practitioners can adopt listwise fine‑tuning to build domain‑specific rerankers that are both accurate and cost‑effective. The findings suggest a shift toward smaller, well‑tuned models over larger prompt‑only systems for tasks where parameter count matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09650v1)
