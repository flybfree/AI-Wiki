---
title: WAKMan: Workload Aware KVCache Manager
url: http://arxiv.org/abs/2610.36355v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_22-19-37Z_WAKMan_WorkloadAwareKVCacheManager.md
generated_at: 2026-10-27 20:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
WAKMan is a workload-aware KV cache eviction policy manager designed for Large Language Model serving systems that use prefix caching to accelerate prefill computation. The paper demonstrates that no single eviction policy (such as LRU or frequency-based approaches) performs optimally across diverse production traffic mixes, and proposes a system that dynamically selects its eviction strategy from live traffic patterns without requiring knowledge of request types or prompt content. WAKMan achieves a 5 percentage point average improvement in cache hit rate over vLLM's default LRU policy while maintaining the lowest mean and worst-case optimality gap across all tested policies.

## Key Takeaways
- Production LLM traffic spans single-turn, multi-turn, agentic, and mixed request types, and these different workloads have fundamentally different caching characteristics: agentic steps return within seconds and favor recency-based eviction, while popular prompts and long conversations return after many intervening requests and favor frequency-based eviction. This means a static policy cannot serve all traffic patterns well.
- Across 20 tested workload mixes, vLLM's default LRU strategy provides 12% higher cache hit rates than the frequency-oriented S3FIFO policy on agentic-heavy mixes but trails it by up to 22% on other mixes. Even a single workload parameter can flip which policy wins for a particular mix, demonstrating the fragility of fixed eviction strategies in heterogeneous production environments.
- WAKMan operates without knowing request types or reading prompts, instead inferring the appropriate eviction policy from live traffic signals. It improves hit rate over LRU by 5 percentage points on average and achieves the lowest mean and worst-case optimality gap of all evaluated policies, making it a robust general-purpose solution for production KV cache management.

## Context
Prefix caching has become a critical optimization in LLM serving infrastructure, allowing servers to reuse Key-Value states across requests that share common prompt prefixes, thereby reducing both latency and serving cost. As LLM deployments scale to handle diverse workloads including chatbots, agentic pipelines, and long-document processing, the KV cache eviction policy becomes a decisive bottleneck that determines whether prefix caching actually delivers its theoretical benefits. This paper addresses a gap in the serving systems literature by treating workload heterogeneity as the central challenge rather than assuming a uniform traffic pattern.

## Implications
For practitioners operating LLM serving infrastructure, WAKMan suggests that hardcoding a single eviction policy like LRU in serving frameworks such as vLLM introduces significant and workload-dependent performance losses that can reach 22% in cache hit rate. The workload-aware approach points toward a future where serving systems incorporate lightweight online policy selection mechanisms, reducing the operational burden on engineers who must currently tune cache policies per deployment. For the broader field, this work highlights that cache management in LLM serving is not a solved problem and that adaptive, inference-free policy selection is necessary to handle the growing diversity of agentic and conversational workloads in production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36355v1)
