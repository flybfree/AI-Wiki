---
title: Character Iconicity vs. Arbitrariness: An Arabic NLP Perspective
published: 2026-08-03T22:47:50Z
authors: Dorieh Alomari, Irfan Ahmad, Maged S. Al-shaibani
url: http://arxiv.org/abs/2608.02935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Character Iconicity vs. Arbitrariness: An Arabic NLP Perspective

## Abstract
Arabic script uses 28 letters, many of which share a common base shape (rasm) and are distinguished only by dot placement. Because early Arabic manuscripts were written without dots yet remained interpretable, dot removal offers a natural test of whether these visual distinctions are functionally necessary. Prior work has shown that dotless Arabic can remain readable and effective for natural language processing (NLP), but it remains unclear whether this success depends on preserving the original rasm groupings or whether arbitrary but consistent remappings to the same reduced rasm set can achieve comparable performance. We address this question by comparing standard dotted and dotless Arabic with arbitrary character remappings constrained to the same 19 undotted rasms. We generated 2,000 random remappings under word- and character-level tokenization and selected four representative mappings with the highest and lowest entropy values. These representations were evaluated across language modeling, text classification, sequence labeling, machine translation, and restoration to the original script. The results show that neither preserving original character distinctions nor retaining traditional rasm-based groupings is necessary for strong NLP performance. Random remappings achieve competitive performance while reducing vocabulary size, out-of-vocabulary (OOV) rates, model size, and training cost. These findings suggest that, from an NLP perspective, Arabic character form-function relationships are largely arbitrary: models rely more on stable distributional structure than on the visual iconicity of letter forms.

## Metadata
- **Published**: 2026-08-03T22:47:50Z
- **Authors**: Dorieh Alomari, Irfan Ahmad, Maged S. Al-shaibani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02935v1)