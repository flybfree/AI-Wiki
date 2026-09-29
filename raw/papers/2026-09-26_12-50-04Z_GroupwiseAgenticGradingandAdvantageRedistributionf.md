---
title: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL
published: 2026-09-26T12:50:04Z
authors: Jinhao Dong, Liang Zhao, Zihao Yue, Wenhan Ma, Linghao Zhang, Lei Li, Shicheng Li, Yifan Song, Bowen Ye, Fuli Luo
url: http://arxiv.org/abs/2609.32577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL

## Abstract
Reinforcement learning (RL) for code agents often uses executable tests to provide binary rewards. With these rewards, Group Relative Policy Optimization (GRPO) assigns identical advantages to test-passing trajectories within each rollout group, overlooking differences in implementation quality and adherence to task requirements. This leaves the policy without a learning signal that favors clean, targeted implementations over those containing unnecessary or out-of-scope changes. We introduce GAGAR, a framework for quality-aware credit redistribution in code agent RL. Built on dynamic sampling that retains groups containing both passing and failing trajectories, GAGAR places all trajectories from each group in a shared workspace, where an SFT-trained agentic grader jointly inspects them and ranks the test-passing candidates. Based on this ranking, we downweight lower-ranked trajectories and proportionally rescale the advantages of all test-passing trajectories to restore their original sum. This sum-preserving redistribution retains the relative weights established by quality-based downweighting while shifting credit toward higher-quality implementations. We evaluate GAGAR at industrial scale using pre-RL SFT checkpoints of MiMo-V2.6-Flash (310B total parameters) and MiMo-V2.6-Pro (1.02T total parameters). Controlled code-only Flash experiments show improved code agent performance, reduced trajectory-length growth, and more stable training. We further apply GAGAR in large-scale mixed-task RL with both Flash and Pro. Our results support combining test-based verification with groupwise agentic grading to improve the quality and stability of code agent RL.

## Metadata
- **Published**: 2026-09-26T12:50:04Z
- **Authors**: Jinhao Dong, Liang Zhao, Zihao Yue, Wenhan Ma, Linghao Zhang, Lei Li, Shicheng Li, Yifan Song, Bowen Ye, Fuli Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32577v1)