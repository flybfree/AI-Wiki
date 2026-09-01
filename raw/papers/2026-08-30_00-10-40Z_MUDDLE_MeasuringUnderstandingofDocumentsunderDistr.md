---
title: MUDDLE: Measuring Understanding of Documents under Distractor and Length Effects
published: 2026-08-30T00:10:40Z
authors: Jason Luo, Saibilila Abudukelimu, Judy Song, Andrew Feng, Shivank Garg, Vasu Sharma, Kevin Zhu
url: http://arxiv.org/abs/2608.29477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MUDDLE: Measuring Understanding of Documents under Distractor and Length Effects

## Abstract
Document question-answering systems increasingly answer questions over collections of retrieved documents rather than one clean source, so robustness to distracting context matters as much as reading ability. When such systems fail, it is often unclear whether the context was too long or the distractors were too close to the topic, because prior work tends to conflate these two effects. We present MUDDLE, a controlled benchmark that separates them. MUDDLE uses 270 human-annotated questions, each tied to a single source document, and instantiates every question in five conditions: the source alone, the source with two or four topically similar hard negatives, and the source with two or four random distractors. The random distractors are matched to the hard negatives in length and provenance, so an accuracy gap between the two arms reflects topical similarity rather than length. All five conditions are rendered in markdown, page images, and raw PDF, but the distractor sweep reported here is run in markdown, since a source plus its distractors exceeds current image and PDF input limits. We score answers with an LLM judge across three model families. In the complete markdown sweep, hard negatives lower accuracy more than length-matched random documents at both context sizes for gpt-5-mini, while random documents stay near the no-distractor baseline. The effect is small but directionally consistent, and for gpt-5-mini hard negatives significantly underperform length-matched random distractors when pooled across context sizes. We release the data and evaluation code for a reproducible study of context degradation.

## Metadata
- **Published**: 2026-08-30T00:10:40Z
- **Authors**: Jason Luo, Saibilila Abudukelimu, Judy Song, Andrew Feng, Shivank Garg, Vasu Sharma, Kevin Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29477v1)