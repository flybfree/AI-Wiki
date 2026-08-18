---
title: SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning
published: 2026-08-17T08:23:05Z
authors: Jaewan Choi, Junyoung Yang, Sangdon Park
url: http://arxiv.org/abs/2608.16249v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning

## Abstract
Machine unlearning in Large Language Models (LLMs) faces a critical trade-off between erasing target knowledge and preserving general utility. We propose SAUL (Sharpness-Aware Augmented-Lagrangian Unlearning), which formulates unlearning as a constrained minimization problem following the principle of "forget enough, but no more than necessary." At its core, SAUL formulates forgetting as an explicit constraint with a prescribed satisfaction criterion, whereas prior unlearning methods typically specify the desired level of forgetting implicitly through optimization objectives. An augmented Lagrangian controller adaptively adjusts forget-side pressure according to constraint violation and can eventually deactivate the forget-side update as the prescribed criterion remains satisfied. Sharpness-aware updates on both retain and forget objectives, together with a dual-optimizer design that maintains role-separated states, further stabilize the resulting unlearning dynamics. We evaluate SAUL on the TOFU, WMDP, and MUSE benchmarks, demonstrating favorable forgetting-utility trade-offs over representative sharpness- and perturbation-based baselines under benchmark-specific forgetting criteria. Beyond the complete SAUL framework, we further show on TOFU that applying the augmented-Lagrangian controller as a drop-in modifier to representative baselines improves their post-forgetting utility, demonstrating the practical value of explicit forgetting control.

## Metadata
- **Published**: 2026-08-17T08:23:05Z
- **Authors**: Jaewan Choi, Junyoung Yang, Sangdon Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16249v1)