---
title: DAPD: Dual-Anchored Policy Distillation
published: 2026-08-03T06:00:44Z
authors: Jianyu Wu, Yizhou Wang, Encheng Su, Chen Tang, Shixiang Tang
url: http://arxiv.org/abs/2608.01735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DAPD: Dual-Anchored Policy Distillation

## Abstract
On-policy (self) distillation (OPSD) is increasingly adopted for language-model post-training. It strengthens the teacher with privileged information but can induce a privilege illusion: the student learns privilege-dependent behavior it cannot reproduce from its inference-time context, yet behaves as if the training-time privileged information remained available, ultimately degrading performance. In this paper, we identify information asymmetry between the privileged teacher and the student at inference as the root cause of this failure in OPSD. To resolve this asymmetry, we propose Dual-Anchored Policy Distillation (DAPD), a unified framework with two levels of anchoring. Dual-Path Anchoring (DPA) introduces a self-conditioned bridge and aligns reference and rollout behavior along two matched-information paths, preventing privilege-dependent behavior from being transferred to the inference-time student. Dual-Source Anchoring (DSA) applies these paths in both reference-to-rollout and rollout-to-reference directions, reducing reliance on privileged reference guidance while preserving correctness supervision. Extensive experiments show that DAPD significantly alleviates privilege illusion, outperforming OPSD on Qwen3-4B by +2.00 points on average across tasks. Notably, its gains persist across scales, reaching +2.69 at 4B and +2.78 at 32B.

## Metadata
- **Published**: 2026-08-03T06:00:44Z
- **Authors**: Jianyu Wu, Yizhou Wang, Encheng Su, Chen Tang, Shixiang Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01735v1)