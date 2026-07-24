---
title: From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin
url: http://arxiv.org/abs/2607.18912v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_09-52-57Z_FromaMultilingualStreamingASRBackbonetoKenyan_Lang.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an end‑to‑end engineering study that adapts NVIDIA Nemotron 3.5 ASR Streaming 0.6B to three Kenyan languages—Kikuyu, Dholuo, and Kalenjin—while preserving streaming constraints such as cache‑aware FastConformer RNN‑T, prompt conditioning, and a decoder. The authors fine‑tune the model on curated corpora, apply Unicode normalization, filter utterances by duration, and evaluate using true‑streaming metrics that exclude artifacts like non‑speech labels or short‑utterance over‑generation.

## Key Takeaways
- Kikuyu achieves 42.97% WER and Dholuo 33.98% WER after full‑parameter fine‑tuning, showing language‑specific performance gains despite limited data.  
- Kalenjin reaches 68.74% WER on a clean diagnostic subset but its score is not an independent generalization estimate because the validation set mixes test origins and excludes long pauses.  
- The study documents negative findings such as over‑generation of non‑speech labels, boundary‑sensitive WER issues, and cloud job‑lifecycle failures that must be mitigated in production.

## Context
African ASR remains under‑served because of orthographic inconsistency, annotation gaps, and evaluation mismatches with real deployment. This work demonstrates that a multilingual streaming backbone can be adapted without discarding its core architecture, offering a scalable path for low‑resource languages.

## Implications
For practitioners, the paper provides an auditable checklist for adapting streaming ASR models to African languages, reducing reliance on external benchmarks. Industry adoption could accelerate deployment of language‑specific speech services in Kenya and similar regions where local content is valuable but resources are scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18912v1)
