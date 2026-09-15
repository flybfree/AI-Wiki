---
title: BOOST: Concurrent Access to Host Memory and HBM to Accelerate LLM Inference
url: http://arxiv.org/abs/2609.13592v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-11_23-02-24Z_BOOST_ConcurrentAccesstoHostMemoryandHBMtoAccelera.md
generated_at: 2026-09-15 10:25
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces BOOST, a novel runtime system designed to overcome GPU memory bandwidth and capacity bottlenecks in large language model inference. By enabling concurrent and proportional access to both high-bandwidth memory (HBM) and host memory without requiring kernel modifications, BOOST effectively combines the bandwidth of both tiers to significantly accelerate LLM serving performance compared to traditional hierarchical or prefetching approaches.

## Key Takeaways
- Current GPU memory systems operate hierarchically, either serving exclusively from HBM or prefetching data from host memory, which leaves host memory bandwidth underutilized and consumes valuable HBM bandwidth during writes.
- BOOST achieves full utilization of both memory tiers by making page allocation and runtime data management wave-aware, using modulo-based placement for static model weights and a dynamic free KV page pool that aligns with GPU threadblock waves.
- Evaluated on a Grace Hopper system integrated with vLLM, BOOST improves Time-per-Output-Token by 4.3% at fixed batch sizes and boosts overall throughput by an average of 31%, substantially outperforming conventional prefetching methods which degrade performance under high load.

## Context
As large language models continue to scale in size and complexity, the demand for faster inference has exposed critical limitations in traditional GPU memory architectures. The hierarchical separation between fast on-chip HBM and slower host memory creates a bandwidth bottleneck that restricts throughput, particularly when model weights and dynamic KV caches exceed available HBM capacity. This research addresses a growing industry challenge by rethinking how GPU memory tiers are managed at runtime rather than through rigid hardware or kernel-level constraints.

## Implications
The introduction of wave-aware memory management demonstrates that significant performance gains can be achieved without modifying underlying neural network kernels, making it highly practical for widespread adoption in existing inference frameworks like vLLM. By effectively pooling host and HBM bandwidth, this approach offers a scalable pathway to reduce inference costs and improve latency for large-scale AI deployments, directly impacting cloud providers and enterprise AI infrastructure planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.13592v1)
