---
title: Polite but Misaligned: Evaluating LLM Politeness Judgments Against Human Pragmatic Norms
url: http://arxiv.org/abs/2609.29001v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_04-08-59Z_PolitebutMisaligned_EvaluatingLLMPolitenessJudgmen.md
generated_at: 2026-09-27 16:20
model: qwen3.6-35b-a3b
---

## Summary
This study investigates whether large language models assess social pragmatics in alignment with human judgments by evaluating politeness across two English-language datasets featuring continuous ratings and categorical labels. The analysis reveals that inter-model agreement consistently exceeds model-human agreement, indicating a divergence between machine assessments and human pragmatic norms. Furthermore, the research identifies systematic biases in model predictions, such as neutral compression and reliance on explicit linguistic cues over subtle rapport-building strategies.

## Key Takeaways
- Models demonstrate stronger agreement with one another than with human annotators, suggesting that LLMs may share common biases or training artifacts rather than reflecting diverse human pragmatic standards; alignment appears driven by explicit linguistic cues while rapport-building strategies frequently contribute to misalignment.
- In categorical politeness tasks, models exhibit a systematic "neutral compression" bias, characterized by the overproduction of Neutral labels and significant underprediction of Impolite instances, a pattern that remains robust even when validated against expert consensus on a diagnostic subset.
- The findings underscore the limitations of aggregate agreement metrics in evaluating LLM pragmatics, advocating for nuanced assessments that examine directional patterns of disagreement across different human references to better understand where and why models deviate from human social norms.

## Context
As LLMs are increasingly deployed in socially sensitive applications, ensuring they understand and generate appropriate pragmatic behavior is critical for safety and user trust. This research addresses a gap in current evaluation frameworks by moving beyond simple accuracy metrics to probe the deeper alignment of model judgments with human social expectations, highlighting potential risks in how models interpret politeness and rapport.

## Implications
Practitioners should be cautious when relying on LLMs to moderate content or assess user interactions, as the tendency toward neutral compression may lead to under-detection of impolite behavior. Future development must prioritize fine-tuning and evaluation strategies that address these specific pragmatic misalignments, particularly regarding subtle social cues, to improve model reliability in real-world social contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.29001v1)
