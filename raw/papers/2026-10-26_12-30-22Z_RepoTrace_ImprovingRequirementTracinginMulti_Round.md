---
title: RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions
published: 2026-10-26T12:30:22Z
authors: Huanyu Liu, Yezheng Cheng, Jinliang You, Tianxiao Huang, Linyu Li, Zheng Fang, Peng Cao, Ge Li
url: http://arxiv.org/abs/2610.35333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions

## Abstract
Code agents have become increasingly capable of performing software engineering tasks through interaction with software environments. However, agents tend to degrade as the number of interaction rounds increases, making it difficult to maintain existing software during iterative modification. We analyze 2,656 agent trajectories in EvoCode-Bench and identify requirement focus misalignment as a recurring failure pattern, where agents struggle to distinguish the primary modification targets of a requirement from unrelated code.   We propose Repotrace a requirement-driven repository understanding harness that combines repository structure with requirement semantics to construct a requirement-code correspondence and injects it into the agent context. This correspondence enables code agents to follow the repository architecture, trace requirements across multi-round interactions, and identify the core code elements corresponding to the current requirement. Experiments show that Repotrace improves the mean per-round reward (MPR) across different models (e.g., +19.99 on GLM-5.2) and agent harnesses (e.g., +10.22 on Claude Code). Across rounds, Repotrace increases the average per-round reward from 0.163 to 0.371 on Terminus-2 with DeepSeek-V4-Pro, while reducing average regression errors by 56.78%. We release the source code and agents' trajectories to support future research.

## Metadata
- **Published**: 2026-10-26T12:30:22Z
- **Authors**: Huanyu Liu, Yezheng Cheng, Jinliang You, Tianxiao Huang, Linyu Li, Zheng Fang, Peng Cao, Ge Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35333v1)