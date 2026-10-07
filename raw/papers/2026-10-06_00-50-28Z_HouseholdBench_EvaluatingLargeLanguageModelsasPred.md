---
title: HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior
published: 2026-10-06T00:50:28Z
authors: Jin Huang, Diego Ferreras Garrucho, Yutong Xie, Walter M. Yuan, Qiaozhu Mei, Chen Lian, Jonathon Hazell
url: http://arxiv.org/abs/2610.07563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior

## Abstract
Large language models (LLMs) have the potential to meet a key goal in economics: a quantitative model of household decision making, across a variety of settings. Yet existing evaluations cover few surveys and outcomes, and do not study how households adjust to changing economic conditions. We introduce a new evaluation, HouseholdBench, which unites 6 U.S. household surveys and 32 prediction tasks spanning numeric, categorical and probabilistic outcomes, related to consumption, income, labor, expectations, and housing. Using past behavior, demographics and macroeconomic conditions, the tasks test whether LLMs predict behavior, including how households adjust to changes in various policies. We evaluate 13 proprietary and open-weight LLMs against a no-change baseline and a gradient-boosted tree model. Most LLMs outperform the no-change baseline, including for policy response tasks -- with the best model lowering error for numeric outcomes by 12.2%. Across most tasks, gradient-boosted trees rank first; leading proprietary LLMs approach their performance, but open-weight models lag. LLMs exhibit systematic over- and underprediction across different tasks. We identify methods that enable a 4 billion parameter open-weight model to match proprietary models' performance: fine-tuning and aggregating 16 predictions per observation. Improvements generalize to policy-response tasks, which are excluded from fine-tuning. We release our datasets, code, and leaderboard on our website: https://jn-huang.github.io/householdbench

## Metadata
- **Published**: 2026-10-06T00:50:28Z
- **Authors**: Jin Huang, Diego Ferreras Garrucho, Yutong Xie, Walter M. Yuan, Qiaozhu Mei, Chen Lian, Jonathon Hazell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07563v1)