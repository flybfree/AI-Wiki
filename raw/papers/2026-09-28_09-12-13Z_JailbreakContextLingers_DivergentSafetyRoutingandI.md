---
title: Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents
published: 2026-09-28T09:12:13Z
authors: Xi Wang, Songlei Jian, Yiming Zhang, Bin Ji, Zhaoye Li, Ma Jun, Baosheng Wang, Jie Yu
url: http://arxiv.org/abs/2609.34686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents

## Abstract
As large language models increasingly operate as tool-using agents, post-jailbreak safety feedback is often assumed to serve as a reliable safeguard; however, how lingering jailbreak context shapes subsequent agent behavior remains largely unexplored. To systematically examine this dynamic, we introduce a paired continuation framework across 192 parent tasks spanning 42 domains, evaluating 12,148 analyzed continuation pairs (curated from a 12,288-pair initially design) across eight diverse agents. We find that identical safety feedback induces sharply model-dependent behavioral routing rather than uniform protection: redirecting unsafe trajectories toward legitimate completion (\emph{rescue}), sustaining unauthorized execution (\emph{persistent unsafe}), or triggering over-refusal on benign tasks (\emph{collateral loss}). Through layer-wise activation patching, we discover a shared \emph{late-commit pattern} where causal intervention effects surge sharply near the final layers (relative depths of 0.958--0.984) despite an over 30-fold variation in peak magnitude across architectures. Crucially, critical-layer representations correlate with macroscopic routing outcomes, and intervening at these layers causally alters concrete next-step tool actions. Building on this causal foundation, we test whether localized intervention-derived features can serve as predictive proxies for full-trajectory routing outcomes on unseen parent tasks under leave-one-parent-task-out evaluation, finding that they provide viable predictive signals in responsive agents with peak ROC AUCs reaching 0.675 for \emph{rescue}, 0.777 for \emph{collateral loss}, and 0.702 for \emph{persistent unsafe}. These findings establish a mechanistic lens and a predictive baseline for anticipating the safety and utility trade-offs of post-jailbreak feedback in autonomous agents.

## Metadata
- **Published**: 2026-09-28T09:12:13Z
- **Authors**: Xi Wang, Songlei Jian, Yiming Zhang, Bin Ji, Zhaoye Li, Ma Jun, Baosheng Wang, Jie Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34686v1)