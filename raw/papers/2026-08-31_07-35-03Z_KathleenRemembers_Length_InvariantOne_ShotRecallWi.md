---
title: Kathleen Remembers: Length-Invariant One-Shot Recall Without Attention
published: 2026-08-31T07:35:03Z
authors: George Fountzoulas
url: http://arxiv.org/abs/2608.30376v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Kathleen Remembers: Length-Invariant One-Shot Recall Without Attention

## Abstract
Recurrent, attention-free sequence models share a structural weakness: a fading state cannot perform exact recall of something seen once, far in the past. We add to the Kathleen trunk a second memory layer -- a "notebook": a fixed-key holographic (HRR) associative store with a learned local write gate, a self-gating raw read, and write-triggered forgetting -- 25K parameters that attach to the logits of any trunk. (1) Mechanism: on a controlled needle-in-haystack task the notebook reaches 80-82% one-shot recall at 4x the training length, where the bare trunk scores ~4% and a parameter-matched attention head scores 100% inside its training length and 0% beyond it. Addressing is length-invariant by construction; the untrained memory alone recalls at 90% accuracy identically at 512, 2048 and 4096 bytes. Because the store is a linear superposition, two capabilities follow from arithmetic alone: selective unlearning (one subtraction erases one fact to chance, retained facts unharmed) and per-token attribution (counterfactual erasure names the source fact of every correct byte, 100% provenance). (2) Real text: on WikiText-2 bytes the notebook improves prediction of repeated rare words by +0.15-0.27 bits/byte, the gain growing with the distance between mentions and holding zero-shot at 4x training length; write-triggered forgetting eliminates memory pollution at 8x length (first-mention cost +0.33 -> -0.004). (3) Scope and scale: a parameter-matched attention head does generalize on natural-text repetition, so the notebook's claim is exact recall at O(L); on a WikiText-103 ladder (8 to 512 MB) the zero-shot repeat gain rises monotonically. All experiments are pre-registered, seeds reported, and reproducible on a single free-tier GPU.

## Metadata
- **Published**: 2026-08-31T07:35:03Z
- **Authors**: George Fountzoulas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30376v1)