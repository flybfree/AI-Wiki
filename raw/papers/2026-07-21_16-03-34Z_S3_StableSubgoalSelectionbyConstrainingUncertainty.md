---
title: S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning
published: 2026-07-21T16:03:34Z
authors: Kshitij Kumar Srivastava, Kshitij Jerath
url: http://arxiv.org/abs/2607.19232v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning

## Abstract
Hierarchical Reinforcement Learning (HRL) intends to separate strategic planning from primitive execution. It has been widely successful in solving long-horizon and complex tasks, where flat-RL algorithms have difficulty in learning. However, while the low-level agent in HRL benefits from dense feedback and abundant trial opportunities, the high-level agent receives sparse, delayed feedback from the environment and its performance depends on the low-level execution capability. In this paper, we study whether subgoal selection by the high-level agent can be performed more strategically, by providing it with dynamics-aware intrinsic motivation. Since motivation based on primitive transition dynamics would require broad coverage of the state-action space, we propose to use coarse dynamics, i.e., environment transitions aggregated over multiple steps at the temporal scale at which the high-level agent operates. This approach stabilizes the high-level policy by learning to minimize the predictive uncertainty associated with the coarse dynamics, and provides a guided structure for navigation. We model the predictive uncertainty by evaluating different dispersion metrics as approximated by a Mixture Density Network (MDN). Empirically, we observe that a dense, dynamics-aware intrinsic reward leads to risk-averse subgoal selection, enabling it to outperform state-of-the-art HRL methods in non-stationary long-horizon environments.

## Metadata
- **Published**: 2026-07-21T16:03:34Z
- **Authors**: Kshitij Kumar Srivastava, Kshitij Jerath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19232v1)