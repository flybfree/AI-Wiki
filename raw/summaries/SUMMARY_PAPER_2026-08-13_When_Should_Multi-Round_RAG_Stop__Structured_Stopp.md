---
title: When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1
url: http://arxiv.org/abs/2608.13237v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-42-48Z_WhenShouldMulti_RoundRAGStop_StructuredStoppingJud.md
generated_at: 2026-08-13 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a structured stopping policy for multi-round RAG that reduces the number of retrieval calls while maintaining answer accuracy. By training a Qwen3.5-2B judge on HotpotQA data, the method integrates sufficiency-and-gap judgments into Search-R1’s pipeline and achieves a 77‑call reduction.

## Key Takeaways
- The structured judge cuts retrieval calls by 77 (3.70 %) relative to Native Search‑R1.
- Official Exact Match scores decrease by 0.625 percentage points on the test set.
- These results do not imply unchanged or improved accuracy, safe stopping, or lower total inference cost.

## Context
Multi-round RAG is inherently sequential; early stop decisions influence later stages and can degrade performance. This work addresses that challenge with a structured judgment framework, offering a practical way to manage search budget across rounds.

## Implications
Lowering retrieval calls reduces latency and operational expense without sacrificing much answer quality, encouraging practitioners to adopt structured stopping policies in production RAG systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13237v1)
