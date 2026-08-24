---
title: CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents
published: 2026-08-21T13:58:56Z
authors: Jiancheng Wang, Mingli Zhu, Tong Zhang, Jiaqi Ruan, Wei Wang, Siyuan Liang, Dacheng Tao
url: http://arxiv.org/abs/2608.21114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents

## Abstract
Visual world-model agents such as DreamerV3 act through a recurrent latent state rather than a single observation, which weakens frame-wise observation attacks and makes their perturbations vary sharply over time under a strict per-frame perturbation constraint. We study white-box, causal, online attacks on such agents and propose Critic-Induced Value-Subspace Attacks (\textbf{CIVA}). Our key observation is that, along a rollout, critic-guided perturbations concentrate in a low-dimensional subspace induced by the victim's own critic. Based on this observation, CIVA first probes the frozen victim offline with critic-guided PGD and extracts a low-rank value-subspace by SVD. At test time, it optimizes only the subspace coefficients, smooths them with an exponential moving average (EMA), and maps them back to pixels. This design attacks value-sensitive recurrent dynamics while keeping the online optimization cheap and temporally coherent. Extensive experiments on DMC walker walk, Atari Pong, and Crafter show that CIVA consistently outperforms five recent methods; on DMC walker walk, it achieves the largest reward drop of 26.07\% while keeping temporal variation low, with TempAbs of 0.646.

## Metadata
- **Published**: 2026-08-21T13:58:56Z
- **Authors**: Jiancheng Wang, Mingli Zhu, Tong Zhang, Jiaqi Ruan, Wei Wang, Siyuan Liang, Dacheng Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21114v1)