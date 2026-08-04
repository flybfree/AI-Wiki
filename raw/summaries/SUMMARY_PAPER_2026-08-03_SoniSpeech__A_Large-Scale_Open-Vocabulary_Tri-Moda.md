---
title: SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces
url: http://arxiv.org/abs/2608.00803v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_18-03-37Z_SoniSpeech_ALarge_ScaleOpen_VocabularyTri_ModalDat.md
generated_at: 2026-08-03 23:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
SoniSpeech introduces a large‑scale open‑vocabulary dataset for wearable silent speech interfaces that integrates acoustic echo profiles, audio recordings, and frontal video. The corpus spans 18 000 utterances over 34 hours and achieves a 26.3% word error rate with a CTC‑ResNet‑34 baseline, marking the first benchmark for this task.

## Key Takeaways
- The dataset provides 5 356 unique words and full phoneme coverage from the SODA dialogue corpus, enabling open‑vocabulary recognition.
- It combines three synchronized modalities—ultrasound echo profiles, voiced audio, and frontal video—to capture silent speech signals without intrusive hardware.
- A CTC‑based ResNet‑34 model demonstrates a 26.3% word error rate, establishing a new benchmark for wearable SSI.

## Context
Wearable silent speech interfaces have historically relied on limited vocabularies due to hardware constraints such as facial electrodes. This paper pushes the field forward by creating a multimodal dataset that supports larger vocabularies and real‑world conversational English, highlighting the potential of eyewear sensors in natural interaction.

## Implications
For researchers, SoniSpeech offers a resource to evaluate and improve silent speech recognition models without costly hardware upgrades. Industry practitioners can leverage its open format to develop low‑profile SSI solutions that integrate seamlessly into consumer devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00803v1)
