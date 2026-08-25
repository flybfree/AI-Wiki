---
title: MOSH-WM: Mask-Grounded Soft-Hamiltonian Dynamics for Object-Centric World Models
published: 2026-08-24T03:17:21Z
authors: Zhekai Wang, Haoxiang Huang, Xiang Liu, Zhikang Chen, Yueqing Sun, Qi Gu, Shiji Zhou, Miao Liu, Sen Cui
url: http://arxiv.org/abs/2608.22750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOSH-WM: Mask-Grounded Soft-Hamiltonian Dynamics for Object-Centric World Models

## Abstract
Object-centric world models forecast future videos by evolving a set of entity slots, but the variables receiving dynamics supervision are often unconstrained visual features. We introduce \method{}, a mask-grounded soft-Hamiltonian world model that makes its position-like state explicitly depend on slot-owned image support. A frozen video-slot encoder produces slots and masks; spatial moments of mask-owned support form a canonical state $Q$, temporal differences form $P$, and a learned energy supplies a soft directional bias to a bounded learned increment. Decoder-relevant appearance and identity are stored separately in a causal visual context. A gated composer and bounded residual then combine this context with the propagated phase state to reconstruct decoder-compatible slots. On OBJ3D, given six observed frames and evaluated over the following 30 frames, \method{} reduces LPIPS by 25.0\% and spatial MSE by 33.7\% relative to the strongest object-centric baseline. On CLEVRER, given six observed frames and evaluated over the following ten frames, the corresponding reductions are 14.5\% and 18.7\%. Horizon-resolved visual and object-state measurements show that the complete model accumulates error more slowly throughout the 30-frame closed-loop rollout. Project page:https://github.com/moshwm-anon/-moshwm-anon.github.io.

## Metadata
- **Published**: 2026-08-24T03:17:21Z
- **Authors**: Zhekai Wang, Haoxiang Huang, Xiang Liu, Zhikang Chen, Yueqing Sun, Qi Gu, Shiji Zhou, Miao Liu, Sen Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22750v1)