---
title: A^2Agent: Action-Aware Reinforcement Learning for Repository-Level Code Localization Agents
published: 2026-08-30T14:53:35Z
authors: Doyeon Kim, Suyoung Bae, Yumin Lee, Jee-Hyong Lee
url: http://arxiv.org/abs/2608.29831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A^2Agent: Action-Aware Reinforcement Learning for Repository-Level Code Localization Agents

## Abstract
Localizing issue-relevant code regions is a critical step in automated software engineering. However, due to their reliance on sparse trajectory-level signals, existing methods cannot identify which per-turn actions are effective and often discover correct code regions during exploration but fail to commit them. To address these limitations, we propose an action-aware reinforcement learning method that combines a per-turn reward sequence rewarding both the discovery and commitment of gold code regions with an action-level advantage estimation scheme that isolates each action's credit by grouping turns sharing the same exploration context. Extensive evaluations show that our method improves the average F1 over the state-of-the-art (SOTA) by 1.58% on SWE-Bench Verified and 8.55% on SWE-Bench Pro, with our 4B model outperforming baselines up to 8x larger. Our code is available at https://github.com/donian00/A2Agent.

## Metadata
- **Published**: 2026-08-30T14:53:35Z
- **Authors**: Doyeon Kim, Suyoung Bae, Yumin Lee, Jee-Hyong Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29831v1)