---
title: Stochastic Control Policies for Robust Molecular Transition Path Sampling
published: 2026-08-13T22:07:59Z
authors: Jingqian Liu, Yu-Hsiang Wang, Yanru Qu, Ge Liu
url: http://arxiv.org/abs/2608.13800v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stochastic Control Policies for Robust Molecular Transition Path Sampling

## Abstract
Transition path sampling (TPS) aims to efficiently generate rare molecular transition trajectories between metastable states and is essential for understanding biomolecular mechanisms. Beyond traditional molecular dynamics (MD)-based sampling, machine learning has become central to state-of-the-art TPS. One major class of methods learns control forces during explicit MD rollouts. By preserving the underlying molecular dynamics, these methods tend to produce more physically plausible trajectories than endpoint-conditioned generators that construct paths directly. However, rollout-based control methods have been reported to exhibit unstable and strongly seed-dependent performance. We recast rollout-based control as learning a path-space proposal distribution and investigate stochasticity placement as a design choice for improving exploration and optimization robustness. We develop two stochastic policies: FS-TPS, which directly parameterizes a state-dependent Gaussian distribution over the control policy output, and LaS-TPS, which samples a compact latent control variable and decodes it into structured, cross-atom-correlated force variation. We conduct extensive multi-seed experiments on three biomolecular systems of increasing size: alanine dipeptide, chignolin, and BBL, a fast-folding protein. Stochastic policies consistently improve transition success and path quality over deterministic-policy baselines while substantially reducing sensitivity to random initialization.

## Metadata
- **Published**: 2026-08-13T22:07:59Z
- **Authors**: Jingqian Liu, Yu-Hsiang Wang, Yanru Qu, Ge Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13800v1)