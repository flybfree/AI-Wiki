---
title: JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs
url: http://arxiv.org/abs/2610.19822v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_08-59-35Z_JointServe_ServingMulti_ModelAgentsonMemory_Constr.md
generated_at: 2026-10-14 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
JointServe is a serving system designed for multi-model LLM agent workloads on memory-constrained GPUs, addressing the critical problem that today's serving infrastructure assumes all model weights fit within GPU memory. The system treats weight shards and KV cache blocks as unified residency objects competing for a single memory budget, exploiting structural properties of agent workloads to prefetch models, reduce switching overhead, and protect live-session state. Evaluations demonstrate a 21.7% reduction in session completion time over the strongest whole-model swap baseline, up to 49% improvement on real-world benchmark traces, and a dramatic 46-fold performance gap in crash regimes where baseline systems fail entirely.

## Key Takeaways
- JointServe exploits three structural properties of agent workloads—directed calls, gapped execution, and dual-state residency—to prepare models before they are actually invoked. An intent signal parsed from the caller's own output stream triggers prefetching during generation, meaning the next model's weights begin loading while the current model is still producing tokens, effectively hiding transfer latency behind computation.
- The system introduces partial k* residency, which reduces model switching to incremental layers rather than full weight swaps, and a preemptive transfer scheduler that guarantees a bandwidth share for live-session KV cache restoration. This dual-state residency approach prevents the catastrophic loss of session state that occurs when naive whole-model swapping discards KV blocks at a model switch.
- A dynamic carve-out control step continuously adjusts the weight-versus-KV memory allocation as workload demands shift, and the system maintains usability in crash regimes where every whole-model swap baseline fails to complete sessions. On replayed SWE-bench, tau-bench, and OSWorld traces, SLO attainment improves from 2.8–24.5% to 76.8–100%.

## Context
The evolution of LLM agents from single-model tool callers to planners orchestrating multiple expert models with distinct weight sets represents a fundamental shift in inference serving architecture. Current serving systems were designed under the assumption that a single model's working set fits in GPU memory, an assumption that breaks down on the memory-constrained GPUs typical of private deployments and edge environments. JointServe addresses this gap by rethinking memory management as a unified resource allocation problem rather than a model-loading problem, which is significant as multi-agent architectures become increasingly common in production AI systems.

## Implications
For practitioners deploying multi-model agent pipelines on consumer-grade or edge GPUs, JointServe provides a practical path to running complex agent workflows without requiring data-center-class hardware, potentially democratizing access to sophisticated agentic AI systems. The dramatic improvement in SLO attainment—from as low as 2.8% to over 76%—suggests that current serving infrastructure is a severe bottleneck for agent-based applications, and that workload-aware memory scheduling can unlock performance gains that hardware scaling alone cannot achieve. This work signals a need for serving frameworks to evolve alongside agent architectures rather than treating multi-model inference as a series of independent single-model requests.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19822v1)
