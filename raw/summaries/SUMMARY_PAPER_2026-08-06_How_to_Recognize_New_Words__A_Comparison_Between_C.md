---
title: How to Recognize New Words: A Comparison Between Context Biasing Methods and Speech LLMs
url: http://arxiv.org/abs/2608.05759v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_08-45-33Z_HowtoRecognizeNewWords_AComparisonBetweenContextBi.md
generated_at: 2026-08-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how automatic speech recognition systems can identify rare or unseen vocabulary by comparing two approaches: context‑biasing techniques that augment Whisper with a supplied word list, and prompting speech large language models (LLMs) with contextual information. Experiments on read and non‑read speech show that the biasing methods reduce biased word error rates up to 88 % while leaving other words largely unchanged, whereas LLMs perform best on read material but struggle with non‑read content and are sensitive to prompt ordering and distractor count.

## Key Takeaways
- Context‑biasing can dramatically lower WER for new words (up to 88 %) without harming regular vocabulary.  
- Speech LLMs excel at recognizing familiar words in read speech but generalize poorly to unfamiliar terms, especially when prompted with distractors or in the wrong order.  
- The trade‑off between bias reduction and overall performance depends on whether the task is read or non‑read speech.

## Context
This work addresses a persistent challenge in ASR: handling vocabulary that does not appear frequently during training. By juxtaposing lightweight, model‑specific augmentations with powerful but generic LLMs, the study highlights how specialized techniques can outperform broad models when fine‑tuned for rare terms, while also revealing limitations of prompting large language models on speech data.

## Implications
Practitioners should consider context‑biasing as a cost‑effective solution for domains where new terminology is frequent, such as medical or technical recordings. Meanwhile, LLMs remain attractive for general‑purpose ASR but require careful prompt engineering to mitigate their sensitivity to input structure and distractor density.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05759v1)
