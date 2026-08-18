---
title: From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems
url: http://arxiv.org/abs/2608.15127v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_09-02-16Z_FromLLMInferencetoAgenticWorkloads_Characterizatio.md
generated_at: 2026-08-17 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AgentSysBench, a benchmark suite and measurement toolkit designed to characterize the unique characteristics of agentic AI workloads that extend beyond simple model inference. Across ten representative applications and production traces, the authors identify six distinct properties that differentiate these workloads from conventional LLM serving, revealing significant latency, cost, and resource bottlenecks.

## Key Takeaways
- Execution is heavyweight and stateful, with non‑LLM components dominating latency in five of ten applications and sandbox working‑set memory peaking at 28 GB per session.  
- Applications compose heterogeneous resources—GPU inference, memory retrieval, CPU sandboxes—whose task latencies can diverge by up to 32×.  
- Production sessions often hold state idle for minutes to hours between active steps, creating opportunities for offloading and caching.

## Context
Agentic AI workloads push serving systems beyond the assumptions built for single‑request inference, introducing long‑running coordination of tools and persistent state that strain existing infrastructure. Understanding these dynamics is essential as organizations adopt more complex, multi‑step AI agents in production environments.

## Implications
These findings guide system designers to implement task‑aware serving, resource placement, and caching strategies that can reduce latency by up to 40% and cut redundant compute by over a third, ultimately lowering costs and improving user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15127v1)
