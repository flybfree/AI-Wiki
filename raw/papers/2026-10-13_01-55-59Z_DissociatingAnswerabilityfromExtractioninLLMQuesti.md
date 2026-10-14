---
title: Dissociating Answerability from Extraction in LLM Question Answering over Radiology Reports
published: 2026-10-13T01:55:59Z
authors: Priyanshu Sinha, Kelsey McDonald
url: http://arxiv.org/abs/2610.17576v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dissociating Answerability from Extraction in LLM Question Answering over Radiology Reports

## Abstract
Answering questions from radiology reports involves two decisions: whether the report contains an answer and which span gives it. A false answer presents an unsupported claim as fact; an over-abstention hides what the report says. Yet RadQA results are reported as a single F1 that merges both. We propose an evaluation method that separates them, reporting false-answer and over-abstention rates beside F1 and splitting F1 changes into extraction and answerability terms. We apply it to 13 LLMs on the RadQA test set, zero-shot and with three cumulative demonstration sets, the last adding an unanswerable example. Models with similar F1 differed more than twofold in false-answer rate. The unanswerable example changed when models answered, not how well they extracted: 12 of 13 models abstained more often, and three-quarters of the answers they withdrew had F1 $\geq$ 0.5. Within models, false answers showed no clear association with extraction quality, but acting on the decision itself helped: keeping an answer only when enough other models also answered lowered the zero-shot false-answer rate by 4 points without a detectable F1 change. Because the two decisions can change independently, we suggest radiology QA evaluations report them separately, not through F1 alone.

## Metadata
- **Published**: 2026-10-13T01:55:59Z
- **Authors**: Priyanshu Sinha, Kelsey McDonald
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17576v1)