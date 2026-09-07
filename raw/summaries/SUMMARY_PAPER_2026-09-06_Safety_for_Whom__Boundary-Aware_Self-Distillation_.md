---
title: Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal
url: http://arxiv.org/abs/2609.04482v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_21-03-45Z_SafetyforWhom_Boundary_AwareSelf_DistillationforCo.md
generated_at: 2026-09-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces narrow-boundary safety for LLMs and presents a self-distillation framework that improves refusal handling on specific boundaries. It shows that controlled topic generation with repair data reduces unsafe responses while limiting over‑refusal, achieving near‑perfect boundary compliance in political persuasion tasks.

## Key Takeaways
- The framework combines controlled topic generation, coverage repair, compensation data and harmful‑benign pairs to train a model that distinguishes narrow boundaries, resulting in only 0.20% of prompts needing escalated refusal after multiple attempts.
- Training on refusal data via Escalate boosts target‑domain refusal from 9.47% to 84.75% but inflates XSTest over‑refusal dramatically, highlighting the trade‑off between safety and usability.
- Boundary‑pair data reduces comply‑side over‑refusal from 32.94% to 4.16%, yet harmful‑side refusal only drops slightly, indicating limited gains in overall safety.

## Context
Current LLM safety research focuses on broad harmfulness metrics, often overlooking the need for domain‑specific boundaries that align with user intent. This work addresses that gap by treating safety as a boundary problem rather than a binary classification task.

## Implications
For practitioners, this suggests that safety alignment must be evaluated per intended refusal boundary to balance compliance and over‑refusal. The methodology offers a scalable way to generate targeted refusal data for specialized applications such as political assistants or public‑sector tutors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04482v1)
