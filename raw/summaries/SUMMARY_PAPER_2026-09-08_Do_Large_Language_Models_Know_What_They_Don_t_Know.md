---
title: Do Large Language Models Know What They Don't Know II? A Fully Behavioral, Non-Cognitive Measure of Epistemic Honesty
url: http://arxiv.org/abs/2609.07879v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_18-40-08Z_DoLargeLanguageModelsKnowWhatTheyDon_tKnowII_AFull.md
generated_at: 2026-09-08 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the Epistemic Honesty Quotient (EHQ) to measure whether large language models appropriately acknowledge their knowledge limits. Evaluated on a 3,000‑question benchmark across four categories, the study shows that EHQ scores vary widely from 0.31 to 0.81 despite high performance on standard correctness tests.

## Key Takeaways
- The EHQ reveals behavioral differences that conventional correctness checks miss, indicating models may be overconfident even when their answers are not grounded in available data.
- Substantive‑answer calibration varies across models and does not consistently align with epistemic restraint scores, suggesting a lack of reliable correlation between honesty and accuracy.
- Dataset composition, provider behavior, and confidence elicitation remain critical factors that must be considered when interpreting EHQ results.

## Context
This work addresses a longstanding concern about the transparency of AI systems by moving beyond factual correctness to assess how models behave when they encounter unknowns. It contributes to the broader effort to develop more honest and reliable language models for real‑world deployment.

## Implications
For practitioners, EHQ provides a behavioral metric that can guide model selection and monitoring, ensuring that confidence does not mask ignorance. The field may adopt similar honesty metrics to improve trust in AI outputs across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07879v1)
