---
title: Auditing Provenance Sensitivity in LLM Agent Action Selection
url: http://arxiv.org/abs/2607.20827v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
generated_at: 2026-07-23 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how large language model agents handle evidence that is relevant but unauthorized for a specific decision. By auditing provenance sensitivity across thousands of controlled next‑action tasks, the authors show that models sometimes select actions based on untrusted sources, leading to competing versus supporting outcomes at rates of 5.4 % and 1.7 percent respectively.

## Key Takeaways
- Valid evidence can be weakened while still influencing action selection, revealing a gap between authorized and effective grounding.  
- Unauthorized competition is observed in only 2.4 % of comparisons under controlled degradation, with a confidence interval of 2.1–3.0 percent.  
- Model behavior varies across trusted versus untrusted evidence variants, indicating that source‑authority cues are processed but do not fully block influence.

## Context
The study addresses a growing concern in AI safety: the reliance on potentially misleading or non‑authorized information when agents generate decisions. By isolating factors such as task, proposition, and policy while varying only source authority, it provides a systematic method to evaluate provenance sensitivity that is applicable across multiple open‑weight LLM families.

## Implications
For developers, this work underscores the need for rigorous provenance audits before deploying autonomous agents in high‑stakes environments. Practitioners should monitor not just correct actions but also the presence of unauthorized evidence, as subtle biases can lead to unexpected errors even when overall performance appears sound.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20827v1)
