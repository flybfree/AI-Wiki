---
title: A Speech Corpus for Mizo Automatic Speech Recognition: Whisper and SraVaani 1.0 Fine-Tuning with Morphology-Aware Evaluation
url: http://arxiv.org/abs/2608.19361v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-19_18-30-46Z_ASpeechCorpusforMizoAutomaticSpeechRecognition_Whi.md
generated_at: 2026-08-20 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an Automatic Speech Recognition (ASR) system for the Mizo language, a low‑resource language, by fine‑tuning three Whisper multilingual models and the SraVaani 1.0 Indic model on 17.62 hours of curated speech data. The results show that both models can achieve markedly lower word error rates (WER) than zero‑shot performance.

## Key Takeaways
- Whisper-large-v3 reached a conventional WER of 18.08% and a morphology‑aware WER of 7.22%, demonstrating strong performance even when adapted to an unseen language.
- The SraVaani 1.0 model had a zero‑shot WER of 58.27%, but fine‑tuning reduced its conventional WER to 29.45% and morphology‑aware WER to 17.93%, indicating that targeted training yields substantial gains.
- Fine‑tuning with carefully curated Mizo speech data improves both Whisper and SraVaani models, highlighting the importance of domain‑specific adaptation for low‑resource languages.

## Context
The study addresses a key challenge in natural language processing: providing reliable ASR solutions for under‑represented languages where large annotated corpora are scarce. Multilingual models like Whisper and SraVaani aim to support many languages with limited resources, yet their performance often degrades when applied to isolated languages without fine‑tuning.

## Implications
These findings matter for researchers developing speech technologies for remote communities that rely on Mizo as a primary language. Practitioners can leverage the results to design more effective ASR pipelines, emphasizing the need for morphology‑aware evaluation and fine‑tuned models to achieve usable accuracy in low‑resource settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19361v1)
