---
title: DashArena: Benchmarking LLMs on Interactive Analytic Dashboard Generation
published: 2026-08-11T06:54:37Z
authors: Xiaotong Wang, Dazhen Deng
url: http://arxiv.org/abs/2608.10567v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DashArena: Benchmarking LLMs on Interactive Analytic Dashboard Generation

## Abstract
Analytic dashboards combine coordinated views and interactions for data exploration and decision-making. Recent models can generate them from data and natural-language goals, but evaluating their usefulness remains difficult. Dashboard generation is open-ended, and neither static appearance nor successful execution alone captures analytical support and interaction quality. We introduce DashArena, to our knowledge the first benchmark for open-ended, task-grounded generation of interactive analytic dashboards. Its key innovation is to require each system to generate both a dashboard and a replayable interaction trajectory. A browser executor replays the trajectory and turns the system's intended analytical workflow into reproducible visual and execution evidence. A VLM judge compares candidates using this evidence, and Bradley--Terry aggregation produces the leaderboard. We further distill the judge into the open-weight DashJudge-8B. Human evaluations show that DashJudge-8B effectively reproduces human judgments and ablations show that interaction evidence improves judge agreement. Experiments with frontier models reveal persistent rendering, analytical, and interaction failures. Together, these results show that realistic dashboard generation remains challenging and that interaction-aware evaluation captures failures missed by static or execution-only checks.

## Metadata
- **Published**: 2026-08-11T06:54:37Z
- **Authors**: Xiaotong Wang, Dazhen Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10567v1)