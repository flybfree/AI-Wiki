---
title: Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits
published: 2026-10-09T12:26:34Z
authors: Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, Song Han, Sihao Liu, Ligeng Zhu
url: http://arxiv.org/abs/2610.13494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits

## Abstract
Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agent's reasoning intensity declines alongside slowing progress, summarized as long-horizon deceleration, and the benefits of these custom harnesses vanish as the underlying model improves, summarized as harness staleness. These findings suggest that their benefits may not persist across versions, which motivates a workflow-level approach in which agents build on one another's work across sessions. We model these alternating agent sessions as a context-reset semi-Markov decision process (CR-SMDP) and establish sufficient conditions for alternation to exceed single-agent reference limits, derive an explicit experiment-budget bound, and characterize when session caps preserve this advantage. Guided by this analysis, we introduce Humanize MLE Agents (HMA), which alternates two agents on a shared workspace, limits each session to at most k experiments and resets the context between sessions, without additional task-specific harness or prior knowledge supplements. Across 75 Kaggle tasks in MLE-bench, HMA reaches a state-of-the-art any-medal rate of 78.2%, exceeding the strongest open-source baseline by 8.0 points with a quarter of its time budget. Moreover, among six configurations spanning five heterogeneous agent pairs, HMA improves any-medal rate over the constituent baselines by 6.4 points on average, demonstrating cross-pair generality. A supplementary case on kernel optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, demonstrating applicability beyond MLE.

## Metadata
- **Published**: 2026-10-09T12:26:34Z
- **Authors**: Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, Song Han, Sihao Liu, Ligeng Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13494v1)