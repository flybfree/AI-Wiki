---
title: Divergent large language model predictions from convergent representations in ambiguous word pairs
url: http://arxiv.org/abs/2608.01816v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-26-45Z_Divergentlargelanguagemodelpredictionsfromconverge.md
generated_at: 2026-08-03 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how decoder‑only transformers resolve lexical ambiguity by analyzing three models of different sizes (GPT‑2‑Small, Llama‑3.2‑3B, Qwen2.5‑32B). It finds that internal representations diverge in middle layers then partially reconverge later, while next‑token prediction divergence peaks in the final layers despite low cosine similarity in embeddings.

## Key Takeaways
- Representations become maximally distinct in middle layers and only partially reconverge in late layers.  
- The KL divergence between next‑token predictions reaches its maximum in the final layers, indicating strong disagreement even when embedding space appears similar.  
- A single‑layer ablation shows that models achieve equivalent disambiguation despite qualitatively different layer‑wise vulnerabilities.

## Context
This work highlights a growing disconnect between how transformer embeddings cluster semantically and how those embeddings translate into model outputs, challenging the assumption that similarity in low‑dimensional space fully reflects semantic content. Understanding this dynamic is essential for advancing research on architecture behavior and interpretability.

## Implications
For practitioners relying on embedding‑based retrieval or clustering, late‑layer cosine similarity may not capture true semantic differences, suggesting a need for alternative evaluation metrics. The findings also inform broader efforts to make transformer models more transparent and to design systems that do not depend solely on surface representation similarity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01816v1)
