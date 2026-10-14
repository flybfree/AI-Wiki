---
title: SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding
url: http://arxiv.org/abs/2610.17436v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_21-53-20Z_SchemaWeaver_AcceleratingOn_DeviceMobileAgenticAIv.md
generated_at: 2026-10-14 00:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SchemaWeaver introduces a novel technique for accelerating on-device mobile agentic AI by enforcing schema-guided parallel decoding during the decode phase of LLM tool calling. The method produces multiple tokens in each decode pass, directly targeting the memory-bandwidth-bound bottleneck that dominates latency on mobile processors. Experiments across major mobile SoCs and LLM families demonstrate up to a 3.9× reduction in tool-calling latency compared to competitive baselines, all without requiring any model retraining or architectural modifications.

## Key Takeaways
- The decode phase of LLM inference on mobile devices is fundamentally constrained by memory bandwidth rather than compute power, making conventional compute-optimization approaches ineffective for reducing tool-calling latency in agentic workflows. This hardware-level limitation is the primary barrier to practical on-device mobile agentic AI.
- SchemaWeaver exploits the structured, schema-constrained nature of tool-call outputs to enable parallel decoding, generating multiple tokens simultaneously in a single decode pass. Because tool calls follow predefined schemas (function names, parameter types, argument structures), the system can predict and emit multiple tokens at once rather than sequentially, dramatically cutting the number of decode iterations needed.
- The technique is model-agnostic and training-free: it operates as a generic layer within the LLM inference engine on mobile devices, requiring no fine-tuning, no changes to the underlying LLM weights, and no modifications to the model architecture. This makes it broadly deployable across different LLM families and mobile SoC platforms, as validated by experiments showing consistent speedups across diverse hardware and model configurations.

## Context
On-device agentic AI, where mobile LLMs autonomously call external software tools to complete complex user tasks, is a rapidly growing research and product frontier. However, the sequential token-by-token decoding inherent to autoregressive LLMs makes tool-calling latency prohibitive on mobile hardware, where memory bandwidth is severely limited compared to data-center GPUs. Prior acceleration efforts have largely focused on compute-bound optimizations or speculative decoding, which do not address the bandwidth-bound decode bottleneck on mobile SoCs. SchemaWeaver represents a shift toward leveraging the structural regularity of agentic outputs—specifically tool-call schemas—to sidestep this hardware limitation entirely.

## Implications
For the mobile AI industry, SchemaWeaver offers a practical, deployment-ready path to making agentic AI assistants responsive enough for real-world use on smartphones and edge devices, potentially enabling new categories of on-device autonomous agents that interact with apps, sensors, and services in real time. For practitioners building on-device inference stacks, the technique's training-free and model-agnostic nature means it can be integrated into existing inference engines without costly retraining pipelines or vendor-specific model adaptations, lowering the barrier to adoption across heterogeneous mobile hardware ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17436v1)
