---
title: $R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning
published: 2026-08-26T17:25:10Z
authors: Lehong Wu, Yuxiao Qu, Zheyuan Hu, Ivan Zhang, Limin Wei, Zackory Erickson, Aviral Kumar
url: http://arxiv.org/abs/2608.26053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning

## Abstract
Reasoning in language allows foundation models to spend more test-time compute on hard problems, such as those requiring decomposition, constraint tracking, and prediction of future consequences. Whether this mechanism can improve robotic manipulation remains unclear, where long-horizon tasks require tracking partial progress, reasoning about object relations, recovering from mistakes, and steering noisy low-level policies. In this paper, we study whether VLMs can be trained to reason directly in natural language to guide low-level manipulation policies. We introduce $R^3$, a simple post-training recipe that turns off-the-shelf VLMs into robotic reasoners: it first mid-trains a VLM on expert-generated reasoning traces to initialize the desired reasoning style, then improves the reasoner with single-step rubric-based RL from offline action data. Unlike prior robotic reasoning methods that mostly use structured traces as auxiliary supervision, $R^3$ trains free-form language reasoning to produce test-time guidance for action. We instantiate $R^3$ on Language Table and simulated bimanual grocery packing, two controlled testbeds for studying robotic reasoning and long-horizon manipulation. $R^3$ improves exploration and generalization across unseen tasks and significantly outperforms instruction-only imitation learning baselines on both benchmarks. Our analyses suggest that free-form language reasoning can function as a test-time compute mechanism for steering low-level policies. Our project page is available at https://robotic-reasoner.github.io/.

## Metadata
- **Published**: 2026-08-26T17:25:10Z
- **Authors**: Lehong Wu, Yuxiao Qu, Zheyuan Hu, Ivan Zhang, Limin Wei, Zackory Erickson, Aviral Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26053v1)