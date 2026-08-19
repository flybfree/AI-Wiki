---
title: Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context
published: 2026-08-18T08:25:21Z
authors: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, Xin Zhang, Wei Wu
url: http://arxiv.org/abs/2608.17499v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context

## Abstract
User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it also provides noisy, temporally local evidence about the preceding user-to-user segment. We introduce \textbf{F}eedback-\textbf{A}ware \textbf{C}redit \textbf{A}ssignment (\textsc{FACA}), which aligns each reaction with that segment, derives a locally normalized reaction advantage, and adds it to verified terminal outcome advantage without an extra critic or rollout. Against an outcome-only Interactive GRPO control matched in simulator, visible dialogue, initialization, rollout, and optimization, \textsc{FACA} improves the nine-domain $τ$-family average across three independently trained runs by 5.91 and 10.22 percentage points at 8B and 14B, respectively. Gains concentrate in Telecom; at 8B, randomizing reaction polarity removes the Telecom gain. The same ordering holds zero-shot on Pare-Bench and Co-Gym. These results demonstrate that next-turn user reactions provide actionable local credit for improving multi-turn user-interacting agents.

## Metadata
- **Published**: 2026-08-18T08:25:21Z
- **Authors**: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, Xin Zhang, Wei Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17499v1)