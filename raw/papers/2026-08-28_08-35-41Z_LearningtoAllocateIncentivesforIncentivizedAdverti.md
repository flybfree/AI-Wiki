---
title: Learning to Allocate Incentives for Incentivized Advertising via Offline Model-Based Reinforcement Learning
published: 2026-08-28T08:35:41Z
authors: Zilin Zhao, Han Yang, Tianpei Yang, Fangsheng Huang, Yanfei Cui, Kan Peng, Yi Li, Yiming Zong, Hao Zhang, Yinsong Xue
url: http://arxiv.org/abs/2608.28065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Allocate Incentives for Incentivized Advertising via Offline Model-Based Reinforcement Learning

## Abstract
Complete your ad view and grab a 5-cent bonus! In incentivized advertising, a platform promises users a bonus before observing downstream ad revenue, encouraging them to click and complete ads. It must balance the incentive promised in advance against the revenue realized afterward: insufficient incentives forfeit monetization opportunities, whereas excessive incentives reduce net profit. Because current incentives may also shape user expectations and future engagement, incentive allocation is a sequential decision problem with delayed revenue, cost sensitivity, and carryover effects.   Existing work has not studied decision-making algorithms for this setting. Auto-bidding assumes available ad opportunities, while targeted promotion optimizes incentives outside the ad monetization pipeline. We formulate the problem as an MDP and develop an offline model-based RL framework for cost-controllable sequential incentive allocation. It learns a world model of user feedback and ad revenue, then performs conservative policy optimization. An independent counterfactual scorer evaluates each learned policy on held-out logs, enabling pre-launch selection without costly online exposure. Experiments on large-scale industrial data and online A/B tests show that the scorer provides a stable offline signal. The deployment path from causal inference to offline RL and then Offline-MBRL further validates the framework: MB-IQL improves per-user net profit by 7.96\% over TD3+BC, whereas reverting to plain IQL reduces it by 6.56\% (both \(p<0.0001\)).

## Metadata
- **Published**: 2026-08-28T08:35:41Z
- **Authors**: Zilin Zhao, Han Yang, Tianpei Yang, Fangsheng Huang, Yanfei Cui, Kan Peng, Yi Li, Yiming Zong, Hao Zhang, Yinsong Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28065v1)