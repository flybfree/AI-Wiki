---
title: Where Words Begin and End
published: 2026-10-13T06:11:55Z
authors: Husein Zolkepli
url: http://arxiv.org/abs/2610.17782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Words Begin and End

## Abstract
Forced aligners locate each word of a known transcript in the audio, and many speech pipelines depend on them. In our own data, a widely used CTC aligner inserts a pause at nearly every word boundary, and we found almost no aligner evaluated on telephone audio. We compare nine aligner configurations against human word boundaries on read, conversational and telephone English. The Montreal Forced Aligner (MFA) is the most precise, while CTC aligners consistently start words late, because most frames inside a word go to the blank token. We then fine-tune Whisper with LoRA to predict each word's start and end as timestamp tokens, training only on boundaries placed by people: 47 hours in 87 languages. The resulting aligner is more precise than MFA on every English test condition, and than MFA's own Korean and Dutch models. With FA-Bench's protocol and code on TIMIT, its word-boundary error is 11.6 ms, against 18.2 ms for the best published system. Two choices matter most on telephone conversations: placing the timestamp slots after the word they time, and training on noisy transcripts, which also makes the aligner nearly insensitive to errors in the transcript. The released model reaches 16.0 ms on real landline calls, against 36.5 ms for MFA. The models are available at https://huggingface.co/collections/Scicom-intl/force-alignment

## Metadata
- **Published**: 2026-10-13T06:11:55Z
- **Authors**: Husein Zolkepli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17782v1)