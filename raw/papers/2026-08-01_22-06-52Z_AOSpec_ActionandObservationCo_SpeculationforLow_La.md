---
title: AOSpec: Action and Observation Co-Speculation for Low-Latency Agent Serving
published: 2026-08-01T22:06:52Z
authors: Hao Mark Chen, Jinnan Guo, Wayne Luk, Hongxiang Fan
url: http://arxiv.org/abs/2608.00881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AOSpec: Action and Observation Co-Speculation for Low-Latency Agent Serving

## Abstract
Large language model agents increasingly act through stateful tools, yet model generation and environment execution remain serialized at every step. As decoding accelerates, tool execution becomes a growing bottleneck. Existing action- or observation-only speculation leaves much of this latency exposed: value is concentrated in a few slow calls, some outcomes emerge only through execution, and longer lookahead typically requires an increasingly unlikely chain of action predictions. We present AOSpec, a lossless framework that co-speculates actions and observations across the full agent-environment loop. Expected Value Decoding (EVD) directs observation speculation toward outcomes with the greatest expected latency benefit, optimizing expected time hidden rather than hit rate. For outcomes only execution can reveal, AOSpec launches latency-critical target actions in isolated forks that contain their effects, while Joint Action-State Verification (JASV) verifies both the action and its origin state against committed execution before reuse. JASV recasts long-horizon action dependency from full-chain prediction into target action-state verification, breaking the lookahead--accuracy tradeoff and unlocking long-range overlap without sacrificing serial semantics. Across Terminal-Bench serving settings spanning four harnesses, five actor models, and five serving speeds, AOSpec outperforms every practical baseline, reducing mean end-to-end latency by 11.8-32.5% and p99 latency by up to 42.8%. Its gains increase as decoding accelerates, and its observation model transfers from Terminal-Bench to SWE-bench Verified without retraining.

## Metadata
- **Published**: 2026-08-01T22:06:52Z
- **Authors**: Hao Mark Chen, Jinnan Guo, Wayne Luk, Hongxiang Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00881v1)