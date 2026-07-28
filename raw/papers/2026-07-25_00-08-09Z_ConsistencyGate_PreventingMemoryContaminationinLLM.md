---
title: ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control
published: 2026-07-25T00:08:09Z
authors: Yan Zhang, Shibo Li
url: http://arxiv.org/abs/2607.22962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control

## Abstract
LLM agents that operate over many turns accumulate facts in an external memory store and reuse them as premises for downstream reasoning. A hallucinated fact written at one step therefore persists as a false premise for every subsequent step, a failure mode we call memory contamination. Existing memory management addresses retrieval and capacity but not write-time correctness; this admission problem cannot be solved by utility- or recency-based criteria, and uncontrolled contamination compounds across long trajectories. We propose ConsistencyGate, a write-time admission gate that, before committing a candidate fact m extracted from context c, queries the LLM K times for a soft support score and admits m only when the average exceeds a threshold. The mechanism is model-agnostic, requires no fine-tuning, and reduces to a single forward pass in a log-probability variant for latency-sensitive deployments. To measure the effect on natural data, we construct two real-conversation benchmarks (LoCoMo-Contam and MSC-Contam) by planting controlled single-detail corruptions in long-term conversations from LoCoMo and MSC, and complement them with a structured synthetic corpus (MemContam) that isolates a near-oracle upper bound. Across four LLM backbones, ConsistencyGate reduces contamination on every benchmark relative to a write-everything baseline, with the cost concentrated on facts that are stated only implicitly in the source context. We release all three benchmarks together with the gate implementation.

## Metadata
- **Published**: 2026-07-25T00:08:09Z
- **Authors**: Yan Zhang, Shibo Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22962v1)