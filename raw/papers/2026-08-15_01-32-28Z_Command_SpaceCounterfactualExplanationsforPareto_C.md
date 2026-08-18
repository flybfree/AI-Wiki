---
title: Command-Space Counterfactual Explanations for Pareto-Conditioned Reinforcement Learning
published: 2026-08-15T01:32:28Z
authors: Joanikij Chulev, Hendrik Baier
url: http://arxiv.org/abs/2608.14963v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Command-Space Counterfactual Explanations for Pareto-Conditioned Reinforcement Learning

## Abstract
Pareto Conditioned Networks learn multiple multi-objective reinforcement learning behaviours by conditioning a single policy on a desired return command. However, the local mapping from command and state to action remains opaque. We propose command-space counterfactual explanations for PCNs: given a fixed state, original command, and foil action, we search, in a black-box setting, for a minimally changed desired-return command under which the same trained policy would choose the foil. Our contributions are threefold. First, we formulate PCN explanations as return-command interventions, using a return-only PCN variant that avoids the added ambiguity of horizon-conditioning. Second, we adapt adversarial machine learning methods to reinforcement-learning explanations. Third, we introduce a boundary-seeded directional search that improves over purely local optimization in the command-action landscape, resulting in our proposed approach CF-ZOO. The resulting explanations are actionable and intuitively expressed in the user's own preferences: "If your trade-off had shifted slightly towards X, the agent would have chosen Y."

## Metadata
- **Published**: 2026-08-15T01:32:28Z
- **Authors**: Joanikij Chulev, Hendrik Baier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14963v1)