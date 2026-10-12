---
title: Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents
published: 2026-10-09T06:11:39Z
authors: Ziang Ye, Wentao Shi, Lei Chen, Zhengzhou Cai, Yu Wang, Zhiyuan Yao, Zihan Wang, Xierui Song, Fuli Feng, Yixin Cao
url: http://arxiv.org/abs/2610.13058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents

## Abstract
Large language model agents increasingly operate in long-horizon environments where early mistakes can trigger cascading failures and trap agents in dead-end trajectories. Agents must therefore be able to proactively recover from such states and turn their exploratory experience into guidance for subsequent decisions. We introduce ReTRAIL, a framework that enables agents to rewind the environment to earlier states while preserving valid progress and carrying forward knowledge learned from abandoned exploration. The environment state moves backward while the agent's knowledge continues to move forward. ReTRAIL trains a shared policy with two complementary signals: State-Anchored GRPO compares alternative continuations from revisited states to improve execution, while a branch-advancement reward guides reflection through the progress of subsequent exploration. Experiments across four interactive benchmark MineSweeper, Sokoban, ALFWorld and ScienceWorld show that simply adding a rewind primitive provides limited benefit and can even degrade performance. In contrast, ReTRAIL enables agents to rewind from unproductive states and use insights from abandoned branches to guide subsequent exploration. These results demonstrate the value of coupling environment rewinding with experience reuse within an ongoing task for long-horizon task solving. The code is available at https://github.com/whi497/ReTRAIL.

## Metadata
- **Published**: 2026-10-09T06:11:39Z
- **Authors**: Ziang Ye, Wentao Shi, Lei Chen, Zhengzhou Cai, Yu Wang, Zhiyuan Yao, Zihan Wang, Xierui Song, Fuli Feng, Yixin Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13058v1)