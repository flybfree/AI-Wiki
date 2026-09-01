---
title: Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation
url: http://arxiv.org/abs/2608.29846v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_15-22-46Z_Influence_DirectedDistillation_SolvingtheDiversity.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles the diversity bottleneck in sampled-token on-policy distillation by introducing Influence-Directed Adaptive On-Policy Distillation (IDA-OPD). It shows that IDA-OPD improves pass@k and matches strong teacher-informed methods while using only sampled-token log probabilities, unlike costly full-vocabulary objectives.

## Key Takeaways
- First-order local entropy influence decouples each update's entropy effect into the teacher-student log-probability gap and the student's local probability structure, linking entropy contraction to negative-influence positions.
- IDA-OPD replaces expensive full-vocabulary forward KL with divergence-adaptive advantage shrinkage using only sampled-token log probabilities, preserving entropy-expanding updates while shrinking entropy-contracting ones.
- Experiments demonstrate that IDA-OPD consistently improves pass@k, inherits the teacher's diversity, matches the strongest teacher-informed methods at strictly lower cost, and broadly maintains vanilla OPD's pass@1 without full-vocabulary teacher information.

## Context
On-policy distillation aims to efficiently transfer knowledge from large teacher models to smaller student models. Traditional approaches often rely on expensive full-vocabulary objectives that limit scalability and practical deployment in real-world settings.

## Implications
IDA-OPD offers a scalable solution for high-quality, diversity-preserving distillation on reasoning tasks, reducing computational overhead while maintaining strong performance, which benefits both researchers and industry practitioners seeking efficient model compression.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29846v1)
