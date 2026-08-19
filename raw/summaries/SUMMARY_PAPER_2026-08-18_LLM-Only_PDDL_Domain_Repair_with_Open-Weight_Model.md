---
title: LLM-Only PDDL Domain Repair with Open-Weight Models
url: http://arxiv.org/abs/2608.17341v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_04-00-02Z_LLM_OnlyPDDLDomainRepairwithOpen_WeightModels.md
generated_at: 2026-08-18 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether open-weight large language models can repair PDDL planning domains using only their textual capabilities. It compares a symbolic baseline with an LLM, reporting an F1 score of .49 versus .87 for the best model but noting low pass rates on some tests.

## Key Takeaways
- The symbolic baseline achieves an F1 score of .49, indicating limited repair quality compared to LLMs.  
- The top-performing LLM reaches an F1 score of .87 with high reasoning effort, showing strong ability to produce correct repairs.  
- Even the best configuration that includes test traces yields only a 0.92 pass rate, revealing reliability issues on certain domains like Thoughtful.

## Context
Automated model repair is essential for maintaining accurate planning specifications as users generate both valid and invalid test plans. Recent advances in open-weight LLMs promise to automate such tasks without requiring proprietary symbolic tools. This study tests those capabilities within a standard PDDL repair framework.

## Implications
The findings suggest that current open-weight models cannot reliably guarantee constraint satisfaction, limiting their use for trustworthy automated repairs. Practitioners may need hybrid approaches combining symbolic reasoning with LLM assistance to achieve dependable results in planning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17341v1)
