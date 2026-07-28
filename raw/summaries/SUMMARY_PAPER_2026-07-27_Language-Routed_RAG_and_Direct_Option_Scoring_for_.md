---
title: Language-Routed RAG and Direct Option Scoring for Multilingual Financial QA: DS@GT at FinMMEval
url: http://arxiv.org/abs/2607.22841v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_18-31-11Z_Language_RoutedRAGandDirectOptionScoringforMultili.md
generated_at: 2026-07-27 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DS@GT, a retrieval‑augmented question answering system for multilingual financial exams that combines LangGraph routing with Retrieval‑Augmented Direct Scoring (RADS). By selecting language‑specific models and using a 30 209 entry knowledge base indexed with BGE‑M3 embeddings, the approach achieves strong performance across English, Spanish, Greek, Chinese, and Hindi.

## Key Takeaways
- Retrieval uses BGE‑M3 embeddings and FAISS indexing over a 30 209‑entry multilingual knowledge base; low‑resource languages benefit from weighted Reciprocal Rank Fusion to fuse per‑language and cross‑lingual indices.  
- Model selection is language‑routed: Qwen3‑14B for Arabic, Chinese, Hindi; Qwen2.5‑14B for English; Llama‑3.1‑8B for Greek, a routing derived from empirical ablations that reveal substantial performance gaps between languages.  
- Chain‑of‑thought prompting severely degrades Greek accuracy (90.7 % to 20.9 %), and enabling Qwen3’s default thinking mode collapses Arabic RADS performance to near‑chance levels.

## Context
This work tackles the gap in multilingual domain reasoning where retrieval infrastructure is limited, showing that generic NLP pipelines cannot capture language‑specific reasoning needs. It highlights how routing and scoring strategies can be tuned per language to improve factual accuracy.

## Implications
Practitioners should adopt language‑aware retrieval pipelines rather than relying on a single universal model. They must avoid chain‑of‑thought prompting for low‑resource languages like Greek, as it harms performance, and select scoring methods that align with each model’s behavior, especially in financial certification exams where structured reasoning is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22841v1)
