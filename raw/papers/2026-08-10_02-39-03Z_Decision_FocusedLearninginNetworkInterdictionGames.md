---
title: Decision-Focused Learning in Network Interdiction Games
published: 2026-08-10T02:39:03Z
authors: Luca M. Hartmann, Parinaz Naghizadeh
url: http://arxiv.org/abs/2608.09036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decision-Focused Learning in Network Interdiction Games

## Abstract
We study decision-focused learning (DFL) in shortest-path network interdiction (SPNI) games, a Stackelberg game where an interdictor (leader) strengthens the networks' arcs against attacks, while an evader (follower) who is uncertain about costs of attacking network arcs relies on a machine-learned predictor to identify the shortest path. While DFL is highly effective as an end-to-end optimization framework, we show that it faces a fundamental structural failure when employed in this game setting: its training objective admits a broad decision-equivalence class of cost estimators that achieve zero nominal loss yet fail under interdiction, reversing DFL's usual advantage over a naive prediction-focused learning (PFL) approach. To address this, we propose Adversarial DFL (A-DFL), which replaces nominal training samples with interdicted scenarios to collapse the harmful equivalence class. Experiments on synthetic and real-world networks confirm that A-DFL restores DFL's advantage in this game setting, enabling effective end-to-end optimization.

## Metadata
- **Published**: 2026-08-10T02:39:03Z
- **Authors**: Luca M. Hartmann, Parinaz Naghizadeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09036v1)