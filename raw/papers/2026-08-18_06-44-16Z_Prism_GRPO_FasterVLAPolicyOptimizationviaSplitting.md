---
title: Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups
published: 2026-08-18T06:44:16Z
authors: Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping, Han Ding, Guande Wu, Panpan Xu, Jun Huan
url: http://arxiv.org/abs/2608.17423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups

## Abstract
GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose rollouts all succeed or all fail have zero advantage and are discarded by dynamic sampling. These groups are especially common early in training, when most rollouts fail, wasting much of the expensive robotic rollout budget. We introduce Prism-GRPO, which augments binary outcome reward with a weighted trajectory-level execution-quality score. By splitting same-outcome groups into a quality spectrum, Prism-GRPO recovers training signal while ensuring that every success still outranks every failure. Quality scores can be derived from simulator contacts, executed actions, or visual observations, avoiding task-specific progress rewards. We prove that Prism-GRPO never increases the probability that a sampled group is discarded for having zero advantages, and derive a gradient-alignment condition under which its combined update remains a local ascent direction for task success. Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts. It also suppresses a reward-hacking shortcut, with the cleaner behavior transferring under direct deployment to a real robot. Through ablations, we show consistent gains across contact-, smoothness-, and VLM-derived quality signals.

## Metadata
- **Published**: 2026-08-18T06:44:16Z
- **Authors**: Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping, Han Ding, Guande Wu, Panpan Xu, Jun Huan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17423v1)