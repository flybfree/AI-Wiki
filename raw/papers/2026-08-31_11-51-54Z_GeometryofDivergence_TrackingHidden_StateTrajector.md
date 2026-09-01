---
title: Geometry of Divergence: Tracking Hidden-State Trajectories for Adaptive Multi-Turn Reasoning
published: 2026-08-31T11:51:54Z
authors: Jie Liang, Zhengxin Yu, Hamid Nasiri, Peter Garraghan
url: http://arxiv.org/abs/2608.30650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometry of Divergence: Tracking Hidden-State Trajectories for Adaptive Multi-Turn Reasoning

## Abstract
LLM agents need to sustain goal-consistent reasoning across long multi-turn interactions under strict resource constraints. However, as the multi-turn context accumulates, it can destabilize the underlying LLM's internal representation of task-relevant information from earlier turns, blurring the boundary between constructive reasoning and representation drift. We formulate multi-turn reasoning as a hidden-state trajectory of the underlying LLM that is characterized via two complementary signals: temporal curvature that captures the directional consistency of turn-to-turn updates, and variance slope which measures the expansion or contraction of the exploration space. Across four tasks and three underlying LLMs, we observed that these geometric signals distinguish between correct and incorrect episodes prior to completion. We further decompose each episode into three-action chains formed from four actions (Read, Write, Respond, Transfer) and show that separability is action-dependent, with different signals distinguishing various chain patterns. Our experiments demonstrate that trajectory geometry can identify critical turns in the reasoning process, increasing task success rates on $τ$-Bench from 24.1% to 39.6% while reducing token cost by 11.2%.

## Metadata
- **Published**: 2026-08-31T11:51:54Z
- **Authors**: Jie Liang, Zhengxin Yu, Hamid Nasiri, Peter Garraghan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30650v1)