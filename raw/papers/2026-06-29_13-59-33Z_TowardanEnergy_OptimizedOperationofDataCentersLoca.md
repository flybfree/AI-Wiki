---
title: Toward an Energy-Optimized Operation of Data Centers Located in Wind Farms Using Reinforcement Learning
published: 2026-06-29T13:59:33Z
authors: Jan Stenner, Alexander Kilian, Sebastian Peitz, Hermann de Meer
url: http://arxiv.org/abs/2606.30316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward an Energy-Optimized Operation of Data Centers Located in Wind Farms Using Reinforcement Learning

## Abstract
This paper studies Reinforcement Learning as an online controller for curtailment-aware workload shifting in wind-turbine-integrated high-performance computing (HPC) data centers. We introduce a reproducible fixed-day simulation framework with synthetic wind and price signals and delayed completion feedback, designed to be extensible toward more complex scenarios. As a controlled benchmarking basis, we then focus on the minimal case with one wind turbine and one co-located data center. In this setting, pure Reinforcement Learning exhibits a pronounced credit-assignment problem and tends to underuse free wind energy early in the day. We therefore evaluate two complementary countermeasures: optimization-based Imitation Learning and potential-based Reward Shaping. Across multi-seed training and a 200-day test set, Proximal Policy Optimization (PPO) and a Soft Actor-Critic (SAC) variant with an additional on-policy update routine achieve strong empirical performance among learned policies, and both Imitation Learning and Reward Shaping provide improvements in relevant configurations. A performance gap to the optimizer remains, which is expected: the optimizer plans offline with full-day foresight, whereas Reinforcement Learning must decide online from current observations without future realizations. The benchmark and ablation results provide a transparent basis for extending the approach toward richer multi-site and continuous-time scenarios.

## Metadata
- **Published**: 2026-06-29T13:59:33Z
- **Authors**: Jan Stenner, Alexander Kilian, Sebastian Peitz, Hermann de Meer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.30316v1)