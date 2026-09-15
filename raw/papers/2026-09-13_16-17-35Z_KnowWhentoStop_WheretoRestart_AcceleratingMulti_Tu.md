---
title: Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation
published: 2026-09-13T16:17:35Z
authors: Zhiyu Gui, Kexin Huang, Jia Guo, Junkang Wu, Zihao Wang, Zhiqiang Zhang, Jun Zhou, Jiancan Wu, Xiang Wang
url: http://arxiv.org/abs/2609.14636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation

## Abstract
On-policy distillation (OPD) has become a standard approach for transferring capabilities from large teachers to compact students. Its cost, however, is dominated by autoregressive student rollouts and scales poorly in multi-turn agentic settings. Existing acceleration methods truncate or relocate the supervision signal according to fixed, offline budgets, despite substantial variation in teacher-signal reliability both within and across trajectories. Our empirical analysis on $τ^2$-bench reveals a clear structure in this variation: informative supervision is concentrated in the prefix of each turn, and, most importantly for multi-turn agentic training, the cross-turn loss of teacher endorsement is temporally locked to the student's first erroneous action rather than accumulating gradually over turns. Building on these findings, we propose STRIDE (Stop-and-Restart on-policy Distillation acceleration), which combines two complementary techniques: adaptive early stopping, which terminates a rollout once the cumulative teacher log-probability falls below an out-of-distribution threshold, and a prefix buffer, which caches high-quality prefixes and restarts generation at the weakest correct turn. Together, these mechanisms induce a data-driven curriculum that progressively extends coverage to later turns. On $τ^2$-bench retail, our method matches full-trajectory OPD and exceeds the 30B teacher at a $3.73\times$ speedup, surpasses the baseline itself at $2.34\times$, and retains a $4.51\times$ speedup under cross-domain multi-teacher training. As a supplementary generalization test beyond the agentic setting, STRIDE outperforms full OPD on AIME 2025 at a $5.10\times$ speedup and on AIME 2024 at a $3.08\times$ speedup; averaged across the two evaluations, both fixed-budget truncation baselines remain below full OPD.

## Metadata
- **Published**: 2026-09-13T16:17:35Z
- **Authors**: Zhiyu Gui, Kexin Huang, Jia Guo, Junkang Wu, Zihao Wang, Zhiqiang Zhang, Jun Zhou, Jiancan Wu, Xiang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14636v1)