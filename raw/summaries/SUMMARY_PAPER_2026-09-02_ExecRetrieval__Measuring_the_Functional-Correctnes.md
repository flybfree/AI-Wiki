---
title: ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval
url: http://arxiv.org/abs/2609.01865v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_20-55-17Z_ExecRetrieval_MeasuringtheFunctional_CorrectnessGa.md
generated_at: 2026-09-02 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ExecRetrieval, a benchmark designed to measure whether code‑embedding retrieval can distinguish correct implementations from near‑clone buggy variants that are verified to fail execution. By pairing each canonical Python task with up to four single‑edit counterfactuals, the authors evaluate 23 embedding configurations and BM25, finding that top systems retrieve the correct code only about one third of the time at recall@1 while achieving perfect exec@10 performance. The results show that rank‑1 misses are overwhelmingly buggy variants and that canonical scores fall below distractors in a large fraction of queries.

## Key Takeaways
- ExecRetrieval creates a controlled pool of execution‑verified buggy code that is near‑identical to the correct implementation, enabling direct testing of functional discrimination rather than lexical similarity.  
- The top hosted retrieval systems achieve exec@10 = 1.00 but only exec@1 = 0.331, indicating they rank the correct code low despite perfect recall at a higher position.  
- Rank‑1 misses are paired buggy variants in 91.5–99.4% of cases and canonical scores are below distractors in 67–78% of queries across leading systems.

## Context
The paper addresses a longstanding gap in AI research where code retrieval benchmarks lack execution verification, limiting the ability to assess functional correctness. By introducing counterfactuals that preserve lexical similarity while breaking runtime behavior, ExecRetrieval provides a more realistic evaluation for coding agents and retrieval‑augmented generation systems.

## Implications
For developers building coding assistants, this benchmark underscores the need to prioritize functional accuracy over mere code similarity in retrieval pipelines. Practitioners can use these findings to design better embedding models or hybrid search strategies that reduce reliance on buggy distractors and improve overall system reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01865v1)
