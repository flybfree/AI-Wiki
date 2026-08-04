---
title: CraftAlign: Feature-Grounded Evaluation and Revision Guidance for AI Stories
url: http://arxiv.org/abs/2608.01377v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_16-57-05Z_CraftAlign_Feature_GroundedEvaluationandRevisionGu.md
generated_at: 2026-08-03 23:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CraftAlign, a framework that evaluates AI-generated stories against human writing patterns and generates revision guidance to improve them. It combines a feature estimator and an energy model to score narrative features and provides structured perturbations for editors. Experiments demonstrate accurate pattern detection and superior revision outcomes compared with baselines.

## Key Takeaways
- The framework predicts 304 explicit writing features using Qwen3.5-9B, enabling fine-grained assessment of style and narrative elements.
- A class‑conditional energy model scores these feature configurations against human versus AI patterns, conditioning on the original prompt when available.
- At inference time CraftAlign applies schema‑valid structured perturbations that shift the feature configuration toward human writing patterns and converts them into natural‑language guidance for editors.

## Context
Current large language models produce fluent stories but often retain an unmistakable artificial feel due to clichés, over‑explanation, linear causality, and stereotyped endings. Existing evaluation tools rely on coarse labels or holistic scores, while revision methods are limited to localized edits that cannot address broader structural issues.

## Implications
CraftAlign offers a systematic way to bridge the gap between AI and human storytelling by providing actionable feedback rather than just scores. This could lead to higher‑quality outputs in industry applications such as content creation and education where narrative coherence is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01377v1)
