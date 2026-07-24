---
title: Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing
published: 2026-07-21T10:19:17Z
authors: Laurin Wagner, Mario Zusag, Bernhard Thallinger
url: http://arxiv.org/abs/2607.18934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing

## Abstract
Modern ASR models trained on heterogeneously annotated data treat transcription style (verbatim vs. intended) as an uncontrolled latent variable, causing measurable decoding instability, evaluation confounding (up to 60% of reported WER attributable to style mismatch), and unreliable word-level timing. We show that models already encode both styles; the challenge is controlled activation. Using coverage-aware decoder task tokens trained on parallel verbatim/intended transcript pairs, we raise German disfluency F1 from 10% to 79% zero-shot, despite English-only training. Full English-only fine-tuning surpasses all baselines in verbatim accuracy, disfluency detection, and intended-mode quality across both languages. We further introduce supervised cross-attention fine-tuning that improves word-level timestamps on disfluent speech beyond forced-alignment baselines. Finally, we propose verbatimize, a new task enabling scalable creation and enrichment of speech corpora with high-quality canonical verbatim transcriptions.

## Metadata
- **Published**: 2026-07-21T10:19:17Z
- **Authors**: Laurin Wagner, Mario Zusag, Bernhard Thallinger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18934v1)