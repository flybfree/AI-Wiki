---
title: Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models
published: 2026-09-01T18:00:45Z
authors: Kunlin Cai, Kaiyuan Zhang, Zihang Xiang, Jinghuai Zhang, Abeer Alwan, Fnu Suya, Yuan Tian
url: http://arxiv.org/abs/2609.01723v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models

## Abstract
Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speech creates a large and underexplored query design space with no established criterion for identifying an effective query. For representation engineering, the multi-level speech characteristics and temporal variability of speech make low-level representations and direct comparisons inadequate for capturing membership signals. To address these challenges, we present the first black-box MIA framework explicitly tailored to TTS models at both the speaker and record levels. For query generation, we characterize the feasible query space and establish two criteria, scorable extent and memorization elicitation, for evaluating five representative queries, identifying recitation as the strongest. For representation engineering, we obtain multi-level speech representations from embedding models and temporally align the generated and target audio for fine-grained comparison. Evaluations across three state-of-the-art TTS models (CosyVoice2, F5-TTS, and XTTS-v2) fine-tuned on two benchmark datasets (VCTK and British Dialect) reveal severe privacy leakage: speaker-level AUC remains above 0.80 and approaches 1.0 in the strongest settings, while record-level AUC ranges from 0.80 to 0.90 and remains effective even in challenging scenarios where both members and non-members are of the same speakers. We further identify speech characteristics associated with disproportionate vulnerability to memorization.

## Metadata
- **Published**: 2026-09-01T18:00:45Z
- **Authors**: Kunlin Cai, Kaiyuan Zhang, Zihang Xiang, Jinghuai Zhang, Abeer Alwan, Fnu Suya, Yuan Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01723v1)