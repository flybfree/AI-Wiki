---
title: Where A Small Language Model Helps in Invoice Categorisation, Understood Through Embedding Geometry
url: http://arxiv.org/abs/2608.18033v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_17-28-01Z_WhereASmallLanguageModelHelpsinInvoiceCategorisati.md
generated_at: 2026-08-18 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper explores how a small language model (SLM) can be used to automatically categorise invoices into the correct General Ledger code. By analysing the pre‑trained embedding geometry of SBERT and DeBERTa, the authors show that these embeddings form anisotropic but locally isotropic clusters that align with vendor identity, achieving 0.96 accuracy on a single GPU fine‑tuned model. The results demonstrate strong generalisation even with only about 100 client‑specific invoices.

## Key Takeaways
- The embedding space of the financial corpus is globally anisotropic yet composed of locally isotropic clusters that reflect vendor identity, suggesting that similar vendors produce similar sentence embeddings.
- Fine‑tuning SBERT on a single GPU yields 0.96 classification accuracy, surpassing both zero‑shot LLMs and a vendor‑identity baseline, especially for rare or new categories.
- A structured input that would aid human readers does not improve SLM performance, indicating that the model relies more on underlying embedding geometry than surface formatting.

## Context
The study addresses a critical bottleneck in automated accounting: precise invoice classification. While large language models offer high accuracy, they incur high computational and privacy costs. Small language models provide a cost‑effective alternative but require understanding of their internal representation to optimise performance.

## Implications
For practitioners, the findings suggest that leveraging SBERT’s embedding geometry can deliver robust GL code assignment with minimal resources. The insight that input structure is less important than underlying embeddings may guide future design of user‑friendly interfaces for SLM deployment in finance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.18033v1)
