---
title: The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock
published: 2026-10-14T09:35:54Z
authors: Ningxin Pan, Hanyu Li, Yeqing Shen, Ning Ding, Yehui Tang, Wentao Zhang
url: http://arxiv.org/abs/2610.20665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock

## Abstract
Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate agents while games continue running during inference. Paired evaluations show that GPT-6.1-sol outperforms the faster Jev when games are paused, but falls behind when they keep running. We propose Two-Timescale Offline Recursive Self-Improvement (TORSI): a slow teacher studies failures and tests corrections in paused games between attempts, then writes reusable instructions for a fast student. The student acts without teacher calls during gameplay, and validation scores determine which updates are adopted. Two rounds raise Jev's average test score from 13.51 to 24.19 on a 0--100 progress scale, improving all six game types. The instructions also improve average scores for three other models without retuning. These findings point toward real-time intelligence: enabling powerful LLM agents to remain effective in a continuously changing world by organizing deliberation, learning, and action across timescales.

## Metadata
- **Published**: 2026-10-14T09:35:54Z
- **Authors**: Ningxin Pan, Hanyu Li, Yeqing Shen, Ning Ding, Yehui Tang, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20665v1)