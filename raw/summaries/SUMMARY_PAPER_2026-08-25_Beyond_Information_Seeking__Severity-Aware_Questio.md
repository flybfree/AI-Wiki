---
title: Beyond Information Seeking: Severity-Aware Question Supervision for Proactive Medical Dialogue
url: http://arxiv.org/abs/2608.24521v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_13-09-45Z_BeyondInformationSeeking_Severity_AwareQuestionSup.md
generated_at: 2026-08-25 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Expected-Severity-Risk (ESR), a new objective for proactive medical dialogue that selects questions based on their potential impact on high‑severity diagnostic errors. Experiments show ESR reduces severe miss rates and improves overall accuracy with only a small increase in question count.

## Key Takeaways
- ESR values each candidate question by its expected reduction in severity‑aware terminal risk, not just information gain.
- The ranking is derived from train‑only statistics, so the policy can be deployed without teacher‑side computation at inference time.
- Compared to generic decision‑aware supervision, ESR specifically improves the high‑severity error profile while keeping question count low.

## Context
Medical dialogue agents must balance evidence acquisition with patient safety, a challenge that standard uncertainty‑reduction methods cannot fully address. This work demonstrates how consequence‑aware supervision can guide better clinical interactions.

## Implications
For healthcare AI developers, ESR offers a practical framework to prioritize questions that matter most in life‑threatening scenarios. Adopting such severity‑aware policies could lead to safer and more efficient patient conversations across medical chatbots.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24521v1)
