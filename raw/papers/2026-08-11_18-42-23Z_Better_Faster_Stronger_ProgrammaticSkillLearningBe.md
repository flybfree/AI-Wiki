---
title: Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost
published: 2026-08-11T18:42:23Z
authors: Zixi Huang, Xiheng Wang, Andrew Wang, William Jurayj, Bernal Jiménez Gutiérrez, Daniel Khashabi, Nicholas Andrews
url: http://arxiv.org/abs/2608.11338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost

## Abstract
Recently, the practice of augmenting LLM agent capability with skills has gained prevalence. We explore the cost effective adaptation of agents to novel domains by means of learning skills. Existing works focus on performance gain over cost effectiveness. As a result, little is known about what skill learning strategies save cost. We argue that among all the different skill learning methods, those that view skills as programs can achieve the best cost reduction. By executing sequences of actions deterministically, a program-augmented agent can reliably and cheaply achieve goals that would otherwise require trial and error and risk degenerate behavior over long horizons. An agent can learn at inference time by incrementally discovering these programs and equipping them for future tasks. We hypothesize that past trajectories contain enough signal to guide skill learning, even without replay or validation, provided the agent can learn to analyze them. To test our claims, we propose SpeedRunner, a coding agent that analyzes trajectories and refactors skills for better performance on future tasks. Across three different embodied environments, we show that SpeedRunner consistently achieves the frontier in learning and cost reduction while remaining robust against distribution shifts and environmental randomness.

## Metadata
- **Published**: 2026-08-11T18:42:23Z
- **Authors**: Zixi Huang, Xiheng Wang, Andrew Wang, William Jurayj, Bernal Jiménez Gutiérrez, Daniel Khashabi, Nicholas Andrews
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11338v1)