---
title: Just-In-Time Agent Memory with Runtime Agentic Research
url: http://arxiv.org/abs/2609.34385v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_06-01-09Z_Just_In_TimeAgentMemorywithRuntimeAgenticResearch.md
generated_at: 2026-09-28 22:55
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Just-In-Time Agent Memory (JAM), a trainable framework that dynamically constructs query-conditioned context at runtime to overcome the rigid limitations of traditional Ahead-of-Time memory architectures. By combining a hierarchical Memorizer for raw history preservation with an iterative Researcher for targeted evidence retrieval, JAM delivers superior performance on agent memory and long-context benchmarks while maintaining significantly lower computational overhead than prior trained approaches.

## Key Takeaways
- Traditional AOT memory systems pre-build context before requests arrive, which often discards fine-grained information needed later; JAM solves this by generating query-specific context at runtime through a hierarchical page-store and compact navigational summaries.
- The framework relies on Memory-Gym, an evidence-grounded data synthesis pipeline spanning six domains and nine task types, with the Researcher optimized via verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization.
- Empirical evaluations demonstrate that JAM consistently outperforms both AOT-style memory systems and earlier trained agentic memory models in complex reasoning tasks while remaining substantially more efficient during online serving.

## Context
As AI agents increasingly operate across extended multi-turn interactions and complex tool-use scenarios, managing contextual information efficiently has emerged as a critical bottleneck. Conventional memory designs prioritize offline construction to minimize inference costs but frequently fail to preserve the nuanced details required for dynamic decision-making. This paper addresses that gap by introducing a runtime-adaptive memory paradigm that aligns context construction directly with query requirements.

## Implications
The shift toward just-in-time memory construction enables developers to deploy more scalable and cost-effective AI agents capable of handling intricate, long-horizon workflows without sacrificing critical contextual fidelity. Practitioners can adopt JAM’s training pipeline and architectural components to build production-ready systems that dynamically balance information retention with retrieval efficiency, ultimately improving agent reliability in real-world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34385v1)
