---
title: Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety
url: http://arxiv.org/abs/2607.18828v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_08-05-35Z_EvaluatingmedicalAIundermissinginformation_same_pr.md
generated_at: 2026-07-23 23:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a stress‑testing framework for medical AI that simulates missing clinical information by truncating the final user turn in HealthBench conversations. Evaluations with four leading models reveal that judge perception of safety shifts when the same provider is excluded, indicating that apparent over‑commitment can be an artifact rather than a true knowledge gap.

## Key Takeaways
- Judge agreement on safety is moderate (Fleiss' kappa = 0.65) and positive same‑provider bias emerges after adjusting for individual leniency, suggesting model ordering changes when the provider’s own judgment is removed.
- LLM judges are significantly more permissive than independent clinicians on a blinded subset, crediting uncertainty on 66–84% of items versus 52%, widening the permissiveness gap in author‑audited clinical‑underdetermined cases.
- Closed‑ended MedQA anchors confirm high accuracy and minimal option‑order effects across models, indicating that safety discrepancies stem from calibration rather than factual knowledge.

## Context
Medical AI safety testing has traditionally relied on closed benchmarks; this work expands the paradigm to open‑ended conversations where information gaps are inherent. By involving both LLM judges and human clinicians as evaluators, it highlights how evaluator dynamics can influence perceived model behavior in real clinical dialogue settings.

## Implications
Clinicians and developers must recognize that safety judgments may be influenced by provider bias rather than model shortcomings. The findings urge more holistic evaluation protocols that account for evaluator variability to ensure robust AI deployment in uncertain medical contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18828v1)
