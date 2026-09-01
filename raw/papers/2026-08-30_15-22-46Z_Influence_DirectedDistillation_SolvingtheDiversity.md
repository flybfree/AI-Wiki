---
title: Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation
published: 2026-08-30T15:22:46Z
authors: Run Yang, Runpeng Dai, Jie Sun, Jielei Zhang, Fan Zhou, Hongtu Zhu, Peiyi Li, Longwen Gao
url: http://arxiv.org/abs/2608.29846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation

## Abstract
Sampled-token on-policy distillation (OPD) efficiently transfers capabilities from teacher to student using student-generated tokens, requiring teacher probabilities only for sampled tokens. Yet it frequently suffers from diversity distillation failure: the student's pass@1 improves while its pass@$k$ plateaus, failing to inherit the teacher's diversity. To explain this, we introduce First-Order Local Entropy Influence, a signed first-order proxy that decouples each update's entropy effect into the teacher--student log-probability gap and the student's local probability structure, and empirically links entropy contraction to negative-influence positions. Motivated by this, we propose Influence-Directed Adaptive On-Policy Distillation (IDA-OPD): rather than relying on costly full-vocabulary Forward-KL objectives, it preserves entropy-expanding updates while replacing entropy-contracting ones with divergence-adaptive advantage shrinkage, using only the teacher's sampled-token log-probability. Experiments on reasoning-oriented distillation show IDA-OPD consistently improves pass@$k$, inheriting the teacher's diversity through distillation, matches the strongest teacher-informed methods at strictly lower cost, and broadly maintains vanilla OPD's pass@1, all without full-vocabulary teacher information.

## Metadata
- **Published**: 2026-08-30T15:22:46Z
- **Authors**: Run Yang, Runpeng Dai, Jie Sun, Jielei Zhang, Fan Zhou, Hongtu Zhu, Peiyi Li, Longwen Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29846v1)