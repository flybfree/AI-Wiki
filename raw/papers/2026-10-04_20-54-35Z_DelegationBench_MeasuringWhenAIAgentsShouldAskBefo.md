---
title: DelegationBench: Measuring When AI Agents Should Ask Before Acting
published: 2026-10-04T20:54:35Z
authors: Shiva Pochampally
url: http://arxiv.org/abs/2610.05532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DelegationBench: Measuring When AI Agents Should Ask Before Acting

## Abstract
AI agents that send emails, edit files, and make purchases must decide when to act on their own and when to check with the user first. This decision is usually evaluated by showing a model a proposed action, asking whether it should proceed, and scoring agreement with human labels. We introduce DelegationBench to test whether such scores can be trusted. It has 156 scenarios with four possible responses (act, ask for permission, ask for missing information, refuse), and most scenarios come in matched pairs that change a single feature: whether the action was requested, what is at stake, whether it can be undone, or who will see it. Across ten models from five families, agreement scores mislead in three ways. A simple keyword rule, which we wrote after seeing the benchmark, agrees with our annotators more often than eight of the models, yet its decision changes in only 9 of 48 matched pairs. Equivalent ways of asking the same question change how often a model acts by up to 52.5 percentage points. And every model stops to ask the user less often when it must carry out the task with tools than when it judges a proposed action. When rules are stated explicitly, the same models follow them almost perfectly, so the gaps are not explained by a general inability to follow rules. We release the benchmark and evaluation tools and recommend reporting these properties separately rather than as one score.

## Metadata
- **Published**: 2026-10-04T20:54:35Z
- **Authors**: Shiva Pochampally
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05532v1)