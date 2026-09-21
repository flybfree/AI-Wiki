---
title: MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems
published: 2026-09-18T09:25:06Z
authors: Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
url: http://arxiv.org/abs/2609.21533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

## Abstract
LLM-based multi-agent systems generate collaboration traces that record how agents plan tasks, verify intermediate results, and repair failures. Reusing these procedures requires preserving an action's prerequisites and the outputs needed by subsequent agents. Our empirical studies show that grouping these dependencies into functional memory units improves their retention, while connecting units increases retrieval of the units and links jointly required by a task. The preferred combination of units also changes between instructions and checklists, even when each combination's content is fixed across formats. Updating choices from the outcomes of each combination and format pairing outperforms scoring combinations and formats separately. These findings motivate MACE, a memory-agent co-evolution framework that adapts memory organization and agent memory use through execution feedback. Its MemGoG structure represents functional units as subgraphs of related conditions, actions, and outputs, connecting them through support, conflict, and repair relations. MACE Loop selects task-relevant units and relations within a memory budget and provides each agent with instructions or checklists for its current operation. It records the selected units, presentation formats, agent outputs, and task outcomes to update unit scores and relations for retrieval and inform subsequent presentation choices. Across eight benchmarks, MACE outperforms ten baselines with an average score of 81.11%, compared with 78.97% for the strongest baseline, SAGE.

## Metadata
- **Published**: 2026-09-18T09:25:06Z
- **Authors**: Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21533v1)