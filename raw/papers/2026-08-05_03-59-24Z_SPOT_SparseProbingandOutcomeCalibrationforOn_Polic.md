---
title: SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation
published: 2026-08-05T03:59:24Z
authors: Zikun Qu, Min Zhang, Mingze Kong, Zhiwei Shang, Yikun Ban, Shuang Qiu, Zhongxiang Dai
url: http://arxiv.org/abs/2608.04419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation

## Abstract
On-policy distillation (OPD) provides dense teacher supervision on student-generated trajectories, but standard reverse-KL training can assign insufficient probability to other plausible continuations. Teacher entropy alone does not reveal whether uncertainty is concentrated among a few plausible next tokens or dispersed over a long probability tail, nor whether the student already represents those candidates well. Moreover, local teacher probabilities may not predict downstream success. We introduce Sparse Probing and Outcome-calibrated Targets OPD (SPOT), which addresses two coupled decisions, where to probe and what to distill, through an acquisition--exploration--exploitation procedure. During acquisition, a position-level score combines normalized teacher entropy, the probability mass captured by a small top-$k$ candidate set, and student--teacher mismatch to allocate a limited probing budget. During exploration, SPOT evaluates teacher-proposed candidates through verifier-scored student continuations. During exploitation, these outcomes produce a closed-form, KL-regularized target that favors candidates with better downstream outcomes while remaining anchored to the teacher distribution. Extensive experiments across multiple student models and reasoning benchmarks demonstrate the effectiveness of SPOT in improving reasoning performance while balancing solution quality and coverage.

## Metadata
- **Published**: 2026-08-05T03:59:24Z
- **Authors**: Zikun Qu, Min Zhang, Mingze Kong, Zhiwei Shang, Yikun Ban, Shuang Qiu, Zhongxiang Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04419v1)