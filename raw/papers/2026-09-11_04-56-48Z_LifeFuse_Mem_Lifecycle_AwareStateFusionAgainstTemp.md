---
title: LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory
published: 2026-09-11T04:56:48Z
authors: Hanyu Zhao, Yuqian Feng, Zhenyu Song, Yuanchao Cheng, Yance Jiao, Tengfei Pan, Li Du
url: http://arxiv.org/abs/2609.12436v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory

## Abstract
Long-running LLM agents require memory mechanisms that maintain coherent internal states across interactions. We study a lifecycle-labeled memory setting in which write episodes provide lifecycle metadata during training, and phase-aware readout is used during evaluation. This setting reflects the need to distinguish information that should remain influential across future interactions from information that should affect only the current context. A mismatch between these lifecycles can cause temporary information to overwrite durable knowledge, leading to behavioral drift in persistent agents. Within this setting, we introduce \textbf{LifeFuse-Mem}, a lifecycle-aware neural memory framework that separates information according to its temporal commitment. LifeFuse-Mem uses dedicated memory components and lifecycle-aware updates to allow stable and transient knowledge to evolve locally without converting temporary context into durable state. On the controlled anti-overwrite benchmark, LifeFuse-Mem improves acquisition-controlled retention and reduces temporary overwrite; on two public long-memory benchmarks, it remains broadly competitive. These results suggest that explicit lifecycle signals can help diagnose and mitigate overwrite in compact online memory.

## Metadata
- **Published**: 2026-09-11T04:56:48Z
- **Authors**: Hanyu Zhao, Yuqian Feng, Zhenyu Song, Yuanchao Cheng, Yance Jiao, Tengfei Pan, Li Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12436v1)