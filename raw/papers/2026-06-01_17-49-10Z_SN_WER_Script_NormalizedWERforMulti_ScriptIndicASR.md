---
title: 'SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation'
published: 2026-06-01T17:49:10Z
authors: Priyaranjan Pattnayak
url: http://arxiv.org/abs/2606.02548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation

## Abstract
Word Error Rate (WER) is the dominant metric for automatic speech recognition (ASR), but it can overestimate errors when references and hypotheses encode the same words in different scripts. This issue is common in multilingual settings where ASR models may emit romanized text. We propose Script-Normalized WER (SN-WER), a training-free, evaluation-only scoring method that transliterates both reference and hypothesis text into a language-specific canonical script before computing WER. We evaluate SN-WER on 5 Indic languages, 2 datasets, and 3 ASR models. On curated FLEURS data, SN-WER reduces inflated model gaps by up to 12%, while on noisier Common Voice data the reductions are smaller or inconsistent, indicating genuine recognition weaknesses rather than only script mismatch. Controlled stress tests show a 67% attenuation of artificial romanization-induced WER inflation, while lexical-substitution controls show near-identical sensitivity to semantic errors, with Delta SN-WER / Delta WER approximately 1.09. SN-WER is robust to transliterator choice, normalization changes, and shows low token-collision rates below 0.1% in the evaluated Indic setting. We argue that SN-WER should be reported alongside WER and CER as a companion metric for script-insensitive ASR evaluation, especially when transcripts feed downstream search, indexing, or multilingual LLM pipelines.

## Metadata
- **Published**: 2026-06-01T17:49:10Z
- **Authors**: Priyaranjan Pattnayak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.02548v1)