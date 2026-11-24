---
title: INSEP: Refusal-Direction Inseparability as a Defense Against Abliteration
published: 2026-11-20T21:06:00Z
authors: Ivan Brugere, Junqi Jiang, Saumitra Mishra, Sumitra Ganesh
url: http://arxiv.org/abs/2611.28314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# INSEP: Refusal-Direction Inseparability as a Defense Against Abliteration

## Abstract
Abliteration is a widely used white-box attack against the safety alignment of large language models (LLMs). It elicits harmful behavior by estimating a refusal direction in the model's activation space and projecting that direction out of the residual-stream write-out matrices. We propose INSEP, a defense that fine-tunes the model to reduce the separability of harmful and benign activations along the refusal direction. Abliteration estimates this direction as a difference in class means and projects it out. Reducing separability weakens the signal the attack relies on. An adversarial eigendecomposition selects the most separable prompt subsets. A low-rank adapter reduces their separation along that direction. Behavioral losses preserve the base model's refusal and the quality of its benign responses during training. We benchmark INSEP against six published defenses under five attacks, across eight LLMs from 1B to 14B parameters and several model families. Beyond response harm, we measure coherence, directness, over-refusal, and MMLU, to distinguish robust refusal from low harm produced by evasive or degraded responses. INSEP ranks first on the mean composite score across all eight base models while retaining utility, in the largest abliteration-defense evaluation reported to date.

## Metadata
- **Published**: 2026-11-20T21:06:00Z
- **Authors**: Ivan Brugere, Junqi Jiang, Saumitra Mishra, Sumitra Ganesh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.28314v1)