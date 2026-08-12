---
title: myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR
url: http://arxiv.org/abs/2608.11036v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-12-42Z_myMediWhisper_ConstructionofBurmeseMedicalSpeechCo.md
generated_at: 2026-08-11 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces myMediWhisper, a framework that builds a high-quality Burmese medical speech corpus and fine-tunes Whisper models for clinical dialogue ASR. Using full fine‑tuning (FFT) and parameter‑efficient fine‑tuning with LoRA, the authors achieve a state‑of‑the‑art Word Error Rate of 23.44% on clean data. Data augmentation improves robustness in noisy and reverberant conditions.

## Key Takeaways
- The study creates an 28‑hour Burmese medical speech corpus recorded by native speakers, providing the first large‑scale domain‑specific dataset for Whisper fine‑tuning in this language.
- Full fine‑tuning (FFT) without augmentation yields a WER of 23.44%, outperforming larger general‑domain models that suffer from overfitting to noisy augmentations.
- Waveform and spectrogram level data augmentation, while harmful on clean speech, markedly boosts performance under realistic noise and acoustic impairments across both FFT and LoRA settings.

## Context
Whisper’s multilingual pre‑training offers a strong baseline for low‑resource languages, yet medical speech presents unique challenges due to specialized vocabulary and variable acoustic conditions. This work demonstrates that targeted domain adaptation can surpass generic fine‑tuning on larger corpora, highlighting the value of curated, high‑quality resources.

## Implications
Clinicians and AI developers can leverage myMediWhisper to build reliable ASR tools for Burmese medical consultations, reducing errors in critical health communication. The dataset and model checkpoints are publicly available, encouraging further research into low‑resource clinical NLP pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11036v1)
