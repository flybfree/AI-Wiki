---
title: Train, Retrieve, or Both? A Four-Arm Head-to-Head for Correct Statutory Citation on the Ontario Residential Tenancies Act
url: http://arxiv.org/abs/2606.20359v1
type: paper-summary
date: 2026-06-18
source_paper: 2026-06-18_15-21-53Z_Train_Retrieve_orBoth_AFour_ArmHead_to_HeadforCorr.md
generated_at: 2026-06-18 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates four approaches to generating correct statutory citations from the Ontario Residential Tenancies Act: zero‑shot fine‑tuning, LoRA SFT‑only, RAG‑only, and a hybrid SFT+RAG. The results show that retrieval is indispensable for accurate citation, while a cheap bge‑small hybrid outperforms larger, specialized pipelines and reaches 0.481 exact‑match with no hallucinated citations.

## Key Takeaways
- Base models cannot cite the RTA and LoRA SFT‑only misrecalls sections; retrieval is essential to prevent hallucinations.
- The SFT+RAG hybrid achieves the highest score at 0.481 exact‑match while generating zero hallucinated citations, demonstrating that fine‑tuning plus retrieval yields a robust solution.
- A low‑cost bge‑small hybrid matches or exceeds performance of larger embedder and cross‑encoder reranker pipelines, indicating strong results without specialized models.

## Context
Legal question answering demands precise statutory citation, yet most AI systems hallucinate sections. Retrieval mechanisms help locate relevant law fragments, reducing errors. This study demonstrates that integrating fine‑tuning with retrieval can produce reliable citations on a specific Canadian act without relying on massive, domain‑specific language models.

## Implications
For practitioners building legal assistants, the hybrid approach offers an affordable and effective way to generate correct citations, eliminating the need for costly large retrieval models or extensive training data. This research supports the broader trend toward lightweight, accurate AI solutions in regulated domains where precision is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.20359v1)
