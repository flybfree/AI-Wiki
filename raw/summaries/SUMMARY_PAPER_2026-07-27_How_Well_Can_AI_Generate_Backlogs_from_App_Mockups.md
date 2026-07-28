---
title: How Well Can AI Generate Backlogs from App Mockups?
url: http://arxiv.org/abs/2607.22902v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_20-40-22Z_HowWellCanAIGenerateBacklogsfromAppMockups.md
generated_at: 2026-07-27 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how well AI can generate sprint backlogs from visual app mockups using GPT‑4o with three prompting strategies. It reports average F1 scores of 52–66% for epics and user stories and up to 35% precision gains when architectural context is added, while tasks remain harder. The authors introduce Revised Recall that combines ground‑truth metrics with developer assessments.

## Key Takeaways
- The zero‑shot baseline tends toward recall over precision, yielding lower F1 scores for epics and user stories.
- Adding compositional chain‑of‑thought reasoning improves balance between recall and precision, raising average F1 to 52–66%.
- Architectural context especially helps backend tasks, boosting precision by up to 35%, yet developers still flag about 26% of false positives as useful.

## Context
Generating project artifacts from visual input is a growing area where multimodal models can reduce manual effort. This work demonstrates that prompting strategies and added contextual cues can meaningfully affect the quality of AI‑generated backlogs, offering a practical step toward automated agile planning.

## Implications
Developers may integrate these prompts to accelerate sprint planning while maintaining human oversight. The hybrid approach balances automation with developer judgment, potentially streamlining early‑stage project setup across teams.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22902v1)
