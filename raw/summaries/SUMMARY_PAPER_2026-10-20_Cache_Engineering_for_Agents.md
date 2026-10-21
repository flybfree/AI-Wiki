---
title: Cache Engineering for Agents
url: http://arxiv.org/abs/2610.28577v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_17-32-24Z_CacheEngineeringforAgents.md
generated_at: 2026-10-20 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "cache engineering" as a new paradigm for managing key-value (KV) cache in LLM agent serving, replacing the prior approach of "context engineering" that trims or summarizes conversation history. The authors propose direct cache operations—drop and repos—that allow agents to control their active KV cache without modifying the trajectory prefix or triggering costly re-prefilling. They co-design the AKV serving engine to handle the resulting stateful cache reuse challenges, demonstrating significant improvements in both benchmark accuracy and serving efficiency.

## Key Takeaways
- The paper identifies a fundamental flaw in context engineering: modifying the trajectory prefix to reduce cache size invalidates all subsequent cached states, forcing expensive re-prefilling of retained context and potentially degrading task accuracy when too little context is kept. Cache engineering sidesteps this by operating directly on the KV cache without altering the underlying token sequence.
- Two core cache operations are formalized: "drop" proactively excludes selected cached entries from future attention computations, and "repos" adjusts the position encodings of retained keys to maintain correct positional relationships. These operations enable fine-grained cache management independent of trajectory modification.
- The authors identify "history dependence" as a critical serving challenge: identical token sequences can produce different cache states depending on the sequence of cache operations applied, making traditional prefix-matching cache reuse strategies insufficient. The AKV serving engine addresses this with a stateless external API while internally managing stateful cache reuse, eviction, and restoration.
- Experimental results show a tool-response rolling-drop cache policy improves average benchmark scores by 1.7 points and reduces average cost by 27.7% compared to threshold-triggered summarization. AKV delivers up to 1.2x output throughput and 1.5x P95 request latency speedup, while recursive self-improvement of cache policies further reduces cost by 7.1% beyond expert-designed policies.

## Context
As LLM agents tackle increasingly complex tasks involving long observation-action trajectories, KV cache I/O and storage have become the dominant serving cost, and trajectories frequently exceed the model's maximum context window. The field has relied on context engineering techniques such as summarization and history trimming to manage this growth, but these approaches introduce re-prefill overhead and accuracy trade-offs. This paper reframes the problem from a trajectory-management perspective to a cache-management perspective, which represents a significant shift in how serving infrastructure is designed for agentic workloads.

## Implications
For practitioners deploying LLM agents at scale, cache engineering offers a path to substantially lower serving costs and higher throughput without sacrificing task accuracy, directly impacting the economics of agentic AI products. The AKV engine's stateless external interface means it can integrate with existing serving APIs, lowering adoption barriers for production systems. The finding that agents can recursively self-improve their own cache policies also suggests a future direction where serving infrastructure adapts autonomously, reducing the need for manual tuning by engineers and enabling more efficient long-horizon agent deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28577v1)
