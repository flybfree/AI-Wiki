---
title: Carryover Drafting: Recycling Rejected States for Speculative Decoding
url: http://arxiv.org/abs/2609.14717v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-13_18-20-31Z_CarryoverDrafting_RecyclingRejectedStatesforSpecul.md
generated_at: 2026-09-15 03:31
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces Carryover Drafting, a novel approach to speculative decoding that recycles discarded hidden states from rejected tokens during the target model's forward pass. By treating these previously wasted representations as temporary key-value context for subsequent drafting rounds, the method enhances draft quality without altering existing interfaces. Experimental results demonstrate significant improvements in token acceptance rates and end-to-end inference speedups across multiple models and tasks.

## Key Takeaways
- Conventional speculative decoding wastes computational resources by discarding hidden states associated with rejected tokens, yet these discarded representations contain valuable predictive information that can be leveraged to improve future draft quality.
- The proposed Carryover Drafting mechanism recycles rejected target hidden states as a bounded temporary KV context, requiring only a single learned embedding to differentiate them from committed context while maintaining low inference overhead.
- A novel parallel draft--verify--draft training strategy successfully exposes the drafter to inference-aligned rejected states without sacrificing training parallelism, yielding 6.5–14.7% higher acceptance lengths and up to 28.8% speedup improvements in translation tasks.

## Context
Speculative decoding has emerged as a leading technique for accelerating large language model inference by reducing the number of sequential forward passes required. However, current implementations fundamentally ignore the computational work spent evaluating rejected tokens, representing a significant inefficiency in modern LLM serving pipelines. This research addresses a critical gap between training paradigms and actual inference behavior, aligning draft generation more closely with real-world deployment conditions.

## Implications
By efficiently repurposing otherwise wasted computation, Carryover Drafting offers practitioners a lightweight upgrade path to significantly boost inference throughput without requiring architectural overhauls or additional hardware. The method's compatibility with existing drafter interfaces and its demonstrated speedup gains make it highly applicable to production LLM serving frameworks like vLLM. Ultimately, this approach advances the practical viability of speculative decoding for latency-sensitive applications such as real-time translation and interactive AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14717v1)
