---
title: Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision
published: 2026-09-02T03:34:47Z
authors: Sitong Pan, Yipeng Shen, Yilin Lu, Caiwen Ding, Lu Cheng, Qianwen Wang
url: http://arxiv.org/abs/2609.02057v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision

## Abstract
Reliable web-agent monitoring is difficult when model-internal uncertainty signals such as token logits are unavailable. In this work, we study prefix-level risk prediction for web agents using observable trajectory signals: given an evolving prefix, estimate whether the current execution remains on track or is tending toward failure. We derive two observable trajectory representations: Macro features summarize cross-step agent--environment behavior and feedback, while Micro features measure the consistency of intention, action, and anticipated state change through repeated black-box queries. Instead of inheriting the final result label, we label the first critical error that remains uncorrected in the observed continuation and is associated with final failure as a key-step boundary, preserving valid early prefixes of failed trajectories as on track. Across WebArena-Lite and Online Mind2Web web agent benchmarks with five open- and closed-source backbones, observable trajectory signals are competitive with internal-signal baselines. The resulting predictors also support early intervention under fixed false-cut budgets and transfer across held-out website categories. These findings show that observable trajectory signals support valuable risk prediction abilities.

## Metadata
- **Published**: 2026-09-02T03:34:47Z
- **Authors**: Sitong Pan, Yipeng Shen, Yilin Lu, Caiwen Ding, Lu Cheng, Qianwen Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02057v1)