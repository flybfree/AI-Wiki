---
title: Where Should a Document Live: Context, Representations, or Parameters?
url: http://arxiv.org/abs/2609.17346v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-15_15-47-02Z_WhereShouldaDocumentLive_Context_Representations_o.md
generated_at: 2026-09-15 21:08
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper investigates how large language models should best incorporate new information, comparing context-based (KV-cache), parametric (fine-tuning), and latent representation methods across five knowledge-intensive benchmarks. The authors find that Cartridges, a KV-cache approach, consistently outperforms parametric adaptation in both oracle and multi-document retrieval settings, closely matching in-context learning while offering significant accuracy gains. However, the study also highlights that high-performing methods like Cartridges and full fine-tuning are susceptible to catastrophic forgetting, particularly in coding tasks.

## Key Takeaways
- In controlled oracle evaluations, KV-cache based Cartridges demonstrate superior accuracy across nearly all storage budgets, surpassing parametric adaptation methods by approximately 10 percentage points while maintaining efficient

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.17346v1)
