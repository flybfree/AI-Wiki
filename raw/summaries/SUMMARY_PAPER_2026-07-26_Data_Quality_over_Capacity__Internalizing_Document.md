---
title: Data Quality over Capacity: Internalizing Documents into LoRA Adapters for Closed-Book QA
url: http://arxiv.org/abs/2607.21861v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_23-14-59Z_DataQualityoverCapacity_InternalizingDocumentsinto.md
generated_at: 2026-07-26 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper demonstrates that baking a closed‑book corpus directly into the weights of a 4‑bit Gemma model using LoRA adapters yields higher accuracy than relying on retrieval or expanding context windows. Across experiments from single documents to a 99‑document set, once adapter capacity is sufficient, data quality becomes the primary driver of performance, surpassing changes in rank, learning rate, or architecture.

## Key Takeaways
- A single curation pass that shortens gold answers to canonical 1–6 word spans and drops trivia raises closed‑book accuracy from 57.7 % to 85.7 % on a 15‑document corpus, outperforming any architectural tweak.
- Capacity is a hard gate: training data cannot improve results below a minimum adapter rank that scales with corpus size, and this trend couples inversely with learning rate.
- On the same 15‑document slice, an internalized LoRA adapter (84.2 % recall) beats both a BM25‑RAG pipeline (58.9 %) and a gold‑chunk oracle (65.6 %) at lower latency.

## Context
This work addresses a core limitation of large language models: their inability to answer questions about unseen or closed corpora without external retrieval. By internalizing knowledge, the approach reduces reliance on costly retrieval systems while maintaining low inference latency, aligning with trends toward efficient, self‑contained LLM deployments.

## Implications
For industry practitioners, embedding knowledge directly into model weights can lower costs and improve speed for specialized QA tasks where data privacy or latency constraints matter. The findings suggest that curating high‑quality training examples is more impactful than chasing higher LoRA ranks, guiding resource allocation in fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21861v1)
