---
title: Memory-Bounded Continuation of Greedy Sampling for Continual Anomaly Detection
published: 2026-08-15T15:19:12Z
authors: Yoon Gyo Jung, Jaewoo Park, Kuan-Chuan Peng, Seongdeok Bang, Octavia Camps
url: http://arxiv.org/abs/2608.15277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory-Bounded Continuation of Greedy Sampling for Continual Anomaly Detection

## Abstract
Greedy sampling produces a compact yet representative summary of normal data, which is essential for reliable anomaly detection that relies on measuring distance from normality. For continual anomaly detection where tasks arrive sequentially, extending greedy sampling is straightforward with unbounded memory through coreset accumulation. However, practical deployment requires fixed memory where the coreset size remains constant regardless of task count. We observe that continued greedy sampling, which iteratively applies greedy selection over previously greedy-sampled sets, effectively preserves representativeness under strict memory limits. Despite discarding data at each step to satisfy the memory constraint, coreset quality degrades gracefully rather than catastrophically, enabling reliable anomaly detection across the tasks. We provide theoretical justification by showing that resulting greedy-continued coreset approximates the oracle coreset within a bounded gap. We instantiate this principle in ContCore, which constructs a greedy-continued coreset through greedy expansion on new task features followed by greedy consolidation to enforce the memory budget. Unlike neural methods susceptible to catastrophic forgetting or naive coreset accumulation requiring unbounded memory, ContCore maintains fixed memory with theoretical guarantees. Empirically, ContCore achieves state-of-the-art performance across 11 task schedules on MVTecAD and VisA, and extends effectively to online continual AD settings where prior methods degrade significantly. Code: https://github.com/jungyg/ContCore

## Metadata
- **Published**: 2026-08-15T15:19:12Z
- **Authors**: Yoon Gyo Jung, Jaewoo Park, Kuan-Chuan Peng, Seongdeok Bang, Octavia Camps
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15277v1)