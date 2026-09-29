---
title: Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving
url: http://arxiv.org/abs/2609.33536v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_13-03-38Z_DoesExecutionRequireTargetKVFidelity_AMixed_Fideli.md
generated_at: 2026-09-28 21:52
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces ElasticKV, a mixed-fidelity key-value runtime designed to mitigate GPU memory bottlenecks in large language model serving by decoupling execution readiness from strict target KV fidelity requirements. By maintaining a compact intermediate KV state that allows fidelity to be managed dynamically based on memory pressure, ElasticKV significantly reduces latency without compromising generation quality. Evaluations demonstrate that ElasticKV achieves up to 4.0x lower time-to-first-token and 9.1x lower P90 TTFT compared to vLLM under high concurrency across diverse workloads and hardware platforms.

## Key Takeaways
- ElasticKV challenges the conventional assumption that execution requires full target KV fidelity by introducing a compact intermediate KV state, which transforms fidelity reduction into a runtime-managed property rather than a hard constraint, thereby preventing request stalls and preemptions

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33536v1)
