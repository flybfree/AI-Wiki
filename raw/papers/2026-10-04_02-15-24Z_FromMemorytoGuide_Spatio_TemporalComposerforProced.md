---
title: From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory
published: 2026-10-04T02:15:24Z
authors: Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
url: http://arxiv.org/abs/2610.04868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory

## Abstract
Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts. This approach dangerously equates readable text with reliable execution. To bridge this gap, we introduce From Memory to Guide, a novel paradigm that transitions procedural memory from passive text delivery to active, inference-time policy adaptation. We instantiate this paradigm through the Spatio-Temporal Composer, an active policy compiler that explicitly manages exactly how and when retrieved knowledge should be applied. Rather than treating skills as plug-and-play modules, Composer dynamically aligns historical knowledge with current environmental constraints (spatial adaptation) and precisely dictates its applicable lifecycle (temporal orchestration). It actively transforms static memories into strictly bounded Runtime Guides---equipping the agent with localized objectives and behavioral guardrails without requiring a single parameter update. Extensive evaluations on 13 demanding, long-horizon software engineering tasks in EngramBench demonstrate the clear advantages of this architecture. Composer not only robustly prevents context mismatch but drives an absolute pass-rate increase of 7.2 percentage points on the most complex tasks, while simultaneously slashing the main agent's token usage by 32.2%.

## Metadata
- **Published**: 2026-10-04T02:15:24Z
- **Authors**: Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04868v1)