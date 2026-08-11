---
title: A Distribution Mapping Approach to Counterfactually Fair Reinforcement Learning
published: 2026-08-09T14:42:47Z
authors: Jianhan Zhang, Jitao Wang, John D. Piette, Donglin Zeng, Chengchun Shi, Zhenke Wu
url: http://arxiv.org/abs/2608.08743v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Distribution Mapping Approach to Counterfactually Fair Reinforcement Learning

## Abstract
Reinforcement learning (RL) seeks to optimize sequential decisions to maximize population-level benefits over time. However, when deployed in high-stakes settings such as healthcare, RL decisions might systematically restrict some subpopulation's access to valuable services in a manner contrary to the values and goals of stakeholders. Counterfactual fairness (CF) offers a promising framework to address this problem based on causal reasoning. This paper develops a data preprocessing algorithm that, when used in tandem with policy learning, enables CF in RL. Our algorithm relies on a novel quantile distribution mapping method for sequentially estimating the counterfactual states and rewards in the data preprocessing step, subsuming common additivity assumptions used for counterfactual prediction as a special case. We theoretically prove that the per-step level of counterfactual unfairness and infinite-horizon suboptimality gap can be bounded under mild regularity conditions. We also empirically test our algorithm in numerical experiments as well as in application to a real-world interventional digital health dataset.

## Metadata
- **Published**: 2026-08-09T14:42:47Z
- **Authors**: Jianhan Zhang, Jitao Wang, John D. Piette, Donglin Zeng, Chengchun Shi, Zhenke Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08743v1)