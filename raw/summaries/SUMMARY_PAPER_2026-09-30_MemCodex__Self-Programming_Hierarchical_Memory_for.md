---
title: MemCodex: Self-Programming Hierarchical Memory for Language Agents
url: http://arxiv.org/abs/2609.39765v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_13-57-27Z_MemCodex_Self_ProgrammingHierarchicalMemoryforLang.md
generated_at: 2026-09-30 22:00
model: qwen3.6-35b-a3b
---

## Summary
MemCodex introduces a self-evolving hierarchical memory system that organizes agent experiences into executable programs for summaries, relational knowledge, skills, and latent memory to address heterogeneous access needs in language agents. Unlike predefined workflows, this approach uses open-ended program evolution to dynamically rewrite layer constructions, indexing, retrieval, and routing mechanisms based on query complexity. The system achieves significant performance gains, improving task success by 10.1% over strong baselines while reducing context token usage by 3.4 times and accelerating inference speed by 2.1 times through a unified runtime called MemArena.

## Key Takeaways
- Current agent memory systems struggle with heterogeneous access requirements, where single-hop queries need isolated evidence while multi-hop questions demand synthesis across multiple sources; existing adaptive methods still rely on predefined design spaces for memory components and their compositions rather than truly adapting to these varying structural needs.
- MemCodex employs open-ended program evolution to search the design space of layer programs by rewriting how each hierarchical layer is constructed, indexed, retrieved, and routed, allowing the system to adapt both within-layer implementations and cross-layer compositions dynamically based on executable memory programs for summaries, relational knowledge, reusable skills, and latent memory.
- The introduction of MemArena provides a unified runtime interface for heterogeneous data and memory systems, enabling MemCodex to outperform the strongest adaptive-memory baseline with a 10.1% increase in average task success while maintaining superior efficiency through 3.4 times fewer context tokens and 2.1 times faster inference speeds compared to existing approaches.

## Context
As language agents increasingly tackle complex, multi-step reasoning tasks, the bottleneck of managing long-term memory efficiently has become critical; static or rigidly structured memory systems often fail to scale with the diverse retrieval patterns

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39765v1)
