---
title: HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification
url: http://arxiv.org/abs/2608.07204v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_13-19-40Z_HNR_DAC_Hard_NegativeRerankingandDistribution_Alig.md
generated_at: 2026-08-09 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HNR-DAC, a two‑stage framework for scientific claim verification that addresses the intertwined problems of evidence confusability and classifier inference on retrieved paragraphs. On the NLPCC 2026 Task 10 Track 2 benchmark, the final configuration achieves 97.21% Hit@3, 95.79% Macro‑F1, and an average score of 95.13%, ranking third overall while delivering the highest Macro‑F1 of 93.05%.

## Key Takeaways
- HNR quantifies evidence confusability by measuring how non‑gold paragraphs resemble genuine evidence using a base reranker’s scores, thereby identifying the most confusable candidates to contrast with gold evidence.  
- DAC trains on the Top‑1 paragraph produced by the same frozen HNR used for inference, ensuring that the classifier sees only the evidence it will actually encounter at test time.  
- The final model outputs both the classification decision and a set of three paragraph identifiers (Top‑3), providing higher precision than single‑paragraph predictions.

## Context
Scientific claim verification is essential for extracting reliable knowledge from large corpora, yet current methods struggle with intra‑paper distractors that mimic genuine evidence. This paper contributes to AI research by integrating retrieval quality assessment directly into the classification pipeline, moving beyond static classifiers toward adaptive, data‑driven systems.

## Implications
For researchers and industry practitioners, HNR-DAC demonstrates a practical path to higher accuracy in domain‑specific verification tasks, reducing false positives that could propagate errors. The approach can be adapted to other knowledge extraction problems where evidence quality directly impacts downstream decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07204v1)
