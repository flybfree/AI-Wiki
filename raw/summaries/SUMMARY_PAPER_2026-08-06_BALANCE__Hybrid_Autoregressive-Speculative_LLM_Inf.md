---
title: BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks
url: http://arxiv.org/abs/2608.05926v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_11-57-36Z_BALANCE_HybridAutoregressive_SpeculativeLLMInferen.md
generated_at: 2026-08-06 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BALANCE, a hybrid autoregressive-speculative inference framework for edge LLM serving that balances latency and memory by running both methods simultaneously on an edge server. It solves a throughput maximization problem under user latency constraints and memory limits, delivering a constant-approximation solution. Experiments show BALANCE outperforms pure AD or SD in task throughput.

## Key Takeaways
- The framework assigns users to either autoregressive decoding (AD) or speculative decoding (SD) while both models run concurrently on the edge server.
- It formulates a task throughput maximization problem that combines user scheduling with resource allocation, acknowledging NP-hardness and providing a polynomial-time algorithm with constant approximation guarantee.
- Experiments demonstrate that BALANCE consistently improves throughput over conventional AD or SD methods.

## Context
Edge inference aims to deliver large language model services directly on mobile network edge nodes to reduce latency. However, the tradeoff between sequential autoregressive decoding’s long response time and speculative decoding’s memory overhead remains a bottleneck for heterogeneous user demands. This paper addresses that limitation by integrating both paradigms within a single server architecture.

## Implications
BALANCE offers a practical solution for edge AI services where resource constraints are tight yet high throughput is desired. Practitioners can adopt the scheduling algorithm to allocate compute and memory efficiently, potentially enabling scalable LLM deployment in wireless networks without sacrificing user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05926v1)
