---
title: MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging
published: 2026-09-08T05:30:30Z
authors: Junxi Wang, Te Sun, Jiayi Zhu, Chen Zhang, Siyuan Li, Xuyang Liu, Zichen Wen, Xiaobing Tu, Jinkui Ren, Xiantao Zhang, Ziqi Yuan, Linfeng Zhang
url: http://arxiv.org/abs/2609.08273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging

## Abstract
Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding. However, continuously accumulated memory introduces substantial storage and retrieval costs during inference. To address this issue, we propose \textbf{MemForest}, a general memory compression framework adaptable to various agent memory systems. Specifically, MemForest partitions historical memory into event-centric units by leveraging global semantic similarity and local temporal continuity. For each unit, it constructs a maximum spanning tree, termed an EventTree, and progressively merges redundant memory nodes by selecting high-weight edges, reducing storage overhead. Furthermore, we introduce an anchor-guided propagation retrieval mechanism that retrieves relevant memory nodes from the temporal neighborhoods of key nodes, improving retrieval accuracy. Extensive experiments demonstrate the effectiveness of MemForest. Under the unimodal Mem0 framework, MemForest retains \textbf{97.1%} of the original performance while compressing \textbf{50%} of historical memory across three benchmarks (LoCoMo, LongMemEval, and PersonaMem), achieving a \textbf{1.89x} retrieval speedup. Under the multimodal M3-Agent framework, it preserves \textbf{99.7%} of the original performance with a \textbf{50%} compression ratio across two benchmarks (M3-Bench-robot and M3-Bench-web), achieving a \textbf{2.24x} retrieval speedup. \textcolor{RoyalBlue}{\textit{Our code is available at [https://github.com/Celina-love-sweet/MemForest.}}](https://github.com/Celina-love-sweet/MemForest.}})

## Metadata
- **Published**: 2026-09-08T05:30:30Z
- **Authors**: Junxi Wang, Te Sun, Jiayi Zhu, Chen Zhang, Siyuan Li, Xuyang Liu, Zichen Wen, Xiaobing Tu, Jinkui Ren, Xiantao Zhang, Ziqi Yuan, Linfeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08273v1)