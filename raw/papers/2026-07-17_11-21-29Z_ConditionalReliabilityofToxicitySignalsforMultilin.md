---
title: Conditional Reliability of Toxicity Signals for Multilingual and Code-Mixed Abuse Detection
published: 2026-07-17T11:21:29Z
authors: Indraveni Chebolu, Rohan Singh, Arnab Mallick, Harmesh Rana
url: http://arxiv.org/abs/2607.15861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional Reliability of Toxicity Signals for Multilingual and Code-Mixed Abuse Detection

## Abstract
Moderation systems increasingly rely on external toxicity tools, but those tools are unreliable under code-mixing, transliteration, slang, and language mismatch. We study the \emph{conditional reliability} of toxicity priors in Indian multilingual and code-mixed short text: English toxicity, Indic abuse, and rule-based severity cues can be useful evidence, but only in some linguistic and abuse-severity contexts. We propose ToxGate, a trust-fusion head that conditions each auxiliary signal on the encoder representation before adding it to the prediction state. Across three short-text abuse datasets, four transformer encoders, and five seeds per setting, ToxGate improves over matched plain encoders in 10 of 12 in-domain settings and 7 of 8 transfer settings. The largest and most interpretable gains occur in high-risk moderation slices, including explicit slurs, violent threats, and cross-dataset transfer. The broader lesson is that moderation systems should treat external toxicity tools and priors as conditional evidence rather than fixed features or ground truth, in focused ablations, source-specific gating gives the strongest results in transfer, severe-abuse slices, and high-risk triage.

## Metadata
- **Published**: 2026-07-17T11:21:29Z
- **Authors**: Indraveni Chebolu, Rohan Singh, Arnab Mallick, Harmesh Rana
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15861v1)