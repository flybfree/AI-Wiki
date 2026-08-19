---
title: LLMs for Medical Consultation Are Evaluated Too Late: The Preformulation Gap
url: http://arxiv.org/abs/2608.17330v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_03-40-56Z_LLMsforMedicalConsultationAreEvaluatedTooLate_TheP.md
generated_at: 2026-08-18 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models behave when medical consultations start with vague or minimized patient concerns, rather than after a clear problem is identified. It compares three API models across physician-written vignettes under two instruction settings and finds that self‑care advice often appears before any patient answer in baseline conditions but not under structured handoff instructions.

## Key Takeaways
- Self-care or home-management advice appeared in 9 of 12 baseline case-model cells, indicating premature guidance before patient input. - Structured handoff summaries were absent in baseline cells (0/12) but present in 10 of 12 instruction cells, showing documentation differences. - The entry‑to‑care instruction altered sequencing and documentation without reliably prompting decisive factual elicitation.

## Context
This study highlights a gap between how AI systems are tested—after a problem is fully formed—and how they might behave at the very first contact with patients who often start consultations with uncertainty or incomplete information. In medical AI, early engagement can affect patient trust and clinical workflow integration.

## Implications
Practitioners must evaluate LLMs based on observable first‑contact behavior rather than relying solely on final diagnostic accuracy metrics. Addressing this preformulation gap could improve real‑world deployment of conversational health assistants in primary care settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17330v1)
