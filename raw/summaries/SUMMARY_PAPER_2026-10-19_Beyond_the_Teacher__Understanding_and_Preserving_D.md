---
title: Beyond the Teacher: Understanding and Preserving Distillation Overshoot in Agentic On-Policy Distillation
url: http://arxiv.org/abs/2610.25034v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-18_05-44-26Z_BeyondtheTeacher_UnderstandingandPreservingDistill.md
generated_at: 2026-10-19 23:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies and characterizes "distillation overshoot," a counterintuitive phenomenon in on-policy distillation (OPD) for multi-turn agentic tasks where a smaller, initially weaker student model temporarily surpasses its stronger teacher during training before regressing as distillation continues. The authors trace this overshoot to two competing dynamics—repairing weak student decisions versus eroding successful student choices the teacher disfavors—and propose Success-Preserving On-Policy Distillation (SPOD), a method that selectively masks conflicting teacher supervision on successful student choices while introducing a soft probability floor to prevent erosion, achieving up to 15.2 percentage point gains over standard OPD and surpassing the teacher by up to 20 points across multiple benchmarks.

## Key Takeaways
- Distillation overshoot arises from a temporal imbalance between two effects of OPD: early in training, teacher corrections repair weak student decisions faster than the teacher erodes the student's own successful strategies, allowing the student to combine external guidance with its own strengths and temporarily exceed the teacher. As training progresses, erosion overtakes repair and these gains vanish, meaning standard OPD training schedules inherently destroy the very advantage they create.
- SPOD addresses overshoot by requiring only binary episode success signals and model probabilities already available during OPD training, making it a low-overhead intervention. It masks teacher supervision on successful student choices and applies a soft probability floor to counteract erosion, while retaining full teacher guidance on unsuccessful trajectories. This selective approach preserves beyond-teacher gains rather than allowing them to decay.
- Across two model families and three agentic benchmarks, SPOD consistently outperforms ordinary OPD and evaluated variants. Critically, SPOD's final checkpoints surpass even the best intermediate checkpoints produced by standard OPD in all six experimental settings, demonstrating that beyond-teacher performance can be not merely preserved but extended further through training.

## Context
On-policy distillation has become a central technique for transferring capabilities from large teacher models to smaller student models, particularly in agentic settings where multi-turn decision-making is required. Prior work has largely assumed that distillation monotonically improves student performance toward the teacher's level. This paper disrupts that assumption by revealing that the training dynamics of OPD contain an inherent self-destructive mechanism: the same supervision that repairs student weaknesses simultaneously erodes student strengths. Understanding this tension is critical for the growing field of model distillation, where practitioners routinely train agents for agentic tasks such as tool use, planning, and multi-step reasoning, and where the assumption that longer training always yields better results may be fundamentally flawed.

## Implications
For practitioners deploying distilled agentic models, this work signals that standard OPD training schedules may be systematically discarding peak student performance, meaning that early-stopping or checkpoint selection strategies are insufficient and require architectural modifications to the training procedure itself. SPOD's minimal overhead—needing only binary success labels and existing probability outputs—makes it immediately applicable to existing distillation pipelines without additional data collection or model modifications. For the broader field, the finding that a student can legitimately and sustainably exceed its teacher challenges the prevailing assumption that distillation is inherently a ceiling-limited process, opening new research directions into how teacher-student interactions can be designed to amplify rather than homogenize student capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25034v1)
