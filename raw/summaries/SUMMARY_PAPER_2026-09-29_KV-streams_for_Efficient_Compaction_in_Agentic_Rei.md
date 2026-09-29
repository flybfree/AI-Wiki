---
title: KV-streams for Efficient Compaction in Agentic Reinforcement Learning
url: http://arxiv.org/abs/2609.35750v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_17-57-42Z_KV_streamsforEfficientCompactioninAgenticReinforce.md
generated_at: 2026-09-29 01:51
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces KV-streams, a novel compaction mechanism designed to address GPU memory bottlenecks in agentic reinforcement learning by enabling efficient handling of long context traces without sacrificing training throughput. By streaming the key-value cache forward rather than flushing it during compaction, KV-streams achieve significant speedups ranging from 2.6x to 5x across multiple strategies while maintaining model performance and allowing the cache to function as a recurrent state for retaining historical information.

## Key Takeaways
- KV-streams provide a plug-and-play optimization that drastically improves training efficiency by streaming the KV cache forward instead of flushing it after compaction, thereby eliminating the costly prefilling operations associated with traditional methods and delivering wall-clock speedups between 2.6x and 5x across three different compaction strategies.
- The streamed KV cache naturally functions as a recurrent state that preserves information from contexts that have long since been removed; controlled experiments reveal that reinforcement learning alone is sufficient for this memory behavior to emerge, challenging prior assumptions about the necessity of additional architectural components for such retention.
- The method is lightweight

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35750v1)
