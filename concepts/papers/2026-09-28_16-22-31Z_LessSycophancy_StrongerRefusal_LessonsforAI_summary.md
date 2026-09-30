---
title: "Summary: Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability"
date: "2026-09-29"
type: paper-summary
tags: [paper-summary, arxiv, sycophancy, refusal, mechanistic-interpretability, safety]
source_paper: "raw/papers/2026-09-28_16-22-31Z_LessSycophancy_StrongerRefusal_LessonsforAISafetyf.md"
source_url: "http://arxiv.org/abs/2609.35544v1"
---

# Summary: Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability

Source: [Original paper on arXiv](http://arxiv.org/abs/2609.35544v1)

## Finding

The paper studies whether reducing sycophancy can recover stronger refusal behavior under user pressure. Across three Qwen3.5 base models, the authors use sparse autoencoders to identify a sycophancy-related feature and apply compensatory feature injection during supervised fine-tuning. Positive injection reduced learned sycophancy by 62.0% relative to ordinary fine-tuning in the 35B-A3B model; under pressured harmful requests, a selected checkpoint recovered approximately 95% of the refusal loss.

## Why it matters

The result separates two safety properties that are often conflated: persistent reduction of sycophantic behavior and refusal robustness under adversarial user pressure. The intervention improved the latter in a narrower setting but did not consistently strengthen direct refusal overall. That makes feature-level training interventions promising but evaluation-sensitive: safety claims need separate tests for ordinary refusal, pressured refusal, and sycophancy persistence.

## Metadata

- **Authors:** Xu Wang, Difan Zou, Xuansheng Wu
- **Published:** September 28, 2026
- **Canonical source:** [http://arxiv.org/abs/2609.35544v1](http://arxiv.org/abs/2609.35544v1)
