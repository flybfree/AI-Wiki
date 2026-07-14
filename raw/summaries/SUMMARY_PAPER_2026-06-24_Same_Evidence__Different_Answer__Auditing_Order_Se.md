---
title: "Summary: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models"
url: http://arxiv.org/abs/2606.26079v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-24_17-53-26Z_SameEvidence_DifferentAnswer_AuditingOrderSensitiv.md
generated_at: 2026-06-24 22:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-06-24 Same Evidence  Different Answer  Auditing Order Se

## Summary
The paper audits order sensitivity in multimodal large language models by testing how shuffling input order affects answers across a set of models. It finds that all models exhibit noticeable answer flips, ranging from 24% to 50%, indicating strong dependence on ordering despite shared evidence.

## Key Takeaways
- The audit reveals that none of the 18 examined MLLMs are order‑invariant, with flip rates spanning a wide range that suggests systematic ordering bias.
- A same‑ordering control shows that observed flips exceed the baseline stochastic noise floor set by the decoder at temperature zero, indicating real ordering effects beyond randomness.
- Mitigation experiments show that prompt changes affecting only one modality do not transfer to the other, implying that order robustness cannot be achieved solely through prompt engineering.

## Context
Order‑sensitivity is a critical reliability issue for multimodal AI systems where inputs may arrive in different sequences. Current evaluation practices often ignore this aspect, leading to misleading performance metrics and limited trustworthiness of deployed models.

## Implications
For practitioners, the findings warn that prompt‑level fixes are insufficient for ensuring consistent output across order variations. Future research should explore architectural or training strategies that make models truly order‑robust, aligning with emerging AI evaluation guidelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.26079v1)
