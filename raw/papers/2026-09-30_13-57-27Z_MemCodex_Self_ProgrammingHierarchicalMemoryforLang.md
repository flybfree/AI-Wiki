---
title: MemCodex: Self-Programming Hierarchical Memory for Language Agents
published: 2026-09-30T13:57:27Z
authors: Xiaoqiang Wang, Bang Liu
url: http://arxiv.org/abs/2609.39765v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCodex: Self-Programming Hierarchical Memory for Language Agents

## Abstract
Agent memory faces heterogeneous access needs: a single-hop question may require one piece of evidence, whereas a multi-hop question must combine evidence from multiple sources. Predefined memory workflows cannot adapt to these varying needs. Recent adaptive methods search or learn over memory components and their compositions, but the design space itself remains predefined. We introduce MemCodex, a self-evolving hierarchical memory system that organizes experience into executable memory programs for summaries, relational knowledge, reusable skills, and latent memory. Open-ended program evolution searches the open design space of layer programs by rewriting how each layer is constructed, indexed, retrieved, and routed, thereby adapting both within-layer implementations and cross-layer composition. At query time, reads traverse the hierarchy from coarse to fine and stop once sufficient evidence is found, descending to the original history when needed. We further develop MemArena, a unified runtime that places heterogeneous data and memory systems behind a common interface. MemCodex improves average task success by 10.1% relative to the strongest adaptive-memory baseline, while using 3.4x fewer context tokens and achieving 2.1x faster inference.

## Metadata
- **Published**: 2026-09-30T13:57:27Z
- **Authors**: Xiaoqiang Wang, Bang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39765v1)