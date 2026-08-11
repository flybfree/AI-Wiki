---
title: PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.08726v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_14-20-12Z_PAST_PrivilegedAdaptationfromCompleteStudentTrajec.md
generated_at: 2026-08-10 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Privileged Adaptation from Student Trajectories (PAST), a method that enriches on‑policy self‑distillation by treating each completed student trajectory as privileged information for the teacher while keeping the student’s distillation prefixes unchanged. The authors show that PAST improves average performance over vanilla OPSD by 5.6 percentage points across three reasoning benchmarks, demonstrating that both complete‑trajectory access and teacher adaptation yield gains.

## Key Takeaways
- PAST uses full student trajectories as additional privileged data for the OPSD teacher, allowing it to adapt toward verified success on failed paths while preserving correct trajectory distributions.  
- The teacher’s forward‑KL projection to a conditional arithmetic mean separates trajectory‑specific variation from the policy shift available to the student, making the frozen student an ideal fixed point for correct trajectories.  
- Experiments confirm that gains arise from both complete‑trajectory access and teacher adaptation; removing or shuffling trajectories eliminates improvements.

## Context
On‑policy self‑distillation aims to improve model performance by leveraging a teacher’s knowledge of its own rollouts, yet standard approaches ignore the hindsight information contained in completed trajectories. PAST bridges this gap by integrating trajectory context into teacher adaptation, offering a more nuanced alignment between teacher and student.

## Implications
For practitioners, PAST provides a practical way to harness richer self‑supervision without altering the distillation process, potentially boosting reasoning model accuracy on complex tasks. The method’s emphasis on trajectory‑conditioned teacher design could inspire future work that balances privacy constraints with maximum learning efficiency in AI training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08726v1)
