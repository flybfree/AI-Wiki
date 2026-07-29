---
title: Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe
url: http://arxiv.org/abs/2607.25292v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-58-46Z_Instruction_TunedLanguageModelsCannotSamplefromDis.md
generated_at: 2026-07-28 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper demonstrates that instruction‑tuned language models do not generate diverse responses as intended; instead they produce identical answers on repeated queries. The authors introduce the KNOWS/DOES split to explain why models can describe a distribution but cannot sample from it, and they show that prompting for a description reduces error compared with aggregating individual model calls.

## Key Takeaways
- Instruction‑tuned models collapse to a single output on more than half of items in a public‑opinion benchmark, indicating a degenerate sampling primitive.  
- The same model can accurately describe the response distribution in one call, highlighting a gap between description and generation.  
- Prompt‑perturbed argyle (PPA) reduces error by 21% without additional cost, offering a practical mitigation.

## Context
The study addresses a longstanding concern that language models used as surrogate respondents may not behave like human survey participants. By revealing the KNOWS/DOES split, it clarifies how alignment training degrades sampling capabilities across diverse model families.

## Implications
For applications requiring per‑persona outputs, researchers must avoid aggregating identical model calls and instead use descriptive prompts to improve accuracy. This insight can guide design of more realistic AI survey systems and inform responsible deployment practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25292v1)
