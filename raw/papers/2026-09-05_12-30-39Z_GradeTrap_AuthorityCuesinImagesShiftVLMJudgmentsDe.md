---
title: GradeTrap: Authority Cues in Images Shift VLM Judgments Despite Explicit Instructions to Ignore Them
published: 2026-09-05T12:30:39Z
authors: Deep Dessai
url: http://arxiv.org/abs/2609.06058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GradeTrap: Authority Cues in Images Shift VLM Judgments Despite Explicit Instructions to Ignore Them

## Abstract
As vision-language models (VLMs) become increasingly capable and are deployed in consequential real-world settings, they must evaluate evidence independently rather than defer uncritically to human authority. We introduce GradeTrap, a controlled evaluation that places two social cues in direct conflict: a student answer, which should attract sycophantic agreement, and a conflicting answer attributed to a peer, teacher, or official answer key, which should attract authority-based deference. Models produce free-form answers while being explicitly instructed to solve independently and ignore all student answers, feedback, and grading marks. We test the models on 60 synthetic real-world trade-off scenarios. Five neutral trials establish a stable model-relative preference, followed by three repetitions of six experimental cues including controls. On the 45-item common intersection across Gemini 3.5 Flash-Lite, GPT-5.6 Luna, and Claude Haiku 4.5, a generic second-answer control yields 5.4% conflicting-answer selection. Relative to that control, pooled within-item changes show no reliable peer-review effect, a 6.9-point teacher-review effect, and a 19.5-point official-key effect. In contrast, a displayed conflicting student answer alone compared to a displayed student reference answer alone only raises selection from 2.2% to 5.2%. Official-key provenance therefore redirects judgements more than a student answer or the generic second-answer control, despite an explicit ignore instruction and an opposing student answer given along with the official key. Effects vary in magnitude across the three models.

## Metadata
- **Published**: 2026-09-05T12:30:39Z
- **Authors**: Deep Dessai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06058v1)