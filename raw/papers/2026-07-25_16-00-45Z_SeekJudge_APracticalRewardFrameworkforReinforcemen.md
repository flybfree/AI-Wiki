---
title: SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents
published: 2026-07-25T16:00:45Z
authors: Yang Wan, Zhenhao Zhang, Jierui Wang, Linchao Zhu
url: http://arxiv.org/abs/2607.23263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents

## Abstract
Deciding whether a trajectory actually fulfills its instruction governs how we measure computer-use agents on long-horizon graphical-user-interface tasks and how we train them with reinforcement learning. This judgment has long relied on rule-based evaluation, which struggles to align with human intention and goes stale when an app updates or its online content drifts. Existing model-based judges attempt to address these problems but still leave a performance gap to the rule-based evaluation. We propose the \textbf{SeekJudge} framework, in which four role-specialized agents, a Condense, a Ground, a Seek and an Analyze agent, reach a verdict through a Seek--Analyze loop over the trajectory. A seed-calibrated distillation pipeline trains one specialized $9$B model to serve as the shared backbone for all four agents. Measured by downstream success rate on held-out RL test goals, SeekJudge is the first practical model-based reward to match or surpass native rule-based supervision in online RL. Beyond accuracy, SeekJudge provides step-level judgments, runs far cheaper than a closed-source large model, and keeps a small per-call context that scales to much longer trajectories. We further contribute a general architectural improvement to the reward server that speeds up judging in RL. Together these make model-based reward a practical drop-in for rule-based supervision in CUA reinforcement learning.

## Metadata
- **Published**: 2026-07-25T16:00:45Z
- **Authors**: Yang Wan, Zhenhao Zhang, Jierui Wang, Linchao Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23263v1)