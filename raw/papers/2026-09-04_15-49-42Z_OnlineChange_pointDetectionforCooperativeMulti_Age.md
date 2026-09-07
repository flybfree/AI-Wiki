---
title: Online Change-point Detection for Cooperative Multi-Agent Reinforcement Learning
published: 2026-09-04T15:49:42Z
authors: Fatemeh Saberi Khomami, Julita Vassileva
url: http://arxiv.org/abs/2609.05298v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Change-point Detection for Cooperative Multi-Agent Reinforcement Learning

## Abstract
Cooperative multi-agent reinforcement learning (MARL) systems rely on past experience for learning coordinated behaviour, but this experience may become unreliable if the environment or task objective changes during training. In such cases, agents first need a way to recognize that the situation has changed before deciding how to adapt. This paper studies online change-point detection for cooperative MARL using reward-derived signals. We propose \emph{Patterns of Past Rewards} (PPR), a lightweight algorithm-agnostic detector that smooths agents' return streams, highlights recent changes, and applies a statistical drift detector to flag significant shifts. We evaluate PPR in a custom Speaker-Listener environment based on the Multi-Agent Particle Environment under two controlled non-stationarity scenarios. Our results show a trade-off between detection speed and alarm stability. A smoothed-return baseline detects earlier but produces many repeated alarms. In contrast, applying the detector directly to raw returns often misses the shift. PPR offers a more balanced approach by limiting redundant detections while still identifying the controlled shifts. These findings highlight PPR as a lightweight, reward-based monitoring tool that enables cooperative MARL systems to reliably identify major changes during training.

## Metadata
- **Published**: 2026-09-04T15:49:42Z
- **Authors**: Fatemeh Saberi Khomami, Julita Vassileva
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05298v1)