---
title: Locally-Guided Actor-Critic: Training a Goal-conditioned Actor with a Subgoal-aware Critic
published: 2026-08-31T08:00:40Z
authors: Olivier Serris, Stéphane Doncieux, Olivier Sigaud
url: http://arxiv.org/abs/2608.30406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locally-Guided Actor-Critic: Training a Goal-conditioned Actor with a Subgoal-aware Critic

## Abstract
Goal-conditioned reinforcement learning struggles with long horizons when rewards are sparse. While a planner can provide subgoals to guide a low-level policy, its use at test time may introduce practical subgoal management difficulties. An alternative paradigm utilizes a high-level planner to assist learning, while the policy remains conditioned only on the final goal, enabling planner-free deployment. Among these methods, Reinforcement Learning with Imagined Subgoals (RIS) introduces a regularization term that encourages the policy to take the same actions for the final goal as it does for an intermediate goal. This regularization, however, may lead to goal-chaining issues when intermediate goals are low-dimensional. Potential-based reward shaping (PBRS) translates plans into an additional reward while ensuring that the optimal policy remains unchanged. Yet, it can generate deceptive rewards in terminal states. We study these failure cases and first propose an alternative reward shaping method (RS) that removes these deceptive rewards at the expense of theoretical guarantees of PBRS. Similar to this RS variant, we then propose another method named Locally-Guided Actor Critic (LG-AC) that rewards the agent for reaching intermediate goals. Unlike RS, where intermediate rewards are implicit in the shaping signal, we explicitly condition a value estimator on the full sequence of intermediate goals but represent the value function as a sum of subgoal-conditioned value functions, enabling dense hindsight relabeling. We evaluate all these methods in tasks with challenging goal-chaining requirements and empirically highlight specific cases in which either action regularization or reward shaping yield low performance, while LG-AC achieves the best overall performance across tasks.

## Metadata
- **Published**: 2026-08-31T08:00:40Z
- **Authors**: Olivier Serris, Stéphane Doncieux, Olivier Sigaud
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30406v1)