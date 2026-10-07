---
title: Understanding and Mitigating Inference-Time Overreliance Using Agentic Memory
published: 2026-10-05T19:48:54Z
authors: Luoxi Tang, Yuqiao Meng, Nilesh Auradkar, Muchao Ye, Dazheng Zhang, Zhaohan Xi
url: http://arxiv.org/abs/2610.07311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding and Mitigating Inference-Time Overreliance Using Agentic Memory

## Abstract
Agentic memory allows LLM agents to reuse past experience, yet retrieved memories can also distort inference even when they are benign, correctly stored, and appropriately retrieved. We study this failure mode, which we call memory over-reliance. Across benchmarks and memory architectures, we find that memory is useful when past experience transfers to the current task, but can become misleading when only part of the evidence transfers. Failures are strongest under partial query-memory overlap, a pattern further confirmed by controlled experiments thatvary the amount of overlapping evidence. Motivated by this finding, we propose MEMTRIM, a plug-and-play framework that indexes memory evidence at write time and controls its reuse at read time. MEMTRIM removes repeated or conflicting evidence while preserving useful memory-specific information, requires no retraining, and applies to both embedding-based and structured memory systems.Experiments show that MEMTRIM reduces memory overreliance while preserving the benefits of useful memory across models and memory settings.

## Metadata
- **Published**: 2026-10-05T19:48:54Z
- **Authors**: Luoxi Tang, Yuqiao Meng, Nilesh Auradkar, Muchao Ye, Dazheng Zhang, Zhaohan Xi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07311v1)