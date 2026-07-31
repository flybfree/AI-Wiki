---
title: Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory
published: 2026-07-30T16:13:02Z
authors: Jiannan Yang, Veronika Thost, Xiang Ling, Tengfei Ma
url: http://arxiv.org/abs/2607.28437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Oracle-Budgeted Molecular Optimization with Short-Term Graph Memory

## Abstract
Molecular optimization is commonly performed under a limited oracle budget, which makes deciding what to evaluate as important as deciding what to generate. We introduce short-term graph memory, a plug-in module that preserves the generator architecture and native update rule while learning from previously evaluated molecules to prioritize subsequent oracle queries. The module maintains an online graph neural surrogate that pre-screens each round's candidate pool, so the fixed oracle budget is spent on molecules with higher predicted utility. Applied to a fragment-based generator on a standard molecular optimization benchmark, it improves the mean top-10 score at no extra oracle cost and never falls behind the base on any oracle; the gain extends to all four generators we tested at a tight budget of one thousand calls. We then analyze how surrogate-guided selection interacts with the exploration and exploitation behavior of different generators. Its benefit at larger budgets is consistent with two properties of the backbone: how broadly it searches, and how effectively its native search already exploits oracle feedback. We provide a simple way to spend a fixed oracle budget more selectively, and evidence on which generators benefit from it.

## Metadata
- **Published**: 2026-07-30T16:13:02Z
- **Authors**: Jiannan Yang, Veronika Thost, Xiang Ling, Tengfei Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28437v1)