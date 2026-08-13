---
title: REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation
published: 2026-08-12T06:15:33Z
authors: Yang Sun, Lichao Ma, Houyuan Qin, Yuxin Liu, Hanyang Lu, Yao Zhu, Pinlong Cai, Guohang Yan
url: http://arxiv.org/abs/2608.11698v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation

## Abstract
On-policy distillation (OPD) trains a student on its own trajectories under dense token-level supervision from a teacher. Reward-extrapolation methods such as ExOPD amplify the teacher-reference log-likelihood ratio to move beyond direct imitation, but apply a single global coefficient $λ$ to every token. This can drive the student to fit extreme peaks in the implicit reward, causing reward hacking and unstable training, and the optimal $λ$ varies across domains, requiring costly sweeps. We propose REOPD, a reliability-adaptive reward extrapolation framework for OPD. REOPD combines a token-level compatibility weight with a batch-level adaptive budget, yielding a token-wise coefficient $λ_{b,t}=1+γ_b q_t$ that preserves teacher alignment while selectively extrapolating along reliable teacher-reference directions. It requires no verifier, reward model, value model, or extra rollout beyond standard OPD. REOPD outperforms G-OPD on single-teacher mathematics and on both domains in the multi-teacher setting, while matching G-OPD on single-teacher code, demonstrating effective fine-grained reliability adaptation across domains and teacher configurations.

## Metadata
- **Published**: 2026-08-12T06:15:33Z
- **Authors**: Yang Sun, Lichao Ma, Houyuan Qin, Yuxin Liu, Hanyang Lu, Yao Zhu, Pinlong Cai, Guohang Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11698v1)