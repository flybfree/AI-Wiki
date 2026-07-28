---
title: Reasoning or Memorization: Can LLMs Understand and Generate Chinese Xiehouyu Riddles?
url: http://arxiv.org/abs/2607.23440v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_03-39-29Z_ReasoningorMemorization_CanLLMsUnderstandandGenera.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether large language models can understand and generate Chinese xiehouyu riddles, a traditional game that relies on wordplay rather than factual knowledge. By creating novel xiehouyu that have never appeared in training data, the authors avoid contamination from existing examples and measure memorization versus reasoning using delta accuracy (Δacc) between low‑frequency and new items. The study also tests free‑form explanation generation and human rating of AI‑created riddles.

## Key Takeaways
- Frontier Chinese models achieve a Δacc of 23.6% on novel xiehouyu, far above the low baseline for native speakers, indicating they have memorized many rare terms rather than truly reasoning about them.  
- English‑centric frontier models show only a mean Δacc of 5.1%, suggesting their Chinese knowledge is limited compared to dedicated Chinese training data.  
- AI‑generated xiehouyu receive lower human ratings than those produced by humans, highlighting that current LLMs struggle with creative linguistic tasks despite high accuracy scores.

## Context
Understanding how language models handle culturally specific and low‑frequency content like xiehouyu is crucial for evaluating their reasoning capabilities beyond memorization. The paper contributes to the debate on whether LLMs can truly grasp nuanced linguistic games or merely recall patterns from massive datasets, especially in non‑English languages.

## Implications
For developers, this research warns that performance metrics such as Δacc may reflect data bias rather than genuine comprehension. Practitioners should be cautious about extrapolating reasoning abilities across languages and should consider human evaluation alongside automated scores when assessing model creativity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23440v1)
