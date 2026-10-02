---
title: Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents
url: http://arxiv.org/abs/2610.02002v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_16-32-38Z_Mem___Non_DestructiveMemoryforLong_TermOrganizatio.md
generated_at: 2026-10-01 22:06
model: qwen3.6-35b-a3b
---

## Summary
Mem++ introduces a non-destructive memory framework for LLM agents that preserves entire documents with temporal metadata, shifting from write-time distillation to read-time selection to handle versioned organizational decisions effectively. By retaining all document versions without generative compression at ingestion, the system enables answering models to access the precise information available at specific points in time. Evaluations on OrgMemBench show Mem++ outperforms leading baselines by 8.0 to 13.1 points and achieves superior scores compared to standard RAG across multiple benchmarks.

## Key Takeaways
- Mem++ eliminates write-time distillation by storing every document in its entirety along with date and author metadata, ensuring that no information is lost or fixed before questions are asked; instead, it performs read-time selection to retrieve only documents relevant up to the temporal scope of a query.
- The framework demonstrates significant performance gains on the OrgMemBench organizational benchmark, surpassing the strongest memory baseline by margins ranging from

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02002v1)
