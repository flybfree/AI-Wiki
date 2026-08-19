---
title: LLM-Derived Preference Judgments Are Not Self-Consistent
url: http://arxiv.org/abs/2608.17644v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_11-01-47Z_LLM_DerivedPreferenceJudgmentsAreNotSelf_Consisten.md
generated_at: 2026-08-18 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the numerical preference judgments that large language models (LLMs) generate for human users can be faithfully represented by a single, self-consistent utility function. The authors find that observed willingness‑to‑pay differences often violate the logical consistency required for such utilities, revealing persistent errors across multiple LLMs and domains.

## Key Takeaways
- The difference in stated willingness‑to‑pay between two items does not match the payment that would make a user indifferent to swapping them, indicating a breakdown in self‑consistency.  
- Statistical tests show that observed responses deviate significantly from the best‑fitting single utility function across flight, apartment, and hotel examples.  
- These inconsistencies persist regardless of which LLM is used, suggesting that LLM‑derived preferences cannot be reliably summarized by one utility model.

## Context
Understanding user preferences through LLMs enables agents to make informed decisions in recommendation systems and personal assistants. However, the assumption that a single utility function captures all stated preferences may lead to flawed behavior if the underlying data are inconsistent.

## Implications
If LLM‑derived utilities are unreliable, downstream systems that rely on them for decision making risk producing suboptimal or contradictory actions. Practitioners must incorporate additional validation steps or alternative preference models to mitigate this risk.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17644v1)
