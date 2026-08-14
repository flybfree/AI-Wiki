---
title: Fast A/B/n Testing: Exact Multi-Policy Comparison via Tree-Coupled Feedback Sharing
published: 2026-08-13T05:10:43Z
authors: Yuxiao Wen
url: http://arxiv.org/abs/2608.12831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast A/B/n Testing: Exact Multi-Policy Comparison via Tree-Coupled Feedback Sharing

## Abstract
Online platforms increasingly compare many adaptive decision policies---ranking systems, recommendation algorithms, pricing rules, and language-model agents---while each reward-bearing interaction can be costly or risky. A direct A/B/n design gives each of $J$ policies its own horizon-$T$ trajectory and therefore uses $JT$ outcomes. We introduce Tree-Coupled A/B Testing (\TCAB), an exact feedback-sharing design for arbitrary history-dependent contextual-bandit policies. At each round, a predictable tree connects the current policy histories; every parent--child context--action law is maximally coupled, and one reward is shared within each component of matched tree edges. Every policy retains exactly its standalone finite-horizon trajectory law, even though the policies are deliberately dependent. If $D_{e,t}$ records a mismatch on tree edge $e$ at round $t$, the number of reward queries satisfies the pathwise identity $N(T)=T+\sum_{t,e}D_{e,t}$ and hence equals $T$ plus cumulative tree-edge total variation in expectation. This cost is conditionally optimal among exact edge-local designs on the selected tree, and a current-round minimum-spanning tree is myopically optimal among tree designs. For fixed $J$, sublinear pseudo-regret of every policy and almost-sure uniqueness of the oracle action imply $\mathbb{E}[N(T)]=T+o(T)$, versus $JT$ for independent runs. We also obtain finite-sample variance bounds for pairwise policy contrasts. Experiments on reward-model evaluation, multiple-choice language-model evaluation, and adaptive search policies demonstrate substantial improvements in the cost--precision frontier.

## Metadata
- **Published**: 2026-08-13T05:10:43Z
- **Authors**: Yuxiao Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12831v1)