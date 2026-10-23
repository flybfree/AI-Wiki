---
title: Cache Engineering for Agents
url: http://arxiv.org/abs/2610.28577v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-20_17-32-24Z_CacheEngineeringforAgents.md
generated_at: 2026-10-22 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "cache engineering" as a new paradigm for managing key-value (KV) cache in LLM agent serving, replacing the prior approach of context engineering that trims or summarizes conversation history. The authors propose direct cache operations—drop and repos—that allow agents to control active cache without modifying the trajectory prefix or triggering costly re-prefilling. They co-design the AKV serving engine to handle the stateful nature of these operations and demonstrate significant improvements in both benchmark accuracy and serving efficiency.

## Key Takeaways
- The paper identifies a fundamental limitation of prior context engineering approaches: trimming or summarizing the trajectory prefix invalidates all subsequent cached states, forcing expensive re-prefilling of retained context. This creates a tension between reducing cache size and preserving task accuracy, since too aggressive trimming degrades agent performance while too little trimming fails to control costs.
- The proposed cache operations—drop (excluding selected cache entries from future attention) and repos (adjusting position encodings of retained keys)—allow agents to manage their active KV cache without altering the underlying trajectory. The authors formalize these operations and identify "history dependence" as a critical serving challenge: identical token sequences can produce different cache states depending on the sequence of cache operations applied, making naive prefix matching insufficient for correct cache reuse.
- The AKV serving engine provides a stateless external interface compatible with existing serving APIs while internally managing stateful cache reuse, eviction, and restoration. A tool-response rolling-drop cache policy improves average benchmark scores by 1.7 points and reduces average cost by 27.7% compared to conventional threshold-triggered summarization. With AKV, throughput improves up to 1.2x and P95 request latency sees a 1.5x speedup. Recursive self-improvement of cache policies further reduces cost by 7.1% beyond expert-designed policies.

## Context
As LLM agents tackle increasingly complex tasks involving long trajectories of observations and actions, KV cache I/O and storage have become the dominant serving cost, and trajectories frequently exceed the model's maximum context window. Prior solutions relied on context engineering—modifying the conversation history to reduce cache size—but this approach is fundamentally at odds with the prefix-caching optimizations that modern serving engines depend on. This paper represents a shift from treating the cache as a passive byproduct of the conversation to treating it as an actively managed resource, bridging the gap between agent-level reasoning needs and serving-engine-level efficiency constraints.

## Implications
For practitioners deploying LLM agents at scale, cache engineering offers a path to substantially lower serving costs and latency without sacrificing task accuracy, which is critical for production agent systems handling long-horizon tasks. The AKV engine's stateless API design means it can integrate with existing serving infrastructure, lowering the barrier to adoption. The finding that recursive self-improvement of cache policies outperforms expert-designed policies suggests a future direction where agents autonomously optimize their own memory management, potentially enabling more efficient and adaptive agent architectures across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28577v1)
