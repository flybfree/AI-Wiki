---
title: AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery
published: 2026-08-02T15:12:58Z
authors: Yaoyu Su
url: http://arxiv.org/abs/2608.01303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery

## Abstract
Symbolic alpha factor discovery can score a completed expression, but it provides no direct label for the structural decisions that produced it. Generative flow networks (GFlowNets) preserve a diverse, reward-proportional distribution over complete expressions, yet their trajectory-level objective does not compare unchosen sibling actions at an intermediate state. We introduce AlphaG-OPD, a structural on-policy distillation framework that turns terminal factor evaluations into local action guidance. Its design separates three decisions. Component I determines where to teach by exposing grammar-valid siblings at partial abstract-syntax-tree (AST) states visited by the current forward policy. Component II determines what is reliable enough to teach: it evaluates three supported siblings under four shared suffixes and admits a KL-bounded target only when their matched comparisons exhibit sufficient winner agreement and a positive empirical lower confidence bound (LCB). Component III determines how strongly and for how long to teach by consolidating accepted targets through bounded replay, score-indexed expiry, and forward-gradient balancing, without additional factor evaluations. Terminal reward, Trajectory Balance, the backward policy, grammar, and factor-pool rules remain unchanged. An equal-physical-score four-arm ablation tests paired teaching, reliability gating, and consolidation. Across China's CSI300, CSI500, and CSI1000 and the U.S. S&P 500, the complete method delivers strong cross-market performance over multiple random seeds.

## Metadata
- **Published**: 2026-08-02T15:12:58Z
- **Authors**: Yaoyu Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01303v1)