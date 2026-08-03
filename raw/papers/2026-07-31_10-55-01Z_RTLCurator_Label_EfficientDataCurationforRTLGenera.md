---
title: RTLCurator: Label-Efficient Data Curation for RTL Generation
published: 2026-07-31T10:55:01Z
authors: Siyang Cai, Cangyuan Li, Wenjing Chang, Kun Wang, Haoyu Gao, Yinhe Han, Ying Wang
url: http://arxiv.org/abs/2607.29283v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RTLCurator: Label-Efficient Data Curation for RTL Generation

## Abstract
Training large language models (LLMs) to write register-transfer level (RTL) requires large corpora of paired specifications and code, and such data is scarce enough that most public corpora are now synthesized. Synthesis provides scale but not correctness, and in two widely used RTL datasets only 24.4% and 53.5% of pairs pass generated functional tests. This raises the question of how much of such a corpus to keep and which part of it. Correctness alone is a poor answer. A pair that misbehaves in one corner case still shows valid syntax and interface conventions, and complex sequential designs are both harder to generate and harder to validate, so filtering by correctness leaves a corpus of short and simple modules. Correctness is also hard to obtain, since behavior leaves little trace on the surface in RTL, and validating an entire corpus only sorts pairs into passed and failed. We present RTLCurator, which learns a behavior-aware compatibility prior by contrasting each specification with implementations that fail simulation, and calibrates it to a new corpus using a small number of validated pairs. It then constructs the retained subset by balancing alignment, representation coverage, and RTL structural richness. On CodeV and RTLCoder, keeping 80% of the corpus this way improves on training with the full corpus across all reported metrics while validating only 10% of the pool, whereas ranking by the score alone falls below random selection and filtering the whole pool by simulation does no better.

## Metadata
- **Published**: 2026-07-31T10:55:01Z
- **Authors**: Siyang Cai, Cangyuan Li, Wenjing Chang, Kun Wang, Haoyu Gao, Yinhe Han, Ying Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29283v1)