---
title: Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation
url: http://arxiv.org/abs/2610.28586v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_17-40-08Z_CapableTeacher_MyopicScorer_Reward_FreeTeacherRepa.md
generated_at: 2026-10-20 22:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a fundamental flaw in agentic on-policy distillation (OPD): the "rollout-scorer gap," where a teacher model's next-token scoring is myopic and fails to penalize safe but unproductive actions that outcome-based reinforcement learning would reject. The authors propose Rollout-to-Scorer Distillation (R2S), a method that repairs the teacher's scoring behavior before distillation by mining high-disagreement states, running teacher takeovers, and fine-tuning the teacher to produce takeover-informed scores. R2S outperforms three state-of-the-art agentic-OPD methods across all twelve tested teacher-student-environment configurations by an average of 12.8 success points.

## Key Takeaways
- The paper challenges the prevailing "compounding error" explanation for OPD failures. The authors demonstrate that from states where the student diverges most from the teacher, the teacher's own takeovers can still successfully finish the task, yet the student trained on the teacher's token-level scores exhausts its turn budget. This proves the problem is not merely the student wandering outside the teacher's reliable region, but rather the scoring mechanism itself.
- The "rollout-scorer gap" is the core diagnostic contribution: the teacher's next-token scoring evaluates each token in isolation without visibility into episode outcomes. This lets through safe, delaying moves that outcome-based RL would punish with zero reward, a penalty that agentic OPD structurally lacks. The gap exists between what the teacher can do (successful takeovers) and what it scores (locally safe tokens).
- R2S operates entirely without task rewards. It mines high-disagreement states from an untrained student, runs teacher takeovers from those states, filters using reward-free checks such as consensus or an LLM judge, and fine-tunes the teacher to internalize takeover-informed scoring on every assistant token from the divergence turn onward. The repaired teacher is then frozen as the sole scorer for standard OPD, requiring no reward signal during either the repair phase or the subsequent training.

## Context
Agentic on-policy distillation is a growing paradigm for training capable language-model agents from teacher demonstrations, particularly relevant as agentic AI systems proliferate in tool-use, coding, and multi-step reasoning tasks. Existing mitigations for OPD failures—episode-length curricula, teacher-guided turns, prefix replay, and disagreement-based intervention—operate under the assumption that the teacher's scoring is fundamentally sound and the student simply drifts too far. This paper reframes the failure as a scoring deficiency rather than a trajectory-distribution problem, which is a significant conceptual shift for the distillation and imitation-learning literature.

## Implications
For practitioners building agentic AI pipelines, R2S offers a reward-free repair procedure that can be applied before standard OPD training, potentially improving agent performance without requiring hand-crafted reward functions or environment-specific reward engineering. The consistent 12.8-point improvement across diverse teacher-student-environment combinations suggests the rollout-scorer gap is a general failure mode rather than a niche artifact, making the insight broadly applicable to anyone deploying teacher-student distillation for autonomous agents. The method's reliance on LLM judges or consensus checks as reward-free validators also points toward practical deployment pathways where ground-truth task rewards are unavailable or expensive to obtain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28586v1)
