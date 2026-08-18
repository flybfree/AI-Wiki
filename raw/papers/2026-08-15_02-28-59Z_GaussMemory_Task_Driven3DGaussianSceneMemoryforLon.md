---
title: GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-Horizon Robotic Manipulation
published: 2026-08-15T02:28:59Z
authors: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa
url: http://arxiv.org/abs/2608.14986v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-Horizon Robotic Manipulation

## Abstract
Long-horizon robotic manipulation fundamentally relies on persistent spatial memory. However, existing 3D memory systems function merely as passive recorders: they store observations using fixed, hand-crafted rules, treating every scene element--whether a critical grasp target or an irrelevant background wall--with equal importance. In this paper, we propose a paradigm shift from passive storage to active, task-driven spatial memory. We argue that a robot's memory should not simply record what it sees, but actively learn how to remember--discovering which objects to track precisely, how aggressively to update them, and what to discard, all learned end-to-end without hand-designed rules. Crucially, this active paradigm is realized by unifying memory update and readout as two sides of the same cognitive process, enabling bidirectional flow where task needs shape update strategies and vice versa. To instantiate this vision, we introduce GaussMemory, which leverages 3D Gaussian Splatting as a persistent geometric substrate. On LIBERO, GaussMemory outperforms MemoryVLA on Goal and Long-10; on VLABench, it surpasses $π_0$-FAST by +5.2% (Track 1) and +6.0% (Track 6).

## Metadata
- **Published**: 2026-08-15T02:28:59Z
- **Authors**: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14986v1)