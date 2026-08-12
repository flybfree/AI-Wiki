---
title: Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy
url: http://arxiv.org/abs/2608.10532v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-15-20Z_BenchmarkingLLM_GuidedControl_PlanePoliciesforBack.md
generated_at: 2026-08-11 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether a large language model can replace static load‑balancing rules in HAProxy by continuously monitoring backend health and issuing API calls to isolate faulty servers. Experiments across 240 runs show that models with roughly 3 billion active parameters achieve an 88 % reduction in client‑perceived 5xx errors, while smaller or cheaper models either fail or worsen performance.

## Key Takeaways
- LLM policies become unreliable below a capability threshold near 3B active parameters and can be worse than no policy.  
- Above the threshold every model, regardless of architecture, yields an 88 % drop in 5xx errors compared with static routing.  
- The trade‑off is high token consumption that multiplies cost tenfold and drains load onto survivors, inflating tail latency up to 2.8×.

## Context
This work demonstrates how generative AI can augment traditional control‑plane mechanisms for fault isolation in real‑time systems, highlighting the balance between model size and operational efficiency. It contributes to the growing interest in deploying LLMs as dynamic decision layers within infrastructure automation pipelines.

## Implications
For cloud operators, the findings suggest that only sufficiently capable models should be used for automated backend routing, while cheaper static rules may suffice for lower‑risk deployments. Practitioners must weigh latency penalties and cost spikes when selecting model size and reasoning mode.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10532v1)
