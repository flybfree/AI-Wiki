---
title: HopRefusalBench: Diagnosing Refusal Failures in Search-Augmented Agents for Multi-Hop Reasoning
url: http://arxiv.org/abs/2608.01358v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_16-20-55Z_HopRefusalBench_DiagnosingRefusalFailuresinSearch_.md
generated_at: 2026-08-03 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HopRefusalBench, a benchmark for diagnosing refusal failures in search-augmented agents on multi-hop reasoning tasks. It shows that even state-of-the-art models stop only about half the time with correct reasons and often produce hallucinated or budget-exhausted outputs instead of proper non‑answers.

## Key Takeaways
- The benchmark reveals that root and middle items are harder to refuse than terminal items, indicating difficulty in intermediate reasoning validation. 
- All models achieve higher target‑aware correct halting rates on false premise questions than on underspecified ones, suggesting better handling when premises are clearly wrong. 
- Despite explicit refusal responses, 84.7–98.4% correctly identify the rationale, pointing to a bottleneck in committing to non‑answers rather than generating them.

## Context
Search‑augmented language models rely on external retrieval to answer complex questions, yet their reliability when a question is fundamentally unanswerable remains unexplored. This work fills that gap by systematically measuring refusal behavior across multiple failure modes.

## Implications
For practitioners, HopRefusalBench provides concrete metrics and diagnostic tools to improve model trustworthiness in production pipelines. It also highlights the need for better mechanisms to commit to non‑answers rather than hallucinate or exhaust search budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01358v1)
