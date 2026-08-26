---
title: Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts
published: 2026-08-25T15:24:48Z
authors: Meruyert Aristombayeva, Jason S. Lucas, Chaewan Chun, Dongwon Lee
url: http://arxiv.org/abs/2608.24707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts

## Abstract
While text-based hallucination detection has been extensively studied, spoken hallucination detection remains largely unexplored, particularly for low-resource languages. We present the first multilingual spoken hallucination benchmark comprising 12,013 news samples across English, Russian, and Kazakh with controlled hallucinations of three types and three severity levels. Samples comprise original articles and aligned hallucinated counterparts in text and audio. We complement the synthetic corpus with 290 fact-checked fake news items collected natively in Russian (225) and Kazakh (65), translated into the other language and rendered through the same TTS-ASR pipeline. We assess fine-tuned multilingual encoders and, in zero-shot in-context settings, multimodal decoder models on transcript-based versus direct audio processing. Transcript-based detection generally outperforms direct audio processing, with binary-task degradation for strong encoders tracking per-language ASR error. On real-world fakes, synthetic-trained detectors transfer strongly (macro-F1 0.82-0.88 on original text), while Russian provenance analysis reveals both veracity-related and model-dependent machine-style signals, quantifying a key confound in synthetic hallucination benchmarks.

## Metadata
- **Published**: 2026-08-25T15:24:48Z
- **Authors**: Meruyert Aristombayeva, Jason S. Lucas, Chaewan Chun, Dongwon Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24707v1)