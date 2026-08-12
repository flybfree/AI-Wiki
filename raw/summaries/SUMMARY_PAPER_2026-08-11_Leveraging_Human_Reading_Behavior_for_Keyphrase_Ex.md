---
title: Leveraging Human Reading Behavior for Keyphrase Extraction: A Webcam-based Eye-tracking Corpus
url: http://arxiv.org/abs/2608.10688v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-11-42Z_LeveragingHumanReadingBehaviorforKeyphraseExtracti.md
generated_at: 2026-08-11 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether lightweight webcam-based eye-tracking features can enhance keyphrase extraction from Chinese academic abstracts in Library and Information Science (LIS). By constructing the CLIS-ET corpus with first fixation duration, fixation number, and total fixation duration, the authors show that these human reading behavior signals improve KPE performance. The study demonstrates that integrating these features directly into existing models without heavy computational overhead yields better results.

## Key Takeaways
- Eye-tracking features consistently improved keyphrase extraction performance across the evaluated models.
- The combination of fixation number (FN) and total fixation duration (TFD) achieved the best results on the Att-BiLSTM+CRF model, indicating that these metrics capture useful reader attention signals.
- This work introduces a cost-effective webcam-based eye-tracking approach and presents CLIS-ET, a Chinese academic eye‑tracking corpus containing FFD, FN, and TFD features.

## Context
Most keyphrase extraction methods focus solely on textual representation and ignore the human reading process that naturally highlights important content. By incorporating behavioral cues such as fixation patterns, this research bridges the gap between computational modeling and real‑world comprehension, offering a more realistic basis for extracting salient information in Chinese academic texts.

## Implications
Incorporating eye-tracking data can lead to more accurate keyphrase detection, benefiting LIS practitioners who need reliable summaries of abstracts. Practitioners may leverage these low‑cost features to improve automated summarization tools and research that aims to align AI outputs with human attention patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10688v1)
