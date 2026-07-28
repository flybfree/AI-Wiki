---
title: Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation
url: http://arxiv.org/abs/2607.24054v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_06-51-29Z_SuccessIsNotSelf_Explanatory_AuditingSuccessProven.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a problem known as missing evaluation object success provenance, where an agent’s correct answer may hide the reason for its success because the information state changes during evaluation. Using AcquaBench, the authors demonstrate that outcome evidence cannot reliably distinguish intended reasoning from accidental target acquisition across four standardized surfaces.

## Key Takeaways
- GOLD minus CLEAN reveals a 19.1 to 25.9 percentage point advantage when the correct value is available, indicating success follows the proper information state.
- In D2, GOLD still exceeds SHAM under distributed sufficiency, with AUROC values of 0.376 and 0.142, showing behavioral dependence can persist beyond the intended observation unit.
- A 5.0‑point CLEAN score gap compresses to a raw GOLD difference of -0.6 points without causing rank inversion, highlighting that benchmark scores do not always reflect true performance.

## Context
The paper addresses a longstanding challenge in agent evaluation: distinguishing genuine reasoning from superficial answer acquisition when the underlying data is altered during testing. By introducing AcquaBench and its substitution framework, it provides a systematic way to audit whether an agent’s success is truly grounded in correct information rather than accidental exposure.

## Implications
For researchers, this work suggests that benchmark reports must include provenance information to avoid misleading conclusions about model performance. Practitioners should design evaluation protocols that preserve the integrity of the evaluated state and report both score differences and their interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24054v1)
