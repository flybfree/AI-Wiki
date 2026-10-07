---
title: APEX: Speculate smarter, not deeper
published: 2026-10-06T05:17:08Z
authors: Manvi Jha, Zach Zhang, Zhichao Xu, Linbo Liu, Sai Muralidhar Jayanthi, Vinayak Arannil
url: http://arxiv.org/abs/2610.07780v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APEX: Speculate smarter, not deeper

## Abstract
Speculative decoding reduces large language model inference latency by drafting multiple tokens before target-model verification, but its effectiveness depends on both the proposal mechanism and draft depth. Fixed configurations cannot respond to changes in predictability, repetition, and acceptance during generation, so deeper drafting can increase wasted computation without proportional speedup. We introduce APEX, a learned controller that balances decoding speed and draft-token waste through request-level expert selection and block-level depth adaptation. APEX-Router selects among EAGLE-3, n-gram, and draft-model speculation for each request, while APEX-Depth adjusts draft length at each verification block using causal decoding signals and recent verifier feedback. APEX models accepted draft length as censored survival feedback, learning position-wise rejection hazards, block execution costs, and an action utility that balances throughput, accepted progress, and wasted tokens. This allows the controller to adapt speculation while retaining the target model's verification procedure. We integrate APEX into vLLM and evaluate it with Qwen3-8B across six workloads, achieving up to 5.24X speedup over autoregressive decoding. Across the aggregate evaluation, APEX-S achieves 4.27X speedup, while APEX-B achieves 3.27X speedup with a 41.0% relative reduction in wasted-token percentage compared with fixed n-gram speculation at k=16, providing distinct operating points for balancing acceleration and draft-token utilization.

## Metadata
- **Published**: 2026-10-06T05:17:08Z
- **Authors**: Manvi Jha, Zach Zhang, Zhichao Xu, Linbo Liu, Sai Muralidhar Jayanthi, Vinayak Arannil
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07780v1)