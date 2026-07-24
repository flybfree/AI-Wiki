---
title: Robust Asynchronous Q-Learning under Reward and State Corruption via Batching
published: 2026-07-23T01:21:05Z
authors: Sreejeet Maity, Aritra Mitra
url: http://arxiv.org/abs/2607.20822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Asynchronous Q-Learning under Reward and State Corruption via Batching

## Abstract
Motivated by reinforcement learning in harsh environments, we consider the problem of learning an optimal policy subject to adversarially corrupted feedback. Specifically, at each time-step, an adversary can perturb both the reward and state observations of the learner following the Huber contamination model. To defend against such data corruption, we propose {\texttt{BR-Async-Q}}: a novel, epoch-based, robust \(Q\)-learning algorithm built upon two key ideas: (i) partitioning the online data stream into batches to reduce variance, and (ii) constructing robust estimates of the Bellman optimality operator using such batched data. We prove a high-probability $\ell_\infty$ error bound for {\texttt{BR-Async-Q}} that matches that for vanilla \(Q\)-learning, up to a small additive term that scales with the fraction of corrupted samples. To our knowledge, this provides the first robustness guarantee for asynchronous \(Q\)-learning subject to both reward and state corruption. Furthermore, when only rewards are corrupted, the dependence of our algorithm's bound on the corruption fraction is minimax optimal.

## Metadata
- **Published**: 2026-07-23T01:21:05Z
- **Authors**: Sreejeet Maity, Aritra Mitra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20822v1)