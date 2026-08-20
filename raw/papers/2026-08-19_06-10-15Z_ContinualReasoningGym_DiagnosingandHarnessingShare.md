---
title: Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR
published: 2026-08-19T06:10:15Z
authors: Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, Lifeng Fan
url: http://arxiv.org/abs/2608.18574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR

## Abstract
Reinforcement learning with verifiable rewards (RLVR) commonly post-trains reasoning models on multiple tasks, while rerunning multitask RLVR (MTRL) as new tasks are added makes capability expansion costly. We therefore study continual RLVR, which updates the existing model as each task arrives. The central question is whether a model updated this way can perform as well as a jointly trained model. To answer this question, we introduce Continual Reasoning Gym, a continual-RLVR environment that organizes text and visual reasoning tasks into five task sequences. In this setting, we identify two key observations: Sequential RLVR exhibits modest forgetting, yet its final performance remains below that of MTRL. To understand the latter, we decompose final performance and show that forgetting accounts for only part of the gap. To explain the former, we identify shared reasoning: transferable reasoning structure allows training on one task to support others on average. We therefore introduce Continual Prompt Replay (CPR), which harnesses shared reasoning to improve learning on the arriving and future tasks by replaying previous-task prompts and regenerating their responses with the current policy. On average, only CPR reaches MTRL-level performance.

## Metadata
- **Published**: 2026-08-19T06:10:15Z
- **Authors**: Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, Lifeng Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18574v1)