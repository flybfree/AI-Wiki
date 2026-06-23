---
title: On the Position Bias of On-Policy Distillation
url: http://arxiv.org/abs/2606.22600v1
type: paper-summary
date: 2026-06-22
source_paper: 2026-06-21_17-20-21Z_OnthePositionBiasofOn_PolicyDistillation.md
generated_at: 2026-06-22 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the bias in on‑policy distillation where token‑level losses are treated equally, causing later tokens to provide poor supervision as rollouts lengthen. By applying constrained optimization, it introduces Importance‑Weighted On‑Policy Distillation (IW‑OPD) that dynamically upweights earlier tokens and downweights later ones based on distribution discrepancy. Experiments show IW‑OPD converges faster, yields higher learning efficiency, and improves final performance by up to 6.9 points compared with standard OPD.

## Key Takeaways
- Uniform token weighting in OPD leads to degraded supervision at later positions as student rollouts diverge from the teacher’s distribution.  
- The first 30 % of tokens can achieve comparable results to using all tokens, while only the last 30 % contributes little learning value.  
- IW‑OPD assigns importance weights proportional to accumulated discrepancy, resulting in faster convergence and better final performance across same‑size and cross‑scale settings.

## Context
On‑policy distillation aims to accelerate reinforcement learning by leveraging dense teacher feedback, yet standard formulations ignore the temporal decay of supervision quality. This limitation hampers scalability when training long rollouts, prompting a need for adaptive weighting strategies that respect the underlying optimization constraints.

## Implications
For practitioners, IW‑OPD offers a practical way to improve training speed without sacrificing performance, reducing compute costs and enabling larger model sizes. The approach also provides a principled framework for future distillation methods that must account for temporal bias in teacher signals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.22600v1)
