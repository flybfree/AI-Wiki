---
title: MGAL: A Multilingual Granularity-Aware Long-Context Benchmark
url: http://arxiv.org/abs/2608.20853v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_08-19-00Z_MGAL_AMultilingualGranularity_AwareLong_ContextBen.md
generated_at: 2026-08-23 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MGAL, a multilingual granularity‑aware long‑context benchmark built from UN reports in six languages ranging from 8K to 128K tokens. It evaluates LLMs across four linguistic granularities (word, sentence, paragraph, document) and three positions within the text, revealing that models excel at word‑level tasks but falter on coarser ones.

## Key Takeaways
- LLMs perform well on word‑level comprehension but struggle with higher granularity such as sentences or paragraphs.  
- Closed‑source models retain a clear advantage in lower‑resource languages, highlighting resource bias.  
- Models often follow surface cues like connectives rather than discourse roles when neighboring sentences share topics.

## Context
Long‑context evaluation remains limited to document level and high‑resource languages, hindering research on fine‑grained multilingual performance. This work expands the scope, offering a systematic test for granularity and position effects across six official UN languages.

## Implications
Practitioners must design models that handle both fluency and factual consistency, especially in low‑resource settings. The benchmark will guide future model development toward more robust long‑context understanding and equitable performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20853v1)
