---
title: SWIM: Student Writing Simulation via Proficiency-Conditioned Generation
url: http://arxiv.org/abs/2609.03215v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_23-10-51Z_SWIM_StudentWritingSimulationviaProficiency_Condit.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language models can simulate student writing across proficiency levels using a task called SWIM that conditions generation on a proficiency metric. Experiments comparing prompting, supervised fine-tuning and reinforcement learning show that prompting offers limited control while SFT improves alignment and RL with a proficiency-alignment reward yields the best results.

## Key Takeaways
- Prompting provides only shallow control over student writing traits, failing to capture lexical, grammatical and organizational differences between proficiency levels.
- Supervised fine‑tuning (SFT) significantly enhances profile alignment across all writing dimensions compared with prompting alone.
- Reinforcement learning using a reward that explicitly penalizes misalignment with the target proficiency yields further improvements in both content and language quality.

## Context
This work addresses a gap in LLM research where most studies focus on high‑quality generation rather than reproducing authentic student variation. By grounding simulation in measurable proficiency profiles, SWIM contributes to more realistic educational AI applications that adapt to learner abilities.

## Implications
Educators can leverage these findings to design prompts or fine‑tuned models that better reflect individual writing levels, improving assessment fairness and personalized feedback. Practitioners should prioritize supervised training over simple prompting when aiming for accurate proficiency‑conditioned simulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03215v1)
