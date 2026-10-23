---
title: Diagnosing Personalization Failures in Mobile GUI Agents
published: 2026-10-22T01:04:24Z
authors: Zhixin Lin, Dongliang Xu, Jungang Li, Shidong Pan, Jun Feng, Yanbin Sun, Jing Li, Liang Liu, Yue Yao
url: http://arxiv.org/abs/2610.30573v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diagnosing Personalization Failures in Mobile GUI Agents

## Abstract
Unlike conventional GUI agents, personalized GUI agents require user preferences to guide sequential execution over changing GUI states. This raises two challenges: determining HOW each preference should alter execution strategy and WHEN it should take effect along the interaction trajectory. Existing benchmarks primarily evaluate overall task success, offering limited insight into these questions. We introduce PrefDiag-Bench with two components: (1) a categorization of preferences into five types, characterizing HOW they affect execution; and (2) a stage-wise diagnostic framework with 1,664 probes, tracing WHEN preferences should take effect and where failures occur. We evaluate eleven GUI agent systems, including end-to-end agents and agentic workflows, under two forms of user context: explicit user profiles and behavioral memory logs. Although existing agents achieve relatively high completion rates on non-personalized tasks, performance is substantially lower on preference-personalized tasks. Even the best-performing model, Seed-2.0-Pro, achieves only 47.17% on Process preferences under explicit user profiles. Agents struggle particularly with Ranking and Process preferences. Further analysis reveals two key capability bottlenecks: selecting relevant evidence from user history and recognizing when preferences should take effect during execution. Controlled interventions that explicitly provide relevant evidence improve end-to-end task success by up to 7.06%. PrefDiag-Bench offers a more systematic evaluation of GUI agents' personalization capabilities beyond overall task success. Code and data are available at https://github.com/Zhixin-L/PrefDiag-Bench.

## Metadata
- **Published**: 2026-10-22T01:04:24Z
- **Authors**: Zhixin Lin, Dongliang Xu, Jungang Li, Shidong Pan, Jun Feng, Yanbin Sun, Jing Li, Liang Liu, Yue Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30573v1)