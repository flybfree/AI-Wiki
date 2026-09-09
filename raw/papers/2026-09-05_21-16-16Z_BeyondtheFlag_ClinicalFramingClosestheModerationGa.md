---
title: Beyond the Flag: Clinical Framing Closes the Moderation Gap in Suicide Risk Measurement
published: 2026-09-05T21:16:16Z
authors: Shreyas Krishnan, Gun Ahn, Jungjin Kim
url: http://arxiv.org/abs/2609.06263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Flag: Clinical Framing Closes the Moderation Gap in Suicide Risk Measurement

## Abstract
Moderation APIs are built to flag policy-violating content, not to measure graded clinical risk. But a platform's duty does not end at detection: the response owed to passive distress differs sharply from the response owed to active planning with means access, and emerging regulation (e.g., California Senate Bill 243) is turning that distinction into a compliance requirement. We therefore ask how well deployed safety signals recover clinically meaningful severity. We release a benchmark of 516 r/SuicideWatch posts rated by a licensed psychiatrist on a four-level ordinal schema (Indicator, Ideation, Behavior, Attempt) grounded in the Columbia Suicide Severity Rating Scale, and evaluate moderation APIs, prompted LLMs, and supervised baselines under seven ordinal-aware metrics. Three findings. Vendor moderation APIs separate low- from high-severity posts well (0.860 high-risk F1) but measure severity poorly (0.395 macro F1), systematically over-predicting the most severe category. Clinically grounded zero-shot prompting recovers much of that gap (0.562 macro F1), and expert-authored framing (not fine-tuning, added reasoning, or naive multi-agent aggregation) is the effective lever. The value of reasoning depends on register: it hurts on long, noisy Reddit posts and helps on short, clinician-authored statements. We argue graded severity, not a binary flag, is what a proportionate duty of care requires, and release our evaluation framework to support that measurement.

## Metadata
- **Published**: 2026-09-05T21:16:16Z
- **Authors**: Shreyas Krishnan, Gun Ahn, Jungjin Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06263v1)