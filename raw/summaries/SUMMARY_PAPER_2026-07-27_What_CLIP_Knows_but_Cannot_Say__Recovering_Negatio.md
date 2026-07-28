---
title: What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features
url: http://arxiv.org/abs/2607.23271v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_16-15-50Z_WhatCLIPKnowsbutCannotSay_RecoveringNegationfromFr.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem that contrastive vision‑language models such as CLIP treat semantically opposite phrases like “a dog” and “not a dog” with nearly identical embeddings, making them insensitive to negation. The authors introduce PeakPatch, a lightweight post‑hoc correction system that recovers lost negation signals without retraining CLIP’s weights.

## Key Takeaways
- Representational Collapse occurs when middle layers build compositional syntax but final layers collapse it as visual alignment rises, producing a syntax‑blind representation.  
- PeakPatch uses an Embedding Correction Network (ECN) with cross‑attention to extract a negation‑specific signal from the peak layer and injects a deviation vector into the final embedding space.  
- The system adds only 5.2 million parameters, achieving 74.3 % on COCO MCQ (+35.1 over CLIP) while preserving the standard cosine similarity interface.

## Context
Vision‑language models rely heavily on frozen embeddings to maintain interpretability and compatibility with existing pipelines. Negation handling is a critical yet poorly addressed aspect of these systems, limiting their utility in tasks requiring precise semantic contrast. This work demonstrates that subtle architectural behaviors can be mitigated without full fine‑tuning.

## Implications
Practitioners can integrate PeakPatch into CLIP deployments to improve performance on out‑of‑distribution negation retrieval with minimal overhead. The approach also benefits text‑to‑image generation, showing a 18.4 point gain in negation scores across multiple backbones.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23271v1)
