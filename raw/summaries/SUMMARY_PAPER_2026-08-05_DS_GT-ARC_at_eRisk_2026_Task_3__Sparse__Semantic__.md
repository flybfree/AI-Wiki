---
title: DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences
url: http://arxiv.org/abs/2608.03883v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-19-22Z_DS_GT_ARCateRisk2026Task3_Sparse_Semantic_andLLMRe.md
generated_at: 2026-08-05 01:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents the submissions for eRisk 2026 Task 3, which aims to rank Reddit sentences by their relevance to each of the 18 adult ADHD symptoms measured in ASRS‑v1.1. The authors report that an LLM‑based reranker achieved the highest official scores, followed by a prototype query‑expansion pipeline, indicating that staged retrieval with semantic and language‑model refinements is effective.

## Key Takeaways
- The absence of annotated training data forced reliance on zero‑shot experiments, manual validation, and weakly guided retrieval pipelines.  
- Combining sparse BM25 retrieval with evidence‑aware rescoring for self‑referential symptom reports improves candidate selection.  
- LLM reranking outperformed other methods and aligned closely with expert top‑10 rankings, supporting staged retrieval as a promising approach.

## Context
The task highlights the challenge of medical symptom detection in unstructured social media text where labeled data are scarce. Staged retrieval pipelines that leverage both traditional sparse mechanisms and modern large language models address this gap by balancing scalability with semantic precision.

## Implications
For practitioners developing clinical AI tools, this work demonstrates that integrating LLM rerankers into retrieval systems can yield significant performance gains without extensive annotation. The approach may be adapted to other symptom‑based or mental‑health screening tasks where interpretability and relevance are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03883v1)
