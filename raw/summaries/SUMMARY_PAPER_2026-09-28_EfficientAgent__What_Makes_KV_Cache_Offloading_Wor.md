---
title: EfficientAgent: What Makes KV Cache Offloading Work for Concurrent Agents?
url: http://arxiv.org/abs/2609.33762v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_17-01-29Z_EfficientAgent_WhatMakesKVCacheOffloadingWorkforCo.md
generated_at: 2026-09-28 21:38
model: qwen3.6-35b-a3b
---

## Summary
EfficientAgent addresses the inconsistent performance of KV cache offloading in concurrent LLM agent systems by identifying the "reuse working set" as the critical determinant for effective caching. The method utilizes a stack-distance model to estimate this working set from historical data, enabling precise sizing of the host memory tier and adaptive runtime policies that ensure cached state persists until reuse. This approach significantly reduces prompt recomputation and end-to-end latency across diverse hardware configurations compared to fixed or unmanaged offloading strategies.

## Key Takeaways
- Offloading yields inconsistent results because cached state is frequently evicted before it can be reused; specifically, while one agent waits for tool execution, the server processes contexts from other agents, meaning the host tier must retain the "reuse working set" of the entire agent pool to prevent premature eviction.
- EfficientAgent introduces a stack-distance model to predict the reuse working set based on agent histories, allowing the system to size the host tier accurately and implement runtime policies that stop writing evicted context when tiers are small while fully utilizing capacity when tiers are large enough.
- Evaluations on SWE-bench Verified coding agents demonstrate that sizing the host tier to the estimated working set cuts recomputed prompt tokens by 93% and reduces end-to-end time by 39%, with adaptive policies mitigating performance degradation in undersized tiers and avoiding overhead in oversized tiers across multiple GPUs and models.

## Context
As LLM agents gain traction, serving systems encounter severe memory constraints due to the repetitive transmission of full conversation histories during each interaction turn. KV cache offloading is a common technique to alleviate GPU memory pressure by migrating key-value states to host memory, yet its effectiveness has been erratic in multi-agent deployments where complex scheduling and context switching disrupt caching efficiency.

## Implications
Practitioners managing concurrent agent workloads should focus on estimating the reuse working set rather than deploying static cache configurations

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33762v1)
