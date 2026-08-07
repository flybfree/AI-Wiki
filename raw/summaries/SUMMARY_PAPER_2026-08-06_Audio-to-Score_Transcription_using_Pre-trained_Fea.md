---
title: Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset
url: http://arxiv.org/abs/2608.06165v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-33-18Z_Audio_to_ScoreTranscriptionusingPre_trainedFeature.md
generated_at: 2026-08-06 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SheetSage-A2S Dataset and a new A2S model that uses pre-trained features, data augmentation, and the dataset to transcribe audio into score symbols for popular music. It reports a symbol error rate of 4.98% on classical quartets and 20.92% on the new dataset, outperforming prior methods.

## Key Takeaways
- The SheetSage-A2S Dataset provides 61 hours of audio with kern score encodings for 9,468 clips from 6,066 unique songs, enabling A2S research on popular music. - Data augmentation and the MuQ pretrained feature extractor improve model generalisation and performance. - The proposed model achieves a 20.92% symbol error rate on the dataset, establishing a strong benchmark.

## Context
Audio-to-score systems aim to convert spoken musical notes into symbolic scores, a task that has been studied mainly for classical repertoire. This work expands the scope to popular music, which lacks existing annotated datasets and models, highlighting a gap in current AI research.

## Implications
For practitioners, the dataset and model provide tools to evaluate A2S performance on real-world music, encouraging further development of robust transcription systems. The findings suggest that pre-trained audio features combined with augmentation can significantly boost accuracy, offering a path for scalable music transcription technologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06165v1)
