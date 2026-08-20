---
title: MemFuse: Multi-Source Memory Fusion from Fragmented Observations
published: 2026-08-19T09:04:07Z
authors: Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, Kun Shao
url: http://arxiv.org/abs/2608.18704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemFuse: Multi-Source Memory Fusion from Fragmented Observations

## Abstract
Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories. In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic memories while preserving their source provenance. To address these gaps, we introduce **MemFuseBench**, a benchmark for *multi-source memory fusion*. MemFuseBench is built with a Scene-to-Sensor pipeline that synthesizes controllable scenarios into source-tagged observations, evidence-grounded questions, and adversarial distractors. It enables systematic evaluation of temporal reasoning, cross-source evidence fusion, and robustness to noise. We further propose **MemFuse**, a structured memory system that preserves source-level evidence in event-layer atomic memory and organizes related atomic events into cluster-layer fused memory within a causal fusion graph. During retrieval, MemFuse retrieves and organizes related evidence fragments while maintaining traceability to original source events. Experiments on MemFuseBench show that MemFuse achieves the best overall performance among the evaluated memory systems under all three LLM settings and consistently improves performance on questions requiring cross-source evidence fusion.

## Metadata
- **Published**: 2026-08-19T09:04:07Z
- **Authors**: Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, Kun Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18704v1)