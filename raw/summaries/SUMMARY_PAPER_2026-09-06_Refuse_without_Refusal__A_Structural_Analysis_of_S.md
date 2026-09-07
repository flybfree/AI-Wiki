---
title: Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models
url: http://arxiv.org/abs/2609.04714v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_04-37-10Z_RefusewithoutRefusal_AStructuralAnalysisofSafety_T.md
generated_at: 2026-09-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper analyzes safety-tuning responses to identify why models give false refusals by separating boilerplate refusal statements from rationales. Experiments show that relying only on rationales reduces false refusals while keeping safety performance similar. This suggests that the structure of safety outputs matters for alignment.

## Key Takeaways
- Boilerplate refusal statements cause reliance on superficial cues, leading to more false refusals.
- Training models solely on rationales improves discrimination between harmful and benign queries without sacrificing safety.
- Rationale‑only approaches work in both offline ICL configuration and inference‑time mitigation methods.

## Context
Large language models must balance helpfulness with safety, but current refusal mechanisms often misinterpret benign prompts as dangerous. The paper contributes a structural insight that the composition of model responses influences alignment outcomes.

## Implications
Practitioners should design safety datasets that focus on rationales rather than generic refusals to build more reliable agents. This research guides future work toward precise, fine‑grained supervision for better aligned systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04714v1)
