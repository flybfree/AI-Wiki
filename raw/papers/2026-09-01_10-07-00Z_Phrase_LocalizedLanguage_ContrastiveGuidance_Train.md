---
title: Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech
published: 2026-09-01T10:07:00Z
authors: Che Hyun Lee, Sangkwon Park, Donghun Kang, Dongwook Lee, Youngho Cho, Heeseung Kim, Sungroh Yoon
url: http://arxiv.org/abs/2609.01016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech

## Abstract
Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a separate guidance for each region, so each part is guided by its own language. To choose where to apply this localized guidance, we propose a self-attention probing technique that finds the phrase boundaries without external alignments. Together, these components generate speech in which each region carries the accent of its own language, requiring no fine-tuning or auxiliary models. Across diverse language pairs, LCG robustly increases the nativeness of the code-switched phrase while suppressing accent leakage, and preserving overall speaker identity and naturalness.

## Metadata
- **Published**: 2026-09-01T10:07:00Z
- **Authors**: Che Hyun Lee, Sangkwon Park, Donghun Kang, Dongwook Lee, Youngho Cho, Heeseung Kim, Sungroh Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01016v1)