---
title: FeatureLoop: Benchmarking Coding Agents under Evolving Requirements
published: 2026-10-26T14:15:53Z
authors: Jia Feng, Alyssa Wu, Cuiyun Gao, Yunlong Wang, Songyuanyi Lu, Zhichao Hu
url: http://arxiv.org/abs/2610.35488v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FeatureLoop: Benchmarking Coding Agents under Evolving Requirements

## Abstract
Software development with coding agents often begins with a rough request that users refine after trying the implementation. Final correctness alone does not capture the repeated guidance this process requires. We introduce FeatureLoop, a benchmark of 61 human-reviewed tasks from 34 repositories across five primary programming languages and seven software forms. Each task follows one development goal in a persistent workspace through evolution feedback, which adds or clarifies requirements, and completion feedback, which reports failures of stated requirements. Cumulative executable checks track new behavior, repair, and preservation of earlier functionality. We evaluate 12 frontier models and find that the strongest completes 72.1% of tasks with both feedback types. Across models, however, only 15.4% of observed failed stages recover within two corrective revisions. Further analysis reveals incomplete repairs, regressions, and model-specific differences in feedback use and token efficiency, identifying obstacles to reliable, low-intervention development.

## Metadata
- **Published**: 2026-10-26T14:15:53Z
- **Authors**: Jia Feng, Alyssa Wu, Cuiyun Gao, Yunlong Wang, Songyuanyi Lu, Zhichao Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35488v1)