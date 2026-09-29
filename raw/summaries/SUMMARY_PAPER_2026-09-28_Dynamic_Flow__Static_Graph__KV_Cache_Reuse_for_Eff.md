---
title: Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs
url: http://arxiv.org/abs/2609.34727v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_09-29-25Z_DynamicFlow_StaticGraph_KVCacheReuseforEfficientLL.md
generated_at: 2026-09-28 23:09
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces a compute-storage co-design for efficient Key-Value cache reuse in on-device large language model serving specifically tailored for mobile Neural Processing Units. By addressing the constraints of static compilation and limited memory bandwidth inherent to mobile hardware, the proposed system achieves significant reductions in time-to-first-token latency compared to existing caching strategies that assume dynamic cloud environments.

## Key Takeaways
- The authors propose an intra-graph mechanism that maps selective KV recomputation onto statically compiled NPU execution graphs, effectively bridging the gap between algorithmic dynamicity and hardware staticity to enable efficient prefix and non-prefix reuse without violating compilation constraints.
- To overcome severe mobile memory and I/O bandwidth limitations, a hierarchical KV manager is introduced featuring a tree-hash-semantic hybrid structure alongside cost-aware prefetching and eviction policies that optimize data placement and retrieval efficiency.
- The design incorporates an inter-graph scheduler for dynamic programming-based chunk merging to minimize padding, combined with a two-dimensional pipeline that overlaps KV loading, rerotation, and storage operations with NPU execution, resulting in a 40-60% reduction in time-to-first-token latency across representative workloads.

## Context
On-device LLM inference is critical for privacy-preserving personal intelligence, yet mobile NPUs face distinct architectural challenges compared to cloud GPUs, particularly regarding static graph compilation and constrained memory hierarchies. This work addresses a significant gap in the literature by adapting KV cache optimization techniques, traditionally designed for dynamic cloud environments, to the rigid resource constraints of edge AI accelerators where assumptions about abundant bandwidth do not hold.

## Implications
These advancements enable more practical and responsive local LLM applications on smartphones and embedded devices, reducing reliance on cloud APIs while maintaining low latency for long-context interactions. Practitioners developing mobile AI frameworks can leverage these co-design principles to build scalable serving solutions that maximize hardware utilization within strict power and bandwidth budgets, fostering the growth of truly local-first personal intelligence ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34727v1)
