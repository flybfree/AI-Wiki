---
title: SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness
published: 2026-09-17T14:58:29Z
authors: Haozhe Liu, Tian Ye, Sensen Gao, Qihang Cao, Yitong Li, Mingchen Zhuge, Duomin Wang, Ruihua Zhang, Ping Luo, Jiawang Bian, Lei Zhu, Ligeng Zhu, Enze Xie, Song Han
url: http://arxiv.org/abs/2609.20519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

## Abstract
As coding agents move from supervised code completion to unattended, around-the-clock exploration, their work expands from isolated predictions into long trajectories of reasoning, tool use, and feedback. Token efficiency therefore becomes important for scaling recursive self-improvement. We take an RSI-inspired approach at the harness layer, scaling auto-research loops across increasingly numerous and diverse environments for harness rollouts. At this scale, the process yields reusable improvements that transfer beyond their development setting, moving automated harness discovery toward production-level outcomes. Four mechanisms survive selection and form SoL-Pi, spanning action execution, context compaction, observation handling, and delegated reading. On the 51-task EdgeBench evaluation, SoL-Pi achieves performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7-49.0% and API cost by about one third. In other words, estimated hourly savings are \$8.75-\$13.50 relative to native Codex and Claude Code harnesses, and \$4.36-\$5.71 relative to Pi.

## Metadata
- **Published**: 2026-09-17T14:58:29Z
- **Authors**: Haozhe Liu, Tian Ye, Sensen Gao, Qihang Cao, Yitong Li, Mingchen Zhuge, Duomin Wang, Ruihua Zhang, Ping Luo, Jiawang Bian, Lei Zhu, Ligeng Zhu, Enze Xie, Song Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.20519v1)