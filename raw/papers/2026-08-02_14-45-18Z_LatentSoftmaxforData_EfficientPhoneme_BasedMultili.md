---
title: Latent Softmax for Data-Efficient Phoneme-Based Multilingual ASR Across Tonal and Non-Tonal Languages
published: 2026-08-02T14:45:18Z
authors: Saierdaer Yusuyin, Nanling Jiang, Hao Huang, Zhijian Ou
url: http://arxiv.org/abs/2608.01281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent Softmax for Data-Efficient Phoneme-Based Multilingual ASR Across Tonal and Non-Tonal Languages

## Abstract
Phoneme-based multilingual automatic speech recognition (ASR) can share acoustic evidence across languages more directly than language-specific subword modeling. When tonal and non-tonal languages are jointly trained, however, their supervision granularity does not match: tonal languages annotate tone-marked vowels, whereas non-tonal languages typically provide only base-vowel labels. A standard softmax either treats the two as unrelated classes, weakening cross-lingual sharing, or collapses tones, losing distinctions required by tonal languages. We propose Latent Softmax, a connectionist temporal classification (CTC)-compatible output layer that models tone-marked vowels as subclasses and base vowels as major classes, while consonants and the CTC blank remain singleton labels. When only a base-vowel major-class label is observed, the tone-marked vowel subclass is treated as latent and marginalized out. Multilingual experiments on AISHELL-1 Mandarin and LibriSpeech English show that Latent Softmax reduces speech-to-phoneme (S2P) phoneme error rates over a standard softmax multilingual baseline by 8.4% on AISHELL-1, 17.5% on LibriSpeech test-clean, and 12.6% on test-other. The improved speech-to-phoneme encoders also yield consistent word error rate gains for both large-language-model phoneme-to-grapheme conversion and projector-based interfaces. After code-switching adaptation, Latent Softmax further reduces projector-based mixed error rate by 2.6% on ASRU2019 and 9.5% on CS-Dialogue datasets.

## Metadata
- **Published**: 2026-08-02T14:45:18Z
- **Authors**: Saierdaer Yusuyin, Nanling Jiang, Hao Huang, Zhijian Ou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01281v1)