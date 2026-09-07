---
title: Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection
published: 2026-09-04T07:00:51Z
authors: Jingyi Wang, Da Li, Kaixin Wang, Zhangqin Huang
url: http://arxiv.org/abs/2609.04803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection

## Abstract
Pass receiver selection is a fundamental task in football analytics, aiming to predict the intended receiver under a given game state. This task is challenging with event-centered freeze-frame observations, a broadcast-like setting that provides only partial and variable player visibility without complete trajectories or stable player identities. The model must therefore reason over anonymous visible candidates, opponent pressure, and recent context under partial observation. To address this setting, we propose a Hierarchical Possession-aware Graph Pointer Network (HPGPN), which formulates pass receiver selection as variable-size candidate prediction over visible teammates. HPGPN jointly models current player interactions, local event context, and possession-level temporal dynamics. It represents the current pass situation with a graph, incorporates fixed event context, and uses dynamic possession history to capture how the attacking sequence evolves. Candidate representations are refined hierarchically by integrating spatial, contextual, and historical evidence, and a glimpse pointer head scores the receiver candidates. Experiments on public football event and freeze-frame data show that HPGPN improves pass receiver selection performance. Ablation studies demonstrate the effectiveness of graph-based interaction modeling, fixed event context, and dual-branch dynamic possession-history modeling.

## Metadata
- **Published**: 2026-09-04T07:00:51Z
- **Authors**: Jingyi Wang, Da Li, Kaixin Wang, Zhangqin Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04803v1)