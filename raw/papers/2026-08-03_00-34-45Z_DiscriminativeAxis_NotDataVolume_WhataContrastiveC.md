---
title: Discriminative Axis, Not Data Volume: What a Contrastive Corpus Teaches an Audio Embedding
published: 2026-08-03T00:34:45Z
authors: Abdul Basit Tonmoy
url: http://arxiv.org/abs/2608.01560v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discriminative Axis, Not Data Volume: What a Contrastive Corpus Teaches an Audio Embedding

## Abstract
Scaling the corpus is the default remedy when a contrastive representation lacks an attribute. We report a case where it does nothing, and identify what does: adding a lexical-speech round to a frozen-base multimodal embedding model raises zero-shot keyword spotting by 76 points while reducing speech-emotion recognition by 14. The loss is not a capacity limit: fine-tuning on 7,442 clips from a prosody-controlled corpus recovers emotion past its pre-speech level at a five-point keyword cost. Nor is it data volume: 29,428 mined clips whose captions explicitly name emotions, at matched exposure, move emotion by -0.0007. The difference is structural: a contrastive objective encodes an attribute only when the in-batch negatives cannot be separated without it; the controlled corpus holds sentence content fixed, so prosody is the only separating signal, whereas mined captions name emotion yet remain separable by scene content. Intervention on the same audio confirms causality: raising caption similarity does not recover emotion, but collapsing caption diversity so that emotion becomes the only separating axis recovers it by 8.9 points across three seeds, with a smaller, same-signed gain on a non-acted corpus, while keyword accuracy trades back. Corpus structure, not size or caption vocabulary, controls what a contrastive audio embedding encodes.

## Metadata
- **Published**: 2026-08-03T00:34:45Z
- **Authors**: Abdul Basit Tonmoy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01560v1)