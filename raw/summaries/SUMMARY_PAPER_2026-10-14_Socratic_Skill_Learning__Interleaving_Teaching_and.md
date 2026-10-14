---
title: Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills
url: http://arxiv.org/abs/2610.17860v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_07-23-34Z_SocraticSkillLearning_InterleavingTeachingandPract.md
generated_at: 2026-10-14 00:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Socratic Skill Learning (SSL), a framework for teaching LLM agents transferable task skills by interleaving expert guidance with autonomous student practice, where the student agent remains the sole environment operator and skill author. Through a new benchmark called SkillTransferBench (35 task families, 408 executable cases), the authors demonstrate that SSL achieves 0.801 utility on the main cohort, outperforming no-skill baselines (0.723), trajectory distillation methods like Trace2Skill (0.761), and contrastive distillation methods like SKILL-KD (0.751), while an optimized Issue-Guided variant further improves efficiency by reducing educator token usage by 61.7%.

## Key Takeaways
- SSL fundamentally restructures skill acquisition by making the student agent the active author and tester of skills, while an educator agent provides guided investigation prompts. This interleaved approach ensures that learned procedures are validated against real conditions of use rather than merely distilled from successful trajectories, addressing a core limitation where a single successful task attempt leaves critical procedural conditions untested.
- The authors constructed SkillTransferBench, a rigorous evaluation suite pairing public variation specifications with held-out evaluation in fresh solver sessions across 35 task families and 408 executable cases. On the main 22-family, 155-case cohort, Fixed-Window SSL reaches 0.801 utility, surpassing adapted Trace2Skill at 0.761 and adapted SKILL-KD at 0.751, demonstrating that interleaved guidance consistently outperforms both expert authoring and post-hoc teaching across three different model pairs.
- Issue-Guided SSL introduces a token-efficiency innovation by tracking unresolved questions across skill revisions to selectively focus educator review. This variant reaches 0.805 utility while consuming 61.7% fewer educator tokens and 16.9% fewer total acquisition tokens than Fixed-Window SSL, showing that targeted, question-driven review is both more effective and substantially cheaper than fixed-window review as the demand for new lessons declines.

## Context
LLM agents increasingly rely on reusable "skills" to perform complex tasks across sessions, but existing skill-learning methods such as trajectory distillation and contrastive knowledge distillation tend to extract procedures from successful runs without verifying their boundary conditions or failure modes. This paper addresses a critical gap in the agent-learning pipeline: how to produce skills that genuinely transfer to novel task variations rather than merely encoding a single successful episode. By framing skill acquisition as a Socratic dialogue between an educator and a student agent, the work connects to broader research on curriculum learning, active learning, and human-in-the-loop agent training, while introducing a benchmark that raises the evaluation bar for transferable agent skills.

## Implications
For practitioners building agentic systems, SSL offers a practical recipe for generating high-quality, transferable skills without requiring human experts to hand-author every procedure, potentially reducing maintenance costs in production agent deployments. The Issue-Guided variant's dramatic token savings (61.7% fewer educator tokens) make the approach viable for resource-constrained environments where repeated skill acquisition is costly. For the broader AI research community, SkillTransferBench provides a standardized, executable evaluation harness that can expose whether skill-learning methods truly generalize beyond their training tasks, setting a higher bar for future work in agent skill distillation and transfer.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17860v1)
