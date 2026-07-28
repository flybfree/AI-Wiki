# Summary: 2026-07-26_08-50-28Z_LanguageShapesInstructionHierarchyComplianceinMult.md
Saved: 2026-07-27 20:19
Source: 2026-07-26_08-50-28Z_LanguageShapesInstructionHierarchyComplianceinMult.md
Model: None

---

## Summary  
The paper investigates how the language of an instruction influences compliance with instruction hierarchy (IH) rules in multilingual large language models, revealing that higher‑priority instructions can paradoxically become disruptive when the model is specialized for their language. To address this gap, the authors introduce XIH‑Bench, a comprehensive benchmark evaluating IH across six languages, four domains, and three IH configurations. Their analysis uncovers two consistent patterns: (1) language‑dependent asymmetry in compliance, where a language that strengthens higher‑priority instruction obedience can weaken it for lower‑priority instructions, and (2) the Language Boundary Effect, which shows cross‑language conflicts improve compliance relative to same‑language conflicts. The work also demonstrates that model specialization makes lower‑priority instructions harder to override, posing reliability and security risks in multilingual deployment.

## Key Contributions  
- [Finding 1] IH compliance exhibits a clear language‑dependent asymmetry: the higher‑priority instruction can become disruptive in the lower‑priority position when the model is specialized for that language.  
- [Finding 2] Cross‑language conflicts yield higher compliance than same‑language conflicts, a phenomenon termed the Language Boundary Effect.  
- [Finding 3] Language specialization makes lower‑priority instructions harder to override, creating multilingual reliability and security risks.

## Methodology  
The authors constructed XIH‑Bench by generating instruction pairs where a high‑priority instruction may conflict with a low‑priority one across six languages (e.g., English, Spanish, Mandarin, Arabic, Hindi, Korean). They selected four domains (medical, legal, financial, and general) to reflect diverse application contexts. For each domain they evaluated three IH settings: same‑language conflicts, cross‑language conflicts, and hierarchical overrides. Model compliance was measured using automated metrics (e.g., instruction‑level accuracy) combined with human judgments to verify correctness.

## Results  
Across a suite of multilingual LLMs, the authors observed that higher‑priority instructions in model‑favored languages were overridden less often than expected, while lower‑priority instructions in those same languages were more frequently overridden. The cross‑language conflict setting improved compliance by approximately 12 % compared with same‑language conflicts, confirming the Language Boundary Effect. This effect held across all domains and models, indicating a systematic bias rather than an isolated artifact.

## Significance  
These findings reveal that multilingual instruction hierarchy is not uniform; language influences both the strength of obedience and the safety of lower‑priority instructions. The work calls for language‑aware evaluation frameworks and model design practices to prevent unintended instruction overrides, thereby enhancing the reliability and security of deployed multilingual systems.

## Related Concepts  
Instruction hierarchy (IH), multilingual LLMs, cross‑language vs same‑language conflicts, Language Boundary Effect, language specialization, compliance metrics.
