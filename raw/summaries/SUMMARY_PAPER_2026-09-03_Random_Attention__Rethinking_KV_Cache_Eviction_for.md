---
title: Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning
url: http://arxiv.org/abs/2609.03430v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_06-38-38Z_RandomAttention_RethinkingKVCacheEvictionforEffici.md
generated_at: 2026-09-03 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Random Attention as a method for evicting tokens from the KV cache in large language models without computing any relevance scores. It demonstrates that randomly discarding tokens within each attention head yields performance comparable to top-scoring selectors while significantly improving throughput. Experiments across four models and six reasoning tasks confirm this approach matches the strongest prior evictor.

## Key Takeaways
- The prompt is fragile; most of the gap between selectors lies in whether their random draw happens to keep it, indicating selection signals are largely noise.
- Reasoning traces protect against eviction through redundancy: text restates needed information and attention heads maintain separate copies, so a random selection can retain enough copies without scores.
- Random Attention achieves 32‑43% higher throughput than vLLM’s current implementation while matching the strongest prior evictor across multiple models.

## Context
Current KV cache management is dominated by score‑based selectors that rely on uncertain estimates of future importance, creating bottlenecks for long reasoning tasks. This work challenges the assumption that such scores are necessary, highlighting the role of redundancy and randomness in maintaining model state.

## Implications
For practitioners deploying LLM inference at scale, Random Attention offers a low‑overhead alternative to complex scoring pipelines, enabling higher throughput with minimal code changes. The insight that redundancy can substitute for precise selection signals may inspire future cache strategies beyond attention heads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03430v1)
