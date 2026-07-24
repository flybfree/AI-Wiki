---
title: Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing
url: http://arxiv.org/abs/2607.18934v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_10-19-17Z_TranscriptionPolicyasaLatentVariable_ActivatingCon.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the problem of uncontrolled transcription style in ASR models by treating it as a latent variable that can be activated or suppressed. By training coverage-aware decoder tokens on parallel verbatim and intended transcript pairs, they achieve high zero-shot performance on German disfluency detection and improve word‑level timing with supervised cross‑attention fine‑tuning. The authors also introduce the “verbatimize” task for scalable generation of canonical verbatim transcripts.

## Key Takeaways
- Models already encode both verbatim and intended transcription styles, but this latent variable is not controllable, leading to decoding instability and up to 60% WER variance due to style mismatch.  
- Coverage‑aware decoder tokens trained on parallel pairs raise German disfluency F1 from 10% to 79% zero‑shot despite English‑only training, while full fine‑tuning outperforms baselines in verbatim accuracy and intended‑mode quality across languages.  
- Supervised cross‑attention fine‑tuning improves word‑level timestamps beyond forced‑alignment baselines, enabling precise timing for disfluent speech.

## Context
In automatic speech recognition research the distinction between verbatim and intended transcripts is often ignored, causing evaluation artifacts and limiting model reliability. This work highlights that style information is implicitly present in models but not exploitable without explicit control mechanisms.

## Implications
For industry practitioners this enables more accurate voice assistants by allowing precise selection of transcription modes, reducing user confusion and improving trust. The “verbatimize” task also provides a practical pipeline for creating high‑quality verbatim corpora, supporting research and product development that require canonical transcriptions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18934v1)
