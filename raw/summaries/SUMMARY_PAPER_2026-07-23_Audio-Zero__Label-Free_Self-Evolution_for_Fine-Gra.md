---
title: Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning
url: http://arxiv.org/abs/2607.20166v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-03-25Z_Audio_Zero_Label_FreeSelf_EvolutionforFine_Grained.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
Audio-Zero introduces a label-free self-evolution framework designed to boost fine-grained audio reasoning within large audio language models. By constructing an auditory self-play game from unlabeled contrast pairs, the method generates verifiable rewards without external annotations and improves performance on nuanced tasks while preserving broad audio understanding.

## Key Takeaways
- Audio-Zero builds an auditory self‑play game where most players hear reference audio and one odd listener hears a subtle variant, providing verifiable rewards without external labels.
- The model generates descriptive clues about the audio it perceives and then reasons to identify the odd listener by exploiting inconsistencies among those clues.
- Experiments on Qwen2-Audio-7B-Instruct and Qwen2.5-Omni-7B demonstrate gains on TREA, MMAU Test‑mini and MMAR, showing that fine‑grained reasoning improves while overall audio understanding remains stable.

## Context
The rapid advancement of large audio language models has focused on coarse semantic tasks, but precise auditory perception—such as recognizing event order or repetitions—remains challenging. Audio-Zero addresses this gap by leveraging unsupervised self‑play to generate rich, fine‑grained descriptions directly from unlabeled data.

## Implications
This approach reduces reliance on costly annotation pipelines and demonstrates that iterative self‑evolution can yield high‑quality reasoning capabilities. Practitioners can adopt similar label‑free training paradigms for other modalities seeking scalable improvements in subtle perception tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20166v1)
