---
title: VocalAffectBench: Evaluating Vocal Emotion Recognition in AI Audio Models
published: 2026-08-28T23:03:43Z
authors: Models Luc Debaupte, Tyler Baumgartner, Brandon Tai, Candice Fan, Bill Wang, Yi Zhong
url: http://arxiv.org/abs/2608.28932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VocalAffectBench: Evaluating Vocal Emotion Recognition in AI Audio Models

## Abstract
Voice products increasingly need affective cues that are present in speech but absent from transcripts. We introduce VocalAffectBench, a public, test-only benchmark for evaluating whether AI audio models can identify expressed vocal emotion from raw audio. The benchmark contains 273 human-recorded English WAV clips from 51 speaker accounts totaling 1.95 hours across seven labels: angry, disgusted, fearful, happy, neutral, sad, and surprised, with 39 clips per class. All baselines are evaluated from audio alone, without transcripts or contextual metadata. Across six released baselines, average accuracy is 35.5%. The strongest baseline, gemini_3_5_flash, reaches 46.5% on the seven-way task, above the 14.3% random baseline but far from robust emotion recognition. A secondary valence-bucket analysis maps labels into positive, neutral, and negative classes, excluding surprised because its valence is ambiguous. Aggregate accuracy under this coarser view is 50.9%. Performance is highly uneven across classes. By recall, neutral is identified most reliably at 75.6% averaged across baselines, while surprised and fearful reach only 10.7% and 15.4%, respectively. These results show that the evaluated baselines can extract some affective signal from speech, but discrete expressed-emotion recognition remains fragile, especially for non-neutral emotions that are often most important in voice agent workflows.

## Metadata
- **Published**: 2026-08-28T23:03:43Z
- **Authors**: Models Luc Debaupte, Tyler Baumgartner, Brandon Tai, Candice Fan, Bill Wang, Yi Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28932v1)