---
title: Conformity Breaks Conformal Prediction
published: 2026-09-03T20:05:47Z
authors: Yibo Hu, Hanyu Su
url: http://arxiv.org/abs/2609.04445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformity Breaks Conformal Prediction

## Abstract
A conformal certificate can be valid when an LLM answers alone and invalid when the same LLM sees peers that unanimously assert a wrong answer. The question is unchanged; the model's score for the correct answer changes. We call this a score-mechanism shift: clean calibration certifies how the model scores answers alone, but not how it scores them under peer pressure. We show that this shift silently breaks conformal prediction in multi-agent LLM systems. Across open-weight models and multiple-choice QA tasks, coverage falls from a calibrated 90% to 74% under unanimous-wrong peers at the standard alpha = 0.10 operating point. The average hides a sharper failure: by targeting the low-confidence items the certificate still covers, an attacker nearly halves coverage on that subgroup, from 87% to 47%, while the monitored average remains much higher. The failure also reaches the decision layer: a system that should escalate when uncertain can instead become confident enough to act on the attacker's wrong answer. Standard conformal fixes do not solve the problem, because the question distribution has not changed; the model's scoring behavior has.

## Metadata
- **Published**: 2026-09-03T20:05:47Z
- **Authors**: Yibo Hu, Hanyu Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04445v1)