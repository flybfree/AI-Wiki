---
title: When Financial Fine-tuning Fails: A Three-Level Detectability Analysis of Numerical Hallucination in Domain-Adapted Language Models
url: http://arxiv.org/abs/2609.04806v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_07-02-42Z_WhenFinancialFine_tuningFails_AThree_LevelDetectab.md
generated_at: 2026-09-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates numerical hallucination in financial language models under domain fine‑tuning and finds that fine‑tuned variants generate many fabricated numbers across three detectability levels. The base model performs well but FT‑A and FT‑A+B+C show severe degradation, especially overt hallucination.

## Key Takeaways
- Domain fine‑tuning causes a sharp rise in overt numerical fabrication, reaching 82.5% for FT‑A and 98% for FT‑A+B+C.
- Numeracy supervision does not reduce hallucination; instead it amplifies errors across all three detectability categories.
- Template injection is identified as the primary mechanism driving these hallucinations.

## Context
Financial language models are used to summarize regulatory reports, where inaccurate numbers can have real‑world consequences. This study adds a systematic detection framework that separates overt, explicit, and implicit numerical claims, which prior work has not done in controlled fine‑tuning scenarios.

## Implications
Practitioners must adopt evaluation protocols that capture all forms of hallucination to avoid deploying models that silently produce false financial data. Embedding grounding mechanisms or allowing abstention can mitigate the risks introduced by domain adaptation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04806v1)
