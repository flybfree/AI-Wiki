---
title: When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies
url: http://arxiv.org/abs/2608.25717v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_12-34-12Z_WhenRAGFailstoEqualize_Geo_biasinFactualQuestionAn.md
generated_at: 2026-08-26 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates whether retrieval-augmented generation (RAG) can equalize factual errors across public companies by comparing six LLMs on atomic attributes under various context conditions. It finds geographic disparities in accuracy when no context is provided and that even with perfect context the gaps persist, linking them to model knowledge and representation.

## Key Takeaways  
- No-context accuracy varies strongly by geography, showing uneven parametric knowledge among firms.  
- Retrieval gains are tied to baseline performance; models improve only where they already know the answer.  
- Misleading contexts cause models to copy false information, indicating retrieval can propagate errors rather than correct them.

## Context  
This study challenges the assumption that RAG universally fixes factual inaccuracies in large language models. By focusing on a real-world dataset of public companies, it reveals how geographic and representational biases affect model behavior beyond synthetic benchmarks.

## Implications  
For practitioners, this suggests that relying solely on retrieval may be insufficient without addressing underlying knowledge gaps or context quality. Industry adoption must consider both model size and the accuracy of retrieved information to avoid propagating incorrect data in factual QA tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25717v1)
