---
title: HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA
url: http://arxiv.org/abs/2608.13004v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_09-24-48Z_HybridRAG_BN_ARetrieval_AugmentedFrameworkwithFine.md
generated_at: 2026-08-13 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
HybridRAG-BN introduces a retrieval‑augmented framework for Bangla knowledge‑base question answering that combines BM25 and BGE‑M3 hybrid search, generates answers with the GGUF version of Gemma‑4‑31B‑Instruct, and verifies them using a LoRA‑fine‑tuned Gemma model. The system also employs fallback replacement and DuckDuckGo assistance to handle unresolved cases. Experiments on public and private leaderboards achieve token‑level F1 scores of 0.71654 and 0.72912, respectively, placing the model first.

## Key Takeaways
- HybridRAG-BN leverages both BM25 and BGE‑M3 to improve retrieval coverage for Bangla queries, addressing limited language resources.  
- The answer generation relies on a GGUF‑compressed Gemma‑4‑31B‑Instruct model, enabling efficient inference while maintaining high quality.  
- A LoRA fine‑tuned version of the same model is used for verification and refinement, ensuring factual consistency.

## Context
This work contributes to low‑resource language AI by demonstrating that large‑language models can be effectively adapted with lightweight LoRA updates for specific tasks like Bangla KBQA. The integration of hybrid retrieval mechanisms shows promise for augmenting weak language resources without extensive annotation.  

## Implications
For practitioners, HybridRAG-BN offers a template to combine efficient retrieval and verification in multilingual QA pipelines. In industry, the approach reduces reliance on massive annotated datasets while maintaining high accuracy, supporting scalable deployment of knowledge‑base assistants in Bengali‑speaking markets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13004v1)
