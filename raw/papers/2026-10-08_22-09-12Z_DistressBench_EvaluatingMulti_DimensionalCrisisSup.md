---
title: DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models
published: 2026-10-08T22:09:12Z
authors: Drew Rein, Patrick Oathout, Vishal Kumar, Udari Madhushani Sehwag
url: http://arxiv.org/abs/2610.12758v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models

## Abstract
Language models have been adopted faster than evaluation practices that reliably assess their risks, and a growing share of use is affective rather than informational. Within that traffic users disclose suicide and self-harm (SSH) crises. Existing safety benchmarks score models primarily on refusal, but refusal is not the desired behavior here; the conversation requires a substantive supportive response. We introduce DistressBench, 718 English conversations with clinician-authored user turns spanning 23 SSH subcategories, each paired with a task-specific rubric of weighted atomic criteria across seven dimensions of crisis support and a clinician reference response. A model's score is the weighted average over the criteria its reply satisfies, reading directly as the fraction of required care delivered. The best of 25 frontier models satisfies 88.4% of weighted criteria and the median model 71.4%, against 98.7% for clinician references scored on the same criteria. Pooled across all 25 models, in 35.3% of conversations where a model satisfied every criterion for recognizing the crisis, it failed to route the user toward human help. The shortfall concentrates in the dimensions requiring the model to act rather than withhold. Contrasting each dimension's median model against its best separates capability limits from choices: de-escalation reaches 74.6% in the strongest model against a median of 46.0%, and safety disclaimers 84.6% against 8.3%. Multi-turn conversations score below single-turn ones (68.5% against 74.2%). We release the corpus, rubrics, judge calibration labels, and a companion annex of 20 long-horizon red-team transcripts. These results argue for evaluating crisis safety on the care a model delivers rather than on what it declines to say, and for treating de-escalation and resource routing as deployment requirements.

## Metadata
- **Published**: 2026-10-08T22:09:12Z
- **Authors**: Drew Rein, Patrick Oathout, Vishal Kumar, Udari Madhushani Sehwag
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12758v1)