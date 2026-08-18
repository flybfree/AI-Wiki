---
title: The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT
published: 2026-08-16T21:49:54Z
authors: Kirill Borodin, Vasiliy Kudryavtsev, Ivan Viakhirev
url: http://arxiv.org/abs/2608.15940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT

## Abstract
Modern encoder-decoder systems can produce fluent text even when their input contains no recoverable message. We study this failure in ASR and NMT through the models' reserved null tokens, asking whether the score for ending generation already carries a usable abstention signal. Across speech recognizers and translation models, we audit native null-token scores and scalar logit shifts. In Whisper, we additionally probe decoder states and compare supervised row edits with conventional external gates. The evaluated models often expose a useful abstention signal, but stock decoding does not reliably act on it. Raising the null-token score can sharply suppress fabrication, but aggressive intervention also deletes valid speech or shortens legitimate translations. These findings turn the null token into a diagnostic lens on hallucination and motivate evaluating abstention methods by both suppression and deletion costs, rather than by hallucination reduction alone.

## Metadata
- **Published**: 2026-08-16T21:49:54Z
- **Authors**: Kirill Borodin, Vasiliy Kudryavtsev, Ivan Viakhirev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15940v1)