---
title: Memory Control Signals Emerge Before Action in Long Horizon Agents
published: 2026-09-23T03:23:34Z
authors: Mingxuan Wang, Guorun Yao, Fei Luo, Yinglong Guo, Chao Ning, Bo Wang, Hongyue Chen, Yanbiao Ma, Jungong Han
url: http://arxiv.org/abs/2609.27286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory Control Signals Emerge Before Action in Long Horizon Agents

## Abstract
Long horizon language model agents continuously accumulate interaction history, increasing computational cost while making relevant information harder to preserve and reuse. Existing context management methods mainly focus on how to compress or retrieve history, but largely leave open whether the model itself already represents the need for these memory operations before they occur. We study the hidden state immediately before each agent action and find that compression and recall needs are already encoded in the model's internal representations. These signals cannot be explained by simple context length or interaction progress, and they exhibit distinct formation patterns across model depth. We further show that most memory decision information is preserved in a compact recent context, while selectively restored historical evidence complements the long range dependencies that recent context misses. Based on these findings, we propose Preaction Memory with Evidence Retrieval (PaMER), which combines state guided compression with external evidence retrieval. PaMER+ further introduces step level evidence selection to recover only the historical information required by the current task. Experiments on WorkBuddyBench, across multiple context management baselines and model backbones, show that our framework substantially reduces context consumption while maintaining competitive task performance.

## Metadata
- **Published**: 2026-09-23T03:23:34Z
- **Authors**: Mingxuan Wang, Guorun Yao, Fei Luo, Yinglong Guo, Chao Ning, Bo Wang, Hongyue Chen, Yanbiao Ma, Jungong Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27286v1)