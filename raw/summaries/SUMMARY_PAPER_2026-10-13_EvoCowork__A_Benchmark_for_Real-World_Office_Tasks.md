---
title: EvoCowork: A Benchmark for Real-World Office Tasks
url: http://arxiv.org/abs/2610.14828v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_11-43-07Z_EvoCowork_ABenchmarkforReal_WorldOfficeTasks.md
generated_at: 2026-10-13 21:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EvoCowork introduces a 240-task benchmark designed to evaluate whether harness-level recursive self-improvement in AI agents produces reusable procedural knowledge or merely task-specific fixes when applied to real-world office workflows. The benchmark spans presentations, documents, spreadsheets, and cross-office workflows while keeping model weights fixed, and its key empirical finding is that improvements gained on single-modality feedback tasks do not reliably transfer to coordinated multi-file workflows, with cross-office scores changing by only +0.03 or -1.72 despite in-domain gains of up to 4.90 points.

## Key Takeaways
- The benchmark enforces a strict separation between feedback learning, revision selection, and final evaluation, ensuring that methods trained on single-modality tasks are subsequently tested on unseen single-modality tasks and cross-office workflows under a shared initial harness and explicit computational budgets, preventing overfitting to the feedback loop itself.
- Scoring goes beyond content accuracy to include native file structure, formula correctness, cross-file consistency, and visual quality, reflecting the practical requirement that office deliverables must be natively editable and mutually consistent across multiple files rather than merely textually correct.
- In static evaluations across two models and four harnesses, the best configuration achieves only 42.25 overall and 30.62 on cross-office tasks, and harness evolution methods like ACE and AHE show that in-domain improvements of 4.90 and 2.64 points translate to negligible or negative cross-office gains, demonstrating a fundamental transfer gap between isolated file-type proficiency and coordinated workflow competence.

## Context
This paper addresses a critical gap in the evaluation of self-improving and agentic AI systems: existing benchmarks often measure single-task performance or rely on model fine-tuning, whereas real office work demands that agents iteratively refine multiple interdependent artifacts without changing the underlying model. By holding model weights fixed and evolving only the harness (the procedural scaffolding around the model), EvoCowork isolates whether procedural learning generalizes or overfits, a question central to the viability of autonomous agent systems in enterprise settings.

## Implications
For practitioners building autonomous office agents, the findings caution against assuming that iterative self-improvement on individual file types will automatically yield competence in multi-file, cross-departmental workflows, suggesting that harness design must explicitly account for cross-file consistency and coordination rather than optimizing each modality in isolation. For the broader AI research community, EvoCowork provides a standardized, budget-constrained evaluation protocol that records capability, transfer, and cost of harness evolution, offering a reproducible testbed to distinguish genuine procedural generalization from superficial task-specific patching before deploying self-improving agents in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14828v1)
