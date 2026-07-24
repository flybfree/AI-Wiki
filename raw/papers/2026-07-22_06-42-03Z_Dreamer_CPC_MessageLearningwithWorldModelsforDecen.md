---
title: Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning
published: 2026-07-22T06:42:03Z
authors: Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi
url: http://arxiv.org/abs/2607.19809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning

## Abstract
In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) into the world model of DreamerV3. Each agent independently maintains a world model and a message module, and infers and exchanges messages from the latent states of the world model that reflect the history of past observations and actions. We evaluated Dreamer-CPC in two environments: Observer, a non-cooperative information-sharing task, and CatchApple, a newly introduced task in which task-relevant observations are temporarily missing. In both environments, Dreamer-CPC outperformed IPPO-CPC, an existing CPC-based method that generates messages from current observations, as well as no-communication baselines. In particular, in CatchApple, Dreamer-CPC achieved 4 to 5 times the episode return of IPPO-CPC, demonstrating effective coordination where other methods fail due to missing observations. These results suggest that communication grounded in the latent dynamics of world models can support decentralized decision-making when current observations alone are insufficient.

## Metadata
- **Published**: 2026-07-22T06:42:03Z
- **Authors**: Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19809v1)