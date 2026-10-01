---
title: Linguistic Loopholes in LLM Unlearning: From a 174-Language Benchmark to Coverage-Aware Unlearning
url: http://arxiv.org/abs/2609.40286v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_17-48-13Z_LinguisticLoopholesinLLMUnlearning_Froma174_Langua.md
generated_at: 2026-09-30 22:15
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the "cross-lingual loophole" in large language model unlearning, where forgetting a fact in one language fails to remove it when queried in another or via paraphrasing. The authors propose language budgeted multilingual unlearning and introduce COVER, a method that selects an optimal subset of source languages to maximize erasure across all languages while minimizing damage to unrelated capabilities. Experiments show COVER significantly reduces residual access to forgotten knowledge compared to uniform selection, validated on both synthetic benchmarks and real low-resource news data.

## Key Takeaways
- Unlearning a fact is not language-agnostic; changing the query language or answer language can reopen forgotten knowledge, creating a cross-lingual loophole. To study this, the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40286v1)
