---
title: Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers
url: http://arxiv.org/abs/2609.02702v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-06-46Z_TraceasState_ReasoningTracesasConditionalStatesfor.md
generated_at: 2026-09-02 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces “Trace as State,” a method that treats reasoning traces collected during long‑context tasks as textual proxies for hidden task state and inserts them before the context block on a fresh pass. The authors demonstrate that this placement reduces memory usage compared with providing the condition after the context, leading to significant performance gains across multiple models and datasets.

## Key Takeaways
- Providing task state early as a trace can cut exponential memory requirements for causal state update processors.  
- Inserting traces before the long‑context block improves exact match scores on GraphWalks Parents, raising DeepSeek V4 Pro Preview from 29.2% to 81.8% and GLM‑5.2 from 66.4% to 100.0%.  
- The approach outperforms the matched control “Trace Append” in 26 of 27 model‑task‑metric combinations.

## Context
Long‑context transformers struggle when reasoning depends on information discovered later, creating a mismatch between causal processing and stateful computation. This paper addresses that gap by modeling hidden states as textual traces, offering a lightweight alternative to traditional memory tricks.

## Implications
For practitioners, “Trace as State” enables more scalable long‑context models without sacrificing performance. The technique can be adopted in industry pipelines where resource constraints limit large memory footprints while maintaining high accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02702v1)
