---
title: Time Present and Time Past: Benchmarking Large Language Models on Temporally Evolving Document Understanding
url: http://arxiv.org/abs/2608.08512v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_06-17-41Z_TimePresentandTimePast_BenchmarkingLargeLanguageMo.md
generated_at: 2026-08-10 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TIDE, a benchmark for answering questions about evolving documents such as laws and customs codes where correct answers depend on the version in force on a specific date. The study evaluates nine recent large language models across three evaluation protocols and finds that their macro‑averaged accuracy is only 68.5%, with version resolution reaching 59.7% and failure to reject outdated versions dropping to 26.7%.

## Key Takeaways
- TIDE provides the first expert‑verified dataset of 3,050 QA pairs spanning eight task types on code‑mixed customs documents issued between 1969 and 2025, highlighting the difficulty of temporal version resolution in real‑world legal texts.  
- Models are more inclined to produce confident parametric answers than to reject incorrect or outdated versions, indicating a bias toward answering rather than refusing when uncertain.  
- The hard date gate separating correct meaning from correct time reveals that only 26.7% of models correctly identify when supplied information no longer governs the query.

## Context
Temporal question answering remains an unsolved problem in AI because existing datasets treat time merely as metadata, not as a governing factor for answer validity. This work underscores the need for benchmarks that model version control and date‑specific semantics, which are critical for legal and regulatory applications where outdated statutes can have real consequences.

## Implications
For practitioners developing or deploying LLMs in regulated domains, TIDE’s results warn against assuming models will automatically respect temporal constraints without explicit training. The findings suggest that future systems must incorporate hard date checks and version validation to avoid providing misleading information.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08512v1)
