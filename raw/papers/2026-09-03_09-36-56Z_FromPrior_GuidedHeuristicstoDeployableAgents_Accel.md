---
title: From Prior-Guided Heuristics to Deployable Agents: Accelerating Demonstration-Driven Reinforcement Learning for Deadline-Constrained Network Control
published: 2026-09-03T09:36:56Z
authors: Vincenzo Norman Vitale, Mohammad Solki, Antonia Maria Tulino, Andreas F. Molisch, Jaime Llorca
url: http://arxiv.org/abs/2609.03590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Prior-Guided Heuristics to Deployable Agents: Accelerating Demonstration-Driven Reinforcement Learning for Deadline-Constrained Network Control

## Abstract
Timely delivery of delay-sensitive information over dynamic, heterogeneous networks is essential for NextG interactive applications, yet providing strict End-to-End (E2E) peak latency guarantees remains an open challenge. Two obstacles limit the adoption of learning-based network control in this setting: traditional volume-based routing metrics, while highly effective for general traffic management, are not designed to capture traffic urgency; and Deep Reinforcement Learning (DRL) controllers trained from scratch suffer from sample inefficiency, long training times, and early-stage exploration volatility. This paper introduces a deployment-focused network control framework that addresses both obstacles. First, we present Effective Congestion (EC), a deadline-aware metric family that quantifies interface congestion by packet urgency and proactively filters non-viable traffic, coupled with a Uniform Path Grouping (UPG) distribution heuristic promoting robust load-balancing; the resulting policies are embedded into Multi-Agent Deep Reinforcement Learning Effective Congestion ($p^*$) (MADRL EC ($p^*$)), a hybrid architecture combining a distributed scheduler with a centralized RL-based router. Second, we introduce a unified training objective that generalizes existing policy-learning paradigms---behavioral cloning, offline Reinforcement Learning (RL), online RL, and offline-to-online schemes---as special cases, combining a live-reward term, a pre-collected-reward term, and a policy-imitation term. From this objective, we derive the Model-Guided Annealed Reinforcement Learning (MGA-RL) protocol, instantiated on a Deep Deterministic Policy Gradient (DDPG) backbone: a deployment-oriented, demonstration-driven training approach that generalizes conventional Offline-to-Online (O2O) schemes, in which trajectories from a lightweight [...]

## Metadata
- **Published**: 2026-09-03T09:36:56Z
- **Authors**: Vincenzo Norman Vitale, Mohammad Solki, Antonia Maria Tulino, Andreas F. Molisch, Jaime Llorca
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03590v1)