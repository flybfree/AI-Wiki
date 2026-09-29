---
title: DashAct: A Progressive Diagnostic Benchmark for GUI Agents in Interactive Dashboard Analysis
published: 2026-09-26T08:58:50Z
authors: Chuhan Zhang, Qi Xie, Ziyue Wang, Jianing Yin, Yunfan Zhou, Dazhen Deng, Yingcai Wu
url: http://arxiv.org/abs/2609.32385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DashAct: A Progressive Diagnostic Benchmark for GUI Agents in Interactive Dashboard Analysis

## Abstract
Interactive dashboards require users to reveal and connect evidence across stateful interactions. Although graphical user interface (GUI) agents could automate this process, existing dashboard benchmarks primarily report final answers or task success. They provide limited insight into whether failures arise from maintaining the analytical process, selecting actions, or grounding visual targets. We introduce DashAct, to our knowledge the first benchmark to diagnose these failures at a fine-grained level within the same dashboard task. DashAct contains 357 human-verified interaction trajectories with milestone dependencies and hierarchical target annotations. Its progressive diagnostic cascade evaluates end-to-end execution, restores verified context for next-action prediction, and provides target semantics and a local view for visual grounding. By progressively restoring the conditions for success, DashAct measures the minimum support an agent needs to recover rather than scoring isolated skills. Experiments show that current models struggle even as support is added. The cascade outcomes reveal bottlenecks hidden by end-to-end scores and provide actionable guidance for improving GUI agents.

## Metadata
- **Published**: 2026-09-26T08:58:50Z
- **Authors**: Chuhan Zhang, Qi Xie, Ziyue Wang, Jianing Yin, Yunfan Zhou, Dazhen Deng, Yingcai Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32385v1)