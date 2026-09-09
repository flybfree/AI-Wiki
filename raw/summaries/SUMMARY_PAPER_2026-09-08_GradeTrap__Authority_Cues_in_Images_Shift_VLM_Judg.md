---
title: GradeTrap: Authority Cues in Images Shift VLM Judgments Despite Explicit Instructions to Ignore Them
url: http://arxiv.org/abs/2609.06058v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-05_12-30-39Z_GradeTrap_AuthorityCuesinImagesShiftVLMJudgmentsDe.md
generated_at: 2026-09-08 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GradeTrap, a study that tests whether vision-language models ignore authority cues despite explicit instructions to do so. It finds that official key provenance strongly influences model judgments more than student answers or generic second‑answer controls, even when conflicting student evidence is present.

## Key Takeaways
- The presence of an official answer key increases selection of the authoritative response by 19.5 points relative to a control, indicating strong authority deference.
- A displayed conflicting student answer alone raises selection from 2.2% to 5.2%, showing modest influence compared to teacher‑review effect.
- Within‑item changes show no reliable peer‑review effect, suggesting models do not consistently defer to peers.

## Context
Vision-language models are increasingly used in educational and decision‑making contexts where independent reasoning is required. This study highlights a gap between model instructions and observed behavior, raising questions about trustworthiness of AI outputs when authority cues conflict with user guidance.

## Implications
For developers, the findings suggest that explicit ignore commands may be insufficient to suppress authority bias, necessitating stronger architectural or training interventions. Practitioners should monitor how models handle conflicting social signals in real‑world applications to ensure reliable and unbiased judgments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.06058v1)
